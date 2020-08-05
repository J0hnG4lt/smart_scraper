# Smart Scraper

Our intention here is twofold:

- See if we can learn how to use Sphinx
- See if we can develop a flexible web scraper.

## Use Cases:

- As a user, I want to scrape all fields related to a follower on GitHub just by giving some examples. This should take care automatically of pagination.

## Development

We are using Poetry as a virtual environment manager.

### Documentation

We are using Sphinx.

#### Conventions:

- The main README file is included in the documentation.
- All **__init__.py** files are responsible for including its respective modules and README files.

#### Build

To build all documentation, run the following:

```console
cd docs
make html
```

All documentation should be accessible from `docs/html/index.html`.

## References

### [Pattern](https://github.com/clips/pattern)

Pattern is a web mining module for Python. It has tools for:

    Data Mining: web services (Google, Twitter, Wikipedia), web crawler, HTML DOM parser
    Natural Language Processing: part-of-speech taggers, n-gram search, sentiment analysis, WordNet
    Machine Learning: vector space model, clustering, classification (KNN, SVM, Perceptron)
    Network Analysis: graph centrality and visualization.

It is well documented, thoroughly tested with 350+ unit tests and comes bundled with 50+ examples. The source code is licensed under BSD.
