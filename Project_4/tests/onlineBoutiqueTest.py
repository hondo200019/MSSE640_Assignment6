import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class onlineBoutiqueTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)

    def tearDown(self):
        self.driver.quit()

    def test_buySunGlasses(self):
        driver = self.driver
        wait = self.wait

        # Go to onlineboutique.com
        driver.get("https://cymbal-shops.retail.cymbal.dev/")

        # Select sunglasses
        sunglasses = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/main/div[2]/div/div/div[1]/div[2]/a")))
        sunglasses.click()

        # Add to Cart
        addToCart_Btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Add To Cart']")))
        addToCart_Btn.click()

        # Verify the total is correct
        sunglasses_total = driver.find_element(By.XPATH, "//div[@class='col pr-md-0 text-right']//strong").text
        sunglasses_total = float(sunglasses_total[1:])

        shipping_cost = driver.find_element(By.XPATH, "/html/body/main/section/div/div[1]/div[3]/div[2]").text
        shipping_cost = float(shipping_cost[1:])

        grand_total = driver.find_element(By.XPATH, "/html/body/main/section/div/div[1]/div[4]/div[2]").text
        grand_total = float(grand_total[1:])

        self.assertAlmostEqual(sunglasses_total + shipping_cost, grand_total, places = 2)



if __name__ == "__main__":
    unittest.main()
