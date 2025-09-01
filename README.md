# Cricket-Statistics-Data-Pipeline
Cricket Statistics Data Pipeline using Airflow on Google Cloud – Data Engineering project demonstrating ETL workflow, BigQuery analytics, and dashboard visualization

# Cricket Statistics Data Pipeline in Google Cloud

<img width="1105" height="832" alt="image" src="https://github.com/user-attachments/assets/8281fdee-356d-459f-b840-7efdc8538f87" />


## Project Overview
This is an **end-to-end Data Engineering project** that demonstrates a pipeline for fetching, processing, and visualizing cricket statistics using **Google Cloud Platform (GCP)**. The workflow leverages **Airflow**, **Dataflow**, **Cloud Functions**, and **Looker Studio** to orchestrate, process, and visualize cricket data.  

The pipeline fetches data from the **Cricbuzz API**, stores it in **Google Cloud Storage (GCS)**, triggers a **Cloud Function** to start a **Dataflow job**, and loads the data into **BigQuery**, which serves as the data source for the **Looker Studio dashboard**.

## Technologies Used
- **Google Cloud Platform (GCP)**: Cloud Storage, BigQuery, Dataflow, Cloud Functions
- **Apache Airflow**: Orchestrate workflow steps
- **Python**: Fetching data from API, triggering Cloud Functions, ETL logic
- **SQL**: BigQuery data processing
- **Looker Studio**: Dashboard visualization

## Project Workflow
1. **Data Retrieval**  
   Fetch data from the Cricbuzz API using Python scripts.

2. **Storing Data in GCS**  
   Save the fetched data as a CSV file in a GCS bucket.

3. **Cloud Function Trigger**  
   A Cloud Function triggers automatically whenever a new CSV file is uploaded to the GCS bucket.

4. **Dataflow Job Execution**  
   The Cloud Function triggers a Dataflow job that reads the CSV file from GCS and loads the data into BigQuery.

5. **Looker Studio Dashboard**  
   BigQuery serves as the data source for Looker Studio, where dashboards are created to visualize cricket statistics.


