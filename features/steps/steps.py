from behave import *


@given('positions of X and O on the field and current player"{playerpos, curplayer}"')
def step(playerpos, curplayer):
    print(playerpos)
    print(curplayer)


@then('check combinations "{playerpos, curplayer, combo}"')
def step1(playerpos, curplayer, combo):
    for i in combo:
        if all(j in playerpos[curplayer] for j in i):
            print("You win!")
            return True
    return False


if __name__ == '__main__':
    combo = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
    step({'X': [1, 3, 5, 7, 9], 'O': [2, 4, 6]}, 'X')
    step1({'X': [1, 3, 5, 7, 9], 'O': [2, 4, 6]}, 'X', combo)