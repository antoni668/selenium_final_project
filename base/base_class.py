import datetime


class Base:
    def __init__(self, driver):
        self.driver = driver

    def get_current_url(self):
        get_url = self.driver.current_url
        print(f"Current URL: {get_url}")

    def assert_word(self, word, result):
        assert word.text == result
        print("Good value word")

    def get_screenshot(self):
        nowdate = datetime.datetime.utcnow().strftime("%Y.%m.%d %H.%M.%S")
        screenshot_name = f"screenshot_{nowdate}.png"
        self.driver.save_screenshot(f"screen/{screenshot_name}")

    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print("Good value URL")
