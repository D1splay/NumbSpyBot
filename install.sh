#!/bin/bash


red_text() {
  tput setaf 1; echo "$1"; tput sgr0
}


red_text "Внимание: NumbSpyBot предназначен исключительно для ознакомительных целей!"


read -p "Вы уверены, что хотите продолжить установку? (y/n): " choice


if [[ ! "$choice" =~ [yY] ]]; then
  red_text "Установка отменена."
  exit 1
fi


sudo apt-get update
sudo apt-get install python3

# Установка необходимых библиотек для Python
sudo apt-get install python3-pip
sudo pip3 install os
sudo pip3 install platform
sudo pip3 install subprocess
sudo pip3 install logging
sudo pip3 install asyncio
sudo pip3 install aiogram


python3 - <<EOF
import os
import platform
import subprocess
import logging
import asyncio
import aiogram
print("Установка зависимостей прошла успешно!")
EOF


python3 main.py
