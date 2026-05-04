from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from tool import Logger, take_screenshot
from config import EXPLICIT_WAIT
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, EXPLICIT_WAIT)
        self.logger = Logger()

    def open(self, url):
        self.logger.info(f'打开网址: {url}')
        self.driver.get(url)

    def find(self, locator):
        try:
            element = self.wait.until(EC.presence_of_element_located(locator))
            self.logger.debug(f'找到元素: {locator}')
            return element
        except (TimeoutException, NoSuchElementException) as e:
            self.logger.error(f'未找到元素: {locator}, 错误: {e}')
            take_screenshot(self.driver, 'element_not_found')
            raise

    def click(self, locator):
        try:
            element = self.wait.until(EC.element_to_be_clickable(locator))
            actions = ActionChains(self.driver)
            actions.move_to_element(element).click().perform()
            self.logger.info(f'点击元素: {locator}')
        except Exception as e:
            self.logger.error(f'点击元素失败: {locator}, 错误: {e}')
            take_screenshot(self.driver, 'click_failed')
            raise

    def type(self, locator, text, clear=True):
        try:
            element = self.find(locator)
            if clear:
                element.clear()
            element.send_keys(text)
            self.logger.info(f'输入文本到 {locator}: {text}')
        except Exception as e:
            self.logger.error(f'输入文本失败: {locator}, 错误: {e}')
            take_screenshot(self.driver, 'type_failed')
            raise

    def text_of(self, locator, expected_text=None):
        """
        获取元素文本
        :param locator: 元素定位
        :param expected_text: 可选，指定要等待的文本
        """
        if expected_text:
            try:
                self.wait.until(EC.text_to_be_present_in_element(locator, expected_text))
                self.logger.info(f'元素 {locator} 出现文本: {expected_text}')
            except TimeoutException as e:
                self.logger.error(f'等待文本超时: {expected_text}, 错误: {e}')
                take_screenshot(self.driver, 'wait_text_timeout')
                raise
        else:
            try:
                self.wait.until(EC.visibility_of_element_located(locator))
            except TimeoutException as e:
                self.logger.error(f'等待元素可见超时: {locator}, 错误: {e}')
                take_screenshot(self.driver, 'wait_visible_timeout')
                raise
        
        text = self.find(locator).text
        self.logger.debug(f'获取元素文本 {locator}: {text}')
        return text

    def is_visible(self, locator):
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def get_title(self):
        title = self.driver.title
        self.logger.info(f'当前页面标题: {title}')
        return title

    def get_current_url(self):
        url = self.driver.current_url
        self.logger.info(f'当前页面URL: {url}')
        return url

    def get_attribute(self, locator, attribute):
        try:
            element = self.find(locator)
            value = element.get_attribute(attribute)
            self.logger.debug(f'获取元素属性 {locator} 属性 {attribute}: {value}')
            return value
        except Exception as e:
            self.logger.error(f'获取元素属性失败: {locator}, 属性: {attribute}, 错误: {e}')
            take_screenshot(self.driver, 'get_attribute_failed')
            raise

    def hover(self, locator):
        actions = ActionChains(self.driver)
        element = self.find(locator)
        actions.move_to_element(element).perform()
        self.logger.info(f'悬停元素: {locator}')

    def select_option(self, select_locator, option_locator):
        """选择下拉框选项"""
        from selenium.webdriver.common.action_chains import ActionChains
        import time
        
        try:
            self.click(select_locator)
            time.sleep(0.5)
            
            element = self.find(option_locator)
            ActionChains(self.driver).move_to_element(element).perform()
            element.click()
            
            time.sleep(0.5)
            self.logger.info(f'选择下拉选项: {option_locator}')
        except Exception as e:
            self.logger.error(f'选择下拉选项失败: {option_locator}, 错误: {e}')
            take_screenshot(self.driver, 'select_failed')
            raise

    def upload_file(self, file_input_locator, file_path):
        """上传文件：直接给 input type="file" 发送路径"""
        try:
            element = self.find(file_input_locator)
            element.send_keys(file_path)
            self.logger.info(f'上传文件: {file_path}')
        except Exception as e:
            self.logger.error(f'上传文件失败: {file_path}, 错误: {e}')
            take_screenshot(self.driver, 'upload_failed')
            raise
            
    def press_enter(self):
        """按回车键"""
        try:
            actions = ActionChains(self.driver)
            actions.send_keys(Keys.ENTER).perform()
            self.logger.info('按下回车键')
        except Exception as e:
            self.logger.error(f'按回车键失败: {e}')
            take_screenshot(self.driver, 'press_enter_failed')
            raise
            
    def press_esc(self):
        """按ESC键"""
        try:
            actions = ActionChains(self.driver)
            actions.send_keys(Keys.ESCAPE).perform()
            self.logger.info('按下ESC键')
        except Exception as e:
            self.logger.error(f'按ESC键失败: {e}')
            take_screenshot(self.driver, 'press_esc_failed')
            raise