import os
import random
import time
import sqlite3

#DataBase Connection
connection = sqlite3.connect('TicTacToe.db')
table_query = '''
    CREATE TABLE IF NOT EXISTS TicTacToe (
        name TEXT,
        score INTEGER
    )
'''
cursor = connection.cursor()
cursor.execute(table_query)


# Function to Show Database Content
def show_database_content():
    connection = sqlite3.connect('TicTacToe.db')
    cursor = connection.cursor()

    select_query = '''
        SELECT * FROM TicTacToe
    '''
    cursor.execute(select_query)

    rows = cursor.fetchall()

    if len(rows) > 0:
        print("\nDatabase content:")
        for row in rows:
            print(row)
    else:
        print("The table is empty.")


    connection.close()

#Function to add data to the DataBase
def database(p1,p2,score1=1,score2=-1):
    if check(p1):
        score1=1
        score2=-1
        query = '''
        Update TicTacToe
        Set score = score + ?
        WHERE name = ?
    '''
        cursor.execute(query,(score1,p1))
        if check(p2):
            query = '''
        Update TicTacToe
        Set score = score + ?
        WHERE name = ?'''
            cursor.execute(query,(score2,p2))
        else:
            query = '''
            INSERT INTO TicTacToe (score, name)
            VALUES (?, ?)
'''
            cursor.execute(score2,p2)
    else:
        query = '''
            INSERT INTO TicTacToe (score, name)
            VALUES (?, ?)
'''
        cursor.execute(score1,p1)
        if check(p2):
            query = '''
        Update TicTacToe
        Set score = score + ?
        WHERE name = ?'''
            cursor.execute(query,(score2,p2))
        else:
            query = '''
            INSERT INTO TicTacToe (score, name)
            VALUES (?, ?)
'''
            cursor.execute(score2,p2)

#Function to check in Particular Data is Present in DataBase or Not.
def check(name):
    select_query = '''
        SELECT * FROM TicTacToe
        WHERE name = ?
    '''

    cursor.execute(select_query, (name,))
    row = cursor.fetchone()
    return row

#Function to Draw TicTacToe
def draw():
        print(title)
        print("")
        print(" ",listt[0]," | ",listt[1]," | ",listt[2])
        print(" ——————————————")
        print(" ",listt[3]," | ",listt[4]," | ",listt[5])
        print(" ——————————————")
        print(" ",listt[6]," | ",listt[7]," | ",listt[8])
        print("")

#Function For X Player's Turn
def X_Turn():
        try:
            X=int(input("Player X's Turn : "))

            if listt[X-1]!="X" and listt[X-1]!="O":
                listt[X-1]="X"
                os.system("cls")
                draw()
                print("")
            else:
                print("Spot Already Taken \n")
                X_Turn()
        except:
            print("\nYour input Must be an Integer from 1 to 9 \n")
            X_Turn()

#Function For O Player's Turn   
def O_Turn():
        try:
            O=int(input("Player O's Turn : "))

            if listt[O-1]!="X" and listt[O-1]!="O":
                listt[O-1]="O"
                os.system("cls")
                draw()
                print("")
            else:
                print("Spot Already Taken \n")
                O_Turn()
        except:
            print("\nYour input Must be an Integer from 1 to 9 \n")
            O_Turn()
            
#Function to Check Winner.
def win():
        if (listt[0]== "X" and listt[1]== "X" and listt[2] == "X") or  (listt[3] == "X"and listt[4]== "X" and listt[5] == "X") or (listt[6]== "X" and listt[7] == "X"and listt[8] == "X") or (listt[0]== "X" and listt[3] == "X"and listt[6] == "X") or (listt[1]== "X" and listt[4] == "X"and listt[7] == "X") or (listt[2]== "X" and listt[5] == "X"and listt[8] == "X") or (listt[0] == "X"and listt[4]== "X" and listt[8] == "X") or (listt[2]== "X" and listt[4] == "X"and listt[6] == "X"):
            return "Player_X Won"
                   
        elif (listt[0] == "O"and listt[1] == "O"and listt[2] == "O") or  (listt[3] == "O"and listt[4]== "O" and listt[5] == "O") or (listt[6]== "O" and listt[7]== "O" and listt[8] == "O") or (listt[0]== "O" and listt[3]== "O" and listt[6] == "O") or (listt[1]== "O" and listt[4]== "O" and listt[7] == "O") or (listt[2]== "O" and listt[5] == "O"and listt[8] == "O") or (listt[0] == "O"and listt[4]== "O" and listt[8] == "O") or (listt[2]== "O" and listt[4] == "O"and listt[6] == "O"):
            return "Player_O Won"
        else:
            if listt.count("X")+listt.count("O")==9:
                return "Draw"
            else:
                return "Continue"

#Function for Computer to Always win
def minimax(board, depth, is_maximizing):
        if c=="O":
            scores = {
                "Player_X Won": -1,
                "Player_O Won": 1,
                "Draw": 0}
        else:
            scores = {
                "Player_X Won": 1,
                "Player_O Won": -1,
                "Draw": 0}
    
        result = win()
        if result in scores:
            return scores[result]
    
        if is_maximizing:
            best_score = float('-inf')
            for move in range(9):
                if board[move] != "X" and board[move] != "O":
                    board[move] = c
                    score = minimax(board, depth + 1, False)
                    board[move] = " "
                    best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for move in range(9):
                if board[move] != "X" and board[move] != "O":
                    if c=="O":
                        board[move] = "X"
                    else:
                        board[move] = "O"
                    score = minimax(board, depth + 1, True)
                    board[move] = " "
                    best_score = min(score, best_score)
            return best_score               

#Function For Computer's Turn                                  
def Comp_Turn():
        best_score = float('-inf')
        best_move = None        
        for move in range(9):
            if listt[move] != "X" and listt[move] != "O":
                listt[move] = c
                score = minimax(listt, 0, False)
                listt[move] = " "        
                if score > best_score:
                    best_score = score
                    best_move = move        
        listt[best_move] = c
        os.system("cls")
        draw()
        print()

#Function for selection of X or O by player 1        
def select():
        s=input("Enter 1 to Select 'X' \nEnter 2 to Select 'O' : ")
        if s=="1" or s=="2":
            return s            
        else:
            print("Wrong Input")
            return select()

#Function to decide which player will play first
def tooss():
        ran=random.randint(0,1)
        if ran==1:
            t="Heads"
        else:
            t="Tails"
        tos=input("Enter 1 for Heads\nEnter 2 for Tails : ")
        if tos=="1":
            t1="Heads"
            if t1==t:
                print("\nYou Won the Toss\n")
                return True
            else:
                print("\nYou Lost , as it was",t,"\n")
                return False
        elif tos=="2":
            t1="Tails"
            if t1==t:
                print("\nYou Won the Toss\n")
                return True
            else:
                print("\nYou Lost , as it was",t,"\n")
                return False
        else:
            print("Wrong Input")
            return tooss()

#GAME START
while True:
    print("\nWELCOME!\n\nTicTacToe Main Menu\n")
    game=(input("Enter 1 to play against Computer\nEnter 2 for Double Player\nEnter 3 to see Scores\nEnter any other key to Exit : "))
    
    if game=="1":  
        title="Playing VS Computer"      
        
        while True:
            listt=["1","2" ,"3","4","5","6","7","8","9"]
            os.system("cls")
            
            p1=input("Enter Player 1's Name : ")
            if check(p1):
                query = '''
        Update TicTacToe
        Set score = score + ?
        WHERE name = ?
    '''
            else:
                query = '''
    INSERT INTO TicTacToe (score, name)
    VALUES (?, ?)
'''
            
            os.system("cls")
            
            print("Playing VS Computer\n")
            
            s=select()
            if s=="1":
                c="O"
            elif s=="2":
                c="X"
            os.system("cls")
            
            toss=tooss()
            time.sleep(2)
            
            os.system("cls")
            
            if s=="1" and toss==True:
                draw()
                
                while win()=="Continue":
                    print("Player's Turn\n")
                    X_Turn()
                    if win()=="Player_X Won" or win()=="Draw":
                        break
                    Comp_Turn()
                    if win()=="Player_O Won" or win()=="Draw":
                        break
                if win()=="Player_X Won":
                    print(p1,"You Won")
                    score=1
                elif win()=="Player_O Won":
                    print("You Lost")
                    score=-1
                else:
                    print("Drawn")
                    score=0
            elif s=="1" and toss==False:            
                draw()
                
                while win()=="Continue":
                    Comp_Turn()
                    if win()=="Player_O Won" or win()=="Draw":
                        break
                    print("Player's Turn\n")
                    X_Turn()
                    if win()=="Player_X Won" or win()=="Draw":
                        break
                if win()=="Player_X Won":
                    print(p1,"You Won")
                    score=1
                elif win()=="Player_O Won":
                    print("You Lost")
                    score=-1
                else:
                    print("Drawn")
                    score=0
                
            elif s=="2" and toss==True:            
                draw()
                
                while win()=="Continue":
                    print("Player's Turn\n")
                    O_Turn()
                    if win()=="Player_O Won" or win()=="Draw":
                        break
                    Comp_Turn()
                    if win()=="Player_X Won" or win()=="Draw":
                        break
                if win()=="Player_O Won":
                    print(p1,"You Won")
                    score=1
                elif win()=="Player_X Won":
                    print("You Lost")
                    score=-1
                else:
                    print("Drawn")
                    score=0
                
            elif s=="2" and toss==False:            
                draw()
                
                while win()=="Continue":
                    Comp_Turn()
                    if win()=="Player_X Won" or win()=="Draw":
                        break
                    print("Player's Turn\n")
                    O_Turn()
                    if win()=="Player_O Won" or win()=="Draw":
                        break
                if win()=="Player_O Won":
                    print(p1,"You Won")
                    score=1
                elif win()=="Player_X Won":
                    print("You Lost")
                    score=-1
                else:
                    print("Drawn")
                    score=0

            cursor.execute(query,(score,p1))
            connection.commit()
                
            again=input("\nEnter 1 to play again\nEnter any other key for main menu : ") 
            if again=="1":
                pass
            else:
                os.system("cls")
                break                
            
            
    elif game=="2":               
        title="Playing Multiplayer"
        
        while True:
            listt=["1","2" ,"3","4","5","6","7","8","9"]
            os.system("cls")
            
            p1=input("Enter Player 1's Name : ")
            os.system("cls")
            
            print("Playing Multiplayer\n")
            
            print("Player 1 to Select\n")
            s=select()
            os.system("cls")
            
            if s=="2":
                print("Player 2 is 'X'\n")
            else:
                print("Player 2 is 'O'\n")
            p2=input("Enter Player 2's Name: ")
            os.system("cls")
            
            print("Player 2 to select\n")
            
            toss=tooss()
            time.sleep(2)
            
            os.system("cls")
            
            if s=="1" and toss==True:
                draw()
                
                while win()=="Continue":
                    print("Player 2's Turn\n")
                    O_Turn()
                    if win()=="Player_O Won" or win()=="Draw":
                        break
                    print("Player 1's Turn\n")
                    X_Turn()
                    if win()=="Player_X Won" or win()=="Draw":
                        break
                if win()=="Player_X Won":
                    print(p1,"Won")
                    database(p1,p2)

                elif win()=="Player_O Won":
                    print(p2,"Won")
                    database(p2,p1)
                else:
                    print("Drawn")
                    database(p1,p2,0,0)
                
            elif s=="1" and toss==False:
                draw()
                
                while win()=="Continue":
                    print("Player 1's Turn\n")
                    X_Turn()
                    if win()=="Player_X Won" or win()=="Draw":
                        break
                    print("Player 2's Turn\n")
                    O_Turn()
                    if win()=="Player_O Won" or win()=="Draw":
                        break
                if win()=="Player_X Won":
                    print(p1,"Won")
                    database(p1,p2)
                elif win()=="Player_O Won":
                    print(p2,"Won")
                    database(p2,p1)
                else:
                    print("Drawn")
                    database(p1,p2,0,0)
                
            elif s=="2" and toss==True:
                draw()
                
                while win()=="Continue":
                    print("Player 2's Turn\n")
                    X_Turn()
                    if win()=="Player_X Won" or win()=="Draw":
                        break
                    print("Player 1's Turn\n")
                    O_Turn()
                    if win()=="Player_O Won" or win()=="Draw":
                        break
                if win()=="Player_O Won":
                    print(p1,"Won")
                    database(p1,p2)
                elif win()=="Player_X Won":
                    print(p2,"Won")
                    database(p2,p1)
                else:
                    print("Drawn")
                    database(p1,p2,0,0)
                
            elif s=="2" and toss==False:
                draw()
                
                while win()=="Continue":
                    print("Player 1's Turn\n")
                    O_Turn()
                    if win()=="Player_O Won" or win()=="Draw":
                        break
                    print("Player 2's Turn\n")
                    X_Turn()
                    if win()=="Player_X Won" or win()=="Draw":
                        break
                if win()=="Player_O Won":
                    print(p1,"Won")
                    database(p1,p2,0,0)
                elif win()=="Player_X Won":
                    print(p2,"Won")
                    database(p2,p1)
                else:
                    database(p1,p2,0,0)
                    print("Drawn")
            connection.commit()
            again=input("\nEnter 1 to play again\nEnter anyother key for main menu : ") 
            if again=="1":
                connection = sqlite3.connect('TicTacToe.db')
                cursor = connection.cursor()
                os.system("cls")
                pass
            else:
                os.system("cls")
                break    
    elif game=="3":
        show_database_content()
        again=input("Enter 1 to play game! Else Quit : ")   
        if again=="1":
            
            pass
        else:
            break          
    else:
        connection.close()
        print("\nThank You for Playing...........\n")
        break