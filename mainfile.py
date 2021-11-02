import webbrowser, time
url = input("Enter URL:")
duration = input("Enter DURATION:")
views = input("Enter the number of views you want:")
for i in range(views):
  webbrowser.open_new(url)
  time.sleep(int(duration))
