# My Discord: d1n3x3z7
# My Github: https://github.com/d1n3x3z7
# My Discord Server: https://discord.gg/79P4Vew44D (тут можно помочь с разработкой, попросить помощи или просто найти друзей)

# Если у вас будет желание что-либо изменить в этом коде, обращайтесь ко мне в дискорд

from pathlib import Path

from random import choice
from random import shuffle

from termcolor import cprint

from tkinter import Tk
from tkinter.filedialog import askopenfile

from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options

cwd = Path(__file__).parent.resolve()

Tk().withdraw()

cprint('---------------------------------------------------------------------------------------------',color='magenta')
cprint('!ВНИМАНИЕ!',color='red',on_color='on_light_grey',attrs=('underline','bold'))
cprint('Репорт бот не был достаточно протестирован и результаты его использования точно неизвестны.',color='yellow', on_color='on_grey')
cprint('О своих результатах использования можете писать сюда: https://discord.gg/M7udGmfNzk',color='light_green')
cprint('---------------------------------------------------------------------------------------------\n',color='magenta')

id = input('Введи ID жертвы: ')

cprint('\nВыбери файл с печеньками (.txt)',color='cyan')
cookies = askopenfile(title='Выбери файл с печеньками', initialdir=cwd, filetypes=[("Text Files", "*.txt")]).read().split()

cprint('\nТеперь выбери файл с комментариями к репортам',color='cyan')
comments = askopenfile(title='Выбери файл с комментариями', initialdir=cwd, filetypes=[("Text Files", "*.txt")]).read().split()

shuffle(cookies)
shuffle(comments)

opts = Options()
opts.add_argument('--headless')
opts.add_argument('--no-sandbox')
opts.add_argument('--log-level=3')
opts.page_load_strategy = 'normal'

session = webdriver.Chrome(options=opts) # возможно использование Firefox\Edge\Chrome
session.maximize_window()

for cookie in cookies:
    session.get('https://www.roblox.com/home')

    session.delete_all_cookies()

    session.add_cookie({'name':'.ROBLOSECURITY', 'value': cookie, 'path':'/', 'domain':'.roblox.com','secure':True,'httpOnly':True})

    session.refresh()

    session.get(f'https://www.roblox.com/abusereport/userprofile?id={id}&redirecturl=https%3a%2f%2fwww.roblox.com%2fusers%2f{id}%2fprofile')

    reason = Select(session.find_element(By.ID, 'ReportCategory'))
    reason.select_by_value('3')

    comment = session.find_element(By.XPATH, '//*[@id="Comment"]')
    comment.click()

    comment_text = choice(comments)
    comment.send_keys(comment_text)

    send_report = session.find_element(By.XPATH, '//*[@id="report-abuse"]')
    send_report.click()

cprint('Нажми Enter...', color='black',on_color='on_white')