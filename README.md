Overview
-
In this example, we will use the [Versatile Data Kit (VDK)](https://github.com/vmware/versatile-data-kit) to ingest a local .csv file into a database. In our case we will use local SQLite. Thus exploring the possibility to ingest large locally stored data set into a local or remote database.

Before you continue, make sure you are familiar with the [Getting Started](https://github.com/vmware/versatile-data-kit/wiki/Getting-Started) section of the wiki.

This example provides the complete code to perform the following tasks:

* Data ingestion from CSV
* Data modeling
* Data processing

The directory is organized as follows:

* NSA - contains model code
* Iris.csv - sample dataset

Scenario
-
The sample dataset contains flowers that vary in three categories (Setosa, Versicolor, Virginica). The objective of the study is to train a machine learning model to predict the correct label for each flower. Three machine learning techniques were applied in this study: the Negative Selection Algorithm (NSA), Decision Tree, and Random Forest. 

CSV File
-
For the purpose of this example, we will be using a simple .csv file of the iris dataset, widely utilized by researchers in machine learning studies.

Configuration
-
If you have not done so already, you can install Versatile Data Kit and the plugins required for this example by running the following commands from a terminal:

```console
pip install quickstart-vdk vdk-csv
```

Note that Versatile Data Kit requires Python 3.7+. See the [main guide](https://github.com/vmware/versatile-data-kit/blob/main/README.md#getting-started) for getting started with quickstart-vdk for more details.

Ingestion requires us to set environment variables for:

* the type of database in which we will be ingesting;
* the ingestion method;
* the ingestion target - the location of the target database - if this file is not present, ingestion will create it in the current directory. For this example, we will use beta.db file which will be created in the current directory;
* the file of the default SQLite database against which VDK runs (same value as ingestion target in this case);

Note: if you are using Windows, you need to use 'setx' instead of 'export'.

```console
export VDK_DB_DEFAULT_TYPE=SQLITE
export VDK_INGEST_METHOD_DEFAULT=sqlite
export VDK_INGEST_TARGET_DEFAULT=beta.db
export VDK_SQLITE_FILE=beta.db
```

vdk ingest-csv
-
Make sure to check the help! It has pretty good documentation and examples

```console
vdk ingest-csv --help
```

Ingestion
-
If the .csv file to be ingested (iris.csv in our example), and the beta.db are present in the current directory, the only thing left is to run

```console
vdk ingest-csv -f iris.csv --table-name m1
```

Otherwise, you first of all need to create an empty beta.db file in the main directory then start to run.  

With this command, the CSV data will be ingested into the SQLite database. Upon successful ingestion, the logs should be similar to the ones below

<details>
    <summary>Result logs</summary>

```
2024-03-07 13:25:15,071 [VDK] [WARNI] vdk.internal.builtin_plugins.t     template_impl.py :39   add_template     - Template with name scd1 has been registered with directory C:\Users\Ehsan\AppData\Local\Programs\Python\Python311\Lib\site-packages\vdk\plugin\impala\templates\load\dimension\scd1.We will overwrite it with new directory C:\Users\Ehsan\AppData\Local\Programs\Python\Python311\Lib\site-packages\vdk\plugin\trino\templates\load\dimension\scd1 now.
2024-03-07 13:25:15,071 [VDK] [WARNI] vdk.internal.builtin_plugins.t     template_impl.py :39   add_template     - Template with name scd2 has been registered with directory C:\Users\Ehsan\AppData\Local\Programs\Python\Python311\Lib\site-packages\vdk\plugin\impala\templates\load\versioned.We will overwrite it with new directory C:\Users\Ehsan\AppData\Local\Programs\Python\Python311\Lib\site-packages\vdk\plugin\trino\templates\load\dimension\scd2 now.
2024-03-07 13:25:15,071 [VDK] [WARNI] vdk.internal.builtin_plugins.t     template_impl.py :39   add_template     - Template with name periodic_snapshot has been registered with directory C:\Users\Ehsan\AppData\Local\Programs\Python\Python311\Lib\site-packages\vdk\plugin\impala\templates\load\fact\snapshot.We will overwrite it with new directory C:\Users\Ehsan\AppData\Local\Programs\Python\Python311\Lib\site-packages\vdk\plugin\trino\templates\load\fact\periodic_snapshot now.
2024-03-07 13:25:15,071 [VDK] [INFO ] vdk.plugin.control_cli_plugin. properties_plugin.py :22   initialize_job   - Initialize Control Service based Properties client implementation.
2024-03-07 13:25:15,071 [VDK] [INFO ] vdk.plugin.control_cli_plugin.    execution_skip.py :105  _skip_job_if_nec - Checking if job should be skipped:
2024-03-07 13:25:15,071 [VDK] [INFO ] vdk.plugin.control_cli_plugin.    execution_skip.py :106  _skip_job_if_nec - Job : csv_ingest_job, Team : None, Log config: LOCAL, execution_id: f3861dea-9e7a-48ed-b528-958329ebcd47-1709805315
2024-03-07 13:25:15,071 [VDK] [INFO ] root                              execution_skip.py :111  _skip_job_if_nec - Local execution, skipping parallel execution check.
2024-03-07 13:25:15,071 [VDK] [INFO ] vdk.internal.builtin_plugins.r   file_based_step.py :106  run_python_step  - Entering csv_ingest_step.py#run(...) ...
2024-03-07 13:25:15,521 [VDK] [INFO ] vdk.internal.builtin_plugins.i   ingester_router.py :105  send_tabular_dat - Sending tabular data for ingestion with method: sqlite and target: beta.db
2024-03-07 13:25:15,526 [VDK] [INFO ] step_csv_ingest_ste              csv_ingest_step.py :31   ingest           - Ingested data from C:\csv\iris.csv into table m1 successfully.
Successfully ingested!
2024-03-07 13:25:15,527 [VDK] [INFO ] vdk.internal.builtin_plugins.r   file_based_step.py :112  run_python_step  - Exiting  csv_ingest_step.py#run(...) SUCCESS
2024-03-07 13:25:17,531 [VDK] [INFO ] vdk.plugin.sqlite.ingest_to_sq  ingest_to_sqlite.py :76   ingest_payload   - Ingesting payloads for target: beta.db; collection_id: csv_ingest_job|f3861dea-9e7a-48ed-b528-958329ebcd47-1709805315
2024-03-07 13:25:17,531 [VDK] [INFO ] vdk.plugin.sqlite.sqlite_conne sqlite_connection.py :29   new_connection   - Creating new connection against local file database located at: beta.db
2024-03-07 13:25:17,531 [VDK] [INFO ] vdk.plugin.sqlite.ingest_to_sq  ingest_to_sqlite.py :177  __create_table_i - Table m1 does not exists. Will auto-create it now based on first batch of input data.
2024-03-07 13:25:17,546 [VDK] [INFO ] vdk.plugin.sqlite.ingest_to_sq  ingest_to_sqlite.py :183  __create_table_i - Table m1 created.
2024-03-07 13:25:18,369 [VDK] [INFO ] vdk.internal.builtin_plugins.i     ingester_base.py :573  close_now        - Ingester statistics:
                Successful uploads: 1
                Failed uploads: 0
                Ingesting plugin errors: None

2024-03-07 13:25:18,375 [VDK] [INFO ] vdk.internal.builtin_plugins.r           cli_run.py :170  __log_short_exec - Job execution result: SUCCESS
Step results:
csv_ingest_step.py - SUCCESS

Ingesting csv file C:\csv\iris.csv finished.
```
</details>

To verify that the data is ingested as expected, run

```console
vdk sqlite-query -q "SELECT * FROM m1"
```

The output should be similar to the one below

<details>
    <summary>Output</summary>

```console
  A    B    C    D  variety
---  ---  ---  ---  ----------
5.1  3.5  1.4  0.2  Setosa
4.9  3    1.4  0.2  Setosa
4.7  3.2  1.3  0.2  Setosa
4.6  3.1  1.5  0.2  Setosa
5    3.6  1.4  0.2  Setosa
5.4  3.9  1.7  0.4  Setosa
4.6  3.4  1.4  0.3  Setosa
5    3.4  1.5  0.2  Setosa
4.4  2.9  1.4  0.2  Setosa
4.9  3.1  1.5  0.1  Setosa
5.4  3.7  1.5  0.2  Setosa
4.8  3.4  1.6  0.2  Setosa
4.8  3    1.4  0.1  Setosa
4.3  3    1.1  0.1  Setosa
5.8  4    1.2  0.2  Setosa
5.7  4.4  1.5  0.4  Setosa
5.4  3.9  1.3  0.4  Setosa
5.1  3.5  1.4  0.3  Setosa
5.7  3.8  1.7  0.3  Setosa
5.1  3.8  1.5  0.3  Setosa
5.4  3.4  1.7  0.2  Setosa
5.1  3.7  1.5  0.4  Setosa
4.6  3.6  1    0.2  Setosa
5.1  3.3  1.7  0.5  Setosa
4.8  3.4  1.9  0.2  Setosa
5    3    1.6  0.2  Setosa
5    3.4  1.6  0.4  Setosa
5.2  3.5  1.5  0.2  Setosa
5.2  3.4  1.4  0.2  Setosa
4.7  3.2  1.6  0.2  Setosa
4.8  3.1  1.6  0.2  Setosa
5.4  3.4  1.5  0.4  Setosa
5.2  4.1  1.5  0.1  Setosa
5.5  4.2  1.4  0.2  Setosa
4.9  3.1  1.5  0.2  Setosa
5    3.2  1.2  0.2  Setosa
5.5  3.5  1.3  0.2  Setosa
4.9  3.6  1.4  0.1  Setosa
4.4  3    1.3  0.2  Setosa
5.1  3.4  1.5  0.2  Setosa
5    3.5  1.3  0.3  Setosa
4.5  2.3  1.3  0.3  Setosa
4.4  3.2  1.3  0.2  Setosa
5    3.5  1.6  0.6  Setosa
5.1  3.8  1.9  0.4  Setosa
4.8  3    1.4  0.3  Setosa
5.1  3.8  1.6  0.2  Setosa
4.6  3.2  1.4  0.2  Setosa
5.3  3.7  1.5  0.2  Setosa
5    3.3  1.4  0.2  Setosa
7    3.2  4.7  1.4  Versicolor
6.4  3.2  4.5  1.5  Versicolor
6.9  3.1  4.9  1.5  Versicolor
5.5  2.3  4    1.3  Versicolor
6.5  2.8  4.6  1.5  Versicolor
5.7  2.8  4.5  1.3  Versicolor
6.3  3.3  4.7  1.6  Versicolor
4.9  2.4  3.3  1    Versicolor
6.6  2.9  4.6  1.3  Versicolor
5.2  2.7  3.9  1.4  Versicolor
5    2    3.5  1    Versicolor
5.9  3    4.2  1.5  Versicolor
6    2.2  4    1    Versicolor
6.1  2.9  4.7  1.4  Versicolor
5.6  2.9  3.6  1.3  Versicolor
6.7  3.1  4.4  1.4  Versicolor
5.6  3    4.5  1.5  Versicolor
5.8  2.7  4.1  1    Versicolor
6.2  2.2  4.5  1.5  Versicolor
5.6  2.5  3.9  1.1  Versicolor
5.9  3.2  4.8  1.8  Versicolor
6.1  2.8  4    1.3  Versicolor
6.3  2.5  4.9  1.5  Versicolor
6.1  2.8  4.7  1.2  Versicolor
6.4  2.9  4.3  1.3  Versicolor
6.6  3    4.4  1.4  Versicolor
6.8  2.8  4.8  1.4  Versicolor
6.7  3    5    1.7  Versicolor
6    2.9  4.5  1.5  Versicolor
5.7  2.6  3.5  1    Versicolor
5.5  2.4  3.8  1.1  Versicolor
5.5  2.4  3.7  1    Versicolor
5.8  2.7  3.9  1.2  Versicolor
6    2.7  5.1  1.6  Versicolor
5.4  3    4.5  1.5  Versicolor
6    3.4  4.5  1.6  Versicolor
6.7  3.1  4.7  1.5  Versicolor
6.3  2.3  4.4  1.3  Versicolor
5.6  3    4.1  1.3  Versicolor
5.5  2.5  4    1.3  Versicolor
5.5  2.6  4.4  1.2  Versicolor
6.1  3    4.6  1.4  Versicolor
5.8  2.6  4    1.2  Versicolor
5    2.3  3.3  1    Versicolor
5.6  2.7  4.2  1.3  Versicolor
5.7  3    4.2  1.2  Versicolor
5.7  2.9  4.2  1.3  Versicolor
6.2  2.9  4.3  1.3  Versicolor
5.1  2.5  3    1.1  Versicolor
5.7  2.8  4.1  1.3  Versicolor
6.3  3.3  6    2.5  Virginica
5.8  2.7  5.1  1.9  Virginica
7.1  3    5.9  2.1  Virginica
6.3  2.9  5.6  1.8  Virginica
6.5  3    5.8  2.2  Virginica
7.6  3    6.6  2.1  Virginica
4.9  2.5  4.5  1.7  Virginica
7.3  2.9  6.3  1.8  Virginica
6.7  2.5  5.8  1.8  Virginica
7.2  3.6  6.1  2.5  Virginica
6.5  3.2  5.1  2    Virginica
6.4  2.7  5.3  1.9  Virginica
6.8  3    5.5  2.1  Virginica
5.7  2.5  5    2    Virginica
5.8  2.8  5.1  2.4  Virginica
6.4  3.2  5.3  2.3  Virginica
6.5  3    5.5  1.8  Virginica
7.7  3.8  6.7  2.2  Virginica
7.7  2.6  6.9  2.3  Virginica
6    2.2  5    1.5  Virginica
6.9  3.2  5.7  2.3  Virginica
5.6  2.8  4.9  2    Virginica
7.7  2.8  6.7  2    Virginica
6.3  2.7  4.9  1.8  Virginica
6.7  3.3  5.7  2.1  Virginica
7.2  3.2  6    1.8  Virginica
6.2  2.8  4.8  1.8  Virginica
6.1  3    4.9  1.8  Virginica
6.4  2.8  5.6  2.1  Virginica
7.2  3    5.8  1.6  Virginica
7.4  2.8  6.1  1.9  Virginica
7.9  3.8  6.4  2    Virginica
6.4  2.8  5.6  2.2  Virginica
6.3  2.8  5.1  1.5  Virginica
6.1  2.6  5.6  1.4  Virginica
7.7  3    6.1  2.3  Virginica
6.3  3.4  5.6  2.4  Virginica
6.4  3.1  5.5  1.8  Virginica
6    3    4.8  1.8  Virginica
6.9  3.1  5.4  2.1  Virginica
6.7  3.1  5.6  2.4  Virginica
6.9  3.1  5.1  2.3  Virginica
5.8  2.7  5.1  1.9  Virginica
6.8  3.2  5.9  2.3  Virginica
6.7  3.3  5.7  2.5  Virginica
6.7  3    5.2  2.3  Virginica
6.3  2.5  5    1.9  Virginica
6.5  3    5.2  2    Virginica
6.2  3.4  5.4  2.3  Virginica
5.9  3    5.1  1.8  Virginica
```

</details>
  
Next, you should replace the following file named 'csv_ingest_step.py' with the original file located in the following directory.

In Windows: 
\AppData\Local\Programs\Python\Python311\Lib\site-packages\vdk\plugin\csv\csv_ingest_job'

In Linux:
'\usr\local\lib\python3.10\dist-packages\vdk\plugin\csv\'

<details>
  <summary>csv_ingest_step.py</summary>

```
# Copyright 2021-2023 VMware, Inc.
# SPDX-License-Identifier: Apache-2.0
import logging
import os
import pathlib
from typing import Dict

from vdk.api.job_input import IJobInput

log = logging.getLogger(__name__)


class CsvIngester:
    def __init__(self, job_input: IJobInput):
        self.__job_input = job_input

    def ingest(self, input_file: pathlib.Path, destination_table: str, options: Dict):
        import pandas as pd

        df = pd.read_csv(str(input_file), **options)
        df.dropna(how="all", inplace=True)

        os.remove("C:/csv/beta.db")

        self.__job_input.send_tabular_data_for_ingestion(
            rows=df.values,
            column_names=df.columns.values.tolist(),
            destination_table=destination_table,

        )
        log.info(
            f"Ingested data from {input_file} into table {destination_table} successfully."
        )


def run(job_input: IJobInput) -> None:

    csv_file = pathlib.Path(job_input.get_arguments().get("file"))
    destination_table = job_input.get_arguments().get("destination_table", None)
    if not destination_table:
        destination_table = os.path.splitext(csv_file.name)[0]
    options = job_input.get_arguments().get("options", {})

    csv = CsvIngester(job_input)
    csv.ingest(csv_file, destination_table, options)
    print("Successfully ingested!")
    
```
</details>

Note: You can customize your SQLite query in your code to create complex queries however you want, by editing the 'run' function in the 'model.py' file. Below is the code for transforming tables, subject to customization:

<details>
    <summary>run</summary>

``` run
con = sqlite3.connect("beta.db")
data = pd.read_sql_query("SELECT * from m1;", con)
```

</details>

Possible queries that can be added to the above SQL script to short the results include but are not limited to sorting the results by "ORDER BY Clause", combining rows from two or more tables using "JOIN Operation", search for a specific pattern in columns using "Where", among others.

Finally, place the directory containing files in the 'C:/' directory on Windows. Navigate to the main directory and run the following command:

``` console
vdk run NSA
```

Note: if you are using Linux, you should place the directory containing files in the '/home/ directory in addition to changing the line 23 of the script above as follows:

```
os.remove("/home/csv/beta.db")
```

The output should be similar to the one below:

<details>
    <summary>model output</summary>
    
```
2024-03-07 14:00:55,050 [VDK] [WARNI] vdk.internal.builtin_plugins.t     template_impl.py :39   add_template     - Template with name scd1 has been registered with directory C:\Users\Ehsan\AppData\Local\Programs\Python\Python311\Lib\site-packages\vdk\plugin\impala\templates\load\dimension\scd1.We will overwrite it with new directory C:\Users\Ehsan\AppData\Local\Programs\Python\Python311\Lib\site-packages\vdk\plugin\trino\templates\load\dimension\scd1 now.
2024-03-07 14:00:55,050 [VDK] [WARNI] vdk.internal.builtin_plugins.t     template_impl.py :39   add_template     - Template with name scd2 has been registered with directory C:\Users\Ehsan\AppData\Local\Programs\Python\Python311\Lib\site-packages\vdk\plugin\impala\templates\load\versioned.We will overwrite it with new directory C:\Users\Ehsan\AppData\Local\Programs\Python\Python311\Lib\site-packages\vdk\plugin\trino\templates\load\dimension\scd2 now.
2024-03-07 14:00:55,050 [VDK] [WARNI] vdk.internal.builtin_plugins.t     template_impl.py :39   add_template     - Template with name periodic_snapshot has been registered with directory C:\Users\Ehsan\AppData\Local\Programs\Python\Python311\Lib\site-packages\vdk\plugin\impala\templates\load\fact\snapshot.We will overwrite it with new directory C:\Users\Ehsan\AppData\Local\Programs\Python\Python311\Lib\site-packages\vdk\plugin\trino\templates\load\fact\periodic_snapshot now.
2024-03-07 14:00:55,050 [VDK] [INFO ] vdk.plugin.control_cli_plugin. properties_plugin.py :22   initialize_job   - Initialize Control Service based Properties client implementation.
2024-03-07 14:00:55,050 [VDK] [INFO ] vdk.plugin.control_cli_plugin.    execution_skip.py :105  _skip_job_if_nec - Checking if job should be skipped:
2024-03-07 14:00:55,050 [VDK] [INFO ] vdk.plugin.control_cli_plugin.    execution_skip.py :106  _skip_job_if_nec - Job : NSA, Team : None, Log config: LOCAL, execution_id: ecdbafe5-ae63-4b9c-8577-6fe5c2215ad6-1709807454
2024-03-07 14:00:55,050 [VDK] [INFO ] root                              execution_skip.py :111  _skip_job_if_nec - Local execution, skipping parallel execution check.
2024-03-07 14:01:00,779 [VDK] [INFO ] vdk.internal.builtin_plugins.r   file_based_step.py :106  run_python_step  - Entering 01_model.py#run(...) ...
Enter the number of PCA components, your number must be between zero and 4 : 4
You entered: 4
Tell me which methodology do you want to choose for your discrimination task?
 Type 1 for Artificial Immune System
 Type 2 for Decision Tree
 Type 3 for Random Forests --> 2
You have entered: 2
Please input random state size: 400
Entered random state size is :  400
The accuracy is {accuracy_score(prev_y, test_y.values)}
              precision    recall  f1-score   support

      Setosa       1.00      1.00      1.00        16
  Versicolor       0.89      1.00      0.94        16
   Virginica       1.00      0.85      0.92        13

    accuracy                           0.96        45
   macro avg       0.96      0.95      0.95        45
weighted avg       0.96      0.96      0.96        45
```
</details>

![image](https://github.com/ehsan-farzadnia/ingest-from-csv-machnie-learning-example/assets/161824187/3b046620-2a64-4f54-b549-fe6e6ec37320)


