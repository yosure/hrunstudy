import logging
import time
from typing import List
from dynaconf import settings
import pymysql
import re
from Cryptodome.Cipher import AES
import binascii


# commented out function will be filtered
# def get_headers():
#     return {"User-Agent": "hrp"}


def get_user_agent():
    return "hrp/funppy"


def sleep(n_secs):
    time.sleep(n_secs)


def sum(*args):
    result = 0
    for arg in args:
        result += arg
    return result


def sum_ints(*args: List[int]) -> int:
    result = 0
    for arg in args:
        result += arg
    return result


def sum_two_int(a: int, b: int) -> int:
    return a + b


def sum_two_string(a: str, b: str) -> str:
    return a + b


def sum_strings(*args: List[str]) -> str:
    result = ""
    for arg in args:
        result += arg
    return result


def concatenate(*args: List[str]) -> str:
    result = ""
    for arg in args:
        result += str(arg)
    return result


def setup_hook_example(name):
    logging.warning("setup_hook_example")
    return f"setup_hook_example: {name}"


def teardown_hook_example(name):
    logging.warning("teardown_hook_example")
    return f"teardown_hook_example: {name}"

def os_env(ekey, default=""):
    "提取环境配置变量"
    """字典get()方法
    get()方法用于根据指定的键获取元素的值。
    语法：
    dictionary_name.fromkeys(keys, value)
    Parameter(s)：
    key –它代表要返回其值的键的名称。
    value –这是一个可选参数，用于指定如果项目不存在则返回的值。"""
    print("环境变量"+ekey)
    return settings.get(ekey,default)
    
def get_phone_password(phone):
    time.sleep(3)
    db = pymysql.connect(
        host=settings.DEFAULT_MYSQL_HOST,
        port=3306,
        user=settings.DEFAULT_MYSQL_USER,
        password=settings.DEFAULT_MYSQL_PSWD,
        database="message_core", )
    cursor = db.cursor()
    try:
        count = cursor.execute(
            "select * from message_log where receiverAddress = '%s' and templateName = 'admin_create_user_notice' ORDER BY sendTime desc LIMIT 1" % (phone))
        print(f'查询到{count}条记录')
        # 提取一条查询结果
        result = cursor.fetchone()
        # 提取短信验证码
        code_msg = result[15]
        print(code_msg)
        # re模块是python独有的匹配字符串的模块，该模块种提供功能基于正则表达式实现的，对于字符串进行模糊匹配找到想要的内容信息，一般用于爬虫或者自动化测试前后端不分离项目
        code = re.search(r'初始密码：(\S+)，', code_msg).group(1)
        print(code)
        pwd = aes_encode(code)
        return pwd
    except Exception as e:
        print(e)
    db.close()

def aes_encode(plain_text, key="jkl;POIU1234++==", iv="0000000000000000"):
    plain_text_count = len(plain_text.encode("utf-8"))
    if plain_text_count % 16 != 0:
        add = 16 - (plain_text_count % 16)
    else:
        add = 0
    plain_text_padding = plain_text + ("\0" * add)
    cipher = AES.new(key.encode("utf-8"), AES.MODE_OFB, IV=iv.encode("utf-8"))
    ciper_text = cipher.encrypt(plain_text_padding.encode("utf-8"))

    return binascii.b2a_hex(ciper_text)[:plain_text_count * 2].decode("utf-8")