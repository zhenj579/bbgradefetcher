from selenium import webdriver
import tkinter as tk

root = tk.Tk()
root.title("Blackboard grade fetcher")

dimension = "200x75"

usernameLabel = tk.Label(root, text="Username").grid(row=0)
passwordLabel = tk.Label(root, text="Password").grid(row=1)

usernameEntry = tk.Entry(root)
passwordEntry = tk.Entry(root, show="*")

usernameEntry.grid(row=0, column=1)
passwordEntry.grid(row=1, column=1)

root.geometry(dimension)


def getUsername():
    username = usernameEntry.get()
    return username


def getPassword():
    password = passwordEntry.get()
    return password


def fillInCredentials(usernameField, passwordField, user, pw):
    usernameField.send_keys(user)
    passwordField.send_keys(pw)


def gotoBB(driver):
    bburl = "https://ssologin.cuny.edu/cuny.html?resource_url=https%3A%2F%2Fbbhosted.cuny.edu%252F"
    driver.get(bburl)


def fillOutForm(driver):
    driver.switch_to.parent_frame()
    user = driver.find_element_by_id("CUNYfirstUsernameH")
    pw = driver.find_element_by_id("CUNYfirstPassword")
    theirUsername = getUsername()
    theirPassword = getPassword()
    fillInCredentials(user, pw, theirUsername, theirPassword)
    submitButton = driver.find_element_by_id("submit")
    submitButton.click()

def handleRedirect(driver):
    driver.switch_to.parent_frame()
    bblink = driver.find_element_by_xpath("/html/body/div[1]/div/div/ul/li[1]/a")
    bblink.click()

def clickMyGrades(driver):
    driver.switch_to.parent_frame()
    mygrades = driver.find_element_by_xpath("/html/body/div[5]/div/div/div[2]/div[2]/div/div/div/div[4]/div[2]/div[2]/ul/li[4]/a")
    mygrades.click()

def go():
    executable_path = "c:\se\chromedriver.exe"
    driver = webdriver.Chrome(executable_path)
    gotoBB(driver)
    fillOutForm(driver)
    handleRedirect(driver)
    fillOutForm(driver)
    if driver.title[-16:] != "Blackboard Learn":
        driver.close()
        root.quit()
    clickMyGrades(driver)



getButton = tk.Button(root, text="Go", command=go).grid(row=2, column=1)

root.mainloop()
