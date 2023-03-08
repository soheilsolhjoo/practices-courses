#!/usr/bin/env python
import wordcloud

# from matplotlib import pyplot as plt
# from IPython.display import display


def remove_unwanted(text_str):
    """Remove punctuation marks of a string."""
    # initializing punctuations string
    punc = """!()-[]{};:'"\,<>./?@#$%^&*_~"""

    clean_line = ""
    # Removing punctuations in string
    # Using loop
    for word in text_str:
        if word not in punc:
            clean_line += word
    return clean_line


def select_words(text_str):
    """Select only words and remove uninteresting ones"""

    uninteresting_words = ["a", "about", "above", "across", "after", "afterwards"]
    uninteresting_words += ["again", "against", "all", "almost", "alone", "along"]
    uninteresting_words += ["already", "also", "although", "always", "am", "among"]
    uninteresting_words += ["amongst", "amoungst", "amount", "an", "and", "another"]
    uninteresting_words += ["any", "anyhow", "anyone", "anything", "anyway", "anywhere"]
    uninteresting_words += ["are", "around", "as", "at", "back", "be", "became"]
    uninteresting_words += ["because", "become", "becomes", "becoming", "been"]
    uninteresting_words += ["before", "beforehand", "behind", "being", "below"]
    uninteresting_words += ["beside", "besides", "between", "beyond", "bill", "both"]
    uninteresting_words += ["bottom", "but", "by", "call", "can", "cannot", "cant"]
    uninteresting_words += ["co", "computer", "con", "could", "couldnt", "cry", "de"]
    uninteresting_words += ["describe", "detail", "did", "do", "done", "down", "due"]
    uninteresting_words += ["during", "each", "eg", "eight", "either", "eleven", "else"]
    uninteresting_words += ["elsewhere", "empty", "enough", "etc", "even", "ever"]
    uninteresting_words += ["every", "everyone", "everything", "everywhere", "except"]
    uninteresting_words += ["few", "fifteen", "fifty", "fill", "find", "fire", "first"]
    uninteresting_words += ["five", "for", "former", "formerly", "forty", "found"]
    uninteresting_words += ["four", "from", "front", "full", "further", "get", "give"]
    uninteresting_words += ["go", "had", "has", "hasnt", "have", "he", "hence", "her"]
    uninteresting_words += ["here", "hereafter", "hereby", "herein", "hereupon", "hers"]
    uninteresting_words += ["herself", "him", "himself", "his", "how", "however"]
    uninteresting_words += ["hundred", "i", "ie", "if", "in", "inc", "indeed"]
    uninteresting_words += ["interest", "into", "is", "it", "its", "itself", "keep"]
    uninteresting_words += [
        "last",
        "latter",
        "latterly",
        "least",
        "less",
        "ltd",
        "made",
    ]
    uninteresting_words += ["many", "may", "me", "meanwhile", "might", "mill", "mine"]
    uninteresting_words += ["more", "moreover", "most", "mostly", "move", "much"]
    uninteresting_words += [
        "must",
        "my",
        "myself",
        "name",
        "namely",
        "neither",
        "never",
    ]
    uninteresting_words += ["nevertheless", "next", "nine", "no", "nobody", "none"]
    uninteresting_words += ["noone", "nor", "not", "nothing", "now", "nowhere", "of"]
    uninteresting_words += ["off", "often", "on", "once", "one", "only", "onto", "or"]
    uninteresting_words += ["other", "others", "otherwise", "our", "ours", "ourselves"]
    uninteresting_words += ["out", "over", "own", "part", "per", "perhaps", "please"]
    uninteresting_words += ["put", "rather", "re", "s", "same", "see", "seem", "seemed"]
    uninteresting_words += ["seeming", "seems", "serious", "several", "she", "should"]
    uninteresting_words += ["show", "side", "since", "sincere", "six", "sixty", "so"]
    uninteresting_words += ["some", "somehow", "someone", "something", "sometime"]
    uninteresting_words += ["sometimes", "somewhere", "still", "such", "system", "take"]
    uninteresting_words += ["ten", "than", "that", "the", "their", "them", "themselves"]
    uninteresting_words += ["then", "thence", "there", "thereafter", "thereby"]
    uninteresting_words += ["therefore", "therein", "thereupon", "these", "they"]
    uninteresting_words += [
        "thick",
        "thin",
        "third",
        "this",
        "those",
        "though",
        "three",
    ]
    uninteresting_words += ["three", "through", "throughout", "thru", "thus", "to"]
    uninteresting_words += ["together", "too", "top", "toward", "towards", "twelve"]
    uninteresting_words += ["twenty", "two", "un", "under", "until", "up", "upon"]
    uninteresting_words += ["us", "very", "via", "was", "we", "well", "were", "what"]
    uninteresting_words += ["whatever", "when", "whence", "whenever", "where"]
    uninteresting_words += ["whereafter", "whereas", "whereby", "wherein", "whereupon"]
    uninteresting_words += ["wherever", "whether", "which", "while", "whither", "who"]
    uninteresting_words += ["whoever", "whole", "whom", "whose", "why", "will", "with"]
    uninteresting_words += ["within", "without", "would", "yet", "you", "your"]
    uninteresting_words += ["yours", "yourself", "yourselves"]

    text_str = text_str.split()
    alpha_detector = []
    for iter in text_str:
        alpha_detector.append(iter.isalpha())

    # L_new = []
    # for x in range(0,len(L)):
    #     if j[x] is True:
    #         print(L[x])
    #         L_new.append(L[x])
    return [
        text_str[word]
        for word in range(0, len(text_str))
        if (
            text_str[word].lower() not in uninteresting_words
            and alpha_detector[word] is True
        )
    ]


def word_counter(words_list, word_count):
    for word in words_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return word_count


def main():
    file_name = "paper.txt"
    poster_name = "paper_words.jpg"

    # Open
    text_file = open(file_name, "r")
    Lines = text_file.readlines()
    # print(Lines)

    # Read line-by-line
    clean_line = []
    words = []
    word_count = {}
    for line in Lines:
        # Remove punctuation marks
        # Collect words
        # Remove unineteresting words
        line = select_words(remove_unwanted(line.lower()))

        # Count words and update the dictionary
        word_count.update(word_counter(line, word_count))

    # Draw a word cloud
    cloud = wordcloud.WordCloud(width=800, height=600, scale=5)
    frequency = cloud.generate_from_frequencies(word_count)
    cloud.to_file(poster_name)

    # plt.imshow(frequency, interpolation="nearest")
    # plt.axis("off")
    # plt.show()


if __name__ == "__main__":
    main()
