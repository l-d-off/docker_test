import psycopg2
from datetime import datetime
import faker
import time
import threading

f = faker.Faker()

def main():
  file = open('logs.txt', 'a')
  now = datetime.today().strftime('%d.%m.%Y %H:%M:%S')
  file.write(f'time : {now}\n')
  conn = psycopg2.connect(
    database='postgres_db',
    user='darf',
    password='darf',
    port='5432',
    host='postgres')
  file.write('connected database [postgres_db]\n')
  cursor = conn.cursor()
  try:
    cursor.execute('select count(*) from data;')
    row_count = cursor.fetchone()[0] # 30 -> reboot
    file.write(f'selected row count from table [data] : count = {row_count}\n')
    if row_count >= 30:
      cursor.execute('truncate table data;')
      file.write('cleaned table [data] because row count >= 30\n')
    else:
      file.write('saved table [data] because row count < 30\n')
    # generate and send to postgre
    email = f.email()
    #print('before insert')
    cursor.execute(f'insert into data(email, date) values(\'{email}\', \'{now}\'); commit;')
    #print('after insert, before commit')
    #conn.commit()
    file.write(f'inserted values into [data] : email = {email}, date = {now}\n')
    print(f'row count : {row_count}')
  except:
    # log errors and others to file
    print('connection error')
    file.write('error connection to database [postgres_db]\n')
  finally:
    cursor.close()
    conn.close()
    file.write('disconnected database [postgres_db]\n')
    file.write('\n')
    file.close()

def use_main():
  while 1:
    main()
    time.sleep(60)

thread = threading.Thread(target=use_main)
thread.start()
