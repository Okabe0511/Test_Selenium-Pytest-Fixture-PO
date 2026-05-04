import pytest
TEST_FILE_PATH = r"C:\Users\ROG\Desktop\swtest\test.postman_collection.json"  # 你自定义的文件路径
TEST_WRONG_FILE_PATH = r"C:\Users\ROG\Documents\LTspiceXVII\lib\sym\References\LT1004-2.5.asy"
from Page.create_page import CreatePage

class TestCreate:
    def test_basic_dataset(self, create_page, logger):  
        logger.info('测试创建基础数据集')
        result = create_page.basic_dataset('数据集1', TEST_FILE_PATH, "关系表")
        assert '成功' in result
        logger.info(f'测试结果: {result}')

    def test_cross_modal_dataset(self, create_page, logger):
        logger.info('测试创建跨模态数据集')
        result = create_page.cross_modal_dataset('模态数据集1', TEST_FILE_PATH, TEST_FILE_PATH, TEST_FILE_PATH, "图像", "程序代码")
        assert '成功' in result
        logger.info(f'测试结果: {result}')

    def test_title_null(self, create_page, logger):  
        logger.info('测试创建数据集标题为空')
        result = create_page.basic_dataset('', TEST_FILE_PATH, "关系表")
        assert '请填写完整任务配置信息' in result
        logger.info(f'测试结果: {result}')

    def test_basic_dataset_no_select(self, create_page, logger):
        logger.info('测试创建基础数据集不选择下拉框')
        result = create_page.basic_dataset('数据集1', TEST_FILE_PATH, "")
        assert '请填写完整任务配置信息' in result
        logger.info(f'测试结果: {result}')
    
    def test_cross_modal_only_a(self, create_page, logger):
        logger.info('测试只选择数据集A下拉框')
        result = create_page.cross_modal_dataset('模态数据集1', TEST_FILE_PATH, TEST_FILE_PATH, TEST_FILE_PATH, "图像", "")
        assert '请填写完整任务配置信息' in result
        logger.info(f'测试结果: {result}')

    def test_cross_modal_only_b(self, create_page, logger):
        logger.info('测试只选择数据集B下拉框')
        result = create_page.cross_modal_dataset('模态数据集1', TEST_FILE_PATH, TEST_FILE_PATH, TEST_FILE_PATH, "", "程序代码")
        assert '请填写完整任务配置信息' in result
        logger.info(f'测试结果: {result}')
    
    def test_basic_file_null(self, create_page, logger):
        logger.info('测试创建基础数据集文件为空')
        result = create_page.basic_dataset('数据集1', '', "关系表")
        assert '请填写完整任务配置信息' in result
        logger.info(f'测试结果: {result}')
    
    def test_cross_modal_filea_null(self, create_page, logger):
        logger.info('测试创建跨模态数据集文件A为空')
        result = create_page.cross_modal_dataset('模态数据集1', TEST_FILE_PATH, '', TEST_FILE_PATH, "图像", "程序代码")
        assert '请填写完整任务配置信息' in result
        logger.info(f'测试结果: {result}')

    def test_cross_modal_fileb_null(self, create_page, logger):
        logger.info('测试创建跨模态数据集文件B为空')
        result = create_page.cross_modal_dataset('模态数据集1', TEST_FILE_PATH, TEST_FILE_PATH, '', "图像", "程序代码")
        
        assert '请填写完整任务配置信息' in result
        logger.info(f'测试结果: {result}')

    def test_cross_modal_metadata_null(self, create_page, logger):
        logger.info('测试元数据文件为空')
        result = create_page.cross_modal_dataset('模态数据集1', '', TEST_FILE_PATH, TEST_FILE_PATH, "图像", "程序代码")
        
        assert '请填写完整任务配置信息' in result
        logger.info(f'测试结果: {result}')

    def test_basic_file_wrong(self, create_page, logger):
        logger.info('测试创建基础数据集文件格式错误')
        result = create_page.basic_dataset('数据集1', TEST_WRONG_FILE_PATH, "关系表")
        assert '请填写完整任务配置信息' in result
        logger.info(f'测试结果: {result}')

    def test_cross_modal_filea_wrong(self, create_page, logger):
        logger.info('测试创建跨模态数据集文件A格式错误')
        result = create_page.cross_modal_dataset('模态数据集1', TEST_WRONG_FILE_PATH, TEST_FILE_PATH, TEST_FILE_PATH, "图像", "程序代码")
        assert '请填写完整任务配置信息' in result
        logger.info(f'测试结果: {result}')

    def test_cross_modal_fileb_wrong(self, create_page, logger):
        logger.info(f'测试创建跨模态数据集文件B格式错误')
        result = create_page.cross_modal_dataset('模态数据集1', TEST_FILE_PATH, TEST_WRONG_FILE_PATH, TEST_FILE_PATH, "图像", "程序代码")
        assert '请填写完整任务配置信息' in result
        logger.info(f'测试结果: {result}')

    def test_cross_modal_metadata_wrong(self, create_page, logger):
        logger.info(f'测试创建跨模态数据集元数据文件格式错误')
        result = create_page.cross_modal_dataset('模态数据集1', TEST_FILE_PATH, TEST_FILE_PATH, TEST_WRONG_FILE_PATH, "图像", "程序代码")
        assert '请填写完整任务配置信息' in result
        logger.info(f'测试结果: {result}')
    

