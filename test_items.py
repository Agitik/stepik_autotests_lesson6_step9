import time

link = 'https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_user_should_see_addtshoplist_btn(browser):
    browser.get(link)
    browser.find_element_by_css_selector("#add_to_basket_form > button")
    time.sleep(30)
