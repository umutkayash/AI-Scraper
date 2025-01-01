from selenium.webdriver import Remote, ChromeOptions
from selenium.webdriver.chromium.remote_connection import ChromiumRemoteConnection
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os

load_dotenv()

WEBDRIVER_URL = os.getenv("WEBDRIVER_URL")


def fetch_web_page(url):
    print("Establishing connection with browser service...")
    connection = ChromiumRemoteConnection(WEBDRIVER_URL, "goog", "chrome")
    with Remote(connection, options=ChromeOptions()) as browser:
        browser.get(url)
        print("Handling captcha...")
        captcha_result = browser.execute(
            "executeCdpCommand",
            {
                "cmd": "Captcha.waitForSolve",
                "params": {"detectTimeout": 10000},
            },
        )
        print("Captcha status:", captcha_result["value"]["status"])
        print("Page loaded. Extracting data...")
        page_html = browser.page_source
        return page_html


def parse_html_to_body(html_data):
    parser = BeautifulSoup(html_data, "html.parser")
    page_body = parser.body
    if page_body:
        return str(page_body)
    return ""


def refine_html_content(raw_html):
    parser = BeautifulSoup(raw_html, "html.parser")

    for unwanted_tag in parser(["script", "style"]):
        unwanted_tag.extract()

    refined_text = parser.get_text(separator="\n")
    refined_text = "\n".join(
        line.strip() for line in refined_text.splitlines() if line.strip()
    )

    return refined_text


def segment_content(content, segment_size=6000):
    return [
        content[i : i + segment_size] for i in range(0, len(content), segment_size)
    ]
