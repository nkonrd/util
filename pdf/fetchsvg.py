import requests, time, threading

name = ""
totalPages = 0

def getPage(pageNumber):
   response = requests.get(urls[pageNumber])

   if response.status_code == 200:
      with open(name + "/" + str(pageNumber) + ".svg", 'wb') as f:
         f.write(response.content)
         f.close()

         print('Fetched page ' + str(pageNumber))

   else:
      print("Error occured on page " + str(pageNumber) + "...")

print("Fetching...")

page = 0
while page < totalPages:
   threading.Thread(target = getPage, args = (page,)).start()   
   page += 1
   time.sleep(0.5)

print("done") 