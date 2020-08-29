#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 11:30:54 2019

@author: jahnvirc
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" 
Created on Sun Oct 20 13:47:06 2019

@author: jahnvirc
"""
def jump_or_not(touple):
        bm = [list(item) for item in touple]
        y1_diff = 0
        y2_diff = 0
        for x in range(0,len(bm[0])-1):
            for y in range (0,len(bm)-1):
                y1_diff = bm[y+1][x] - bm[y][x]
                y2_diff = bm[y+1][x+1] - bm[y][x+1]
        y1_diff = abs(y1_diff)
        y2_diff = abs(y2_diff)
        return y1_diff,y2_diff
import time
import math
class Board:
    black_gola_list = []
    white_gola_list = []  
    player =0
    grid = []
    run_time = 0.0
    grid_str = []
    fp = open(r"input2.txt","r")
    play_game = fp.readline().rstrip()
    colour = fp.readline().rstrip()
    run_time = float(fp.readline().rstrip())
    for i in range(0,16):
        val = fp.readline().rstrip()
        grid_str = list(val)
        grid.append(grid_str) 
    fp.close()

    
    if colour =='BLACK':
        player =1
    elif colour =='WHITE':
        player =2
    def __init__(self):
        self.board_size = 16
        self.white_team = []
        self.black_team = []
        self.turn = 1
        self.player_list = []
        self.chosenMove = 0
        self.original_board = [['B','B','B','B','B','.','.','.','.','.','.','.','.','.','.','.'],
                               ['B','B','B','B','B','.','.','.','.','.','.','.','.','.','.','.'],
                               ['B','B','B','B','.','.','.','.','.','.','.','.','.','.','.','.'],
                               ['B','B','B','.','.','.','.','.','.','.','.','.','.','.','.','.'],
                               ['B','B','.','.','.','.','.','.','.','.','.','.','.','.','.','.'],
                               ['.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.'],
                               ['.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.'],
                               ['.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.'],
                               ['.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.'],
                               ['.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.'],
                               ['.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.'],
                               ['.','.','.','.','.','.','.','.','.','.','.','.','.','.','W','W'],
                               ['.','.','.','.','.','.','.','.','.','.','.','.','.','W','W','W'],
                               ['.','.','.','.','.','.','.','.','.','.','.','.','W','W','W','W'],
                               ['.','.','.','.','.','.','.','.','.','.','.','W','W','W','W','W'],
                               ['.','.','.','.','.','.','.','.','.','.','.','W','W','W','W','W']]
        self.board = self.grid
        
            
    def set_board(self, new_board):
        self.board = new_board.copy()
        
    def Turns(self):
        if self.turn == 1:
            self.turn = 2
        else:
            self.turn = 1
            
    def get_white_team(self):
        for i in range (0,16):
            for j in range(0,16):
                if(self.original_board[i][j]=='W'):
                    self.white_team.append((i,j))
        return self.white_team
    def get_black_team(self):
        for i in range (0,16):
            for j in range(0,16):
                if(self.original_board[i][j]=='B'):
                    self.black_team.append((i,j))
        return self.black_team
                    
    def get_black_places(self):
        black_gola_list = []
        for i in range(0, 16):
            for j in range(0, 16):
                if (self.board[i][j]) == 'B':
                    black_gola_list.append((i, j))
        return black_gola_list

    def get_white_places(self):
        white_gola_list = []
        for i in range(0, 16):
            for j in range(0, 16):
                if self.board[i][j] == 'W':
                    white_gola_list.append((i,j))
        return white_gola_list
                
    def check_winner(self):
        blackWin = False
        whiteWin = False
        for locations in self.white_team:
            #print(locations)
            if self.board(locations[0], locations[1]) == 'W' or self.board(locations[0], locations[1]) == '.':
                blackWin = False
                break
            elif self.board(locations[0], locations[1]) == 'B':
                blackWin = True
        for locations in self.black_team:
            if self.board(locations[0], locations[1]) == 'B' or self.board(locations[0], locations[1]) == '.':
                whiteWin = False
                break
            elif self.board(locations[0], locations[1]) == 'W':
                whiteWin = True
        rtn = (blackWin, whiteWin)
        return rtn
    
    def get_board(self):
        return self.board
    
    def print_board(self):
        print(self.board)
    
    def move_piece(self, start_point, end_point):
        temp = self.board[start_point[0]][start_point[1]]
        self.board[start_point[0]][start_point[1]] = '.'
        self.board[end_point[0]][end_point[1]] = temp
        

class Gola:
    def __init__(self, player, board, gola_depth):
        self.board = board
        self.player = player
        self.gola_value = 0
        self.gola_depth = gola_depth
        self.move = 0
        self.children = []
        
    def get_depth(self):
        return self.gola_depth

    def get_player(self):
        return self.player

    def set_value(self, value):
        self.gola_value = value

    def get_value(self):
        return self.gola_value

    def get_board(self):
        return self.board


class Game_play:
    dict_neighbour = {}
    def __init__(self, timeLimit):
        self.visited = []
        self.timeLimit = timeLimit
        self.start = 0.0
        self.end = 0.0
        self.pruned_nodes = 0
        self.boards = 0
        self.follow_jump = 0
        self.check_more_jumps = False
    def neighbour_search(self, row, col, board):
        dr = [-1,+1,+1,-1,-1,+1,0,0]
        dc = [-1,+1,-1,+1,0,0,+1,-1]
        neighbours = []
        gameboard = Board()
        
        if row >= len(board) or col >= len(board):
            return
        if row < 0 or col < 0:
            return
        if board[row][col] == 0:
            return
        for i in range(0,8):
            row_next = row + dr[i]
            col_next= col + dc[i]
            if (row_next) >=len(board) or (col_next) >= len(board[0]):
                continue
            if (row_next) < 0 or (col_next) < 0:
                continue
            if (board[row_next][col_next] == '.'):
                if (board[row][col] == 'W' and (row, col) not in gameboard.white_team):
                    if ((row_next,col_next) in gameboard.white_team):
                        continue

                if (board[row][col] == 'B' and (row, col) not in gameboard.white_team):
                    if ((row_next,col_next) in gameboard.white_team):
                        continue
                neighbours.append((row_next,col_next))
                self.dict_neighbour['E']= (row_next,col_next)
        neighbours.extend(self.jump_search(row, col, board))
        self.dict_neighbour['J']= self.jump_search(row, col, board)
        return neighbours
    
    def jump_search(self, row, col, board):
        dr = [-1,+1,+1,-1,-1,+1,0,0]
        dc = [-1,+1,-1,+1,0,0,+1,-1]
        jump = []
        gameboard = Board()
        for i in range(0,8):
                if (row + dr[i]) >=len(board) or (col + dc[i]) >= len(board[0]):
                    continue
                if (row + dr[i]) < 0 or (col + dc[i]) < 0:
                    continue
                if (board[row + dr[i]][col + dc[i]] != '.'):
                    row_jump = row + 2*dr[i]
                    col_jump= col + 2*dc[i]
                    if (row_jump) >= len(board) or (col_jump) >= len(board[0]):
                        continue
                    if (row_jump) < 0 or (col_jump) < 0:
                        continue
                    if (board[row_jump][col_jump] == '.' and (row_jump,col_jump) not in self.visited):
                        if (board[row][col] == 'W' and (row, col) not in gameboard.white_team):
                            if ((row_jump, col_jump) in gameboard.white_team):
                                continue
                        if (board[row][col] == 'B' and (row, col) not in gameboard.black_team):
                            if ((row_jump, col_jump) in gameboard.black_team):
                                continue
                        self.visited.append((row, col))
                        jump.append((row_jump, col_jump))
                        future_jumps = self.jump_search(row_jump, col_jump, board)
                        jump.extend(future_jumps)
        return jump

    def distance(self,start_point, end_point):
        return math.sqrt((end_point[0]-start_point[0])**2 + (end_point[1]-start_point[1])**2)
    
    def utility(self, gola):
        gameboard = gola.board
        winner = gameboard.check_winner()
        data_board = gameboard.get_board()
        distanceList = []
        value = 0
        black = 0
        white = 0
        for col in range(0,16):
            for row in range(0,16):
                tile = data_board[row][col]
                if tile == 'W':
                    for goals in gameboard.black_team:
                        if data_board[goals[0]][goals[1]] != 'W':
                            distanceList.append(self.distance((row,col),goals))
                    if len(distanceList):
                        white += max(distanceList)  
                    else: 
                        white += -100
                elif tile == 'B':
                    for goals in gameboard.white_team:
                        if data_board[goals[0]][goals[1]] != 'B':
                            distanceList.append(self.distance((row,col),goals))  
                    if len(distanceList):
                        black += max(distanceList)  
                    else:
                        black +=- 100
        if gola.player == 1:
            value = black/white
        else:
            value = white/black
        if winner[0]:
            value = float("inf")
        elif winner[1]:
            value = float("inf")
        return value
    
    def alphaBetaMinimax(self, gola):
        self.start = time.time()
        max_gola, best_move = self.maxValue(gola, float("-inf"), float("inf"))
        data_board = gola.get_board()
        if best_move != None:
            data_board.move_piece(best_move[0], best_move[1])
        print("Time:", self.end - self.start)
        self.pruned_nodes = 0
        self.boards = 0
        data_board.chosenMove = best_move
        data_board.Turns()
        print("Best move",best_move)
        coord = []
        y1_diff,y2_diff = jump_or_not(best_move)
        if y1_diff==2 or y2_diff==2 or (y1_diff ==2 and y2_diff==2):
                coord.append('J')
                coord.extend([t[::-1] for t in best_move])
        elif y1_diff==1 or y2_diff==1 or (y1_diff ==1 and y2_diff==1):
                coord.append('E')
                coord.extend([t[::-1] for t in best_move])
        return max_gola, best_move,coord
    
    def print_output(self,gola):
        mg,best_move,coord =  self.alphaBetaMinimax(gola)  
        out = []
        coordinates = str(coord)
        coordinates = coordinates.replace('(', '')
        coordinates = coordinates.replace(')', '')
        coordinates = coordinates.replace('[', '')
        coordinates = coordinates.replace(']', '')
        coordinates = coordinates.replace("'", '')
        coordinates = coordinates.replace(',','')
        out.extend(list(coordinates))
        count = 0
        print(out)
        for i in range (0,len(out)):
            if out[i] == ' ':
                count +=1
                if count%2 == 0:
                    out[i]= ','
        
        return out,best_move
    
    def maxValue(self, gola, alpha, beta):
        return_gola = gola
        self.end = time.time()
        board = gola.get_board()
        winner = board.check_winner()
        best_move = None
        if (winner[0] == True or winner[1] == True or gola.get_depth() <= 0 or self.end - self.start > self.timeLimit):
            evaluation = self.utility(gola)
            gola.set_value(evaluation)
            return gola, best_move
        player = gola.get_player()
        if player == 1:
            player_positions = board.get_black_places()
            team_positions = board.get_black_team()
            goal_positions = board.get_white_team()
        elif player == 2:
            player_positions = board.get_white_places()
            team_positions = board.get_white_team()
            goal_positions = board.get_black_team()
        #print(goal_positions)
        value = float("-inf")
        data_board = board.get_board()
        board = gola.get_board()
        checkpoint = False
        for move in player_positions:
            if move in goal_positions:
                continue 
            if self.check_more_jumps == False:
                legal_moves = self.neighbour_search(move[0], move[1], data_board)
            elif self.check_more_jumps == True:
                legal_moves = self.neighbour_search(self.follow_jump, move[1], data_board)
            if move in team_positions:
                for move in team_positions:
                    legal_moves = self.neighbour_search(move[0], move[1], data_board)
                    
                    if len(legal_moves) == 0:
                        self.check_more_jumps == False
                        checkpoint = True
                        continue
                    for legal_move in legal_moves:
                        checkpoint = False
                        self.end = time.time()
                        if(self.end-self.start > self.timeLimit):
                            return gola, best_move
                        self.boards += 1
                        board_copy = Board()
                        board_copy.set_board(data_board)
                        board_copy.move_piece(move, legal_move)
                        next_gola = Gola(player, board_copy, gola.get_depth() - 1)
                        next_gola.move = (move, legal_move)
                        child_gola, _ = self.minValue(next_gola, alpha, beta)
                        board_copy.move_piece(legal_move, move)
                        if (value < child_gola.get_value()):
                            moveFrom = move
                            moveTo = legal_move
                            best_move = (moveFrom, moveTo)
                        value = max(value, child_gola.get_value())
                        return_gola = next_gola
                        if value > beta:
                            self.pruned_nodes += 1
                            return_gola.set_value(beta)
                            return return_gola, None
                        alpha = max(alpha, value)
                    
                    
                    
                    
                    
                    
                    
            if len(legal_moves) == 0:
                self.check_more_jumps == False
                continue
                checkpoint = True
            for legal_move in legal_moves:
                checkpoint = False
                self.end = time.time()
                if(self.end-self.start > self.timeLimit):
                    return gola, best_move
                self.boards += 1
                board_copy = Board()
                board_copy.set_board(data_board)
                board_copy.move_piece(move, legal_move)
                next_gola = Gola(player, board_copy, gola.get_depth() - 1)
                next_gola.move = (move, legal_move)
                child_gola, _ = self.minValue(next_gola, alpha, beta)
                board_copy.move_piece(legal_move, move)
                if (value < child_gola.get_value()):
                    moveFrom = move
                    moveTo = legal_move
                    best_move = (moveFrom, moveTo)
                value = max(value, child_gola.get_value())
                return_gola = next_gola
                if value > beta:
                    self.pruned_nodes += 1
                    return_gola.set_value(beta)
                    return return_gola, None
                alpha = max(alpha, value)
        if checkpoint == True:
            for move in goal_positions:
               legal_moves = self.neighbour_search(move[0], move[1], data_board)
               if len(legal_moves) == 0:
                    continue
               for legal_move in legal_moves:
                    self.end = time.time()
                    if(self.end-self.start > self.timeLimit):
                        return gola, best_move
                    self.boards += 1
                    board_copy = Board()
                    board_copy.set_board(data_board)
                    board_copy.move_piece(move, legal_move)
                    next_gola = Gola(player, board_copy, gola.get_depth() - 1)
                    next_gola.move = (move, legal_move)
                    child_gola, _ = self.minValue(next_gola, alpha, beta)
                    board_copy.move_piece(legal_move, move)
                    if (value < child_gola.get_value()):
                        moveFrom = move
                        moveTo = legal_move
                        best_move = (moveFrom, moveTo)
                    value = max(value, child_gola.get_value())
                    return_gola = next_gola
                    if value > beta:
                        self.pruned_nodes += 1
                        return_gola.set_value(beta)
                        return return_gola, None
                    alpha = max(alpha, value)
        return_gola.set_value(value)
        return return_gola, best_move

    def minValue(self, gola, alpha, beta):
        return_gola = gola
        self.end = time.time()
        board = gola.get_board()
        win_detect = board.check_winner()
        best_move = None
        if (win_detect[0] == True or win_detect[1] == True or gola.get_depth() <= 0 or self.end - self.start > self.timeLimit):
            evaluation = self.utility(gola)
            gola.set_value(evaluation)
            return gola, best_move
        player = gola.get_player()
        if player == 1:
            player_positions = board.get_black_places()
            goal_positions = board.get_white_team()
        elif player == 2:
            player_positions = board.get_white_places()
            goal_positions = board.get_black_team()
        value = float("inf")
        data_board = board.get_board()
        for move in player_positions:
            if move in goal_positions:
                continue
            legal_moves = self.neighbour_search(move[0], move[1], data_board)
            if len(legal_moves) == 0:
                continue
            for legal_move in legal_moves:
                self.end = time.time()
                if (self.end - self.start > self.timeLimit):
                    return gola, best_move
                self.boards += 1
                board_copy = Board()
                board_copy.move_piece(move, legal_move)
                next_gola = Gola(player, board_copy, gola.get_depth() - 1)
                next_gola.move = (move, legal_move)
                child_gola, _ = self.maxValue(next_gola, alpha, beta)
                board_copy.move_piece(legal_move, move)
                if (value > child_gola.get_value()):
                    moveFrom = move
                    moveTo = legal_move
                    best_move = (moveFrom, moveTo)
                value = min(value, child_gola.get_value())
                return_gola = next_gola
                if value < alpha:
                    self.pruned_nodes += 1
                    return_gola.set_value(value)
                    return return_gola, None
                beta = min(beta, value)
        return_gola.set_value(value)
        return return_gola, best_move

def convert_to_list(string): 
    li = list(string.split(" ")) 
    return li 

def main():
    fw = open("output.txt","w")   
    game = Board()
    output = []
    flag = True
    run_time = game.run_time
    player = game.player
    player1 = Game_play(run_time)
    myBoard = Board()
    myNode = Gola(player, myBoard, 3)
    #max_gola , best_move = player1.alphaBetaMinimax(myNode)
    output,best_move = player1.print_output(myNode)
    for i in output:
        fw.write(i)
    while(flag):
        if output[0]=='J':
            player1.check_more_jumps = True
            player1.follow_jump = best_move[1]
            game.move_piece(best_move[0],best_move[1])
            fw.write('\n')
            myNode = Gola(player, myBoard, 2)
            game.print_board
            output,best_move = player1.print_output(myNode)
            for i in output:
                fw.write(i)
        elif output[0]=='E':
            flag = False
    fw.close   
if __name__ == "__main__":
    main()

