'''
Dataset & Domain identification from the LOD cloud. This is a level one parsing script. Meaning, this will allow 
identification of dataset and their domains as an object

ex:
{
    'dataset': 'xyz',
    'url': 'http://link_to_datahub.io',
    'domain': 'abc'
}


2017.svg
--------------------------
#f6b33c - Government
#c8a788 - Cross Domain
#29c9cc - Geography
#db777f - Life Science
#36bc8d - Linguistics
#6372C7 - Media
#BCB582 - Publications
#b5b5b5 - Social Networking
#d84d8c - User Generated
---------------------------

2015.svg
---------------------------
#E8FED3 - Publications
#F6DEE7 - Life Science
#EAF7F6 - Cross Domain
#A3FFFA - Social Networking
#FEF1B6 - Geography
#CEFFEB - Goverment
#E8EDFF - Media
#FEEDDF - User Generated
#CCFFFF - Linguistics

'''

from bs4 import BeautifulSoup
import json

def dump_to_file(obj):
    pass

def classify_domains(markup_document):
    soup = BeautifulSoup(markup_document, 'html.parser')
    print soup

def main():
    with open('./cache/2015.svg') as file:
        classify_domains(file)

if __name__ == '__main__':
    main()