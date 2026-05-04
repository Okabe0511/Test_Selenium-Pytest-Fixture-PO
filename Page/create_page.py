from selenium.webdriver.common.by import By
from Base.base_page import BasePage
from time import sleep


class CreatePage(BasePage):
    # 创建数据集页面
    
    # ---------------------- 元素定位 ----------------------
    input_task_name = (By.ID, 'form_item_taskName')
    # 任务名称输入框
    
    dataset_type_basic = (By.XPATH, '//div[@id="form_item_datasetType"]//span[text()="基础数据集"]/ancestor::label')
    # 基础数据集选项
    
    dataset_type_cross_modal = (By.XPATH, '//div[@id="form_item_datasetType"]//span[text()="跨模态数据集"]/ancestor::label')
    # 跨模态数据集选项
    
    select_task_type = (By.XPATH, '//input[@id="form_item_basicDatasetType"]/ancestor::div[contains(@class, "ant-select")]')
    # 基础数据集类型下拉框
    
    task_type_option_relation = (By.XPATH, '//div[contains(@class, "ant-select-item") and text()="关系表"]')
    # 基础数据集类型-关系表选项
    
    upload_file_input = (By.ID, 'form_item_basicDatasetFile')
    # 基础数据集文件上传输入框
    
    upload_file_button = (By.CSS_SELECTOR, '#form_item_basicDatasetFile + div, .ant-upload-selector')
    # 基础数据集文件上传按钮
    
    cross_modal_type_a_select = (By.XPATH, '//input[@id="form_item_crossModalTypeA"]/ancestor::div[contains(@class, "ant-select")]')
    # 跨模态数据集A类型下拉框
    
    cross_modal_type_b_select = (By.XPATH, '//input[@id="form_item_crossModalTypeB"]/ancestor::div[contains(@class, "ant-select")]')
    # 跨模态数据集B类型下拉框
    
    cross_modal_a_option_image = (By.XPATH, '//form/div[3]/div[1]/div[1]/div/div[2]/div/div/div/div[2]/div/div/div/div[2]/div[1]/div/div/div[3]/div')
    # 跨模态数据集A类型-图像选项
    
    cross_modal_b_option_code = (By.XPATH, '//form/div[3]/div[2]/div[1]/div/div[2]/div/div/div/div[2]/div/div/div/div[2]/div[1]/div/div/div[7]/div')
    # 跨模态数据集B类型-程序代码选项
    
    dataset_file_a_input = (By.ID, 'form_item_datasetFileA')
    # 跨模态数据集A文件上传输入框
    
    dataset_file_b_input = (By.ID, 'form_item_datasetFileB')
    # 跨模态数据集B文件上传输入框
    
    metadata_file_input = (By.ID, 'form_item_metadataFile')
    # 元数据文件上传输入框
    
    confirm_button = (By.XPATH, '//span[text()="完 成"]')
    # 完成按钮
    
    cancel_button = (By.XPATH, '//span[text()="取 消"]')
    # 取消按钮
    
    success_message = (By.CSS_SELECTOR, '.ant-message-custom-content > span:nth-child(2)')
    # 成功提示信息

    # ---------------------- 业务方法 ----------------------
    def basic_dataset(self, task_name: str, file_path: str, option: str):
        self.type(self.input_task_name, task_name)
        self.click(self.dataset_type_basic)
        if option != "":
            self.select_option(self.select_task_type, self.task_type_option_relation)
        if file_path != "":
            self.upload_file(self.upload_file_input, file_path)
        self.click(self.confirm_button)
        return self.text_of(self.success_message)

    def cross_modal_dataset(self, task_name: str, metadata_file_path: str, dataset_file_a_path: str, dataset_file_b_path: str, option_a: str, option_b: str):
        self.click(self.dataset_type_cross_modal)
        self.type(self.input_task_name, task_name)
        if option_a != "":
            self.select_option(self.cross_modal_type_a_select, self.cross_modal_a_option_image)
        if dataset_file_a_path != "":
            self.upload_file(self.dataset_file_a_input, dataset_file_a_path)
        if option_b != "":
            self.select_option(self.cross_modal_type_b_select, self.cross_modal_b_option_code)
        if dataset_file_b_path != "":
            self.upload_file(self.dataset_file_b_input, dataset_file_b_path)
        if metadata_file_path != "":
            self.upload_file(self.metadata_file_input, metadata_file_path)
        
        self.click(self.confirm_button)
        return self.text_of(self.success_message)
