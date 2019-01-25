import time
import telepot
import pickle
from telepot.loop import MessageLoop

with open('model.pkl', 'rb') as f:
    model_loaded = pickle.load(f)


def predict(content, model=model_loaded):
    return model.predict_proba([content])[0]


def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)

    if content_type == "text":
        content = msg["text"]
        input = "Input    : {}\n".format(content)
        prob_list = predict(content)
        review = 'positive' if prob_list[0] < prob_list[1] else 'negative'
        output = "Output : This is a {} review!  ({:.2f})".format(review, prob_list[1])
        return_msg = input + output
        bot.sendMessage(chat_id, return_msg)


if __name__ == "__main__":
    bot = telepot.Bot('')
    MessageLoop(bot, handle).run_as_thread()

    while True:
        time.sleep(10)
