#!/bin/sh
ECHO "프로그램 시작하기"
set root = c:\anaconda3
call %root%\Scripts\activate.bat %root%

source conda activate torch
python main.py