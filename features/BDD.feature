Feature: Checking winner's combination
Scenario: Сheck player combination for the winning one
  Given positions of X and O on the field and current player'{playerpos, curplayer}'
  Then check combinations '{playerpos, curplayer, combo}'
