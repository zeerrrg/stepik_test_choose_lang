from selenium.webdriver.common.by import By

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_button_add_to_basket(browser):
    browser.get(link)
    res = browser.find_elements(By.XPATH, '//*[@id="add_to_basket_form"]/bu')
    assert len(res) > 0, "Button not found!"
