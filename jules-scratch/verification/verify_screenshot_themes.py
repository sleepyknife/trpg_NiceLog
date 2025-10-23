import asyncio
from playwright.sync_api import sync_playwright, expect
import os
import re

def verify_screenshot_themes():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Go to the local server
        page.goto('http://localhost:8000')

        # --- Light Theme Verification ---
        # Wait for the first card to be visible
        expect(page.locator('#card-grid .card-glow-hover').first).to_be_visible()
        # Click the first story card to open the modal
        page.locator('#card-grid .card-glow-hover').first.click()
        # Wait for the modal to be visible
        expect(page.locator('#modal')).to_be_visible()
        # Click the share screenshot button
        page.locator('#share-btn').click()
        # Wait for the screenshot preview modal to appear
        preview_modal_light = page.locator('#screenshot-preview-modal')
        expect(preview_modal_light).to_be_visible()
        # Wait for the image to be loaded
        expect(preview_modal_light.locator('img')).to_have_attribute('src', re.compile(r'^data:image\/png'))
        # Take a screenshot
        preview_modal_light.locator('> div').screenshot(path='jules-scratch/verification/light-theme.png')
        # Close modals
        page.locator('#preview-close-btn').click()
        page.locator('#modal-close-btn').click()

        # --- Dark Theme Verification ---
        # Toggle theme
        page.locator('#theme-toggle').click()
        # Wait for the first card to be visible again
        expect(page.locator('#card-grid .card-glow-hover').first).to_be_visible()
        # Click the first story card to open the modal
        page.locator('#card-grid .card-glow-hover').first.click()
        # Wait for the modal to be visible
        expect(page.locator('#modal')).to_be_visible()
        # Click the share screenshot button
        page.locator('#share-btn').click()
        # Wait for the screenshot preview modal to appear
        preview_modal_dark = page.locator('#screenshot-preview-modal')
        expect(preview_modal_dark).to_be_visible()
        # Wait for the image to be loaded
        expect(preview_modal_dark.locator('img')).to_have_attribute('src', re.compile(r'^data:image\/png'))
        # Take a screenshot
        preview_modal_dark.locator('> div').screenshot(path='jules-scratch/verification/dark-theme.png')

        browser.close()

if __name__ == "__main__":
    verify_screenshot_themes()
