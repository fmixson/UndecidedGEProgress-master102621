import pandas as pd


class GeRequirements:

    def __init__(self, degree_applicable_dict, ge_plan):
        self.degree_applicable_dict = degree_applicable_dict
        self.ge_plan = ge_plan
        self.completed_ge_courses = {}
        self.completed_ge_units = []
        self.soc_behav_course_list = []
        self.soc_behav_disc_list = []

    def dataframe(self):
        ge_dataframe = pd.read_csv(self.ge_plan)
        return ge_dataframe

    def two_discipline_check(self, course_key, soc_behav_course_list):
        discipline = course_key.split()
        discipline = discipline[0]
        disc = False
        discipline_set = set(soc_behav_course_list)
        if discipline in discipline_set:
            disc = True

        return disc

    def ge_courses_completed(self, area_name, ge_dataframe):
        for i in range(len(ge_dataframe[area_name])):
            for key in self.degree_applicable_dict:
                if key == ge_dataframe.loc[i, area_name]:
                    # print(area_name)
                    if area_name not in self.completed_ge_courses:

                        self.completed_ge_courses[area_name] = key
                        self.completed_ge_units.append(self.degree_applicable_dict[key])
                        total = sum(self.completed_ge_units)
        return self.completed_ge_courses, self.completed_ge_units

    def soc_behav_courses(self, area_name, ge_dataframe):
        disc = False
        ge_course_list = list(self.completed_ge_courses.values())
        discipline_set = set(self.soc_behav_course_list)
        for i in range(len(ge_dataframe[area_name])):
            for key in self.degree_applicable_dict:
                # print(ge_dataframe.loc[i, area_name])
                if key == ge_dataframe.loc[i, area_name]:
                    # print(area_name)create list of disciplines
                    # if course list has two and discipline does not equal dis list then go.

                    discipline_set = set(self.soc_behav_disc_list)

                    if area_name not in self.completed_ge_courses:
                        # print(key, self.soc_behav_course_list)
                        if key not in ge_course_list:
                            if len(self.soc_behav_course_list) == 2:
                                if len(discipline_set) < 2:
                                     disc = GeRequirements.two_discipline_check(self, course_key=key,
                                                                                soc_behav_course_list=discipline_set)

                            if not disc:
                                self.soc_behav_course_list.append(key)
                                print('soc behav list', self.soc_behav_course_list)
                                self.completed_ge_courses[area_name] = key
                                print(self.completed_ge_courses)
                                self.completed_ge_units.append(self.degree_applicable_dict[key])
                                total = sum(self.completed_ge_units)
                                discipline = key.split()
                                discipline = discipline[0]
                                self.soc_behav_disc_list.append(discipline)
                                discipline_set = set(self.soc_behav_disc_list)
        return self.completed_ge_courses, self.completed_ge_units


    def area_e_ge_requirements(self, ge_dataframe):
        area_e_list = []
        total_ge_units = sum(self.completed_ge_units)
        for i in range(len(ge_dataframe['Electives'])):
            for key in self.degree_applicable_dict:
                if key == ge_dataframe.loc[i, 'Electives']:
                    if len(self.completed_ge_courses) == 9:
                        if total_ge_units < 18:
                            area_e_list.append(key)
                            self.completed_ge_courses['AreaE'] = area_e_list
                            self.completed_ge_units.append(self.degree_applicable_dict[key])
        return self.completed_ge_courses

    def reading_proficiency(self):
        if 'Reading Proficiency' not in self.completed_ge_courses:
            if sum(self.completed_ge_units) >= 12:
                self.completed_ge_courses['Reading_Proficiency'] = 'Met(GE Units)'
        return self.completed_ge_courses



