# 初始化 15x15 的棋盤 (0 代表空位)
BOARD_SIZE = 15
board = [[0 for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

def print_board():
    """繪製棋盤"""
    print("   " + " ".join([f"{i:2}" for i in range(BOARD_SIZE)]))
    for r in range(BOARD_SIZE):
        row_str = f"{r:2} "
        for c in range(BOARD_SIZE):
            if board[r][c] == 0: row_str += " ＋"
            elif board[r][c] == 1: row_str += " ●" # 黑棋
            else: row_str += " ○"                 # 白棋
        print(row_str)

def check_win(r, c, player):
    """檢查是否五子連線"""
    directions = [(0, 1), (1, 0), (1, 1), (1, -1)] # 水平、垂直、對角線
    for dr, dc in directions:
        count = 1
        # 檢查正方向
        nr, nc = r + dr, c + dc
        while 0 <= nr < BOARD_SIZE and 0 <= nc < BOARD_SIZE and board[nr][nc] == player:
            count += 1
            nr, nc = nr + dr, nc + dc
        # 檢查反方向
        nr, nc = r - dr, c - dc
        while 0 <= nr < BOARD_SIZE and 0 <= nc < BOARD_SIZE and board[nr][nc] == player:
            count += 1
            nr, nc = nr - dr, nc - dc
        if count >= 5: return True
    return False

def play_game():
    current_player = 1 # 1 代表黑棋，2 代表白棋
    while True:
        print_board()
        print(f"現在輪到玩家 {current_player} ('●' if 1 else '○')")
        try:
            r = int(input("請輸入行號 (0-14): "))
            c = int(input("請輸入列號 (0-14): "))
            if board[r][c] != 0:
                print("⚠️ 這個位置已經有棋子了，請重試！")
                continue
        except (ValueError, IndexError):
            print("⚠️ 請輸入有效的範圍數字！")
            continue

        board[r][c] = current_player
        
        if check_win(r, c, current_player):
            print_board()
            print(f"🎉 恭喜玩家 {current_player} 獲勝！")
            break
            
        current_player = 2 if current_player == 1 else 1

if __name__ == "__main__":
    play_game()