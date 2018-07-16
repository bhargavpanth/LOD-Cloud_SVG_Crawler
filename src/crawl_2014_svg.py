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

2014.svg
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
    domain_list = list()
    obj = dict()
    soup = BeautifulSoup(svg_file, 'html.parser')
    g_node = soup.find('g')
    children = g_node.findChildren()
    for each_child in children:
        try:
            n = each_child['xlink:href']
        except Exception as e:
            pass
        else:
            obj['url'] = n
            colour_element = each_child.find('g', {'id': 'Oval'})
            dataset_name = each_child.find('tspan')
            if dataset_name is None:
                pass
            else:
                obj['dataset'] = dataset_name.get_text()
            if colour_element is None:
                pass
            else:
                obj['colour'] = colour_element['fill']
            domain_list.append(obj)
    colour_to_domain(domain_list)


def colour_to_domain(obj_list):
    _2014_list = [
        {"colour": "#A3FFFA", "domain" : "Social Networking"},
        {"colour": "#CCFFFF", "domain" : "Linguistics"},
        {"colour": "#CEFFEB", "domain" : "Goverment"},
        {"colour": "#E8FED3", "domain" : "Publications"},
        {"colour": "#EAF7F6", "domain" : "Cross Domain"},
        {"colour": "#F6DEE7", "domain" : "Life Science"},
        {"colour": "#E8EDFF", "domain" : "Media"},
        {"colour": "#FEF1B6", "domain" : "Geography"},
        {"colour": "#FEEDDF", "domain" : "User Generated"}
    ]

    _2017_list = [
        {"colour": "#f6b33c", "domain": "Government"},
        {"colour": "#c8a788", "domain": "Cross Domain"},
        {"colour": "#29c9cc", "domain": "Geography"},
        {"colour": "#db777f", "domain": "Life Science"},
        {"colour": "#36bc8d", "domain": "Linguistics"},
        {"colour": "#6372C7", "domain": "Media"},
        {"colour": "#BCB582", "domain": "Publications"},
        {"colour": "#b5b5b5", "domain": "Social Networking"},
        {"colour": "#d84d8c", "domain": "User Generated"}
    ]

    domain_list = list()

    for each_obj in obj_list:
        # print each_obj['colour']
        for each_list_item in _2014_list:
            if each_obj['colour'] == each_list_item['colour']:
                print each_list_item['colour']
                print each_list_item['domain']
            else:
                continue
        print '---'



def main():
    with open('./cache/2014.svg') as file:
        classify_domains(file)


if __name__ == '__main__':
    main()
