
import mr

def test_high_score():
     data = [("bob", "A", "800"),
             ("bob", "B", "700"),
             ("bob", "A", "800"),
             ("bob", "B", "800"),
             ("bob", "C", "200"),
             ("bob", "C", "300"),

            ]

     assert mr.get_highest_mean_score(data) == "A"


def test_high_score2():
    data = [("bob", "A", "800"),
            ("bob", "B", "800"),
            ("bob", "A", "800"),
            ("bob", "B", "900"),
           ]
    assert mr.get_highest_mean_score(data) == "B"     