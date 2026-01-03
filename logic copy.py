# logic.py

import datetime
import random

# ★ 新規追加関数 1: ユーザーの状況を詳細に記録する関数
def collect_detailed_context():
    print("\n--- 状況の詳細を入力して下さい ---")

    when = input("いつ (例: 昨日、今日の午後) : ")
    where = input("どこで (例: 職場、自宅、電車内) : ")
    who = input("誰に・誰から (例: 上司、友達) : ")
    action = input("どんな言動をされたか (例: 当たり前だと言われた) : ")
    feeling = input("その時、どんな気分か (例: 絶望、怒り) : ")

    context_data = {
        "timestamp": str(datetime.datetime.now()),
        "when": when,
        "where": where,
        "who": who,
        "action": action,
        "feeling": feeling,

    }

    print("\n🚨 状況データが収集されました 🚨")
    for key, value in context_data.items():
        print(f"{key}: {value}")

    return context_data


# ★ 新規追加関数 2: 応答を関西弁(混合)に変換
def convert_to_kansai_hybrid(response_message):

    if response_message.endswith("ですよ。"):
        return response_message.replace(
            "ですよ。", random.choice(["ですよ。", "ですわ。", "やわ。"])
        ）

　　if response_message.endswith("ますね。"):

return response_message.replace(

            "ますね。", random.choice(["ますね。", "ますわ。", "ますやん。"])

        )



    if response_message.endswith("てね。"):

        return response_message.replace(

            "てね。", random.choice(["てな。", "ってや。"])

        )



    response_message = response_message.replace("とても", "めっちゃ")



    return response_message





# 3. 不適切ワードチェック関数

def check_word(message):



    bad_word = ["ばか", "死ね", "うざい"]



    for word in bad_word:

        if word in message:



            context = collect_detailed_context()



            raise ValueError(f"不適切な言葉が含まれています: '{word}'")



    return True





# 応答生成関数

def respond(message):



    responses = {

        "こんにちは": "こんにちは！今日もお疲れ様です😊",

        "疲れた": "無理しないでくださいね。少し休むのも大事です🍵",

        "ありがとう": "こちらこそ、話してくれて嬉しいです🌸"

    }



    reply_message = responses.get(message, "うん、そうなんですね。")



    reply_message_kansai = convert_to_kansai_hybrid(reply_message)



    return reply_message_kansai