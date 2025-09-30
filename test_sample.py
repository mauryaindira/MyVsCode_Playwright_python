
def test_sample():
    assert 2+2 ==4

# test_google.py

def test_google_homepage(page):
    # Navigate to Google
    page.goto("https://www.google.com")

    # Verify the page title
    assert "Google" in page.title()

