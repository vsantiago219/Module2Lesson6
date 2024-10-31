#Product Review Analysis
# #Task 1 Task 1: Keyword Highlighter

keywords = {
    'good': 'upper',
    'excellent': 'upper',
    'bad': 'upper',  
    'poor': 'upper',
    'average':'upper'
}
review = input("Enter review: ")

def change_case(review, keywords):
    for word, case in keywords.items():
        if case == 'upper':
            review = review.replace(word, word.upper())
       
    return review

modified_review = change_case(review, keywords)
print(modified_review)

           

#Task 2: Sentiment Tally

positive_words_to_count = ["good", "awesome", "fantastic", "superb", "excellent", "great" ]
negative_words_to_count = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]
# review = input("Enter review: ")



word_counts = {word: 0 for word in positive_words_to_count}
word_counts = {word: 0 for word in negative_words_to_count}

for word in positive_words_to_count:
    word_counts[word] = review.lower().split().count(word.lower())

for word in negative_words_to_count:
    word_counts[word] = review.lower().split().count(word.lower())

for word, count in word_counts.items():
    print(f"The word '{word}' appears {count} times.")


    

# #Task 3   : Reviews Summary

def get_first_n_chars(review, n):
    if n <= 0:
        return ""
    
    result = ""
    for char in review[:n]:  
        result += char  
        if char == ' ': 
            if len(result) > n:
                return result[:-1] 
   
    return result.rsplit(' ', 1)[0] if ' ' in result else result

result = get_first_n_chars(review, " ", 30, ...)
print(result)
