from testcases.qianzhi_test import TestQianZhi
import pytest
from filelock import FileLock
from random import random
import os

@pytest.fixture(scope="session", autouse=True)
def qian_zhi(tmp_path_factory, worker_id):
    token = str(random())
    print("fixture:请求登录接口，获取token"+token)
    os.environ['token'] = token
    return token
    # TestQianZhi().test_start()