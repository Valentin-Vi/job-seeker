from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from scraper.crawler import Crawler
from exporter.exporter import Exporter

def main():
    try:
        options = Options()
        options.add_argument('--headless')
        driver = webdriver.Firefox(options=options)
        driver.implicitly_wait(1)
        
        crawler = Crawler(driver)
        jobsList = crawler.scrape()
        
        exporter = Exporter('./out')
        exporter.export_to_csv(jobsList)

    except Exception as e:
        print(e)
    except KeyboardInterrupt:
        print("Program interrupted by user")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
    exit(0)
