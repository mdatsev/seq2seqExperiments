import wikipedia
import re
import nltk

sentence_tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

def wiki_extract(page):
    content = page.content
    noFooter = re.split('(== See also ==|== Notes ==|== References ==)', content)[0]
    noHeadings = re.sub(r'== .+ ==', '', noFooter)
    sentences = sentence_tokenizer.tokenize(noHeadings.strip()) #if error run `nltk.download('punkt')`
    words = [nltk.word_tokenize(s) for s in sentences]
    filtered = [[w for w in s if re.search(r'\w+', w)] for s in words]
    return filtered