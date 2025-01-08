from datetime import datetime


def log_progress(message, log_file) -> None:
    ''' This function logs the mentioned message of a given stage of the
    code execution to a log file. Function returns nothing'''

    timestamp_format = "%Y-%m-%d %H:%M:%S"
    now = datetime.now()
    timestamp = now.strftime(timestamp_format)

    with open(log_file, 'a+') as f:
        f.write(timestamp + ': ' + message + '\n')
