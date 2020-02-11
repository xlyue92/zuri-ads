from __future__ import absolute_import
import psycopg2
import pandas as pd
import os

"""
Useful links for the cloud database loading:
"""
#1. aws postgresql
# https://aws.amazon.com/getting-started/tutorials/create-connect-postgresql-db/?trk=gs_card

#2. psycopg2 configuration
# https://towardsdatascience.com/amazon-rds-step-by-step-guide-14f9f3087d28

#3. connection failed issue
# https://serverfault.com/questions/656079/unable-to-connect-to-public-postgresql-rds-instance

def main(host, port, user, password, database, path, tb_name):
    conn = psycopg2.connect(host = host, user = user, port = port,
                           password = password, database = database)
    cursor = conn.cursor()
    table = tb_name
    create_table = """
    create table {}(
    date DATE,
    location_id INT,
    language VARCHAR(20),
    network VARCHAR(30),
    keyword_seed TEXT,
    url_seed TEXT, 
    keywords TEXT, 
    avg_month_search FLOAT,
    competition_level VARCHAR(10),
    clicks FLOAT, 
    impressions FLOAT,
    cost FLOAT,
    ctr FLOAT, 
    avg_cpc FLOAT
    )
    """.format(table)
    cursor.execute(create_table)
    conn.commit()

    with os.scandir(path) as entries:
        for entry in entries:
            if entry.name.endswith('.csv'):
                target = open(entry)
                next(target)
                cursor.copy_from(target, table, sep = ',')
                conn.commit()

if __name__ == '__main__':
    params = {'host': '', 'port': '', 'user': '', 'password': '', 'database': '', 'path': ''}
    fileobj = open('../config/load_config.txt')

    for line in fileobj:
        line = line.strip()
        key_value = line.split('=')
        params[key_value[0]] = key_value[1]
    
    main(params['host'], int(params['port']), params['user'], params['password'], params['database'], 
         params['path'], params['tb_name'])

    