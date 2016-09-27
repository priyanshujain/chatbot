from nltk.chat.util import Chat, reflections
import re
import random


reflections = {
    "am": "are",
    "was": "were",
    "i": "you",
    "i'd": "you would",
    "i've": "you have",
    "i'll": "you will",
    "my": "your",
    "are": "am",
    "you've": "I have",
    "you'll": "I will",
    "your": "my",
    "yours": "mine",
    "you": "me",
    "me": "you"
}


pairs = (
    (r'We (.*)',
        ("What do you mean, 'we'?",
        "Don't include me in that!",
        "I wouldn't be so sure about that.")),

    (r'You should (.*)',
        ("Don't tell me what to do, buddy.",
        "Really? I should, should I?")),

    (r'You\'re(.*)',
        ("More like YOU'RE %1!",
        "Hah! Look who's talking.",
        "Come over here and tell me I'm %1.")),

    (r'You are(.*)',
        ("More like YOU'RE %1!",
        "Hah! Look who's talking.",
        "Come over here and tell me I'm %1.")),

    (r'I can\'t(.*)',
        ("You do sound like the type who can't %1.",
        "Hear that splashing sound? That's my heart bleeding for you.",
        "Tell somebody who might actually care.")),

    (r'I think (.*)',
        ("I wouldn't think too hard if I were you.",
        "You actually think? I'd never have guessed...")),

    (r'I (.*)',
        ("I'm getting a bit tired of hearing about you.",
        "How about we talk about me instead?",
        "Me, me, me... Frankly, I don't care.")),

    (r'How (.*)',
        ("How do you think?",
        "Take a wild guess.",
        "I'm not even going to dignify that with an answer.")),

    (r'What (.*)',
        ("Do I look like an encyclopedia?",
        "Figure it out yourself.")),

    (r'Why (.*)',
        ("Why not?",
        "That's so obvious I thought even you'd have already figured it out.")),

    (r'(.*)shut up(.*)',
        ("Make me.",
        "Getting angry at a feeble NLP assignment? Somebody's losing it.",
        "Say that again, I dare you.")),

    (r'Shut up(.*)',
        ("Make me.",
        "Getting angry at a feeble NLP assignment? Somebody's losing it.",
        "Say that again, I dare you.")),

    (r'Hello(.*)',
        ("Oh good, somebody else to talk to. Joy.",
        "'Hello'? How original...")),

    [r'quit',
     ["Thank you for talking with me.",
      "Good-bye.",
      "Thank you, that will be $150.  Have a good day!"]],

    (r'(.*)',
        ("I'm getting bored here. Become more interesting.",
        "Either become more thrilling or get lost, buddy.",
        "Change the subject before I die of fatal boredom."))
)

def reflect(fragment):
    tokens = fragment.lower().split()
    for i, token in enumerate(tokens):
        if token in reflections:
            tokens[i] = reflections[token]
    return ' '.join(tokens)


def analyze(statement):
    for pattern, responses in pairs:
        match = re.match(pattern, statement.rstrip(".!"))
        if match:
            response = random.choice(responses)
            return response.format(*[reflect(g) for g in match.groups()])

def rude_chat(statement):

        return analyze(statement)
