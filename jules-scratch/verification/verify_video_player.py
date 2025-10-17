from playwright.sync_api import sync_playwright

def run(playwright):
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()

    # Navigate to the local server
    page.goto("http://localhost:8000")

    # Click on the first card to open the modal
    page.locator(".card-glow-hover").first.click()

    # Wait for the modal to be visible
    page.wait_for_selector("#modal", state="visible")

    # Take a screenshot of the modal
    page.locator("#modal > div").screenshot(path="jules-scratch/verification/verification.png")

    browser.close()

with sync_playwright() as playwright:
    run(playwright)