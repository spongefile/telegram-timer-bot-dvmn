# Timer Bot

This project contains a bot for the Telegram messaging application. The bot sets a timer based on user input and provides a visual progress bar in the chat, which updates each second until the timer has finished.

## Dependencies

This bot requires Python 3.8 and the following libraries:

- python-telegram-bot
- pytimeparse

To install the required libraries, use pip:

```pip install python-telegram-bot pytimeparse```


## How to Use

### Environment Variables

To start the bot, you must provide a valid Telegram bot token and a chat ID as environment variables. These can be obtained by creating a bot on Telegram using BotFather and then starting a conversation with the bot.

```export TELEGRAM_TOKEN=<your_telegram_bot_token>```

```export TG_CHAT_ID=<your_chat_id>```


### Run the Bot

To start the bot, run:

```python main.py```

In the chat with your bot, send a message containing a time duration (like '30s' for 30 seconds, '10m' for 10 minutes, '1h' for 1 hour). The bot will then start a timer and send a message showing a progress bar, which it will update every second.

When the timer has finished, the bot will send a "Time's up" message.

## Project Structure

The project consists of two main files:

- `ptbot.py` - contains the Bot class, which provides methods for sending and updating messages, creating timers and countdowns, and starting the bot.

- `main.py` - contains the main logic for the bot, including callback functions for handling user input and notifying users when the timer is up. The file also contains the `render_progressbar` function, which creates a visual progress bar for the timer.

This project is written for educational purposes for an online web developer course, dvmn.org.
