import pytest

class TestMain:
    # 测试用例: 显示所有任务
    def test_show_mission(self, main_page, logger):
        logger.info('===== 测试用例: 显示所有任务 =====')
        assert main_page.show_all() == '全部'
        logger.info('显示所有任务验证通过')
    def test_show_completed(self, main_page, logger):
        logger.info('===== 测试用例: 显示已完成任务 =====')
        assert main_page.show_completed() == '已完成'
        logger.info('显示已完成任务验证通过')
    def test_show_in_progress(self, main_page, logger):
        logger.info('===== 测试用例: 显示进行中任务 =====')
        assert main_page.show_in_progress() == '运行中'
        logger.info('显示进行中任务验证通过')
    def test_show_unconfigured(self, main_page, logger):
        logger.info('===== 测试用例: 显示未配置任务 =====')
        assert main_page.show_unconfigured() == '未配置'
        logger.info('显示未配置任务验证通过')
    ####################################################
    # 测试用例: 搜索数据集
    def test_search_precise(self, main_page, logger):
        logger.info('===== 测试用例: 搜索数据集 =====')
        assert main_page.search_precise('电价预测任务') == '电价预测任务'
        logger.info('搜索数据集验证通过')
    def test_search_vague(self, main_page, logger):
        logger.info('===== 测试用例: 搜索数据集 =====')
        assert main_page.search_vague('EChar') == 'ECharts代码生成任务'
        logger.info('搜索数据集验证通过')
    def test_search_null(self, main_page, logger):
        logger.info('===== 测试用例: 搜索   数据集 =====')
        assert main_page.search_null('') == '暂无数据'
        logger.info('搜索数据集验证通过')
    ####################################################
    # 测试用例: 新增任务
    def test_add_task(self, main_page, logger):
        logger.info('===== 测试用例: 新增任务 =====')
        assert main_page.add_task() == '创建数据制备任务'
        logger.info('新增任务验证通过')
    # 测试用例: 查看详情
    def test_view_task(self, main_page, logger):
        logger.info('===== 测试用例: 查看详情 =====')
        assert main_page.view_task() == '数据集描述'
        logger.info('查看详情验证通过')
    # 测试用例: 删除任务
    def test_delete_confirm(self, main_page, logger):
        logger.info('===== 测试用例: 删除任务 =====')
        assert main_page.delete_confirm() == True
        logger.info('删除任务验证通过')
    # 测试用例: 取消删除任务
    def test_delete_cancel(self, main_page, logger):
        logger.info('===== 测试用例: 取消删除任务 =====')
        assert main_page.delete_cancel() == False
        logger.info('取消删除任务验证通过')

    # 测试用例: 退出登录
    def test_logout(self, main_page, logger):
        logger.info('===== 测试用例: 退出登录 =====')
        logout_msg = main_page.logout()
        assert logout_msg == '退出登录成功'  # 根据实际提示修改
        logger.info('退出登录验证通过')