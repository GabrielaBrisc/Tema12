from selenium import webdriver


class Browser:
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(3)
    driver.set_page_load_timeout(6)

    def Close(self):
        self.driver.quit()