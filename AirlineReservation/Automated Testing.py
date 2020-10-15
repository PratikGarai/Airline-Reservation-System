from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver =  webdriver.Firefox()
#driver  = webdriver.Chrome()

n_tests = 8
n_passed = 0

# <h3>Test 1</h3>
# Conditions : Distinct source and destination<br>
# Expected : Success
print("Press enter to activate test 1 .... ")
input()
print()
driver.delete_all_cookies();
driver.get("http://localhost:8000")
element = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR,"input.form-control:nth-child(4)")))
source = driver.find_element(By.CSS_SELECTOR,"select#id_source")
destination = driver.find_element(By.CSS_SELECTOR,"select#id_destination")
button = driver.find_element(By.CSS_SELECTOR,"input.form-control:nth-child(4)")
source.send_keys("india")
destination.send_keys("france")
button.click()
print("Test 1 : Distinct Source Destination Test")
print("Input : ")
print("Source      : india")
print("Destination : france")
print("Expected : Success")
#checking for errors
try :
    error = driver.find_element(By.CSS_SELECTOR,"div.main-body-block div.error-block")
    print("Got      : Error")
    print("Test failed")
except:
    print("Got      : Success")
    n_passed += 1
    print("Test passed")
print("\n--------------------------------\n")

# <h3>Test 2</h3>
# Conditions : Same source and destination<br>
# Expected : Faliure
print("Press enter to activate test 2 .... ")
input()
print()
driver.delete_all_cookies();
driver.get("http://localhost:8000")
element = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR,"input.form-control:nth-child(4)")))
source = driver.find_element(By.CSS_SELECTOR,"select#id_source")
destination = driver.find_element(By.CSS_SELECTOR,"select#id_destination")
button = driver.find_element(By.CSS_SELECTOR,"input.form-control:nth-child(4)")
source.send_keys("india")
destination.send_keys("india")
button.click()
print("Test 2 : Same Source Destination Test")
print("Input : ")
print("Source      : india")
print("Destination : india")
print("Expected : Error")
#checking for errors
try :
    error = driver.find_element(By.CSS_SELECTOR,"div.main-body-block div.error-block")
    print("Got      : Error")
    n_passed += 1
    print("Test passed")
except:
    print("Got      : Success")
    print("Test failed")
print("\n--------------------------------\n")

# <h3>Test 3</h3>
# Conditions : Correct Registration<br>
# Expected : Success
print("Press enter to activate test 3 .... ")
input()
print()
driver.delete_all_cookies();
driver.get("http://localhost:8000/accounts/register")
name_ = "user"+str(time.time())[-6:]
pass_ = "password"
element = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR,"input.form-control:nth-child(5)")))
name = driver.find_element(By.CSS_SELECTOR,"input#id_username")
passwd = driver.find_element(By.CSS_SELECTOR,"input#id_password")
email = driver.find_element(By.CSS_SELECTOR,"input#id_email")
name.send_keys(name_)
passwd.send_keys(pass_)
email.send_keys(name_+"@test.com")
button = driver.find_element(By.CSS_SELECTOR,"input.form-control:nth-child(5)")
button.click()
print("Test 3 : Correct Registration Test")
print("Input : ")
print("Username :", name_)
print("Password :", pass_)
print("Email    :", name_+"@test.com")
print("Expected : Success")
#checking for errors
try :
    error = driver.find_element(By.CSS_SELECTOR,"div.main-body-block div.error-block")
    print("Got      : Error")
    print("Test failed")
except:
    print("Got      : Success")
    n_passed += 1
    print("Test passed")
print("\n--------------------------------\n")


# <h3>Test 4</h3>
# Conditions : Wrong Registration<br>
# Expected : Error
print("Press enter to activate test 4 .... ")
input()
print()
driver.delete_all_cookies();
driver.get("http://localhost:8000/accounts/register")
name_ = "user**"+str(time.time())[-6:]
pass_ = "password"
element = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR,"input.form-control:nth-child(5)")))
name = driver.find_element(By.CSS_SELECTOR,"input#id_username")
passwd = driver.find_element(By.CSS_SELECTOR,"input#id_password")
email = driver.find_element(By.CSS_SELECTOR,"input#id_email")
name.send_keys(name_)
passwd.send_keys(pass_)
email.send_keys(name_+"@test.com")
button = driver.find_element(By.CSS_SELECTOR,"input.form-control:nth-child(5)")
button.click()
print("Test 4 : Wrong Registration Test")
print("Input : ")
print("Username :", name_)
print("Password :", pass_)
print("Email    :", name_+"@test.com")
print("Expected : Error")
#checking for errors
try :
    error = driver.find_element(By.CSS_SELECTOR,"div.main-body-block div.error-block")
    print("Got      : Error")
    n_passed += 1
    print("Test passed")
except:
    print("Got      : Success")
    print("Test failed")
print("\n--------------------------------\n")

# <h3>Test 5</h3>
# Conditions : Correct Login<br>
# Expected : Success
print("Press enter to activate test 5 .... ")
input()
print()
driver.delete_all_cookies();
driver.get("http://localhost:8000/accounts/login")
element = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR,"input.form-control:nth-child(4)")))
name = driver.find_element(By.CSS_SELECTOR,"input#id_username")
passwd = driver.find_element(By.CSS_SELECTOR,"input#id_password")
name.send_keys("pratik")
passwd.send_keys("pratik")
button = driver.find_element(By.CSS_SELECTOR,"input.form-control:nth-child(4)")
button.click()
print("Test 5 : Correct Login Test")
print("Input : ")
print("Username : pratik")
print("Password : pratik")
print("Expected : Success")
#checking for errors
try :
    error = driver.find_element(By.CSS_SELECTOR,"div.main-body-block div.error-block")
    print("Got      : Error")
    print("Test failed")
except:
    print("Got      : Success")
    n_passed += 1
    print("Test passed")
print("\n--------------------------------\n")


# <h3>Test 6</h3>
# Conditions : False Login<br>
# Expected : Error
print("Press enter to activate test 6 .... ")
input()
print()
driver.delete_all_cookies();
driver.get("http://localhost:8000/accounts/login")
element = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR,"input.form-control:nth-child(4)")))
name = driver.find_element(By.CSS_SELECTOR,"input#id_username")
passwd = driver.find_element(By.CSS_SELECTOR,"input#id_password")
name.send_keys("pratik")
passwd.send_keys("wrong_pass")
button = driver.find_element(By.CSS_SELECTOR,"input.form-control:nth-child(4)")
button.click()
print("Test 6 : Wrong Login Test")
print("Input : ")
print("Username : pratik")
print("Password : wrong_pass")
print("Expected : Success")
print("Expected : Error")
#checking for errors
try :
    error = driver.find_element(By.CSS_SELECTOR,"div.main-body-block div.error-block")
    print("Got      : Error")
    n_passed += 1
    print("Test passed")
except:
    print("Got      : Success")
    print("Test failed")
print("\n--------------------------------\n")

# <h3>Test 7</h3>
# Conditions : Standard flight booking<br>
# Expected : Success
print("Press enter to activate test 7 .... ")
input()
print()
driver.delete_all_cookies();
driver.get("http://localhost:8000")
element = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR,"input.form-control:nth-child(4)")))
source = driver.find_element(By.CSS_SELECTOR,"select#id_source")
destination = driver.find_element(By.CSS_SELECTOR,"select#id_destination")
button = driver.find_element(By.CSS_SELECTOR,"input.form-control:nth-child(4)")
source.send_keys("pakistan")
destination.send_keys("india")
button.click()
element = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR,"div.main-body-block div.flight-div a.btn.btn-success")))
book_button = driver.find_element(By.CSS_SELECTOR,"div.main-body-block div.flight-div a.btn.btn-success")
txt = driver.find_element(By.CSS_SELECTOR,"div.flight-div:nth-child(1) > table:nth-child(3) > tbody:nth-child(1) > tr:nth-child(3) > td:nth-child(2)").text
passengers = int(list(txt.split(" "))[0])//10
book_button.click()
element = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR,"input.form-control:nth-child(4)")))
name = driver.find_element(By.CSS_SELECTOR,"input#id_username")
passwd = driver.find_element(By.CSS_SELECTOR,"input#id_password")
name.send_keys("pratik")
passwd.send_keys("pratik")
button = driver.find_element(By.CSS_SELECTOR,"input.form-control:nth-child(4)")
button.click()
element = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR,"input.form-control:nth-child(3)")))
name = driver.find_element(By.CSS_SELECTOR,"input#id_n_passenger")
name.send_keys(passengers)
button = driver.find_element(By.CSS_SELECTOR,"input.form-control:nth-child(3)")
button.click()
print("Test 7 : Correct Booking Test")
print("Input : Booking tickets for passengers not exceeding the vacancy of flight")
print("Expected : Success")
#checking for errors
try :
    error = driver.find_element(By.CSS_SELECTOR,"div.main-body-block div.error-block")
    print("Got      : Error")
    print("Test failed")
except:
    print("Got      : Success")
    n_passed += 1
    print("Test passed")
print("\n--------------------------------\n")

# <h3>Test 8</h3>
# Conditions : Standard flight booking with passenger overload<br>
# Expected : Failure
print("Press enter to activate test 8 .... ")
input()
print()
driver.delete_all_cookies();
driver.get("http://localhost:8000")
element = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR,"input.form-control:nth-child(4)")))
source = driver.find_element(By.CSS_SELECTOR,"select#id_source")
destination = driver.find_element(By.CSS_SELECTOR,"select#id_destination")
button = driver.find_element(By.CSS_SELECTOR,"input.form-control:nth-child(4)")
source.send_keys("pakistan")
destination.send_keys("india")
button.click()
element = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR,"div.main-body-block div.flight-div a.btn.btn-success")))
book_button = driver.find_element(By.CSS_SELECTOR,"div.main-body-block div.flight-div a.btn.btn-success")
txt = driver.find_element(By.CSS_SELECTOR,"div.flight-div:nth-child(1) > table:nth-child(3) > tbody:nth-child(1) > tr:nth-child(3) > td:nth-child(2)").text
passengers = int(list(txt.split(" "))[0])+1
book_button.click()
element = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR,"input.form-control:nth-child(4)")))
name = driver.find_element(By.CSS_SELECTOR,"input#id_username")
passwd = driver.find_element(By.CSS_SELECTOR,"input#id_password")
name.send_keys("pratik")
passwd.send_keys("pratik")
button = driver.find_element(By.CSS_SELECTOR,"input.form-control:nth-child(4)")
button.click()
element = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR,"input.form-control:nth-child(3)")))
name = driver.find_element(By.CSS_SELECTOR,"input#id_n_passenger")
name.send_keys(passengers)
button = driver.find_element(By.CSS_SELECTOR,"input.form-control:nth-child(3)")
button.click()
print("Test 7 : Incorrect Booking Test")
print("Input : Booking tickets for passengers exceeding the vacancy of flight")
print("Expected : Error")
#checking for exceed warning
element = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR,"div.main-body-block")))
txt = driver.find_element(By.CSS_SELECTOR,"div.main-body-block").text
if txt.strip()=="Number of bookings exceeds vacancy!":
    print("Got      : Error")
    n_passed += 1
    print("Test passed")
else:
    print("Got      : Success")
    print("Test failed")
print("\n--------------------------------\n")

print(n_passed,"tests passed out of",n_tests)
driver.quit()
