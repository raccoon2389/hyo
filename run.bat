@ECHO 프로그램 시작하기
PAUSE
set root = c:\anaconda3
call %root%\Scripts\activate.bat %root%

call conda activate torch
call python main.py
PAUSE