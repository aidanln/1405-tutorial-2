#!/usr/bin/env python3

# By Aidan Lalonde-Novales and Jonathan Pasco-Arnone
# Created September 20th, 2023
# This program seachers through N-X.txt files to find relevant results.

import linecache

'''
FUNCTIONS SECTION
'''

# counts total times a users search term appears
def user_word_counter(filename, user_search):
    search_line = 1
    times_appeared = 0
    while linecache.getline(filename, search_line) != "":
        if linecache.getline(filename, search_line) == (user_search + "\n"):
            times_appeared += 1
        search_line += 1
    return times_appeared

# counts total words
def total_word_counter(filename):
    search_line = 1
    total_words = 0
    while linecache.getline(filename, search_line) != "":
        search_line += 1
        total_words += 1
    return total_words

# finds ratio of a users search term versus total words
def ratio_finder(filename, user_search):
    user_words = user_word_counter(filename, user_search)
    total_words = total_word_counter(filename)
    if (user_words != 0):
        return round((user_words / total_words), 4)
    else:
        return 0

# finds the index of the largest value of in a list
def index_of_max(desired_list):
    max_value = 0
    max_index = 0
    for i in range(0, (len(desired_list) - 1)):
        if desired_list[i] > max_value:
            max_value = desired_list[i]
            max_index = i
    return max_index

# runs through pages.txt and the above functions to find the files with the
# most of the user's search term and the highest ratio of said search term.
def main_search(user_search):
    search_line = 1
    word_list = []
    ratio_list = []
    while linecache.getline("pages.txt", search_line) != "":
        # removes the "\n" from the end of filename so that my
        # other functions can actually read the filename variable
        filename = list(linecache.getline("pages.txt", search_line))
        filename.pop()
        filename = "".join(filename)
        word_list.append(user_word_counter(filename, user_search))
        ratio_list.append(ratio_finder(filename, user_search))
        search_line += 1

    # results section
    print("\nResults...\n")
    print("Max Page (Count): N-" + str(index_of_max(word_list)) + ".txt")
    print("Max Count:", max(word_list))
    print("Max Page (Ratio): N-" + str(index_of_max(ratio_list)) + ".txt")
    print("Max Ratio:", max(ratio_list))

'''
MAIN SECTION
'''

# ask the user for a search term and show them the most relevant .txt file
def main():
    
    print("\nWelcome to my Search Engine!")
    user_search = input("\nEnter your search term: ")
    main_search(user_search)

    print("\nDone.")

if __name__ == "__main__":
    main()