# CBIR system (Image search engine)

There are three types of image search engines: **search by meta-data**, **search by example**, and a **hybrid approach** of the two.

## Search By Meta-data

When a user performs a search on a search by meta-data system they provide a query, just like in a traditional text search engine, and then images that have similar tags or annotations are returned.

## Search By Example

Search by example systems, on the other hand, rely solely on the contents of the image no keywords are assumed to be provided. The image is analyzed, quantified, and stored so that similar images are returned by the system during a search.

Image search engines that quantify the contents of an image are called **Content-Based Image Retrieval** (CBIR) systems. The term CBIR is commonly used in the academic literature, but in reality, it’s simply a fancier way of saying “image search engine”, with the added poignancy that the search engine is relying strictly on the contents of the image and not any textual annotations associated with the image.

## The 4 Steps of Any CBIR System

- **Defining your image descriptor:**
  At this phase you need to decide what aspect of the image you want to describe. Are you interested in the color of the image? The shape of an object in the image? Or do you want to characterize texture?
- **Indexing your dataset:**
  Now that you have your image descriptor defined, your job is to apply this image descriptor to each image in your dataset, extract features from these images, and write the features to storage (ex. CSV file, RDBMS, Redis, etc.) so that they can be later compared for similarity.
- **Defining your similarity metric:**
  Cool, now you have a bunch of feature vectors. But how are you going to compare them? Popular choices include the Euclidean distance, Cosine distance, and chi-squared distance, but the actual choice is highly dependent on (1) your dataset and (2) the types of features you extracted.
- **Searching:**
  The final step is to perform an actual search. A user will submit a query image to your system (from an upload form or via a mobile app, for instance) and your job will be to (1) extract features from this query image and then (2) apply your similarity function to compare the query features to the features already indexed. From there, you simply return the most relevant results according to your similarity function.

![](https://pyimagesearch.com/wp-content/uploads/2014/11/preprocessing_and_indexing.jpg)
![](https://pyimagesearch.com/wp-content/uploads/2014/11/searching.jpg)

## Notes

- In order to build this system, we’ll be using a simple, yet effective image descriptor: **the color histogram**.
- By utilizing a color histogram as our image descriptor, we’ll be relying on the color distribution of the image. Because of this, we have to make an important assumption regarding our image search engine: **The Assumption:** Images that have similar color distributions will be considered relevant to each other. Even if images have dramatically different contents, they will still be considered “similar” provided that their color distributions are similar as well.
- Using **regions-based** histograms rather than **global** histograms allows us to simulate locality in a color distribution.
- It is very important that you normalize your color histograms so each histogram is represented by the relative percentage counts for a particular bin and not the integer counts for each bin.
  Again, performing this normalization will ensure that images with similar content but dramatically different dimensions will still be “similar” once we apply our similarity function.
- Since we are comparing color histograms, which are by definition probability distributions, the **chi-squared** function is an excellent choice.
  In general, the difference between large bins vs. small bins is less important and should be weighted as such — and this is exactly what the chi-squared distance function does.

## Steps

1. **Defining The Image Descriptor**
2. **Extracting Features from The Dataset (Indexing)**
   ```
   python3 index.py --dataset dataset --index index.csv
   ```
   This script shouldn’t take longer than a few seconds to run. After it is finished you will have a new file, index.csv .
   You’ll see that for each row in the .csv file, the first entry is the filename, followed by a list of numbers. These numbers are your feature vectors and are used to represent and quantify the image.
3. **Defining The Searsher**
   It extract features from the query image and calculate the chi-squared distance between the query image and all of images in the dataset then return the nearest 10 images as a result
   use this script to run the searcher:
   ```
   python3 search.py --index index.csv --query queries/0.jpg --result-path
   ```

## Summary

To build our image search engine.
We utilized a color histogram to characterize the color distribution of our photos. Then, we indexed our dataset using our color descriptor, extracting color histograms from each of the images in the dataset.
To compare images we utilized the chi-squared distance, a popular choice when comparing discrete probability distributions.
From there, we implemented the necessary logic to accept a query image and then return relevant results.

[**Reference**](https://pyimagesearch.com/2014/12/01/complete-guide-building-image-search-engine-python-opencv/)
