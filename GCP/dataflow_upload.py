import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions

# GCP Project & Bucket
PROJECT_ID = "numeric-guide-470805-i9"
REGION = "asia-south1"
BUCKET_NAME = "bkt-ranking-data-krishi"

# Paths
INPUT_CSV = f"gs://{BUCKET_NAME}/batsmen_rankings.csv"
OUTPUT_PREFIX = f"gs://{BUCKET_NAME}/output/batsmen_processed"

# Dataflow pipeline options
options = PipelineOptions(
    runner='DataflowRunner',
    project=PROJECT_ID,
    region=REGION,
    temp_location=f"gs://{BUCKET_NAME}/temp",
    staging_location=f"gs://{BUCKET_NAME}/staging",
    service_account_email='gcs-python-access@numeric-guide-470805-i9.iam.gserviceaccount.com'
)

# Define pipeline
with beam.Pipeline(options=options) as p:
    (p
     | "Read CSV" >> beam.io.ReadFromText(INPUT_CSV, skip_header_lines=1)
     | "Do Something" >> beam.Map(lambda x: x.upper())  # Example transformation
     | "Write Output" >> beam.io.WriteToText(OUTPUT_PREFIX, file_name_suffix=".csv")
    )

print("Dataflow job submitted successfully!")
