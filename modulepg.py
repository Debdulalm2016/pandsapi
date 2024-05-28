#script: modulepg.py

import psycopg2 as pg

def Get_WB_Districts():
    conn = pg.connect(
        host = '35.209.155.226',
        database = "postgis_db",
        user = 'postgis_test',
        password='mygeo80')
    if not conn:
        print('DB Connection Error!')

    cur = conn.cursor()
    query = """select distinct district_name
            from postgis.wb_districts;
            """
    cur.execute(query)
    result = cur.fetchall()
    district_values = []
    for row in result:
        district_values.append(row[0])
    return district_values

def Get_WB_Subdivs_in_District(distname = ''):
    conn = pg.connect(
        host = '35.209.155.226',
        database = "postgis_db",
        user = 'postgis_test',
        password='mygeo80')
    if not conn:
        print('DB Connection Error!')

    cur = conn.cursor()
    query = """select distinct subdiv_name
            from postgis.wb_districts d join postgis.wb_subdivisions s
            on d.district_code = s.district_code
            where d.district_name = %s;
            """
    cur.execute(query,(distname,))
    result = cur.fetchall()
    subdiv_values = []
    for row in result:
        subdiv_values.append(row[0])
    return subdiv_values

def Get_WB_Blocks_in_Subdiv(subdivname = ''):
    conn = pg.connect(
        host = '35.209.155.226',
        database = "postgis_db",
        user = 'postgis_test',
        password='mygeo80')
    if not conn:
        print('DB Connection Error!')

    cur = conn.cursor()
    query = """select distinct b.block_name
            from postgis.wb_subdivisions s join postgis.wb_blocks b
            on s.subdiv_code = b.subdiv_code
            where s.subdiv_name = %s;
            """
    cur.execute(query,(subdivname,))
    result = cur.fetchall()
    block_values = []
    for row in result:
        block_values.append(row[0])
    return block_values

def Get_WB_GPs_in_Block(blockname = ''):
    conn = pg.connect(
        host = '35.209.155.226',
        database = "postgis_db",
        user = 'postgis_test',
        password='mygeo80')
    if not conn:
        print('DB Connection Error!')

    cur = conn.cursor()
    query = """select distinct g.gp_name
            from postgis.wb_gp g join postgis.wb_blocks b
            on g.block_code = b.block_code
            where b.block_name = %s;
            """
    cur.execute(query,(blockname,))
    result = cur.fetchall()
    gp_values = []
    for row in result:
        gp_values.append(row[0])
    return gp_values



