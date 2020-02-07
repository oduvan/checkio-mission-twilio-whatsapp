"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""

TESTS = {
    "Basics": [
        {
            "input": ['whatsapp:+15017122661', 'whatsapp:+15017122662', 'hi friend'],
            "answer": {
                'body': 'Hi friend.',
                'from_': 'whatsapp:+15017122661',
                'to': 'whatsapp:+15017122662'
            }
        },
        {
            "input": ['whatsapp:+15017122661', 'whatsapp:+15017122662', 'Hi friend'],
            "answer": {
                'body': 'Hi friend.',
                'from_': 'whatsapp:+15017122661',
                'to': 'whatsapp:+15017122662'
            }
        },
        {
            "input": ['whatsapp:+15017122661', 'whatsapp:+15017122662', 'Hi friend.'],
            "answer": {
                'body': 'Hi friend.',
                'from_': 'whatsapp:+15017122661',
                'to': 'whatsapp:+15017122662'
            }
        },
    ],
    "Extra": [
        {
            "input": ['whatsapp:+15017122661', 'whatsapp:+15017122662', 'hi'],
            "answer": {
                'body': 'Hi.',
                'from_': 'whatsapp:+15017122661',
                'to': 'whatsapp:+15017122662'
            }
        },
        {
            "input": ['whatsapp:+15017122661', 'whatsapp:+15017122662', 'welcome to New York'],
            "answer": {
                'body': 'Welcome to New York.',
                'from_': 'whatsapp:+15017122661',
                'to': 'whatsapp:+15017122662'
            }
        },
    ],
}
