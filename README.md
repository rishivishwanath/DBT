# DBT

## Project Overview
This project contains scripts and tools for data processing and analysis using Kafka and Spark. It includes functionalities for producing and consuming Kafka messages, as well as Spark jobs for analyzing cricket match data.

## Folder Structure
```
README.md

# Data folder containing input datasets
data/
    ipl_2022_deliveries.csv

# Kafka folder containing producer and consumer scripts
kafka/
    producer.py
    test_consumer.py

# Spark folder containing data analysis scripts
spark/
    bowl.py
    highest_score_overall.py
    highest_score_team_match.py
    runrate.py
```

### Description of Key Files
- **data/ipl_2022_deliveries.csv**: Dataset containing cricket match delivery details.
- **kafka/producer.py**: Script to produce messages to a Kafka topic.
- **kafka/test_consumer.py**: Script to consume messages from a Kafka topic.
- **spark/bowl.py**: Spark job for analyzing bowling data.
- **spark/highest_score_overall.py**: Spark job to find the highest score across all matches.
- **spark/highest_score_team_match.py**: Spark job to find the highest score by a team in a match.
- **spark/runrate.py**: Spark job to calculate run rates.

## Setup Instructions
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd DBT
   ```
2. Install required Python libraries:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up Kafka and Spark environments as per their official documentation.

## Usage
### Kafka
- To produce messages:
  ```bash
  python kafka/producer.py
  ```
- To consume messages:
  ```bash
  python kafka/test_consumer.py
  ```

### Spark
- Run any Spark job using the following command:
  ```bash
  spark-submit spark/<script_name>.py
  ```
  Replace `<script_name>` with the desired script, e.g., `highest_score_overall.py`.

## Dependencies
- Python 3.8+
- Apache Kafka
- Apache Spark
- Required Python libraries (listed in `requirements.txt`)

## Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes and push the branch.
4. Open a pull request with a detailed description of your changes.

