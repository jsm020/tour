import curses # curses modulini import qilamiz
import datetime # datetime modulini import qilamiz

screen = curses.initscr() # ekranni boshqarish uchun screen obyektini yaratamiz
curses.curs_set(0) # kursorning ko'rinmasligini ta'minlaymiz
screen.timeout(100) # screenning yangilanish vaqtini belgilaymiz

while True: # abadiy sikl boshlaymiz
    now = datetime.datetime.now() # hozirgi vaqtni now o'zgaruvchisiga saqlaymiz
    time_str = now.strftime("%H:%M:%S") # soat formatini tanlaymiz va time_str o'zgaruvchisiga saqlaymiz
    screen.clear() # ekranni tozalaymiz
    screen.addstr(0, 0, time_str) # ekranga soatni chiqaramiz
    screen.refresh() # ekranni yangilaymiz
    key = screen.getch() # foydalanuvchi kiritgan tugmani key o'zgaruvchisiga saqlaymiz
    if key == ord('q'): # agar foydalanuvchi 'q' tugmasini bosgan bo'lsa
        break # sikldan chiqamiz

curses.endwin() # curses dasturini yakunlaymiz