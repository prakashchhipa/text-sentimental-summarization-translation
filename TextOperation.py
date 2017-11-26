# -*- coding: utf-8 -*-

import httplib, urllib
import json
from TextSummary import *  
from azure_translator import Translator


accessKey = 'Text-Analysis-Aure-CognitiveService-key'
translatorKey = 'Language-Translation-Aure-CognitiveService-key'
uri = 'cognitive-service-url'
pathPh = '/text/analytics/v2.0/keyPhrases'
pathSenti = '/text/analytics/v2.0/sentiment'
def GetTextDetails (msg):
    "Detects the languages for a set of documents and returns the information."
    documents = { 'documents': [
    { 'id': '1', 'text': msg }]}
    #language
    headers = {'Ocp-Apim-Subscription-Key': accessKey}
    conn = httplib.HTTPSConnection (uri)
    body = json.dumps (documents)
    conn.request ("POST", pathLang, body, headers)
    response1 = conn.getresponse ()
    #phrase
    headers = {'Ocp-Apim-Subscription-Key': accessKey}
    conn = httplib.HTTPSConnection (uri)
    body = json.dumps (documents)
    conn.request ("POST", pathPh, body, headers)
    response2 = conn.getresponse ()

    #sentimental
    headers = {'Ocp-Apim-Subscription-Key': accessKey}
    conn = httplib.HTTPSConnection (uri)
    body = json.dumps (documents)
    conn.request ("POST", pathSenti, body, headers)
    response3 = conn.getresponse ()

    #summarize
    summary = TextSummary.summarize(msg)

    #{"documents":[{"id":"1","detectedLanguages":[{"name":"English","iso6391Name":"en","score":1.0}]}],"errors":[]}
    res1 = response1.read ().split("{")[3].split(":")[1].split(",")[0]
    res2 = response2.read ().split("{")[2].split("[")[1].split("]")[0]
    res3 = response3.read ().split("{")[2].split(":")[1].split(",")[0]
    res4 = "\"" + summary + "\""
    t = Translator(translatorKey)
    hindires2 = t.translate(res2, to='hi-IN')
    hindires4 = t.translate(res4, to ='hi-IN') 

    res =  res1 + ':'+ res3 + ':'+ hindires2 + ':' + hindires4
    res = res.replace("\"","")
#    print(res)
    return res
inp1 = 'This august House had discussed this matter in the last Lok Sabha consequent to the public outrage after the horrifying gang rape committed on a hapless girl who was on her way back to home in December 2012 in the capital city of Delhi. This horrendous incident along with other instances of rape and atrocities on women and children had evoked great amount of rancor among the people across the country. In order to give teeth to the existing laws, this august House, in its wisdom, had decided to bring about drastic amendments in the criminal laws. The House has passed the Criminal Law (Amendment) Act unanimously. The intent of this amendment is widely lauded but it is saddening to note that it has failed to stem the tide of violence. It is agonizing to note that females are targeted everywhere, whether it be at the schools, colleges, work places, streets, buses and even at public functions and at their own homes. It is also astounding to observe that more than 90% of the rapes are by relatives, friends or acquaintances and it mostly takes places in or near the houses where the victims stay. In a male dominated society known for its notorious caste, communal, gender and parochial mindset one would expect even worse. At the outset, I wish to place on record that it is not dearth of adequate laws that stand in the way of containing offences against women and children. It is mindset and attitude that must undergo rapid transformation. Therefore my initial observation is that we should take up this as a challenge to a civilized society and utmost vigilance is to be exercised by the community at large. What is required is to arouse the collective conscience of the society. As the saying goes charity begins at home and lessons relating to values and morals should also start from every household. I underscore the importance of moral education to children right from pre-primary stage itself. Unfortunately such a system is not in vogue in our educational system ands'
inp2 = 'इस लोक सभा ने पिछले लोकसभा चुनाव में इस मामले पर जनता के अपमान के कारण चर्चा की थी, जो दिसंबर 2012 में राजधानी दिल्ली में अपने घर वापस आ रही एक अशांति वाली लड़की पर भयावह सामूहिक बलात्कार के बाद हुई थी। यह भयावह महिलाओं और बच्चों पर बलात्कार और अत्याचारों के अन्य उदाहरणों के साथ-साथ घटनाक्रम पूरे देश में लोगों के बीच बहुत बड़ी संख्या में विद्रोह पैदा हुआ था। मौजूदा कानूनों को दांत देने के लिए, यह सभागृह, अपने ज्ञान में, कठोर लाने का फैसला किया था आपराधिक कानूनों में संशोधन। सदन ने आपराधिक कानून (संशोधन) अधिनियम को सर्वसम्मति से पारित किया है। इस संशोधन का इरादा व्यापक रूप से सराहा गया है, लेकिन यह दुख की बात है कि यह हिंसा के ज्वार को रोकने में नाकाम रही है। महिलाओं को हर जगह लक्षित किया जाता है, चाहे स्कूलों, कॉलेजों, काम के स्थानों, सड़कों, बसों और यहां तक ​​कि सार्वजनिक कार्यों में भी और स्वयं के घरों में भी हो। यह देखकर भी आश्चर्यजनक है कि 90% से अधिक बलात्कार रिश्तेदारों, मित्रों या परिचितों द्वारा ई और यह ज्यादातर जगहों पर या उन घरों के पास लेता है जहां पीड़ितों का रहने वाला है। एक कुख्यात जाति, सांप्रदायिक, लिंग और संकीर्ण मानसिकता के लिए जाना जाता एक पुरुष प्रभुत्व समाज में एक भी बदतर की उम्मीद करेंगे प्रारंभ में, मैं यह रिकॉर्ड करना चाहता हूं कि यह पर्याप्त कानूनों की कमी नहीं है जो महिलाओं और बच्चों के खिलाफ अपराधों को रोकने के रास्ते में खड़े हैं। यह मानसिकता और रवैया है जो तेजी से परिवर्तन से गुजरना होगा। इसलिए मेरा प्रारंभिक अवलोकन यह है कि हमें इसे सभ्य समाज के लिए एक चुनौती के रूप में लेना चाहिए और समाज द्वारा बड़े पैमाने पर सतर्कता का प्रयोग करना है। समाज के सामूहिक अंतःकरण को जगाने के लिए क्या आवश्यक है। जैसा कि कहा जाता है कि दान दान होता है, घर पर शुरू होता है और मूल्यों और नैतिकता से संबंधित सबक को भी हर घर से शुरू करना चाहिए। मैं पूर्व-प्राथमिक स्तर से ही बच्चों को नैतिक शिक्षा के महत्व पर ज़ोर देते हैं दुर्भाग्य से हमारी प्रणाली में ऐसी कोई प्रणाली प्रचलित नहीं है'
#res = GetTextDetails (inp1)
#print (res)
