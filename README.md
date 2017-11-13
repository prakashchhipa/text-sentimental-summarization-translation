# text-sentimental-summarization-translation
This repository is pipeline for text sentimental, summarization &amp; language translation using microsoft cognitive services and gensum.

TextOperation.py - It takes text input and detet the language, compute sentimental score & phrases using mirosoft text analytics cognitive service. It also performs text summariation using gensum library(TextSummary.py) then translate the summarized text to other langauge(hindi is configured currently) again using microsoft text translator cognitive service.

TextSummary.py - Gensum library api call.

TextServer.py - Flask based REST API server to expose text API.

portal/index.html - Simple HTML page for demonstration

input-output.doc - Sample input text(in english) and output summarized text and phrases (in hindi) at gensum scale 0.5

