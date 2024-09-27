# QuIC-360°: Query-based Image Captioning for 360° Images

## Overview

This repository provides the QuIC-360° dataset, a query-based image captioning dataset for 360° images.
QuIC-360° is the first dataset that includes captions annotated based on textual scene queries to describe diverse contexts of 360° images. While existing image captioning datasets are based on images with limited field-of-view, 360° images capture the entire visible context of scenes, offering richer information.
This dataset can be used to develop systems that generate textual descriptions aligned with user interests and relevant contexts from 360° images.

## Dataset Details

### Fundamental Information

- Number of images: 3,940
- Number of captions: 18,459
- Number of queries: 34
- Image source: Flickr, Refer360°
- Caption annotation: Amazon Mechanical Turk (MTurk)
- Average caption length: 19.4 words
- Vocabulary size: 10,862

### Dataset Split

- Train: 3,000 images
- Valid: 400 images
- Test: 400 images
- Refer-test: 140 images (from Refer360°)

### Queries

We pre-defined 34 scene queries that are suitable for describing 360° scenes. (See Table 2)

### License

The license for this dataset is [describe the license here].

### Usage Examples

The QuIC-360° dataset can be used for research in the following areas:

- Query-based image caption generation
- 360° image scene understanding
- Text generation from multi-context images
- User-interest-aware image description generation

## Paper

For more details about this dataset, please refer to the following paper:
[Describe the paper title, authors, etc.]

### Citation

You can copy below or cite with the key `maeda-etal-2023-query` in anthology.bib.

```
@inproceedings{maeda-etal-2023-query,
    title = "Query-based Image Captioning from Multi-context 360$cdegree$ Images",
    author = "Maeda, Koki  and
      Kurita, Shuhei  and
      Miyanishi, Taiki  and
      Okazaki, Naoaki",
    booktitle = "Findings of the Association for Computational Linguistics: EMNLP 2023",
    month = dec,
    year = "2023",
    address = "Singapore",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2023.findings-emnlp.463",
    doi = "10.18653/v1/2023.findings-emnlp.463",
    pages = "6940--6954",
}
```

### Acknowledgements
Please contact `koki.maeda[at]nlp.c.titech.ac.jp` if you have any questions or feedback.
