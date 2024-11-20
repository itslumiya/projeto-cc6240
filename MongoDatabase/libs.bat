@echo off
echo Instalando bibliotecas Python...
python.exe -m pip install --upgrade pip
pip install pandas
pip install keyring
pip install faker
pip install pymongo
echo Instalação completa!