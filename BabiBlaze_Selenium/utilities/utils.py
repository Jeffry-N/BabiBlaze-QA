import inspect
import logging
import os
import datetime


class AutomationLogger:
    @staticmethod
    def automation(log_level=logging.DEBUG):  
        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)
        logger.setLevel(log_level)

        today = datetime.date.today()
        formatted_date = today.strftime("%Y-%m-%d")  # Format the date as needed

        log_file_name = f"Logs/automation_{formatted_date}.log"
        os.makedirs(os.path.dirname(log_file_name), exist_ok=True)

        file_handler = logging.FileHandler(log_file_name, mode='a')
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        return logger