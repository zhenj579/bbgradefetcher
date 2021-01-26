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

executable_path = "c:\se\chromedriver.exe"

def getUsername():
    username = usernameEntry.get()
    return username

def getPassword():
    password = passwordEntry.get()
    return password;

def fillInCredentials(usernameField, passwordField, user, pw):
    usernameField.send_keys(user)
    passwordField.send_keys(pw)

def go():
    driver = webdriver.Chrome(executable_path)
    bblink = "https://ssologin.cuny.edu/cuny.html?resource_url=https%3A%2F%2Fbbhosted.cuny.edu%252F"
    driver.get(bblink)
    user = driver.find_element_by_id("CUNYfirstUsernameH")
    pw = driver.find_element_by_id("CUNYfirstPassword")
    theirUsername = getUsername()
    theirPassword = getPassword()
    fillInCredentials(user,pw, theirUsername, theirPassword)


getButton = tk.Button(root, text="Go", command=go).grid(row=2, column=1)

root.mainloop()
