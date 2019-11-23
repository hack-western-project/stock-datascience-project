import eventregistry
from eventregistry import *
import json
er = EventRegistry(apiKey = '6e2d0035-56b5-48b8-b7e6-b99bec1ecff8')

q = QueryEventsIter(conceptUri = er.getConceptUri("Tesla"),
                    lang = 'eng',
                    keywords = 'Tesla Motors'
                    )

file = open("articles-api-eventregistry.txt","w+")

for event in q.execQuery(er, sortBy = "date"):
    file.write(json.dumps(event))

