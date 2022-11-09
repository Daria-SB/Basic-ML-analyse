import glob

NEG_PATTERN = r"C:\Users\Sasy\neg\*.txt"
POS_PATTERN = r"C:\Users\Sasy\pos\*.txt"


neg_files = glob.glob(NEG_PATTERN)
neg_rew = []
for file in neg_files:
    with open(file, encoding='utf-8') as stream:
       content = stream.read()
    words = content.lower().replace("<br />", " ").split()
    neg_rew.append(words)
 

pos_files = glob.glob(POS_PATTERN)
pos_rew = []
for file in pos_files:
    with open(file, encoding='utf-8') as stream:
       content = stream.read()
    words = content.lower().replace("<br />", " ").split()
    pos_rew.append(words)


words = input("Please, enter your comment here: ")
words = words.lower()
words = words.split()

sentiment = 0
for word in words:
    pos = 0
    neg = 0
    for rew in neg_rew:
        if word in rew:
            neg += 1
    for rew in pos_rew:
        if word in rew:
            pos += 1
    all_ = pos + neg
    if all_ != 0:
        word_sentiment = (pos - neg) / all_
    else:
        word_sentiment = 0.0
    print("Word ", word, "has a sentiment: ", word_sentiment)
    sentiment += word_sentiment
sentiment /= len(words)

if sentiment > 0:
    label = "positive"
else:
    label = "negative"
print("This comment is ", label, "and it's sentiment is ", sentiment)