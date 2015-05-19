from src import application
import argparse
import os
import configparser
import shutil
from src.data import DataStrategy

if __name__ == "__main__":
    DataStrategy.initializeDataStrategy("sqllite")
    config = configparser.ConfigParser()
    config.read('src/config.ini')
    siteLocation = config['SITEADMIN']['fileLocation']
    if not os.path.exists(siteLocation+'/static/stylesheets/style.css'):
        shutil.copytree('src/core/tests/testdata/static/', siteLocation+'/static')
    parser = argparse.ArgumentParser()
    parser.add_argument("--debug", action="store_true")
    args = parser.parse_args()
    if args.debug:
        application.run(host='0.0.0.0', port=5000, debug=True)
    else:
        application.run(host='0.0.0.0', port=5000, debug=False)
