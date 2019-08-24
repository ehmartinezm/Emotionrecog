from google_images_download import google_images_download
#instantiate the class
response = google_images_download.googleimagesdownload()
arguments = {"keywords":"roads","limit":100,"print_urls":True,"format":"jpg"}
paths = response.download(arguments)
#print complete paths to the downloaded images
print(paths)
