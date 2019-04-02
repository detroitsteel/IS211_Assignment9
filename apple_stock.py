#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Top football touchdowns"""

from bs4 import BeautifulSoup
import csv
import urllib3

class scrapeWebPage():
    def __init__(self, url):
        self.http = urllib3.PoolManager()
        self.htmlseek = self.http.request('GET', url)
        self.htmlstatus = self.htmlseek.status
        self.htmlcde = self.htmlseek.data

def scrapeAppleStkPrice():
    """scrapeCBSSport Function - Play the game pig with unlimited players
    against unlimted number of computer players for a specificed time
    limit in seconds.
    The rules of Pig are simple.
    The game features at least two players, with the goal of reaching
    100 points first. Each turn, a player repeatedly rolls a die until
    either a 1 is rolled or the player holds and scores the sum of the
    rolls (i.e. the turn total). At any time during a player's turn,
    the player is faced with two decisions:
    roll ­ If the player rolls a 1: the player scores nothing and it becomes
    the opponent's turn. if the player rolls 2 ­ 6: the number is added to
    the player's turn total and the player's turn continues.
    hold ­ The turn total
    is added to the player's score and it becomes the opponent's turn.
    Args:
        numply (int): The number of human players who will play the game
        numcpu (int): The number of computer players who will play the game
        time (int): How long the game will last before a winner is declared

    Output: Game play according to the rules
    Example:
        >>> pigGame(2)
        >>>Player 1 current turn score is 0.
            1 roll(s) of the die returns 5.
            Roll again type R or to hold type H:h
            Next Player
            Player 2 turn.
            .....
            Player 1 turn.
            Player 1 score is currently 99.

            Player 1 current turn score is 0.
            26 roll(s) of the die returns 6.
            Next Player
            
            Times up. Player number 1 wins with a score of 15.
    """
    #exp_html = open('apple.html', 'w')
    #exp_html.write(self.htmlcde)
    #exp_html.close()
    with open('Apple.html') as fp:
        soup = BeautifulSoup(fp, "lxml")
    f = csv.writer(open("apple_stock.csv", "w"))
    f.writerow(["Close_Price", "Date"])
    remove = soup.thead
    remove.decompose()
    trs = soup.find_all('td')
    for tr in trs:
        #a = tr.find_all("a")
        tds = tr.find("td")
        print tr
        try:
            close = str(tr.get_text())
            date = str(tr.get_text())
            print (close, ' ', date, ' Newline \n')
            f.writerow([close,date])
        except:
            print "bad tr string"
            continue
    return

if __name__ == '__main__':
    url = 'https://www.nasdaq.com/symbol/aapl/historical'
    print url
    #d = scrapeWebPage()
    #print 'Saved URL'
    scrapeAppleStkPrice()
"""
    numoPlayers = int((raw_input("How many human players?\n")))
    numoComputes = int((raw_input("How many computer players?\n")))
    timePlay = int((raw_input("How long in seconds is this game?"
                              "(0 = Unlimited)")))
    if timePlay == 0:
        plyPigGame = Game(numoPlayers, numoComputes)
        plyPigGame.pigGame()
    elif timePlay > 0:
        time_Pig_Game = timedGameProxy(numoPlayers, numoComputes, timePlay)
        time_Pig_Game.timedPigGame()
"""
