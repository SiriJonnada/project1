import requests # type: ignore
import json
from collections import Counter 
import matplotlib.pyplot as plt

## Should put in an if then statement in place of line 9 to get information based on schizophrenia or atreal thing
prompt_condition = input("Which medical condition would you like to search for?")
condition_name = prompt_condition

params = {
    "format" : "json",
    "query.cond" : condition_name
}

r = requests.get('https://clinicaltrials.gov/api/v2/studies', params = params)

data = r.json()

with open ("clinicaltrials.json", "w") as f:
    json.dump(data, f, indent = 4)

## Statistic could be max age

maximum_ages = []

for study in data["studies"]:
    age = study["protocolSection"]["eligibilityModule"].get("maximumAge")
    if age is not None:
        maximum_ages.append(age)

ages_data = []

for age in maximum_ages:
        number = age.replace("Years", "")
        number = int(number)
        ages_data.append(number)

measure_ages = Counter(ages_data)

unique_ages = list(measure_ages.keys())
count_ages = list(measure_ages.values())

plt.bar(unique_ages, count_ages)
plt.title(f"Maximum ages in {condition_name} studies")
plt.xlabel("Maximum Age (Years)")
plt.ylabel("Number of Studies")
plt.show()