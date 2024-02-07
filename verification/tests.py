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
            "input": [(
    (0, 0, 1, 0, 0),
    (0, 1, 0, 1, 0),
    (1, 0, 2, 0, 1),
    (0, 1, 0, 1, 0),
    (0, 0, 1, 0, 0)
)],
            "answer": "cgikMoqsw",
        },
        {
            "input": [(
    (1, 0, 1, 0, 1),
    (0, 2, 0, 2, 0),
    (1, 0, 1, 0, 1),
    (0, 2, 0, 2, 0),
    (1, 0, 1, 0, 1)
)],
            "answer": "aceGIkmoQSuwy",
        },
    ],
    "Extra": [
        {
            "input": [(
    (2, 0, 1, 1, 1),
    (1, 0, 1, 0, 1),
    (1, 0, 1, 0, 1),
    (1, 0, 1, 0, 1),
    (1, 1, 1, 0, 1)
)],
            "answer": "Acdefhjkmoprtuvwy",
        },
        {
            "input": [(
    (1, 1, 1, 1, 1),
    (2, 2, 2, 2, 2),
    (0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0)
)],
            "answer": "abcdeFGHIJ",
        },
        {
            "input": [(
    (1, 0, 0, 0, 2),
    (0, 1, 0, 2, 0),
    (0, 0, 0, 0, 0),
    (0, 2, 0, 1, 0),
    (2, 0, 0, 0, 1)
)],
            "answer": "aEgIQsUy",
        },
        {
            "input": [(
    (0, 1, 2, 0, 1),
    (1, 2, 0, 1, 2),
    (2, 0, 1, 2, 0),
    (0, 1, 2, 0, 1),
    (1, 2, 0, 1, 2)
)],
            "answer": "bCefGiJKmNqRtuVxY",
        },
        {
            "input": [(
    (0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0)
)],
            "answer": "",
        },
        {
            "input": [(
    (1, 1, 1, 1, 1),
    (1, 1, 1, 1, 1),
    (1, 1, 1, 1, 1),
    (1, 1, 1, 1, 1),
    (1, 1, 1, 1, 1)
)],
            "answer": "abcdefghijklmnopqrstuvwxy",
        },
    ]
}
