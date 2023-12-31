from sqlalchemy import create_engine, text
import os

db_string = os.environ['5oivjdzgyicv9f94wiog']
db_connection_string = os.environ['DB_CONNECTION_STRING']

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
