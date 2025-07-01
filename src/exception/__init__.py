import logging
import os
from typing import Tuple

def error_message_detail(error: Exception, exc_info: Tuple) -> str:
    """
    Extracts detailed error information including file name, line number, and error message.

    :param error: The exception object.
    :param exc_info: The tuple returned by sys.exc_info().
    :return: A formatted error message string.
    """
    _, _, tb = exc_info
    if tb:
        last_tb = tb
        while last_tb.tb_next:
            last_tb = last_tb.tb_next

        file_name = os.path.basename(last_tb.tb_frame.f_code.co_filename)
        line_number = last_tb.tb_lineno
    else:
        file_name = "<unknown>"
        line_number = -1

    return f"Error occurred in script [{file_name}] at line [{line_number}]: {str(error)}"

class ApplicationException(Exception):
    """
    Custom application-level exception with detailed traceback support.
    """

    def __init__(self, error: Exception, exc_info: Tuple):
        """
        Initializes the exception and logs detailed traceback info.
        :param error: The original exception.
        :param exc_info: The sys.exc_info() tuple.
        """
        self.error_message = error_message_detail(error, exc_info)
        super().__init__(self.error_message)

        # Log the error with full detail
        logging.error(self.error_message)
