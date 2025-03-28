# 🎧 Spotify End-To-End Data Pipeline Project



## 🚀 Overview

This project demonstrates a fully automated data engineering pipeline that extracts, processes, and analyzes Spotify's Global Top Songs using APIs and AWS services. It showcases how modern cloud-native tools can enable seamless ETL workflows and facilitate advanced analytics.
   **Project Documentation:** [Spotify Data Pipeline](<Spotify_End-To-End_Data_Pipeline_Project.pdf>)

## 🛠️ Architecture Diagram

![Architecture Diagram](architecture%20diagram.png)



## 🔥 Features

- **Data Extraction:** Utilizes the Spotify API to retrieve real-time music data, including details such as artists, albums, and songs from a specified playlist.
- **Serverless Deployment:** Leverages AWS Lambda for efficient and scalable data extraction code deployment.
- **Automation Triggers:** Sets up EventBridge and S3 Event triggers for automatic execution, ensuring timely and consistent data updates.
- **Data Storage:** Organizes storage on Amazon S3 and creates analytics tables with AWS Glue and Athena to provide a comprehensive data pipeline.


## 🛠️ Setting Up AWS Services

1. **Configure AWS Lambda Functions for Data Extraction and Transformation:**

   - **Create Lambda Functions:** Develop AWS Lambda functions to handle data extraction from the Spotify API and perform necessary transformations. 

   - **Set Up Permissions:** Ensure that the Lambda functions have the appropriate permissions to access required AWS resources, such as S3 buckets and Glue services. 

2. **Set Up Amazon S3 Buckets for Data Storage:**

   - **Create S3 Buckets:** Establish Amazon S3 buckets to store both raw and processed data. Organize the data into appropriate folders or prefixes for efficient management. 

   - **Define Bucket Policies:** Implement bucket policies to control access permissions, ensuring that only authorized services and users can interact with the data. 
3. **Utilize AWS Glue and Athena for Data Processing and Analytics:**

   - **Set Up AWS Glue Crawlers:** Configure AWS Glue Crawlers to automatically detect and catalog the schema of the data stored in S3. This creates a metadata repository that Athena can query. 

   - **Create AWS Glue ETL Jobs:** Develop AWS Glue ETL (Extract, Transform, Load) jobs to process and transform the raw data into a structured format suitable for analysis. 

   - **Query Data with AWS Athena:** Use AWS Athena to run SQL queries on the processed data stored in S3. Athena leverages the Glue Data Catalog for schema information, enabling efficient data analysis. 

## 🚀 Running the Pipeline

1. **Trigger the Data Extraction Process:**

   - **Manual Execution:** Initiate the Lambda functions manually through the AWS Management Console or AWS CLI to start the data extraction process. 

   - **Automated Scheduling:** Set up AWS EventBridge (formerly CloudWatch Events) rules to trigger the Lambda functions at specified intervals, automating the data extraction workflow. 

2. **Monitor ETL Jobs:**

   - **AWS Glue Job Monitoring:** Keep track of the AWS Glue ETL job executions through the AWS Glue Console to ensure successful data processing. 

## 📊 Analyzing the Data

 **Query Processed Data with AWS Athena:**

   - **Run SQL Queries:** Utilize AWS Athena to execute SQL queries on the transformed data stored in S3. This allows for flexible and powerful data analysis without the need for managing infrastructure.
     
## 🛠️ How to Use

 **Clone the Repository:**
   ```bash
   git clone https://github.com/sid-7878/Spotify-End-To-End-Data-Pipeline-Project.git
