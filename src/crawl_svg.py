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

import json
from bs4 import BeautifulSoup

def dump_to_file(obj):
    pass

def classify_domains(svg_file):
    soup = BeautifulSoup(svg_file, 'html.parser')
    g_node = soup.find('g')
    children = g_node.findChildren()
    for each_child in children:
        try:
            n = each_child['xlink:href']
        except Exception as e:
            pass
        else:
            print n
            colour_element = each_child.find('g', {'id': 'Oval'})
            dataset_name =  each_child.find('tspan')
            if dataset_name is None:
                pass
            else:
                print dataset_name.get_text()
            if colour_element is None:
                pass
            else:
                print colour_element['fill']
            print '---'



def main():
    with open('./cache/2015.svg') as file:
        classify_domains(file)

if __name__ == '__main__':
    main()
