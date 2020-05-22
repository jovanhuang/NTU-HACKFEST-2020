import pandas as pd
from random import randint

# this is where the printing code resides


def showcard(sheetname):
    data = pd.read_excel(sheetname)
    df = pd.DataFrame(data, columns=['Questions', 'Answers'])
    number = randint(0, 6)
    question = df.loc[number, "Questions"]
    answer = df.loc[number, "Answers"]
    return question, answer




