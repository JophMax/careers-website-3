from sqlalchemy import create_engine, text
import os

db_connection_string = "mysql+pymysql://5oivjdzgyicv9f94wiog:pscale_pw_sFGqtcINN8dS1p4e7sdV8mmhLbEfRBmLr94km78Mbyk@aws.connect.psdb.cloud/careerswebsitev2?charset=utf8mb4"

engine = create_engine(db_connection_string,
                       connect_args={"ssl": {
                         "ssl_ca": "/etc/ssl/cert.pem"
                       }})


def jobs_loaded_import():
  with engine.connect() as conn:
    result = conn.execute(text('select * from jobs'))
    jobs = []

    for row in result.all():
      jobs.append(row._asdict())

    return (jobs)
