import pandas as pd
import os
import time
import logging
from sqlalchemy import create_engine

logging.basicConfig(
    filename="logs/ingestion_db.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode="a"
)
engine=create_engine('sqlite:///inventory.db')
def ingest_db(df, table_name, conn):
    """
    Save dataframe into SQLite table
    """
    df.to_sql(
        table_name,
        con=conn,
        if_exists='replace',
        index=False
    )

start = time.time()

for file in os.listdir('.'):
    if file.endswith('.csv'):

        table_name = file[:-4]

        try:
            logging.info(f"Started processing {file}")
            print(f"Processing {file}...")

            chunk_count = 0

            for chunk in pd.read_csv(file, chunksize=100000):

                if chunk_count == 0:
                    chunk.to_sql(
                        table_name,
                        con=engine,
                        if_exists='replace',
                        index=False
                    )
                else:
                    chunk.to_sql(
                        table_name,
                        con=engine,
                        if_exists='append',
                        index=False
                    )

                chunk_count += 1

                logging.info(
                    f"{file}: Chunk {chunk_count} inserted successfully"
                )

            logging.info(f"Finished processing {file}")
            print(f"Finished {file} successfully!")

        except Exception as e:
            logging.error(
                f"Error processing {file}: {str(e)}"
            )
            print(f"Error processing {file}: {str(e)}")

end = time.time()

total_time = (end - start) / 60

logging.info("========== Ingestion Complete ==========")
logging.info(
    f"Total Time Taken: {total_time:.2f} minutes"
)
logging.info("Data ingestion completed successfully!")

print(f"Total Time Taken: {total_time:.2f} minutes")
print("Data ingestion completed successfully!")