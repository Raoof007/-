"""
سلام
من رئوف زرهی نساج هستم
پایه نهم
تاریخ 27/2/1403
مسابقه علمی پژوهشی پژوهش سرای دانش آموزی
شهرستان دزفول
این بازی Football Buttons
نام دارد
که به زبان شیرین فارسی
فوتبال کلیدی
نام دارد
"""
'''
بازی به این صورت کار میکند:
به صفحه شروع میرویم
حال در صفحه شروع سه کلید وجود دارد شروع ، تنظیمات و خروج 
اگر خروج را زد که از بازی خارج و اگر شروع را زد وارد بازی می شویم

شروع : 
کنترل 2 بازیکن با کلید های سیستم انجام می شود
گروه 1 با کلید های : چپ ، راست ، بالا ، پایین
و گروه 2 با کلید های : A,S,D,W

و بازی فوتبال انجام میشود

تنظیمات :
حاوی کنترل برخی تنظیمات است که با حالت های فعال یا غیر فعال یا رنگ های مختلف است

اجرای برنامه با اندازه کل صفحه : با حالت غیر فعال
رنگ گروه اول : با رنگ قرمز
رنگ گروه دوم : با رنگ آبی

خروج :
برای خروج از بازی
'''
# -----------------------------------------------
# کتاب خانه های مورد نیاز
from pygame import *
from pygame.mouse import *
# سه کتابخانه دست نوشته که در فایل هایی که کنار این فایل قرار گرفت اند وجود دارند
# این سه کتابخانه توابع ، تنظیمات و صفحه اجرای بازی قرار دارند
# توابع
from definitions import *
# کنترل تنظیمات
from ControlSetting import *
# صفحه بازی
from Game import *
import sys

def Loading():
    colors = [(255, 0, 0), (255, 165, 0), (255, 255, 0), (0, 128, 0), (0, 0, 255), (75, 0, 130), (238, 130, 238), (255, 255, 255)]
    progress = 0
    font_S = font.SysFont(None, 33)
    init()

    width, height = 800, 600
    screen = display.set_mode((width, height))

    display.set_caption("Loading Page")
    clock = time.Clock()
    while progress <= 100:
        for h in event.get():
            if h.type == QUIT:
                quit()
                sys.exit()

        color_index = progress % len(colors)
        screen.fill(colors[color_index])

        draw.rect(screen, (255, 165, 0), (100, height//2-20, progress*6, 40))
        draw.rect(screen, (255, 255, 255), (100, height//2-20, 600, 40), 2)

        progress_text = font_S.render(f"Loading... {progress}%", True, (255, 255, 255))

        loading_text = font_S.render("Loading...", True, (255, 255, 255))
        screen.blit(loading_text, (width//2-50, height//2-50))

        progress_text = font_S.render(f"{progress}%", True, (255, 255, 255))
        screen.blit(progress_text, (width//2-20, height//2))

        display.flip()

        progress += 1
        clock.tick(30)

Loading()

screen_x = screen_x/2-100
display.set_caption("             Football Buttons")
screen = display.set_mode((screen_x, screen_y),SCREEN_SIZE)

# تعریف مستطیل برای دکمه
Start_button   = Rect(screen_x/3-40 , screen_y/2+10, 260, 50)
Setting_button = Rect(screen_x/3-40 , screen_y/2+75, 260, 50)
Exit_button    = Rect(screen_x/3-40 , screen_y/2+145, 260, 50)

while True :
    for j in event.get():
        if j.type == QUIT :
            exit()
        if j.type == MOUSEBUTTONDOWN:
            mouse_pos = mouse.get_pos()
            if Start_button.collidepoint(mouse_pos):
                # صفحه بازی
                from Game import *
                Restart(True)
            elif Setting_button.collidepoint(mouse_pos):
                # کنترل تنظیمات
                from definitions import *
                Setting()
            elif Exit_button.collidepoint(mouse_pos):
                exit(0)
            else:None
    Backgrund(int(screen_x),int(screen_y),screen)
    Draw_Get_Bottons_for_Start(screen,Start_button  , "Start the Game",23,Y=5,
                            FONT="comicsansms",size=30)
    Draw_Get_Bottons_for_Start(screen,Setting_button, "Setting the Game",10,Y=5,
                            FONT="comicsansms",size=30)
    Draw_Get_Bottons_for_Start(screen,Exit_button   , "Exit the Game",30,Y=5,
                            FONT="comicsansms",size=30)
    message(    "WELCOME"     ,screen, BG_COLOR, screen_x/2-90 , 50,50,"MISTRAL")
    message(  "To The Game"   ,screen, SUN_TOP, screen_x/2-90 , 120,50,"MISTRAL")
    message("Football Buttons",screen, SKY_TOP, screen_x/2-130 , 200,50,"MISTRAL")
    display.update()
# پایان