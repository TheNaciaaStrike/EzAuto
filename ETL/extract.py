from logger.setup_logging import setup_logging

logger = setup_logging('ETL')

class dataExtraction:
    def __init__(self, file_path):
        self.file_path = file_path

    def extract_data(self):
        logger.debug('Reading XML file')
        #tree = ET.parse(self.file_path)
        #root = tree.getroot()
        #data = []
        #for child in root:
        #    data.append(child.attrib)
        #return data

    def extract_data_csv(self):
        logger.debug('Reading CSV file')
        #data = pd.read_csv(self.file_path)
        #return data

    def extract_data_excel(self):
        logger.debug('Reading Excel file')
        #data = pd.read_excel(self.file_path)
        #return data