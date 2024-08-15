    `# VSM  = Vector support Model 
    # use to convert text into vector number

    # methods => 1. One hot coding
    #            2. Bag of words
    #            3. TF-IDF
    #            4. Word Embedding
    #            5. Label Encoding


    '''
    label encoding 
    use to assign the number as per the index of digit like ->
    hello any one is here or not
    1     2   3   4  5    6  7
    '''


    '''
    one hot encoding 
    use to assign the binary as per they placed ins sentence like ->
    hello     any      one       is       here or  not  { 1,2,3,4,5,6,7} => 0000000
    1000000   0100000  0010000   0001000 ........  0000001
    '''

    '''
    Bag of words
    use to count the  number of occurance of words in sentence
    '''

    # Using Bag of word
    import pandas as pd 
    import numpy as np 

    df = pd.read_csv('spam.csv')
    print(df.Category.value_counts())

    # making new cloumn where spam is 1 or ham is 0

    df['spam'] =df['Category'].apply(lambda x:1 if x == 'spam' else 0)
    print(df.head(2))

    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(df.Message, df.spam, test_size=0.2)
    print(type(X_train.values))


    from sklearn.feature_extraction.text import CountVectorizer     # for use of bag of word
    v = CountVectorizer()
    X_train_cv = v.fit_transform(X_train.values)       # count the number of occurance of words in sentence 
    print(X_train_cv.shape)

    X_train_cv_np = X_train_cv.toarray()

    # Train the naive bayes model
    from sklearn.naive_bayes import MultinomialNB
    model = MultinomialNB()
    model.fit(X_train_cv, y_train)

    X_test_cv = v.transform(X_test)

    # Evaluate Performance
    from sklearn.metrics import classification_report
    y_pred = model.predict(X_test_cv)
    print(classification_report(y_test, y_pred))

    emails = [
        'Hey mohan, can we get together to watch footbal game tomorrow?',
        'Upto 20% discount on parking, exclusive offer just for you. Dont miss this reward!'
    ]

    emails_count = v.transform(emails)
    print(model.predict(emails_count))


    #using pipeline
    from sklearn.pipeline import Pipeline

    clf = Pipeline([
        ('vectorizer', CountVectorizer()),
        ('nb', MultinomialNB())
    ])
    clf.fit(X_train, y_train)

    y_pred = clf.predict(X_test)

    print(classification_report(y_test, y_pred))`