print("コンピュータと一緒にじゃんけんをしよう")
print("1がグー、2がチョキ、3がパーです＊小文字で入力してください")
print("ゲームを続ける場合はyes、終了する場合はnoを入力してください")
import random

def get_user_choice():
    user_choice = input("じゃんけん：(1) グー (2) チョキ (3) パー: ")
    if user_choice in ["1", "2", "3"]:
        return int(user_choice)
    else:
        print("無効な選択です。1から3の数字を選んでください。")
        return get_user_choice()

def get_computer_choice():
    return random.randint(1, 3)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "引き分け"
    elif (
        (user_choice == 1 and computer_choice == 2) or
        (user_choice == 2 and computer_choice == 3) or
        (user_choice == 3 and computer_choice == 1)
    ):
        return "勝ち"
    else:
        return "負け"

while True:
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    
    print(f"あなたの選択: {user_choice}")
    print(f"コンピュータの選択: {computer_choice}")
    
    result = determine_winner(user_choice, computer_choice)
    print(f"結果: {result}")
    
    play_again = input("もう一度プレイしますか？(yes/no): ")
    if play_again.lower() != "yes":
        break
