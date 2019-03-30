# to use this package
## installation
git clone https://github.com/Accumulative/shared-japanese-tools
virtualenv env
source env/bin/activate
python setup.py bdist_wheel
deactivate

cd /route/to/own/package
source own_env/bin/activate
pip install /route/to/shared_japanese_tools/dist/shared_japanese_tools-0.1-py3-none-any.whl

## then in python file
```
from shared_japanese_tools.tinysegmenter import TinySegmenter
from shared_japanese_tools.search import search, Results
```

# To set up the JM dictionary (now included in search.py so not required)
cd shared-japanese-tools
curl http://ftp.monash.edu/pub/nihongo/JMdict_e.gz --output JMdict_e.gz
gzip -d JMdict_e.gz
