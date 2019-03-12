# -*- coding: utf-8 -*-

from flask import jsonify, request
from parser_app import app
from search_functions import *
from config import SEARCH_TAGS, SEARCH_REGS


@app.route("/api/text/find_data", methods=["POST"])
def get_personal_info():
    """
    finds the desired data in the text
    :return: (dict) {"source_text": str, "personal_data": dict}
    """
    source_text = request.json.get("text")
    personal_data = find_by_tags(SEARCH_TAGS, source_text)
    personal_data["dates"] = find_by_regex(SEARCH_REGS["date"], source_text)
    # ответ сохранил с отсортированными по тегам найденными значениями,при необходимости можно легко изменить вид ответа
    return jsonify({
        "source_text": source_text,
        "personal_data": personal_data
    })


@app.route("/api/version", methods=["GET"])
def get_version():
    return jsonify({"version": "super"})
