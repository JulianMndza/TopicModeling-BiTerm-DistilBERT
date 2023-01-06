# Topic Modeling from Facebook comments from LGU public information pages using BiTerm and DistilBERT
[![Generic badge](https://img.shields.io/badge/build-passed-<COLOR>.svg)](https://shields.io/)      [![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)

This project contains modules which model topics from Facebook comments from LGU public information pages using BiTerm and DistilBERT

## File Descriptions
1. FB-Comment-Extract.py
    >Scrapes the comments in the links provided in the basic_links.csv.
2. Preprocessing.py
    >Handles the preprocessing of the dataset and is responsible for the removal of stopwords.
3. Embedding.npy
    >pre-loaded embeddings for faster run time, if ever the data set has been changed or updated a new embedding.npy should be generated.
4. TopicModeling-DistillBert.py
    >A BERT topic model.
5. coherenceModel.py
    >Coherence model that uses the top words for every topic to determine the coherence score of the algorithm using 4 different coherence measure: UMass, C_V, UCI, NPMI
6.  TopicModeling-Biterm_Plus.ipynb
    >A Biterm topic model.
6. basic_links.csv
    >Contains all links for scraping.
7. preprocessed_comments.csv
    >Contains the preprocessed comments that will be used by both topic models.

## Installation & Requirements
##### Minimum System Requirements:
- 64-bit versions of Microsoft Windows 10, 8, 7 (SP1)
- AMD Ryzen 3,  Intel Core i3
- 8 GB RAM minimum, 16 GB RAM recommended
- 1.5 GB hard disk space + at least 1 GB for caches
- Python 3.5 or newer
- PyCharm 64-bit
- Jupyter Notebook

##### Project Setup Instructions:
1. Download zip and extract the files
2. Download the specific chromedrive that matches your chrome version and put the exe file in the Drivers folder of the project.
3. Copy/Move the files into the project folder
4. Open the all files in PyCharm
5. Open the file TopicModel-Biterm_Plus.ipynb in jupyter notebook
6. Install the following libraries using pip or conda:
        - bitermplus
        - umap
        - hdbscan
        - numpy
        - tqdm
        - os
        - sklearn
        - gensim
        - re
        - pandas
        - warnings
        - nltk
        - selenium
        - time
        - BERTopic


## How-to-use
> ##### New Data set
    1. if you need a new data set, put all links in the basic_links.csv file and run FB-Comment-Extract.py
    2. After running the FB scraper, run the preprocessing.py file to clean the data set
> #### Run the models
    1. if you installed all required libraries run both topic model. To be able to run the Bitermplus model you would have to run it in Jupyter Notebook alongside the coherenceModel.py 


 


 
 



