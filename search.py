# import the necessary packages
from pyimagesearch.colordescriptor import ColorDescriptor
from pyimagesearch.searcher import Searcher
import argparse
import cv2
from matplotlib import pyplot

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--index", required=True,
                help="Path to where the computed index will be stored")
ap.add_argument("-q", "--query", required=True,
                help="Path to the query image")
ap.add_argument("-r", "--result-path", required=True,
                help="Path to the result path")
args = vars(ap.parse_args())
# initialize the image descriptor
cd = ColorDescriptor((8, 12, 3))

# load the query image and describe it
query = cv2.imread(args["query"])
features = cd.describe(query)
# perform the search
searcher = Searcher(args["index"])
results = searcher.search(features)

# create figure
fig = pyplot.figure(figsize=(10, 10))
# setting values to rows and column variables
rows = 7
columns = 2
index = 1

# showing image
fig.add_subplot(rows, columns, index)
pyplot.imshow(query)
pyplot.axis('off')
pyplot.title("Query")

index = index + 3

for (score, resultID) in results:
    # load the result image and display it
    result = cv2.imread(args["result_path"] + "/" + resultID)
    index = index + 1
    fig.add_subplot(rows, columns, index)
    pyplot.imshow(result)
    pyplot.axis('off')
    pyplot.title("")

pyplot.show()