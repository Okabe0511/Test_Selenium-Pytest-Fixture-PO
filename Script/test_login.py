import pytest


class TestLogin:
    def test_login_success(self, login_page, logger):
        logger.info('===== 测试用例: 登录成功 =====')

        actual_text = login_page.login('admin', '123456')
        assert actual_text == '登录成功'
        logger.info('登录成功验证通过')

    def test_login_null_username(self, login_page, logger):
        logger.info('===== 测试用例: 用户名为空登录失败 =====')

        actual_text = login_page.login('', '')
        assert actual_text == '输入为空'
        logger.info('用户名为空验证通过')

    def test_login_not_exsist_username(self, login_page, logger):
        logger.info('===== 测试用例: 用户名不存在登录失败 =====')

        actual_text = login_page.login('non_existent_user', '123456')
        assert actual_text == '账号或密码错误，请重新输入'
        logger.info('用户名不存在验证通过')

    def test_login_fail_wrong_username(self, login_page, logger):
        logger.info('===== 测试用例: 用户名错误登录失败 =====')

        actual_text = login_page.login('\' OR 1=1 --', '123456')
        assert actual_text == '账号格式错误，只能包含字母、数字、下划线'
        logger.info('用户名错误验证通过')

    def test_login_fail_wrong_password(self, login_page, logger):
        logger.info('===== 测试用例: 密码错误登录失败 =====')

        actual_text = login_page.login('admin', 'wrongpassword')
        assert actual_text == '账号或密码错误，请重新输入'
        logger.info('密码错误验证通过')

    def test_login_null_password(self, login_page, logger):
        logger.info('===== 测试用例: 密码为空登录失败 =====')

        actual_text = login_page.login('admin', '')
        assert actual_text == '输入为空'
        logger.info('密码为空验证通过')

    def test_show_password(self, login_page, logger):
        logger.info('===== 测试用例: 显示密码 =====')

        assert login_page.show_password('123456') == 'text'
        logger.info('显示密码验证通过')

    def test_hide_password(self, login_page, logger):
        logger.info('===== 测试用例: 隐藏密码 =====')
        assert login_page.hide_password('123456') == 'password'
        logger.info('隐藏密码验证通过')
