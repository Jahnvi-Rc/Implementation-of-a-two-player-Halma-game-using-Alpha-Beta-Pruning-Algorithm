# Implementation-of-a-two-player-Halma-game-using-Alpha-Beta-Pruning-Algorithm

Language: Python 3.7
Libraries: None

Description:
* Fostered a min-max Alpha Beta Pruning Algorithm that aids in the calculation of next move by predicting multiple moves ahead and choosing the best of them
* Implemented upto depth = 1(higher precision in move calculation) of the tree and was able to achieve results in minimum time.

Problem Statement:

In this project, we will play the game of Halma, an adversarial game with some similarities to checkers. The game uses a 16x16checkered gameboard. Each player starts with 19 game pieces clustered in diagonally opposite corners of the board. To win the game, a player needs to transfer all of their pieces from their starting corner to the opposite corner, into the positions that were initially occupied by the opponent. Note that this original rule of the game is subject to spoiling, as a player may choose to not move some pieces at all, thereby preventing the opponent from occupying those locations. Note that the spoiling player cannot win either (because some pieces remain in their original corner and thus cannot be used to occupy all positions in the opposite corner). Here, to prevent spoiling, we modify the goal of the game to be to occupy all of the opponent’s starting positionswhich the opponent is not still occupying.
-Simple wooden pawn-style playing pieces, often called "Halma pawns."
-The board consists of a grid of 16×16 squares.
-Each player's camp consists of a cluster of adjacent squares in one corner of the board. These camps are delineated on the board.
-For two-player games, each player's camp is a cluster of 19 squares. The camps are in opposite corners.
-Each player has a set of pieces in a distinct color, of the same number as squares in each camp.
-The game starts with each player's camp filled by pieces of their own colour.

About:
Halma1.py - Run this code with the initial state of the board already given.
          - The Opponent Move is done using the other code or same code as oponent separately.
   
Homework2.pdf - The Problem statement with rules and unput format. 


