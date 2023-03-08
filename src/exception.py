import sys
from logger import logging


def error_message_detail(error, error_detail=sys.exc_info()):
    """
    Returns a formatted error message string containing the name of the Python script, line number where the error occurred,
    and the error message.

    Args:
        error (Exception): The exception that occurred.
        error_detail (Optional[Tuple[type, BaseException, Optional[TracebackType]]]): The error details. Defaults to sys.exc_info().

    Returns:
        str: The formatted error message string.
    """
    _, _, exc_tb = error_detail
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occurred in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error))
    return error_message

class CustomException(Exception):
    """
    A custom exception class that formats the error message using the error_message_detail function.

    Attributes:
        error_message (str): The formatted error message string.
    """
    def __init__(self, error_message, error_detail=sys.exc_info()):
        """
        Initializes the CustomException object.

        Args:
            error_message (str): The error message string.
            error_detail (Optional[Tuple[type, BaseException, Optional[TracebackType]]]): The error details. Defaults to sys.exc_info().
        """
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail=error_detail)

    def __str__(self):
        """
        Returns the error message string.

        Returns:
            str: The formatted error message string.
        """
        return self.error_message
    
if __name__=="__main__":

    try:
        a=1/0
    except Exception as e:
        logging.info("Divide by Zero")
        raise CustomException(str(e), sys.exc_info())
