import pandas as pd
import xml.etree.ElementTree as ET

import logger.setup_logging as setup_logging
import ETL.extract as extract


logger = setup_logging.setup_logging('main')

_extract = extract.dataExtraction('data.xml')


logger.debug('Reading XML file')
logger.info('Reading XML file')
logger.warning('Reading XML file')
logger.error('Reading XML file')
logger.critical('Reading XML file')

_extract.extract_data()
_extract.extract_data_csv()
_extract.extract_data_excel()
