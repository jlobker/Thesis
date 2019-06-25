import xml.etree.ElementTree as ET
import requests
from lxml import etree, objectify
import argparse

'''
Script scraping news articles from Delpher
Author: Jet Lobker
Usage: python3 delpherscraper.py [year]
It needs an API to function, issued by the KB
Find 1000 newspapers per run in range(132364),
Find the articles in per newspaper, if the subject of the text is artikel, it is saved
Find the url for the OCR text and write the title and text to an output file
'''
parser = argparse.ArgumentParser()
parser.add_argument('year', type=int, help = 'Year')
args = parser.parse_args()

url = 'http://jsru.kb.nl/sru/sru?version=1.2&maximumRecords=1000&operation=searchRetrieve&startRecord={startrecord}&recordSchema=ddd&x-collection=DDD_krantnr&x-facets=&query=%28date%20within%20%2201-01-{year}%2031-12-{year}%22%29'

def ReturnNodes(pattern):
    startrecord = 1
    for i in range(132364):
        r = requests.get(url.format(startrecord=startrecord, year=args.year))
        xml = r.text
        root = ET.fromstring(xml)
        with open('Thesis/artikel{}.txt'.format(args.year), 'a') as f:
            for metadataKey in root.iter(pattern):
                metadata = metadataKey.text
                if 'services' in metadata:
                    metadatasplit = metadata.split('?')
                    metadatalist = metadatasplit.insert(1, [API])
                    metadataapi = ''.join(metadatasplit)
                    metadataurl = requests.get(metadataapi)
                    metadataxml = metadataurl.text
                    metadataroot = ET.fromstring(metadataxml)
                    for subject in metadataroot.iter('{http://purl.org/dc/elements/1.1/}subject'):
                        subjecttext = subject.text
                        if 'artikel' in subjecttext:
                            for identifier in metadataroot.iter('{http://purl.org/dc/elements/1.1/}identifier'):
                                identifierresolver = identifier.text
                                if 'a' in identifierresolver:
                                    identifierocr = identifierresolver + ':ocr'
                                    ocrdata = requests.get(identifierocr)
                                    ocrxml = ocrdata.text
                                    ocrroot = ET.fromstring(ocrxml)
                                    for text in ocrroot.iter('text'):
                                        title = text.find('title')
                                        if isinstance(title.text, str):
                                            f.write(title.text + '\n')
                                        for p in ocrroot.iter('p'):
                                            if isinstance(p.text, str):
                                                f.write(p.text + '\n')
        startrecord = startrecord + 1000

ReturnNodes('{http://www.kb.nl/ddd}metadataKey')
