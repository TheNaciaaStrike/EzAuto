import logging

def setup_logging(module_name):
    logger = logging.getLogger(module_name)
    logger.setLevel(logging.DEBUG)  # Set the base level to DEBUG to capture all levels

    # Create handlers
    stream_handler = logging.StreamHandler()
    file_handler = logging.FileHandler('application.log')

    # Create formatters and add them to handlers
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    stream_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)

    # Add handlers to the logger
    logger.addHandler(stream_handler)
    logger.addHandler(file_handler)

    # Set specific logging levels based on module name
    if module_name == 'main':
        logger.setLevel(logging.DEBUG)
    elif module_name == 'ETL':
        logger.setLevel(logging.DEBUG)
    else:
        logger.setLevel(logging.WARNING)
    
    return logger