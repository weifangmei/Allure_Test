import allure
import pytest


class Test_Allure:

    def setup_class(self):
        pass

    def teardown_class(self):
        pass

    @allure.issue("https://163.com")
    @allure.testcase("https://www.baidu.com/test001")
    @pytest.mark.parametrize("a", [1, 2, 3])
    def test_001(self, a):
        allure.attach("这是一个描述", "试一下")
        assert a != 2

    @allure.severity("blocker")
    @allure.step(title="我是第二个测试")
    def test_002(self):
        assert 1


