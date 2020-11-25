import hashlib
from time import sleep
from random import randint
from datetime import datetime


LOGS_FILENAME = 'tests/test_data/logs_stream.log'
DELIMITER = '\t'
LINE_BREAKER = '\n'


def write(log_filename: str, logs):
    with open(log_filename, 'a') as file_handler:
        for log in logs:
            file_handler.write(log)

def generate_logs(count: int):
    assert count > 0, "Number of log entries should be more than 0"
    return (generate_row() for _ in range(count))

def generate_row():
    return DELIMITER.join((get_today_date(), generate_random_hash(), LINE_BREAKER))

def get_today_date():
    return datetime.today().strftime("%d/%m/%y %H:%M:%S")
            
def generate_random_hash() -> str:
    return hashlib.md5(str(randint(1, 1000)).encode()).hexdigest()

def main():
    while True:
        sleep_duration = randint(1, 5)
        logs_count = randint(20, 25)
        print(f'Writing {logs_count} logs to {LOGS_FILENAME}')
        write(LOGS_FILENAME, generate_logs(logs_count))
        sleep(sleep_duration)

if __name__ == '__main__':
    main()
