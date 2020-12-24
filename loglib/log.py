import configparser
import datetime
import logging
import os
import sys

#設定ファイル読み込み
ini = configparser.ConfigParser(strict=False)
ini.read('./config.ini', encoding='utf-8')

#プログラム名を[Log]Nameから読み込み
Name = (ini.get('Log', 'Name'))

#logsファイルが無いとき
if not os.path.isfile("./logs"):
    try:
        os.mkdir("./logs")
    except PermissionError:
        pprint("logフォルダが作成できませんでした。", "CRITICAL")
        sys.exit(1)

logger = logging.getLogger(Name)

# ログレベルの設定
logger.setLevel(10)

# ログのコンソール出力の設定
sh = logging.StreamHandler()
logger.addHandler(sh)

# ログのファイル出力先を設定
fh = logging.FileHandler(filename=f"./logs/[{Name}]latest.log", encoding="utf-8")
logger.addHandler(fh)

# ログの出力形式の設定
formatter = logging.Formatter('[%(asctime)s:%(lineno)d:%(levelname)s]: %(message)s')
fh.setFormatter(formatter)
sh.setFormatter(formatter)

logger.info(f'Now {Name} log.py Library Start')

def reload():
    #ファイルクローズメッセージ
    pprint("File Close")

    #Loggerをシャットダウン
    logging.shutdown()

    #ファイル名変更
    now = datetime.now(tz=datetime.timezone(datetime.timedelta(hours=9)))
    oldnow = now + datetime.timedelta(days=-1)
    Day = oldnow.strftime('%Y-%m-%d')

    if os.path.isfile("./logs/[{Name}]latest.log"):
        if os.path.isfile(f"./logs/[{Name}]{Day}.log"):
            if os.path.isfile(f"./logs/[{Name}]{Day}.log.backup"):
                os.remove(f"./logs/[{Name}]{Day}.log.backup")

            os.rename(f"./logs/[{Name}]{Day}.log", f"./logs/[{Name}]{Day}.log.backup")
            os.rename("./logs/[{Name}]latest.log", f"./logs/[{Name}]{Day}.log")

        else:
            os.rename("./logs/[{Name}]latest.log", f"./logs/[{Name}]{Day}.log")

def pprint(msg="Not Message", Level="INFO"):
    if Level == "INFO":
        logger.info(msg)
    
    if Level == "WARNING":
        logger.warning(msg)
    
    if Level == "ERROR":
        logger.error(msg)

    if Level == "CRITICAL":
        logger.critical(msg)

    if Level == "DEBUG":
        logger.debug(msg)
