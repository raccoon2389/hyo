#!/bin/sh
ECHO "���α׷� �����ϱ�"
set root = c:\anaconda3
call %root%\Scripts\activate.bat %root%

source conda activate torch
python main.py