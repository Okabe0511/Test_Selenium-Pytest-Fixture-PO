import pytest
from Page.main_page import MainPage
from Page.create_page import CreatePage
import time

TEST_FILE_PATH = r"C:\Users\ROG\Desktop\swtest\test.postman_collection.json"


class TestBusinessFlow:

    def test_full_flow(self, login_page, logger):
        logger.info('===== 开始业务流程测试 =====')

        # 1. 用户登录
        logger.info('----- 步骤1: 用户登录 -----')
        login_result = login_page.login('admin', '123456')
        assert login_result == '登录成功'
        logger.info('登录成功')

        # 2. 删除任务
        logger.info('----- 步骤2: 删除任务 -----')
        main_page = MainPage(login_page.driver)
        assert main_page.delete_confirm() == True
        logger.info('删除任务完成')


        # 3. 新建跨模态任务
        logger.info('----- 步骤3: 新建跨模态任务 -----') 
        create_page = CreatePage(login_page.driver)
        main_page.add_task()
        result = create_page.cross_modal_dataset('模态数据集1', TEST_FILE_PATH, TEST_FILE_PATH, TEST_FILE_PATH, "图像", "程序代码")
        assert '成功' in result
        logger.info(f'创建跨模态数据集结果: {result}')
        time.sleep(5)

        # 4. 退出登录
        logger.info('----- 步骤4: 退出登录 -----')
        main_page = MainPage(login_page.driver)
        logout_result = main_page.logout()
        assert logout_result == '退出登录成功'
        logger.info('退出登录成功')
        logger.info('===== 业务流程测试完成 =====')
