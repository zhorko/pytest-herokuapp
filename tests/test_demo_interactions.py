from selenium.webdriver.support.wait import WebDriverWait 

from pages.demo_home_page import DemoHomePage
from pages.demo_elements_page import DemoElemPage
from pages.demo_radio_page import DemoRadioPage


def test_demo_interactions(_browser):
    
    URL = "https://demoqa.com/"
    wait = WebDriverWait(_browser, 10)

    _browser.maximize_window()
    _browser.get(URL)
    
    # Initializations
    demo_home_page = DemoHomePage(_browser)
    demo_elem_page = DemoElemPage(_browser)
    demo_radio_page = DemoRadioPage(_browser)

    demo_home_page.open_elements(wait)
    demo_elem_page.open_radio(wait)
    
    demo_radio_page.click_radio(wait, "YeS")
    assert demo_radio_page.get_radio_status(wait, "yes") is True

    demo_radio_page.click_radio(wait, "impressive")
    assert demo_radio_page.get_radio_status(wait, "impressive") is True