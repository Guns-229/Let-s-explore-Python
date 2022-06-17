import yaml
from selenium.webdriver.common.keys import Keys


class Test_PythonHomePage:

    @brorser
    def test_search(self):
        global driver
        driver.get("http://www.python.org")
        self.assertIn("Python", driver.title)
        elem = driver.find_element_by_name("q")
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source
