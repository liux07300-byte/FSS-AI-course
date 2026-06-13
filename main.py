import random

def number_guessing_game():
    print("🎉 歡迎來到猜數字遊戲！ 🎉")
    
    # 讓程式隨機挑選一個 1 到 10 之間的數字
    secret_number = random.randint(1, 10)
    attempts = 0

    while True:
        try:
            # 取得使用者的輸入並轉換為整數
            guess = int(input("請猜一個 1 到 10 之間的數字："))
            attempts += 1
            
            # 檢查玩家猜的數字
            if guess < secret_number:
                print("📉 太小了，再試一次！")
            elif guess > secret_number:
                print("📈 太大了，再試一次！")
            else:
                print(f"🏆 恭喜你！你猜對了，答案就是 {secret_number}。")
                print(f"總共猜了 {attempts} 次。")
                break # 猜對了就結束迴圈
                
        except ValueError:
            # 如果使用者輸入的不是數字（例如字母），就會觸發這個錯誤處理
            print("⚠️ 請輸入有效的數字！")

# 啟動遊戲
if __name__ == "__main__":
    number_guessing_game()