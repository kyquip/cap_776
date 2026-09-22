from openpyxl import load_workbook

class MyDataMyStory:
    # Function to Calculate Personal Activity #
    def calulate_personal_activity_index(self):
        tech_productivity_index = self.calulate_tech_productivity_index()
        academic_activity_index = self.calulate_academic_activity_index()
        physical_activity_index = self.calulate_physical_activity_index()
        sleep_and_recovery_index = self.calulate_sleep_and_recovery_index()
        activity_balance_index = self.calulate_activity_balance_index()
        time_utilization_index = self.calulate_time_utilization_index()
        experience_index = self.calulate_experience_index()
        data_continuity_index = self.calulate_data_continuity_index()
        personal_activity_index = round(((0.15 * tech_productivity_index) + (0.2 * academic_activity_index) + \
        (0.15 * physical_activity_index) + (0.2 * sleep_and_recovery_index) + \
        (0.15 * time_utilization_index) + (0.1 * experience_index) + (0.15 * data_continuity_index)), 5)
        print(f"\033[92m[2] Tech Productivity Index is {tech_productivity_index}\033[0m")
        print(f"\033[92m[3] Academic Activity Index is {academic_activity_index}\033[0m")
        print(f"\033[92m[4] Physical Activity Index is {physical_activity_index}\033[0m")
        print(f"\033[92m[5] Sleep and Recovery Index is {sleep_and_recovery_index}\033[0m")
        print(f"\033[92m[6] Activity Balance Index is {activity_balance_index}\033[0m")
        print(f"\033[92m[7] Time Utilization Index is {time_utilization_index}\033[0m")
        print(f"\033[92m[8] Experience Index is {experience_index}\033[0m")
        print(f"\033[92m[9] Data Continuity Index is {data_continuity_index}\033[0m")
        print(f"\033[92m[10] Personal Activity Index is {personal_activity_index}\033[0m")


    # Function to Calculate Tech Productivity #
    def calulate_tech_productivity_index(self):
        total_coding_time = 0

        for row in self.DATA:
            total_coding_time += row[4]

        tech_productivity_index = round(total_coding_time / self.DAYS, 3)
        return tech_productivity_index


    # Function to Calculate Academic Activity #
    def calulate_academic_activity_index(self):
        total_study_time = 0
        total_class_time = 0

        for row in self.DATA:
            total_study_time += row[3]
            total_class_time += row[5]

        academic_activity_index = round((total_study_time + total_class_time) / self.DAYS, 3)
        return academic_activity_index


    # Function to Calculate Physical Activity #
    def calulate_physical_activity_index(self):
        total_fitness_time = 0

        for row in self.DATA:
            total_fitness_time += row[2]

        physical_activity_index = round(total_fitness_time / self.DAYS, 3)
        return physical_activity_index


    # Function to Calculate Sleep and Recovery #
    def calulate_sleep_and_recovery_index(self):
        total_sleep_time = 0

        for row in self.DATA:
            total_sleep_time += row[1]

        sleep_and_recovery_index = round(total_sleep_time / self.DAYS, 3)
        return sleep_and_recovery_index


    # Function to Calculate Activity Balance #
    def calulate_activity_balance_index(self):
        total_unaccounted_time = 0

        for row in self.DATA:
            total_unaccounted_time += row[9]

        activity_balance_index = round(total_unaccounted_time / self.DAYS, 3)
        return activity_balance_index


    # Function to Calculate Time Utilization #
    def calulate_time_utilization_index(self):
        total_time_tracked = 0

        for row in self.DATA:
            total_time_tracked += row[8]

        time_utilization_index = round(total_time_tracked / self.DAYS, 3)
        return time_utilization_index


    # Function to Calculate Experience #
    def calulate_experience_index(self):
        total_feeling = 0
        total_satisfaction = 0
        total_energy = 0

        for row in self.DATA:
            total_feeling += self.get_feeling[row[10]]
            total_satisfaction += self.get_satisfaction[row[11]]
            total_energy += self.get_energy[row[12]]

        experience_index = round((total_feeling + total_satisfaction + total_energy) / (3 * self.DAYS), 3)
        return experience_index


    # Function to Calculate Data Continuity #
    def calulate_data_continuity_index(self):
        excepted_days = 41 # From 12 August to 21 September
        data_continuity_index = round(self.DAYS * 100 / excepted_days, 3)
        return data_continuity_index


    # Default Constructor to Initialise Each and Everything #
    def __init__(self, workbook_name):
        # Declaring Important Data and Parameters #
        self.DAYS = 0
        self.DATA = []
        self.get_feeling = {'Excellent': 5, 'Good': 4, 'Neutral': 3, 'Low': 2, 'Stressed': 1}
        self.get_satisfaction = {'Very Satisfied': 5, 'Satisfied': 4, 'Neutral': 3, 'Unsatisfied': 2, 'Very Unsatisfied': 1}
        self.get_energy = {'High': 3, 'Medium': 2, 'Low': 1}

        try:
            # Loading Workbook and Reading From Sheet #
            workbook = load_workbook(workbook_name, read_only = False, data_only=True)
            sheet = workbook['Daily Log']

            for row in sheet.iter_rows(min_row = 6, max_row = 46, min_col = 1, max_col = 14, values_only = True):
                self.DATA.append(list(row))
                self.DAYS += 1

            # Closing Workbook After Successfully Reading Data #
            workbook.close()
            print("\033[92m[1] Data loaded from workbook successfully.\033[0m")
        except FileNotFoundError:
            print("\033[91m[1] File was not found.\033[0m")


if __name__ == '__main__':
    story = MyDataMyStory('12600351.xlsx')
    story.calulate_personal_activity_index()
# This is the output of the code # 

# sage@Sage-2 minor-project %  source /Users/sage/Documents/minor-project/venv/bin/activate
# (venv) sage@Sage-2 minor-project % /Users/sage/Documents/minor-project/venv/bin/python /Users/sage/Documents/
# minor-project/12600351.py
# [1] Data loaded from workbook successfully.
# [2] Tech Productivity Index is 210.976
# [3] Academic Activity Index is 276.585
# [4] Physical Activity Index is 0.732
# [5] Sleep and Recovery Index is 410.244
# [6] Activity Balance Index is 231.707
# [7] Time Utilization Index is 1208.293
# [8] Experience Index is 3.431
# [9] Data Continuity Index is 100.0
# [10] Personal Activity Index is 365.70905
# (venv) sage@Sage-2 minor-project % 