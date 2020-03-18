import time
from . import mssql
from src.config import config


def backup(db):
    try:
        cursor = mssql.initialize_cursor(config['server'], config['username'],
                                         config['password'], config['port'], config['driver_version'])
        if mssql.rds_backup_procedure_exists(cursor):
            task_id = mssql.start_rds_backup(
                db, config['bucket'], mssql.generate_rds_backup_path(db), cursor)
            while not mssql.task_completed(task_id, cursor):
                print('{} percent completed. Its {} right now'.format(mssql.task_status(
                    task_id, cursor)[0][3], mssql.task_status(task_id, cursor)[0][5]))
                time.sleep(5)
        else:
            mssql.start_native_backup(
                db, config['backup_location'], mssql.generate_native_backup_path(db), cursor)
    except Exception as e:
        print('Error with the connection\n{}'.format(e))


def test():
    try:
        cursor = mssql.initialize_cursor(config['server'], config['username'],
                                         config['password'], config['port'], config['driver_version'])
        return mssql.rds_backup_procedure_exists(cursor)
    except Exception as e:
        print('Something went wrong.\n{}'.format(e))
