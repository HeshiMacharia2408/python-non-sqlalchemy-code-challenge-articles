#!/usr/bin/env python3
import ipdb;

from classes.many_to_many import Article
from classes.many_to_many import Author
from classes.many_to_many import Magazine

if __name__ == '__main__':
    print("HELLO! :) let's debug :vibing_potato:")

    # don't remove this line, it's for debugging!
    ipdb.set_trace()

class Author:
    def _init_(self, name):
        if not isinstance(name, str):
            return TypeError("Please input a name of type str.")
        if len(name) == 0:
            return ValueError("Please fill in your name.")
        self._name = name
        self._articles = []

    def name(self):
        return self._name
        if hasattr(self, '_Author__name'):
            raise AttributeError("Unable to change name")

    def articles(self):
        return self._articles

    def magazines(self):
        return list({article.magazine for article in self._articles})

    def topic_areas(self):
        categories = set()
        for article in self._articles:
            categories.add(article.magazine.category)
        return list(categories) if categories else None


class Magazine:
    def _init_(self, name, category):
        if not isinstance(name, str):
            return TypeError("Please input a name of type str.")
        if (2 <= len(name) <= 16):
            return ValueError("Please input a name containing  between 2 to 16 characters")
        if not isinstance(category, str):
            return TypeError("Please input a category of type str.")
        if len(category) == 0:
            return ValueError("Please fill in the category.")
        self._name = name
        self._category = category
        self._articles = []

    def name(self):
        return self._name 
    
    def category(self):
        return self._category

    def add_article(self, author, title):
        article = Article(author, self, title)
        self._articles.append(article)
        return article

    def articles(self):
        return self._articles

    def article_titles(self):
        return [article.title for article in self._articles]

    def contributors(self):
        contributors = []
        author_counts = {}
        for article in self._articles:
            author = article.author
            if author not in author_counts:
                author_counts[author] = 0
            author_counts[author] += 1
        for author, count in author_counts.items():
            if count > 2:
                contributors.append(author)
        return contributors if contributors else None


class Article:
    def _init_(self, author, magazine, title):
        if not isinstance(title, str):
            raise TypeError("Please input a title of type str.")
        if not (5 <= len(title) <= 50):
            raise ValueError("Please input a title that contains between 5 and 50 characters.")
        self._author = author
        self._magazine = magazine
        self._title = title

    def title(self):
        return self._title

    def author(self):
        return self._author

    def magazine(self):
        return self._magazine

    
