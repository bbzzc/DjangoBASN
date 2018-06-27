#!/usr/bin/python

import psycopg2
from config import config

advo = "Advocacy"
excel = "Excel with a Mentor"
comm = "Community Partnerships"

def create_tables():
    """ create tables in the PostgreSQL database"""
    commands = (
        """
        CREATE TABLE users (
            user_id     SERIAL PRIMARY KEY,
            username    VARCHAR(20) NOT NULL,
            picture     VARCHAR(255),
            bio         VARCHAR(255) NOT NULL,
            email       VARCHAR(255) NOT NULL,
            password    VARCHAR(16) NOT NULL
        )
        """,
        """ CREATE TABLE catagory (
                cat_id      SERIAL PRIMARY KEY,
                cat_code    VARCHAR(4) NOT NULL,
                cat_name    VARCHAR(255) NOT NULL
                )
        """,
        """
        CREATE TABLE testimony (
                test_id         INTEGER PRIMARY KEY,
                pic_descript    VARCHAR(25) NOT NULL,
                picture         VARCHAR(255),
                testimony       VARCHAR(25) NOT NULL,
                keywords        VARCHAR(25) NOT NULL,
                FOREIGN KEY (cat_id)
                    REFERENCES catagory (cat_id)
                    ON UPDATE CASCADE ON DELETE CASCADE
        )
        """,
        """
        CREATE TABLE event (
                event_id        INTEGER PRIMARY KEY,
                eventName       VARCHAR(25) NOT NULL,
                start_date      DATE NOT NULL,
                end_date        DATE NOT NULL,
                start_time      TIME NOT NULL,
                location        VARCHAR(255) NOT NULL,
                POC_name        VARCHAR(255) NOT NULL,
                POC_phone       VARCHAR(25) NOT NULL,
                attendee        VARCHAR(25) NOT NULL,
                FOREIGN KEY (cat_id)
                    REFERENCES catagory (cat_id)
                    ON UPDATE CASCADE ON DELETE CASCADE
        )
        """,
        """
        CREATE TABLE corporation (
                corp_id     INTEGER PRIMARY KEY,
                corpName    VARCHAR(255) NOT NULL,
                addr_1      VARCHAR(255) NOT NULL,
                addr_2      VARCHAR(255) NOT NULL,
                city        VARCHAR(255) NOT NULL,
                state       VARCHAR(2) NOT NULL,
                zip_code    VARCHAR(10) NOT NULL,
                POC_phone   VARCHAR(25) NOT NULL,
                POC_name    VARCHAR(255) NOT NULL
        )
        """,
        """
        CREATE TABLE client (
                event_id        INTEGER PRIMARY KEY,
                eventName       VARCHAR(25) NOT NULL,
                start_date      DATE NOT NULL,
                end_date        DATE NOT NULL,
                start_time      TIME NOT NULL,
                location        VARCHAR(255) NOT NULL,
                POC_name        VARCHAR(255) NOT NULL,
                POC_phone       VARCHAR(25) NOT NULL,
                attendee        VARCHAR(25) NOT NULL,
                FOREIGN KEY (cat_id)
                    REFERENCES catagory (cat_id)
                    ON UPDATE CASCADE ON DELETE CASCADE
        )
        """,
        """
        CREATE TABLE event (
                event_id        INTEGER PRIMARY KEY,
                eventName       VARCHAR(25) NOT NULL,
                start_date      DATE NOT NULL,
                end_date        DATE NOT NULL,
                start_time      TIME NOT NULL,
                location        VARCHAR(255) NOT NULL,
                POC_name        VARCHAR(255) NOT NULL,
                POC_phone       VARCHAR(25) NOT NULL,
                attendee        VARCHAR(25) NOT NULL,
                FOREIGN KEY (cat_id)
                    REFERENCES catagory (cat_id)
                    ON UPDATE CASCADE ON DELETE CASCADE
        )
        """,
        """
        CREATE TABLE event (
                event_id        INTEGER PRIMARY KEY,
                eventName       VARCHAR(25) NOT NULL,
                start_date      DATE NOT NULL,
                end_date        DATE NOT NULL,
                start_time      TIME NOT NULL,
                location        VARCHAR(255) NOT NULL,
                POC_name        VARCHAR(255) NOT NULL,
                POC_phone       VARCHAR(25) NOT NULL,
                attendee        VARCHAR(25) NOT NULL,
                FOREIGN KEY (cat_id)
                    REFERENCES catagory (cat_id)
                    ON UPDATE CASCADE ON DELETE CASCADE
        )
        """,
        """
        CREATE TABLE event (
                event_id        INTEGER PRIMARY KEY,
                eventName       VARCHAR(25) NOT NULL,
                start_date      DATE NOT NULL,
                end_date        DATE NOT NULL,
                start_time      TIME NOT NULL,
                location        VARCHAR(255) NOT NULL,
                POC_name        VARCHAR(255) NOT NULL,
                POC_phone       VARCHAR(25) NOT NULL,
                attendee        VARCHAR(25) NOT NULL,
                FOREIGN KEY (cat_id)
                    REFERENCES catagory (cat_id)
                    ON UPDATE CASCADE ON DELETE CASCADE
        )
        """,
        """
        CREATE TABLE event (
                event_id        INTEGER PRIMARY KEY,
                eventName       VARCHAR(25) NOT NULL,
                start_date      DATE NOT NULL,
                end_date        DATE NOT NULL,
                start_time      TIME NOT NULL,
                location        VARCHAR(255) NOT NULL,
                POC_name        VARCHAR(255) NOT NULL,
                POC_phone       VARCHAR(25) NOT NULL,
                attendee        VARCHAR(25) NOT NULL,
                FOREIGN KEY (cat_id)
                    REFERENCES catagory (cat_id)
                    ON UPDATE CASCADE ON DELETE CASCADE
        )
        """,
        """
        CREATE TABLE event (
                event_id        INTEGER PRIMARY KEY,
                eventName       VARCHAR(25) NOT NULL,
                start_date      DATE NOT NULL,
                end_date        DATE NOT NULL,
                start_time      TIME NOT NULL,
                location        VARCHAR(255) NOT NULL,
                POC_name        VARCHAR(255) NOT NULL,
                POC_phone       VARCHAR(25) NOT NULL,
                attendee        VARCHAR(25) NOT NULL,
                FOREIGN KEY (cat_id)
                    REFERENCES catagory (cat_id)
                    ON UPDATE CASCADE ON DELETE CASCADE
        )
        """,
        """
        CREATE TABLE event (
                event_id        INTEGER PRIMARY KEY,
                eventName       VARCHAR(25) NOT NULL,
                start_date      DATE NOT NULL,
                end_date        DATE NOT NULL,
                start_time      TIME NOT NULL,
                location        VARCHAR(255) NOT NULL,
                POC_name        VARCHAR(255) NOT NULL,
                POC_phone       VARCHAR(25) NOT NULL,
                attendee        VARCHAR(25) NOT NULL,
                FOREIGN KEY (cat_id)
                    REFERENCES catagory (cat_id)
                    ON UPDATE CASCADE ON DELETE CASCADE
        )
        """,
        """
        CREATE TABLE event (
                event_id        INTEGER PRIMARY KEY,
                eventName       VARCHAR(25) NOT NULL,
                start_date      DATE NOT NULL,
                end_date        DATE NOT NULL,
                start_time      TIME NOT NULL,
                location        VARCHAR(255) NOT NULL,
                POC_name        VARCHAR(255) NOT NULL,
                POC_phone       VARCHAR(25) NOT NULL,
                attendee        VARCHAR(25) NOT NULL,
                FOREIGN KEY (cat_id)
                    REFERENCES catagory (cat_id)
                    ON UPDATE CASCADE ON DELETE CASCADE
        )
        """,
        """
        CREATE TABLE vendor_parts (
                vendor_id INTEGER NOT NULL,
                part_id INTEGER NOT NULL,
                PRIMARY KEY (vendor_id , part_id),
                FOREIGN KEY (vendor_id)
                    REFERENCES vendors (vendor_id)
                    ON UPDATE CASCADE ON DELETE CASCADE,
                FOREIGN KEY (part_id)
                    REFERENCES parts (part_id)
                    ON UPDATE CASCADE ON DELETE CASCADE
        )
        """)
    conn = None
    try:
        # read the connection parameters
        params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        # create table one by one
        for command in commands:
            cur.execute(command)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
# FOREIGN KEY (part_id)
# REFERENCES parts (part_id)
# ON UPDATE CASCADE ON DELETE CASCADE

if __name__ == '__main__':
    create_tables()
