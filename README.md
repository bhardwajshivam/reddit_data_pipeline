# Reddit ETL

This project demonstrates an ETL (Extract, Transform, Load) pipeline that ingests data from Reddit, processes it, and loads it into various data stores.

**Technologies Used:**

* **Reddit API:** Source of raw Reddit data (posts, comments, etc.).
* **Airflow:** Orchestration and scheduling of the ETL pipeline.
* **Celery:** Distributed task queue for parallel processing of data.
* **Postgres:** Relational database for data storage and transformation.
* **S3:** Amazon Simple Storage Service for storing intermediate data and long-term archiving.
* **AWS Glue:** Serverless data integration service for data transformation and loading.
* **Athena:** Serverless query engine for interactive analysis of data stored in S3.
* **Redshift:** Data warehousing solution for high-performance analytics and reporting.

**Pipeline Overview:**

1. **Data Extraction:**
   - Utilize the Reddit API to extract relevant data (e.g., posts, comments, user information) based on specified criteria (e.g., subreddits, keywords).
   - Store the raw data in S3 for further processing.

2. **Data Transformation:**
   - Use AWS Glue jobs to:
      - Clean and preprocess the raw data (e.g., handle missing values, remove duplicates, convert data types).
      - Perform data enrichment (e.g., enrich user data with external sources).
      - Aggregate data (e.g., calculate daily post counts, identify trending topics).

3. **Data Loading:**
   - Load processed data into:
      - Postgres for real-time data access and application integration.
      - Redshift for data warehousing and analytical queries.
      - S3 for long-term storage and archival purposes.

4. **Data Analysis:**
   - Use Athena to query and analyze data stored in S3.
   - Generate reports and visualizations to gain insights from the Reddit data.

