from selenium.webdriver.common.by import By
from urllib.parse import urlencode
from models.params import Params
from models.job import Job

BASE_URL = "https://careers.techint.com/search/"

class Crawler:
  def __init__(self, driver):
    self.driver = driver

    self.params = Params("", "argentina", 0)
    self.url = self.build_url(self.params)
    self.driver.implicitly_wait(1)   

    self.driver.get(self.url)

    self.jobsList = []

  def scrape(self):
    self.get_jobs_from_job_board()
    self.get_jobs_details()

    return self.jobsList

  def get_jobs_from_job_board(self):
    self.driver.get(self.url)

    self.page_controls = self.driver.find_elements(By.CLASS_NAME, "pagination") # First page navigation controls
    self.page_count = len(self.page_controls) - 2 # -2 because of the page navigation buttons
    
    for _ in (range(self.page_count)):
      self.jobs = self.driver.find_elements(By.CLASS_NAME, "data-row")
      
      for job in self.jobs:
        colTitle = job.find_element(By.CLASS_NAME, "colTitle").text
        colLocation = job.find_element(By.CLASS_NAME, "colFacility").text
        colType = job.find_element(By.CLASS_NAME, "colLocation").text
        colDate = job.find_element(By.CLASS_NAME, "colDate").text
        colHrefDetails = job.find_element(By.TAG_NAME, "a").get_attribute("href")

        self.jobsList.append(
          Job(colTitle, colLocation, colType, colDate, colHrefDetails, 'N/A')
        )
      
      self.next_page()

  def get_jobs_details(self):
    for job in self.jobsList:
      self.driver.get(job.href_details)
      self.driver.implicitly_wait(1)
      job.details = self.driver.find_element(By.CLASS_NAME, "jobdescription").text

  def build_url(self, params):
    return f"{BASE_URL}?{urlencode(params.as_dict())}"

  def next_page(self):
    self.params.startrow += 25
    self.driver.get(self.build_url(self.params))
    self.driver.implicitly_wait(0.5)
