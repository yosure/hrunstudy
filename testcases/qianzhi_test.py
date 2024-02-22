from httprunner import HttpRunner,Config,Step,RunRequest,RunTestCase,Parameters
import pytest
class TestQianZhi(HttpRunner):
    # 参数化 ，传入字典数据
    # @pytest.mark.parametrize(
    #     "param",
    #     # parameterize Httprunner内置方法，可简写为P
    #     Parameters("userName-password","${parameterize(data/user.csv)}")
    # )
    # def test_start(self, param):
    #     return super().test_start(param)
    
    config=(
        Config("前置")
        .variables(
            
        )
        .base_url("${os_env(BAIDU_URL)}")
        .verify(False)
    )
    teststeps=[
        Step(
            RunRequest("前置步骤一")
            .get("/")
            .validate()
            .assert_equal("status_code",200)
        )
    ]