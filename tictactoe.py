def print_board(arr):
    print(arr[0][0],'|',arr[0][1],'|',arr[0][2])
    print('- - - - - ')
    print(arr[1][0],'|',arr[1][1],'|',arr[1][2])
    print('- - - - - ')
    print(arr[2][0],'|',arr[2][1],'|',arr[2][2])
def validate_input(row,column,arr):
    if row > -1 and column > -1 and row < 3 and column < 3:
        if arr[row][column] == ' ':
            return True
    return False
def check_win(arr):
    if (arr[0][0] == arr[0][1] == arr[0][2] == 'X') or (arr[0][0] == arr[0][1] == arr[0][2] == 'O'):
        return True
    if (arr[1][0] == arr[1][1] == arr[1][2] == 'X') or (arr[1][0] == arr[1][1] == arr[1][2] == 'O'):
        return True
    if (arr[2][0] == arr[2][1] == arr[2][2] == 'X') or (arr[2][0] == arr[2][1] == arr[2][2] == 'O'):
        return True
    if (arr[0][0] == arr[1][1] == arr[2][2] == 'X') or (arr[0][0] == arr[1][1] == arr[2][2] == 'O'):
        return True
    if (arr[0][0] == arr[1][0] == arr[2][0] == 'X') or (arr[0][0] == arr[1][0] == arr[2][0] == 'O'):
        return True
    if (arr[0][1] == arr[1][1] == arr[2][1] == 'X') or (arr[0][1] == arr[1][1] == arr[2][1] == 'O'):
        return True
    if (arr[0][2] == arr[1][2] == arr[2][2] == 'X') or (arr[0][2] == arr[1][2] == arr[2][2] == 'O'):
        return True
    return False
def insert_value(user,row,column,arr):
    arr[row][column] = user
    return arr
if __name__=="__main__":
    arr = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
    print_board(arr)
    count = 1
    while count < 10:
        if count%2 == 0:
            user = 'O'
        else:
            user = 'X'
        row = int(input(f"Enter Row Number for {user}: "))
        column = int(input(f"Enter Column Number for {user}: "))
        if not validate_input(row,column,arr):
            print("Invalid Input ! Try Again !!")
            print_board(arr)
            continue
        arr = insert_value(user,row,column,arr)
        if check_win(arr):
            print_board(arr)
            print(f"{user} WINS !!")
            break
        print_board(arr)
        count += 1