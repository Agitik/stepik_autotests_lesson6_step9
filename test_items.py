link = 'https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_user_should_see_addtshoplist_btn(browser):
    browser.get(link)
    count = browser.find_elements_by_css_selector("#add_to_basket_form > button")
    assert len(count) == 1
