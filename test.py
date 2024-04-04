from openai import OpenAI

# 設置你的 OpenAI API 金鑰

def generate_test(text):
    # 使用 OpenAI API 生成文章摘要
    response = client.chat.completions.create(
        model="gpt-4-0125-preview",  # 根据最新可用模型进行调整
        messages=[
            {"role": "system", "content": "You are a professional TOEIC question maker."},
            {"role": "user", "content": "Give me 10 TOEIC questions, the level is between 700 and 860 points, \
             the question type is sentence fill-in-the-blank, the answers to the questions should be randomly distributed, \
             can not all be A or B or C or D, when you generating the answers, please double check if it is truely make sense."}
        ],
        temperature = 0.5
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    client = OpenAI(api_key = 'your_key')
   
    word_test = generate_test("word")

    # 打印生成的摘要
    print(word_test)
