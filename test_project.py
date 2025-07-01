from project import filterByDifficulty, findUniqueGuessChars, generateGuessedWord
import pandas as pd

def test_filterByDifficulty():
    df = pd.read_csv("/workspaces/95057829/CS50P/Final Project/words.csv")
    df.drop(columns=["id", "Part of Speech", "Length"], inplace=True)
    words = df["Word"].tolist()
    updatedEasyWords = filterByDifficulty(words, "easy")
    updatedMediumWords = filterByDifficulty(words, "medium")
    updatedHardWords = filterByDifficulty(words, "hard")
    updatedHellWords = filterByDifficulty(words, "hell")

    works = True
    for word in updatedEasyWords:
        if not (len(word) < 7):
            works = False
    for word in updatedMediumWords:
        if not (len(word) >= 7 and len(word) < 10):
            works = False
    for word in updatedHardWords:
        if not (len(word) >= 10 and len(word) < 13):
            works = False
    for word in updatedHellWords:
        if not (len(word) >= 13 and len(word) < 15):
            works = False
    assert works

def test_updateUniqueGuessChars():
    assert findUniqueGuessChars("hello") == ["h", "e", "l", "o"]
    assert findUniqueGuessChars("aaaaaaa") == ["a"]
    assert findUniqueGuessChars("google") == ["g", "o", "l", "e"]
    assert findUniqueGuessChars("mississippi") == ["m", "i", "s", "p"]
def test_generateGuessedWord():
    assert generateGuessedWord("instruction", ["n", "s", "t", "r", "u", "c", "o", "r"]) == "_nstruct_on"
    assert generateGuessedWord("hello", ["h", "a", "y"]) == "h____"
    assert generateGuessedWord("economically", ["e", "y", "l", "o", "n" , "m"]) == "e_onom___lly"
    assert generateGuessedWord("mississippi", ["m", "p", "s", "i"]) == "mississippi"
