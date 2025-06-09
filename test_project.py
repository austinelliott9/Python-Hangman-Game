import project

def test_choose_category_valid(monkeypatch): # Checks for a valid category name
    categories = {"animals": ["cat", "dog"], "colors": ["red", "blue"]}
    monkeypatch.setattr("builtins.input", lambda _: "animals")
    assert project.choose_category(categories) == "animals"


def test_choose_category_invalid_then_valid(monkeypatch):
    inputs = iter(["animals", "blue", "colors"]) # Checks non-existant categories
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    assert project.choose_category({"colors": ["blue"]}) == "colors"


def test_get_guess_valid(monkeypatch): # Checks valid, unused guess (and capitalizes it)
    monkeypatch.setattr("builtins.input", lambda _: "a")
    assert project.get_guess(["B", "C"]) == "A"


def test_get_guess_invalid_then_valid(monkeypatch): # Checks non-alphabetical, multiple letters, and used letters as invalid guesses
    inputs = iter(["1", "aa", "A", "b"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    assert project.get_guess(["A"]) == "B"


def test_update_word_status_correct_guess(): # Checks that correct guess fills in multiple spots
    word = "TEST"
    guess = "T"
    status = ["_"] * len(word)
    project.update_word_status(word, guess, status)
    assert status == ["T", "_", "_", "T"]


def test_update_word_status_incorrect_guess(): # Checks that incorrect guess leaves word unchanged
    word = "TEST"
    guess = "A"
    status = ["T", "_", "_", "T"]
    project.update_word_status(word, guess, status)
    assert status == ["T", "_", "_", "T"]
