# Task 1: Keyword Highlighter

keywords = ["good", "excellent", "bad", "poor", "average"]

reviews = [ "This product is really good. I'm impressed with its quality.", "The performance of this product is excellent. Highly recommended!", "I had a bad experience with this product. It didn't meet my expectations.", "This was a poor quality product. Wouldn't recommend it to anyone.", "The product was average. Nothing extraordinary about it." ]

for word in keywords:
    for review in reviews:
        if word in review:
            review = review.replace(word, word.upper())
            print(review)

print('='*50)

            # OR
for word in keywords:
    for review in reviews:
        if word in review:
            print(review,": ", word.upper())


print('='*50)
#  Task 2: Sentiment Tally

positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]

negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]

def sentiment_tally():
    for review in reviews:
                 positive_count = sum(review.count(word1) for word1 in positive_words)
                 negative_count = sum(review.count(word2) for word2 in negative_words)
                 print(review,  "Positive counts:", positive_count, "Negative counts:", negative_count)

sentiment_tally()

print('='*50)

# Task 3: Review Summary

def create_summary(review):
    
    summary = review[:30] + "…"
    return summary

summaries = [create_summary(review) for review in reviews]

for summary in summaries:
    print(summary)

create_summary
