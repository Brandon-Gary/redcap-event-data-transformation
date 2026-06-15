# Event Data Transformation using Python and REDCap
### Problem
Our nursing team regularly conducts mobile clinics throughout the community, and needed an automatic way to display upcoming events on our website. Event information is entered at varying times throughout the year, so manual website updates would be very inefficient and prone to becoming outdated. The goal of this project was to create an automated process that would allow staff to enter event information once and have a continuously updated, chronologically ordered event list displayed online without requiring any additional action.

### Input Data
The team enters event information into the form shown below. Each field is stored as a separte column, and each event is stored as a separte record. An example of the source data is included in this repository as `input_sample_data.csv`

<img width="587" height="435" alt="image" src="https://github.com/user-attachments/assets/2209a409-299c-4be2-a15e-ad14040756ff" />

### Process
The python script `mobile_event_transform.py` performs a complete ETL workflow:
  1. Pulls event data from REDCap using the REDCap API
  2. Converts date fields into datetime data type
  3. Calculates the number of days between the current date and each event date
  4. Uses the above calculation to remove past events and retain only upcoming events
  5. Sorts all events chronologically
  6. Converts the multi-record dataset into a single-record structure to become more suitable for public display
  7. Uploads the transformed dataset into a new REDCap project via the API

Since the newly transformed data exists as a single record, it can be displayed with a public REDCap URL that always remains the same even as event information changes over time. This allows the event list to be embedded directly to the organization's website using an iFrame.

*API tokens and URLs have been removed from the repository for security purposes.*

### Output Data
The CSV file `output_sample_data.csv` shows what the dataset looks like post-transformation. This is the structure that is uploaded back into REDCap.

### Result
The script was setup on a department server and scheduled to run automatically multiple times per day. As the nursing staff add, edit, or remove events in REDCap, the public event list updates automatically without requiring any manual website maintenance. This process eliminated any need for manual updating, ensures that only future events are displayed, and provides the community with an accurate and continuously updated schedule of mobile clinics.

**Example:**
<img width="1879" height="857" alt="image" src="https://github.com/user-attachments/assets/e4d4df3c-c7f3-4038-ab4d-6f7934ff7b77" />


#### Technologies Used:
•	Python
•	Pandas
•	REDCap
•	Windows Task Scheduler
