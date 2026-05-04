from selenium.webdriver.common.by import By
from Base.base_page import BasePage
import time


class MainPage(BasePage):
    """主页 - 包含任务选择和搜索功能"""

    # 任务选择
    label_all = (By.CSS_SELECTOR, 'div.tab-item:nth-child(1)')
    label_completed = (By.CSS_SELECTOR, 'div.tab-item:nth-child(2)')
    label_in_progress = (By.CSS_SELECTOR, 'div.tab-item:nth-child(3)')
    label_unconfigured = (By.CSS_SELECTOR, 'div.tab-item:nth-child(4)')
####################################################

    # 搜索
    search_input = (By.XPATH, '//input[@placeholder="搜索数据集"]')
    search_button = (By.XPATH, '//button[@class="css-dev-only-do-not-override-1p3hq3p ant-btn ant-btn-default ant-input-search-button ant-btn-icon-only"]')
    result1 = (By.XPATH, '//h3[text()="电价预测任务"]')
    result2 = (By.XPATH, '//h3[text()="ECharts代码生成任务"]')
###########################################################    

    #新增任务与查看详情
    add_task_button = (By.XPATH, '//div[text()="新增任务"]')
    view_detail_button = (By.XPATH, '//span[text()="详 情"]')
    add_enter =(By.XPATH, '//div[text()="创建数据制备任务"]')
    view_enter =(By.XPATH, '//div[text()="数据集描述"]')
###########################################################    
    #删除任务
    delete_task_button = (By.XPATH, '//span[text()="删 除"]')
    delete_result = (By.XPATH, '//span[text()="删除任务成功"]')
    # 任务选择方法
    def show_all(self):
        self.click(self.label_all)
        return self.text_of(self.label_all)

    def show_completed(self):
        self.click(self.label_completed)
        return self.text_of(self.label_completed)

    def show_in_progress(self):
        self.click(self.label_in_progress)
        return self.text_of(self.label_in_progress)

    def show_unconfigured(self):
        self.click(self.label_unconfigured)
        return self.text_of(self.label_unconfigured)
###########################################################    

    # 搜索方法
    def search_precise(self, keyword):
        self.type(self.search_input, keyword)
        self.click(self.search_button)
        time.sleep(1)
        return self.text_of(self.result1)

    def search_vague(self, keyword):
        self.type(self.search_input, keyword)
        self.click(self.search_button)
        time.sleep(1)
        return self.text_of(self.result2)

    def search_null(self, keyword):
        self.type(self.search_input, keyword)
        self.click(self.search_button)
        time.sleep(1)
        return self.text_of(self.result1)
###########################################################    

    # 新增任务
    def add_task(self):
        self.click(self.add_task_button)
        return self.text_of(self.add_enter)

    # 查看详情
    def view_task(self):
        self.click(self.view_detail_button)
        return self.text_of(self.view_enter)
###########################################################    

    # 删除任务
    def delete_confirm(self):
        self.click(self.delete_task_button)
        self.press_enter()
        return self.is_visible(self.delete_result)
    
    # 取消删除任务
    def delete_cancel(self):
        self.click(self.delete_task_button)
        self.press_esc()
        return self.is_visible(self.delete_result)
###########################################################

    # 用户头像和退出
    logout_button = (By.CSS_SELECTOR, '.user-avatar.ant-avatar.ant-avatar-circle.ant-avatar-icon')
    logout_message = (By.CSS_SELECTOR, '.ant-message-custom-content > span:nth-child(2)')

    def logout(self):
        self.click(self.logout_button)
        return self.text_of(self.logout_message)
    


