# -*- coding: utf-8 -*-

import pymorphy2
import nltk
import re

from config import PROB_THRESH


morph = pymorphy2.MorphAnalyzer()


def find_by_tags(tags, text):
    """
    find all words in text by grammemes
    :param tags: (list) search tags
    :param text: (str) source text
    :return: (dict) dictionary with all matches grouped by tags
    """
    tags_compilation = {key: [] for key in tags}

    for word in nltk.word_tokenize(text):
        for word_value in morph.parse(word):
            for tag in tags:
                # можно избавиться от последней проверки используя множество вместо списка,
                # но тогда нужно немного покопаться с JSONEncoder
                if tag in word_value.tag and word_value.score >= PROB_THRESH and word not in tags_compilation[tag]:
                    tags_compilation[tag].append(word)

    return tags_compilation


def find_by_regex(reg, text):
    """
    returns a list of matched strings from source text
    :param reg: (raw string) regex
    :param text: (str) source text
    :return: (list) match list
    """
    return re.findall(reg, text)

