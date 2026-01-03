# main_app.py
#

# logic.py から必要な関数をインポート
from logic import check_word, respond

print("こんにちは。あなたの気持ちを話して下さい。（終了するには「またね」と入力）")

while True:
    user_input = input("あなた: ")

    # ユーザーが「またね」と入力したら終了
    if user_input == "またね":
        print("アプリ: またね。また話そうね👋")
        break

    try:
        # 1.logic.py の check_word 関数を呼び出し、入力をチェック
        #   ここで不適切な言葉が検出されると、ValueError が発生し、exceptブロックに飛びます。
        check_word(user_input) # 不適切ワードチェック

        # 2. 不適切がなければ、応答を生成して表示
        reply = respond(user_input)
        print(f"アプリ: {reply}")

    except ValueError as e:
        # 3. エラーが発生した場合、メッセージを表示
        print(f"🚨　エラー!: {e}")
        # エラー発生後も、会話を継続させます