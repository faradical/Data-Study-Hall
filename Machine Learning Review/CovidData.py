# IMPORT DEPENDENCIES
import matplotlib.pyplot as plt, requests, numpy as np

def ushistory(state=None):
    # RETRIEVE HISTORICAL INFECTION DATA
    url = f'https://covidtracking.com/api/v1/states/daily.json'
    response = requests.get(url)
    if response.status_code == 200:
        cov_data = response.json()
        #print(f'Data successfully retrieved')

    # REORGANIZING DATA BY STATE FOR EASE OF USE
    states = list(set([datum['state'] for datum in cov_data]))
    state_dict = {}
    for state in states:
        state_data = []
        for datum in cov_data:
            if datum['state'] == state:
                state_data.append(datum)
        
        state_dict[state] = state_data

    if state != None:
        return state_dict[state]
    else:
        return state_dict

def statehistory(state):
    url = f'https://covidtracking.com/api/v1/states/{state}/daily.json'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()


# Create function for list building
def createList(searchableString,json_to_search):
    return_list = []
    for d in json_to_search:
        if searchableString in d:
            if 'None' in str(d[searchableString]):
                return_list.append(0)
            else:
                return_list.append(d[searchableString])
        else:
            return_list.append(0)
    return return_list


class StateData():
    def __init__(self, state):
        # Retrive Historical Data
        self.state = state
        self.historical_data = statehistory(self.state.lower())
        
        # List of dates
        dates = [daily['dateChecked'] for daily in self.historical_data]
        dates.reverse()
        self.dates = dates
        self.dates_ = [[value] for value in np.arange(len(dates))]

        # Cumulative data
        total_deaths = createList('death', self.historical_data)
        total_hospitalized = createList('hospitalizedCumulative', self.historical_data)
        total_cases = createList('positive', self.historical_data)
        total_deaths.reverse()
        total_hospitalized.reverse()
        total_cases.reverse()
        self.total_deaths = total_deaths
        self.total_hospitalized = total_hospitalized
        self.total_cases = total_cases

        # Daily data
        deaths = createList('deathIncrease', self.historical_data)
        hospitalized = createList('hospitalizedCurrently', self.historical_data)
        cases = createList('positiveIncrease', self.historical_data)
        deaths.reverse()
        hospitalized.reverse()
        cases.reverse()
        self.deaths = deaths
        self.hospitalized = hospitalized
        self.cases = cases

    def daily_chart(self):
        plt.figure(figsize=(20,8))
        plt.plot([self.dates.index(d) for d in self.dates], self.deaths, color='r', label="Deaths")
        plt.plot([self.dates.index(d) for d in self.dates], self.hospitalized, color='b', label="Hospitalizations")
        plt.plot([self.dates.index(d) for d in self.dates], self.cases, color='g', label="Positive Cases")
        plt.title(f"Daily Data for Covid-19 in {self.state.upper()}")
        plt.xlabel("Time")
        plt.ylabel("Number of People")
        tick_locations = [value for value in np.arange(len(self.dates))]
        x_ticks_1 = [d.split('T')[0] for d in self.dates if isinstance(d, str)]
        x_ticks = [d if x_ticks_1.index(d) % 10 == 1 else "" for d in x_ticks_1]
        plt.xticks(tick_locations, x_ticks, rotation="vertical")
        plt.legend(loc="best")
        return plt








