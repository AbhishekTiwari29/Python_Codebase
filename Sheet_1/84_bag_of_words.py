def bag_of_words(sentences):

    words = []

    for sentence in sentences:
        for word in sentence.lower().split():
            if word not in words:
                words.append(word)

    result = []

    for sentence in sentences:
        vector = []
        for word in words:
            vector.append(sentence.lower().split().count(word))

        result.append(vector)

    print("Vocabulary:", words)
    print("Vectors:", result)


sentences = ["I love Python", "I love Java", "Python is easy","I love programming"]

bag_of_words(sentences)