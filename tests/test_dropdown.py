from pages.hero_home_page import HeroHomePage
from pages.hero_dropdown_page import HeroDropPage


def test_dropdown(_browser):
    URL = "https://the-internet.herokuapp.com/"

    _browser.maximize_window()
    _browser.get(URL)

    # Initializations
    hero_home_page = HeroHomePage(_browser)
    hero_drop_page = HeroDropPage(_browser)

    hero_home_page.open_dropdown()
    assert hero_drop_page.select_option(1).text == "Option 1"
