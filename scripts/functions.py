import time

def data_mart_calculation_turnover(connection, date):
    cursor = connection.cursor()

    try:
        cursor.execute(f"call dm.fill_account_turnover_f('{date}'::date)")
        connection.commit()
        time.sleep(1)
    except (Exception) as error:
        print(f'Error executing for date {date}: {error}')
    finally:
            cursor.close()


def data_mart_calculation_f101(connection, date):
    cursor = connection.cursor()

    try:
        cursor.execute(f"call dm.fill_f101_round_f('{date}'::date)")
        connection.commit()
    except (Exception) as error:
        print(f'Error executing for date {date}: {error}')
    finally:
            cursor.close()