import logging
from logging.handlers import TimedRotatingFileHandler
from  datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()


def get_log_file_name():
    """
    Return the name for a log file.

    Args:
        application_path (str): path where the application is running

    Returns:
        String: path for a log file
    """

    current_date = datetime.now().strftime('%Y%m%d')
    path = os.path.join(os.getenv("TEMP_PATH"), f"log_file_{current_date}.log")
    return path


def setup_logging():
    """
    Set up logging configuration to log messages to a rotating log file.
    
    This function configures the logging system to log messages to a log file that
    rotates daily, keeping up to 100 backup log files. The log messages include
    the timestamp, log level, logger name, and the actual message.
    If a TimedRotatingFileHandler with the same file name already exists in the
    logger's handlers, no additional handler will be added, ensuring that the same
    log file is not duplicated.
    
    Logging Levels:
        - DEBUG: Detailed information for debugging purposes.
        - INFO: Informational messages.
        - WARNING: Warnings and potential issues.
        - ERROR: Error messages indicating a problem.
        - CRITICAL: Critical errors that may lead to system failure.
    
    Example Usage:
        To set up logging in your application, call this function at the beginning
        of your script or application to enable logging to a rotating log file. Subsequent
        calls within the same process won't modify the logging configuration.
    
    Note:
        Requires the presence of a 'logs' directory in the current working directory
        to store log files.
    
    Dependencies:
        - logging module
        - TimedRotatingFileHandler from logging.handlers module
        - datetime module
    
    Args:
        application_path (str): path where the application is running

    Returns:
        None
    """

    # LOG function definition
    log_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s - %(message)s')
    # Check if a handler with the same file name already exists
    logger = logging.getLogger()
    for handler in logger.handlers:
        if isinstance(handler, TimedRotatingFileHandler) and handler.baseFilename == get_log_file_name():
            return  # Handler for this file name already exists
    # Create a TimedRotatingFileHandler that rotates log files daily
    log_handler = TimedRotatingFileHandler(
        filename=get_log_file_name(),
        when='midnight',  # Rotate at midnight
        interval=1,  # Rotate every day
        backupCount=100  # Keep up to xx backup log files
    )
    log_handler.setFormatter(log_formatter)
    # Set the logging level for both the logger and the handler
    logger.setLevel(logging.DEBUG)
    log_handler.setLevel(logging.DEBUG)
    # Add the handler to the logger
    logger.addHandler(log_handler)