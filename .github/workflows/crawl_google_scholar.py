from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def crawl_google_scholar():
    # Replace 'your_google_scholar_url' with your actual Google Scholar homepage URL
    url = "https://scholar.google.com/citations?user=6cgYvfIAAAAJ&hl=en"

    # Set up Chrome webdriver (you need to have Chrome and chromedriver installed)
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Run Chrome in headless mode
    driver = webdriver.Chrome(options=options)

    # Open Google Scholar homepage
    driver.get(url)

    # Wait for the page to load
    time.sleep(5)  # Adjust the sleep time as needed

    # Extract number of citations
    citations_element = driver.find_element(By.XPATH, '//td[@class="gsc_rsb_std"][1]')
    citations = citations_element.text

    # Extract h-index
    h_index_element = driver.find_element(By.XPATH, '//td[@class="gsc_rsb_std"][2]')
    h_index = h_index_element.text

    # Close the webdriver
    driver.quit()

    # Update the Markdown file
    update_markdown_file(citations, h_index)

def update_markdown_file(citations, h_index):
    # Read the Markdown file
    with open('../../_pages/publications.md', 'r') as file:
        content = file.read()

    # Update citation count and h-index in the Markdown content
    updated_content = content.replace('<!-- REPLACE_THIS_WITH_CITATIONS -->', citations)
    updated_content = updated_content.replace('<!-- REPLACE_THIS_WITH_H_INDEX -->', h_index)

    # Write the updated content back to the Markdown file
    with open('../../_pages/publications.md', 'w') as file:
        file.write(updated_content)

if __name__ == "__main__":
    crawl_google_scholar()
