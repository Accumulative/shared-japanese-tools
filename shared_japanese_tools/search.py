from xml.etree.ElementTree import parse
from . import helper
import os
import urllib.request
import gzip
import shutil
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'JMdict_e.xml')

if not os.path.exists(filename):
    print('Downloading dictionaries...')
    urllib.request.urlretrieve('http://ftp.monash.edu/pub/nihongo/JMdict_e.gz', os.path.join(dirname, 'JMdict_e.gz'))
    with gzip.open(os.path.join(dirname, 'JMdict_e.gz'), 'rb') as f_in:
        with open(filename, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)

tree = parse(os.path.join(os.path.dirname(__file__), filename))
root = tree.getroot()

class Results(object):
    def __init__(self, definitions, readings, types):
        self.definitions = definitions
        self.readings = readings
        self.types = types


def search(query):
    b_is_kata = helper.is_kata(query)
    element = root.find(
        ".//{}/[{}='{}']...".format("r_ele" if b_is_kata else "k_ele", "reb" if b_is_kata else "keb", query))

    if element is not None:
        definitions = []
        for i in element.findall("sense//gloss"):
            definitions.append(i.text)

        readings = []
        for i in element.findall("k_ele//keb"):
            readings.append(i.text)
        for i in element.findall("r_ele//reb"):
            readings.append(i.text)

        types = []
        for i in element.findall("sense//pos"):
            if "exp" not in i.text:
                types.append(i.text.replace(";", ""))
        if len(types) == 0:
            types = ["exp"]
        return Results(definitions, readings, types)
    return None


def test():
    print(search("違う"))
    print(search("出来る"))
    print(search("こんにちは"))
    print(search("携帯"))
