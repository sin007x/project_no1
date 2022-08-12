import os
from ssl import Options
import tkinter
import tkinter.ttk as ttk
import tkinter.messagebox as msgbox
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from tkinter import *
from tkinter import filedialog
from PIL import Image
from msedge.selenium_tools import Edge, EdgeOptions

root = Tk()
root.title("프로젝")
# root.geometry("400x400+100+100")
# edge_options = EdgeOptions()
# edge_options.use_chromium = True
# edge_options.add_experimental_option("detach", True)

#시계
def clock(): # 현재 시간 표시 / 반복
#    live_T = time.strftime("%y.%m.%d.%a. %H:%M:%S") # Real Time
   live_T = time.strftime("%H:%M:%S")
   clock_width.config(text=live_T)
   clock_width.after(200, clock) # .after(지연시간{ms}, 실행함수)

#검색창
def search_naver():
    url = f"https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query={key_out.get()}"
    driver1 = webdriver.Chrome('chromedriver')
    driver1.get(url)
    time.sleep(1)

def search_goole():
    url = f"https://www.google.com/search?q={key_out.get()}"
    driver2 = webdriver.Chrome('chromedriver')
    driver2.get(url)

def search_daum():
    url = f"https://search.daum.net/search?w=tot&DA=YZR&t__nil_searchbox=btn&sug=&sugo=&sq=&o=&q={key_out.get()}"
    # url = "https://www.daum.net/"
    driver3 = webdriver.Chrome('chromedriver')
    driver3.get(url)

def search_youtube():
    url = f"https://www.youtube.com/results?search_query={key_out.get()}"
    # url = "https://www.daum.net/"
    driver3 = webdriver.Chrome('chromedriver')
    driver3.get(url)

#계산기
def price(event):
    price_label.config(text="결과="+str(eval(price_out.get())))

#검색어
def key_word(event):
    key_label.configure(text="검색 : "+str(key_out.get()))


main_frame = Frame(root)
main_frame.pack(fill="x", padx=5, pady=5) # 간격 띄우기

btn_add_main = Button(main_frame, padx=5, pady=5, width=12, text="프로젝트")
btn_add_main.pack()

#시간
clock_frame = LabelFrame(root,labelanchor="n",text="현재시간")
clock_frame.pack(fill="x", padx=5, pady=5, ipady=5,)

clock_width = Label(clock_frame, font=("Times",24,"bold"), bd=8)
clock_width.pack(fill="x", padx=5, pady=0)

clock()

# 계산기 프레임
price_frame = LabelFrame(root,labelanchor="n",text="계산기")
price_frame.pack(fill="x", padx=5, pady=5, ipady=5,)
price_out = tkinter.Entry(price_frame)
price_out.bind("<Return>", price)
price_out.pack(side="left", fill="x", expand=True, padx=5, pady=5)# 높이
price_label=tkinter.Label(price_frame)
price_label.pack(side="left", fill="x", expand=True, padx=5, pady=5)

#키워드 프레임
key_frame = LabelFrame(root,labelanchor="n",text="검색입력창")
key_frame.pack(fill="x", padx=5, pady=5, ipady=5)
key_out = tkinter.Entry(key_frame)
key_out.bind("<Return>", key_word)
key_out.pack(side="left", fill="x", expand=True, padx=5, pady=5)# 높이
key_label=tkinter.Label(key_frame)
key_label.pack(side="left", fill="x", expand=True, padx=5, pady=5)


# 검색프레임
search_frame = LabelFrame(root, labelanchor="n", text="검색사이트")
search_frame.pack(fill="x", padx=5, pady=5, ipady=5)

#네이버
btn_add_naver = Button(search_frame, padx=5, pady=5, width=12, text="네이버", command=search_naver)
btn_add_naver.pack(side="left" ,padx=5, pady=5, ipady=5)

#구글
btn_add_goole = Button(search_frame, padx=5, pady=5, width=12, text="구글", command=search_goole)
btn_add_goole.pack(side="right", padx=5, pady=5, ipady=5)

#다음
btn_add_daum = Button(search_frame, padx=5, pady=5, width=12, text="다음", command=search_daum)
btn_add_daum.pack(side="right", padx=5, pady=5, ipady=5)

#유튜브프레임
youtube_frame = LabelFrame(root, labelanchor="n", text="유튜브")
youtube_frame.pack(fill="x", padx=5, pady=5, ipady=5)

btn_add_youtube = Button(youtube_frame, padx=5, pady=5, width=12, text="유튜브", command=search_youtube)
btn_add_youtube.pack(fill="x",padx=5, pady=5, ipady=5)

#종료 프레임
youtube_frame = LabelFrame(root, labelanchor="n", text="프로그램 종료")
youtube_frame.pack(fill="x", padx=5, pady=5, ipady=5)

btn_close = Button(youtube_frame, padx=5, pady=5, width=12, text="닫 기", command=root.quit)
btn_close.pack(fill="x",padx=5, pady=5, ipady=5)

root.resizable(True, True) # x(너비), Y(높이) 값 변경 불가 (창 크기 변경 불가)
root.mainloop()


