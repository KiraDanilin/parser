# regular expressions
# можно написать регулярку для поиска даты в формате число строка число
SEARCH_REGS = {
    "date": r"\d{2,4}[\.?\-?]\d{2}[\.?\-?]\d{2,4}"
}

# word search tags
SEARCH_TAGS = ["Name", "Surn", "Patr", "Geox", "NUMB"]

# word search accuracy factor
# влияет на точность поиска, можно варьировать в зависимости от условий
PROB_THRESH = 0.3
