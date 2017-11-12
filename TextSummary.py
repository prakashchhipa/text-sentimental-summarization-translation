from gensim.summarization import summarize as summ

def summarize(text, ratio=0.5):
	return summ(text, ratio)


