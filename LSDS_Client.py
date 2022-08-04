# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import requests
import re

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def responseToLoanDict(aresponse):
    regex = r"\{(.*?)\}"
    match = re.search(regex,aresponse)
    substr = match.group()[2:-1]
    thePieces = substr.split("|")
    newLoan = dict()
    parts = thePieces[0].split("=")
    newLoan[parts[0].strip()] = int(parts[1])
    parts = thePieces[1].split("=")
    newLoan[parts[0].strip()] = parts[1].strip()
    parts = thePieces[2].split("=")
    newLoan[parts[0].strip()] = parts[1].strip()
    parts = thePieces[3].split("=")
    newLoan[parts[0].strip()] = parts[1].strip()
    parts = thePieces[4].split("=")
    newLoan[parts[0].strip()] = parts[1].strip()
    return newLoan

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

BASE_URL = "http://localhost:8080/LSDS_Brewster_RestService-1.0-SNAPSHOT/api"

# try our get loan for ID 100, which may work if server has been up
response = requests.get(f"{BASE_URL}/loan?id=100")
print("response from getLoan call: " + response.text)

# now let's create a loan
loan = {
    "id":0,
    "amount":"200,000.00",
    "rate":"3.5%",
    "term":"36",
    "payment":"22,432.11"
}
response = requests.post(f"{BASE_URL}/loan/create",json=loan)
print("response from createLoan call: " + response.text)

# what happens right now if we create a loan with duplicate id
loan = {
    "id":101,
    "amount":"200,000.00",
    "rate":"3.5%",
    "term":"36",
    "payment":"22,432.11"
}
response = requests.post(f"{BASE_URL}/loan/create",json=loan)
print("response from createLoan call: " + response.text)

# create another loan
loan = {
    "id":0,
    "amount":"200,000.00",
    "rate":"3.5%",
    "term":"36",
    "payment":"22,432.11"
}
response = requests.post(f"{BASE_URL}/loan/create",json=loan)
print("response from createLoan call: " + response.text)

# try our get loan for ID 101, which may work if server has been up
response = requests.get(f"{BASE_URL}/loan?id=101")
print("get for loan id 101: " + response.text)

# let's update a loan
response = requests.get(f"{BASE_URL}/loan?id=102")
aNewLoan = responseToLoanDict(response.text)
aNewLoan.update({"amount":"350,000.00"})
aNewLoan.update({"rate":"2.5%"})
response = requests.post(f"{BASE_URL}/loan/update",json=aNewLoan)
print("response from updateLoan call: " + response.text)

# create another loan
loan = {
    "id":0,
    "amount":"200,000.00",
    "rate":"3.5%",
    "term":"36",
    "payment":"22,432.11"
}
response = requests.post(f"{BASE_URL}/loan/create",json=loan)
print("response from createLoan call: " + response.text)

# now let's update the loan we just created
aNewLoan = responseToLoanDict(response.text)
aNewLoan.update({"term":"120"})
aNewLoan.update({"payment":"9,876.00"})
response = requests.post(f"{BASE_URL}/loan/update",json=aNewLoan)
print("response from updateLoan call: " + response.text)
