import subprocess

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

def ascii_punjabi_to_unicode(text: str) -> str:
    result = subprocess.run(
        ["node", "convert.js", text],  # Node script in current working dir
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        raise RuntimeError(result.stderr)

    # Remove dangling dotted circle
    return result.stdout.replace("\u25CC", "").strip()


def getHukum():
    chrome_options = Options()
    chrome_options.add_argument("--headless") 
    driver = webdriver.Chrome(options=chrome_options)

    url = "https://www.sikhnet.com/hukam"
    driver.get(url)

    # Wait up to 10 seconds for translation rows to load
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.translation-row"))
        )
    except:
        print("Translation rows did not load")
        driver.quit()
        exit()

    # Now get the HTML
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    driver.quit()

    cnt = ""
    for block in soup.select("div.translation-row"):
        orig = block.select_one("div.t-gurmukhi.colorblack")
        mean = block.select_one("div.t-english.colorblue")
        
        if orig and mean:
            origTxt = ascii_punjabi_to_unicode(orig.get_text(strip=True))
            meanTxt = mean.get_text(strip=True)
        
            cnt += f"<p><span style=\"color:#FFB84D\">{origTxt}</span></p><p><span style=\"color:#87CEEB\">{meanTxt}</span></p>"

    return cnt
