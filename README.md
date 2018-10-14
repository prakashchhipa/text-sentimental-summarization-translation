# text-sentimental-summarization-translation (Task Details)
This repository is pipeline for text sentimental, summarization &amp; language translation using microsoft cognitive services and gensum.

**Solution:**

1) TextOperation.py - It takes text input and detet the language, compute sentimental score & phrases using mirosoft text analytics cognitive service. It also performs text summariation using gensum library(TextSummary.py) then translate the summarized text to other langauge(hindi is configured currently) again using microsoft text translator cognitive service.

2) TextSummary.py - Gensum library api call.

3) TextServer.py - Flask based REST API server to expose text API.

4) portal/index.html - Simple HTML page for demonstration

Experiment: input-output.doc - Sample input text(in english) and output summarized text and phrases (in hindi) at gensum scale 0.5

**Execution Environment & Required Library:**

 1. Python 2.x, javscript, HTML
 2. Libraries
    - gensum
    - microsoft cognitive library, azure_translator
    - flask, flask.ext.cors
    - httplib, urllib

**Note for other Enthusiastic Contributor:**

Most welcome to improve the pipeline with respect to replacement of translator service and gensim utilization. Adding up more language support.

**Queries?...Connect with me at:**
LinkedIn: https://linkedin.com/in/prakash-chandra-chhipa
Email: prakash.chandra.chhipa@gmail.com
