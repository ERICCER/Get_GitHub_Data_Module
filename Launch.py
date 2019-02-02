from python_repos import *
from easygui import *
import  webbrowser
from time import sleep
buttonbox(msg = "点击下面按钮以生成图表", choices= ["生成"])
github_repos()
sleep(0.4)

#Bug
try:
    webbrowser.open("python_repos.svg")
except:
    webbrowser.open('Error.svg')
