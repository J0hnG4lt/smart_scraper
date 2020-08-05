# README file for smart_scraper.similarity

Here we define all the classes necessary for comparing strings extracted by a web scraper. Our intention is making any kind of scraper more flexible beyond any kind of rule we may define with XPaths.

## Folder Layout

- **strategy.py**: here we define classes with different algorithms for returning a float number that should indicate the similarity between two strings.
- **web_strings.py**: here we define wrappers for different kinds of strings.
