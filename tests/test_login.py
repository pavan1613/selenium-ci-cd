def test_valid_login(setup):
    from pages.login_page import LoginPage

    login = LoginPage(setup)
    login.open()
    login.login("standard_user", "secret_sauce")

    assert "inventory" in setup.current_url
