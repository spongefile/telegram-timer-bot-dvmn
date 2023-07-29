import ptbot
import os
from pytimeparse import parse

TG_TOKEN = os.getenv('TELEGRAM_TOKEN') 
TG_CHAT_ID = os.getenv('TG_CHAT_ID')  
bot = ptbot.Bot(TG_TOKEN)

def wait(chat_id, question):
    reply_secs = parse(question)
    message_id = bot.send_message(chat_id, "Remaining seconds: {}\n{}".format(
        reply_secs, render_progressbar(reply_secs, 0)))
    bot.create_countdown(reply_secs, notify_progress, chat_id=chat_id, 
                         message_id=message_id, reply_secs=reply_secs)
    bot.create_timer(reply_secs, notify, chat_id=chat_id)

def notify_progress(secs_left, chat_id, message_id, reply_secs):
    bot.update_message(chat_id, message_id, 
                       "Remaining seconds: {}\n{}".format(secs_left, 
                        render_progressbar(reply_secs, (reply_secs - secs_left))))

def render_progressbar(total, iteration, prefix='', suffix='', length=30, 
                       fill='█', zfill='░'):
    iteration = min(total, iteration)
    percent = "{0:.1f}"
    percent = percent.format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    pbar = fill * filled_length + zfill * (length - filled_length)
    return '{0} |{1}| {2}% {3}'.format(prefix, pbar, percent, suffix)

def notify(chat_id):
    bot.send_message(chat_id, "Time's up")

bot = ptbot.Bot(TG_TOKEN)
bot.reply_on_message(wait) 
bot.run_bot()
