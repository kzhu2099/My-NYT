# MyNYT

mynyt is a library that brings the New York Times to you.

Most users of the New York Times appreciate a quick and easy way to access news every day in the morning.
However. they find it difficult to customize based on their individual needs and preferences.
By making a Python library, anyone can easily customize their own NYT summary.

Furthermore, this library provides its own built in Wordle!

- HomePage: https://github.com/kzhu2099/My-NYT
- Issues: https://github.com/kzhu2099/My-NYT/issues

[![PyPI Downloads](https://static.pepy.tech/badge/mynyt)](https://pepy.tech/projects/mynyt)

Author: Kevin Zhu

## Features

- Collects news from different feeds of the NYT
- Processes and orders them, removing duplicates by title
- Converts it to a clean HTML
- Sends it to your email
- Allows for quick customization: feeds, emails, HTML, etc.
- Wordle class

## Installation

To install MyNYT, use pip: ```pip install mynyt```.

However, many prefer to use a virtual environment.

MacOS / Linux:

```sh
# make your desired directory
mkdir /path/to/your/directory
cd /path/to/your/directory

# setup the .venv (or whatever you want to name it)
pip install virtualenv
python3 -m venv .venv

# install mynyt
source .venv/bin/activate
pip install mynyt

deactivate # when you are completely done
```

Windows CMD:

```sh
# make your desired directory
mkdir C:path\to\your\directory
cd C:path\to\your\directory

# setup the .venv (or whatever you want to name it)
pip install virtualenv
python3 -m venv .venv

# install mynyt
.venv\Scripts\activate
pip install mynyt

deactivate # when you are completely done
```

## Usage

The most basic features can be found in the examples, but you must setup the emailing yourself (tutorial below).

```python
from mynyt import MyNYT

news = MyNYT('your.email@gmail.com', 'your appp pass word')

news.get_all_stories()

news.remove_duplicates(all_stories = None)

news.trim_to_length(length = 12)

news.convert_news_to_html()

news.send_email(recipient = 'your.email@gmail.com')
```

See ```CUSTOMIZATION.md``` for information on customization or examples for it in action.

## Tutorials

This project brings in many features that require tutorials on how to use.

### Emailing

Currently, there is only support for gmail. This library uses smtplib to send emails.
For it to work, the user will need to create an app password.

1) To create an app password, you need 2-Step Verification on your Google Account.

This can be through a variety of methods, whether it be through the Google Authenticator App, a secondary email, or a phone number

2) Create the app password

This link will direct you to your app passwords: https://myaccount.google.com/apppasswords.
They grant COMPLETE access to your account. If you do not have a Google Account or wish to use a different "junk" email, simply create a new google account.

Further help can be found here: https://support.google.com/mail/answer/185833?hl=en#:~:text=Important:%20To%20create%20an%20app,create%20a%20new%20app%20password.

### Automatic Execution

If you want a daily email with a snapshot of the NYT at a predetermined time, we have to use automation to make it happen.

#### Crontab: MacOS / Linux ONLY

Because this library provides a news summary of the most recent events, you can use it with a Crontab.
Crontab is available on Unix devices and is not for Windows users.

The format of ```minute hour day-of-month month day-of-week command``` allows us to have the following command:

```x y * * * ...``` will run at y:x o' clock (e.g.: if x was 30 and y was 18, it would be at 6:30 PM)

If you would like to have a daily email at 7:00 AM to run main.py, you could have the following command:

```
0 7 * * * cd /home/path/to/your/directory && .venv/bin/python3 main.py
```

For people that want to have two emails a day (at 7AM and 4PM), simply edit the crontab:

```
0 7,15 * * * cd /home/path/to/your/directory && .venv/bin/python3 main.py
```

If you did not use a venv, simply replace ```.venv/bin/python3``` with your path to python, like ```/path/to/your/python3``` or just ```python3``` if it was added to your path..

Visit https://crontab.guru/ to learn more.

#### Task Scheduler: Windows ONLY

Windows users must take a different approach with Task Scheduler.

Press Win + R, type taskschd.msc, and hit Enter.

Create a basic task and name it, choosing your preferred frequency (like daily). The start time can also be chosen, something like 7AM.
It will start a program, with the program ```C:\path\to\your\python.exe``` and argument ```C:\path\to\your\directory\main.py```.

Visit https://learn.microsoft.com/en-us/windows/win32/taskschd/task-scheduler-start-page to learn more.

## Wordle

Wordle is a game that is now owned by the NYT.
The aim is to guess a 5-letter word within 6 attempts.
When you guess the word, you will be given a color-coded result with the following key:

- Green is the correct letter in the correct spot
- Yellow is the correct letter but it is in a different spot
- Gray/White means that the letter is not in the word.

This game aims to mimic Wordle with thousands of available words.
To use it is very simple! Simply run:

```python
from mynyt import Wordle

game = Wordle()

game.play()
```

Guesses/words are not case sensitive.

You may pass in a custom word to guess for but it must be 5 letters, just like guesses.

It also must be part of the ```guess_list```. This is a list of words that are valid guesses, while ```word_list``` is a list of words that are valid starting points.
Randomly generated words are from the latter, because they are more well known. However, if you want to use a custom target, it must be part of guess_list.

To check if a word falls into either, use ```is_valid_word``` or ```is_valid_guess```

This means that you can guess with ```xylyl``` but it won't ever appear unless if you use ```game.play('xylyl')```.

See examples for more information.

## Disclaimer

This library, mynyt, retrieves publicly available news content via RSS feeds from the New York Times (NYT).
All news articles and content, are owned by the New York Times and are subject to their Terms of Service.
By using this library, you agree to comply with the New York Times' Terms of Service and all relevant copyright laws.

Wordle is owned by the NYT. This library provides a version of Wordle that mimics its behavior for personal and non-commercial use.

The content provided by this library is intended for personal (like sending emails to yourself) and non-commercial use only.
Redistribution, modification, or commercial use of the content retrieved from NYT is prohibited unless explicitly allowed by the New York Times.

## License

The License is an MIT License found in the LICENSE file.