from datetime import datetime
class Schedule:
    def __init__(self):
        self.schedule = {
            "Lunedì": {},
            "Martedì": {},
            "Mercoledì": {},
            "Giovedì": {},
            "Venerdì": {},
            "Sabato": {},
        }
        self.set_standart()

    def add_lesson(self, day, name, room, start_time, end_time):
        lesson = {"room": room, "start_time": start_time, "end_time": end_time}
        if name in self.schedule[day]:
            self.schedule[day][name].append(lesson)
        else:
            self.schedule[day][name] = [lesson]

    def get_schedule_string(self):
        schedule_string = "Orario:\n"
        for day, lessons in self.schedule.items():
            schedule_string += f"  {day}:\n"
            if not lessons:
                schedule_string += "  No lessons\n"
            else:
                for lesson, infos in lessons.items():
                    for info in infos:
                        schedule_string += f"**{lesson}** :  Aula  {info['room']},  Tempo  {info['start_time']} - {info['end_time']}\n"
        return schedule_string

    def get_lesson_time(self):
       pass


    def set_standart(self):
        self.add_lesson("Lunedì", "INGLESE", "1 - 11", "07:55", "8:55")
        self.add_lesson("Lunedì", "MATE E COMP", "1 - 11", "8:55", "9:45")
        self.add_lesson("Lunedì", "S.M.S", "Palestra", "9:55", "10:55")
        self.add_lesson("Lunedì", "S.M.S", "Palestra", "10:55", "11:45")
        self.add_lesson("Lunedì", "SISTEMI E RETI", "1 - 25", "11:55", "12:55")
        self.add_lesson("Lunedì", "STORIA", "1 - 25", "12.55", "13.55")

        self.add_lesson("Martedì", "INGLESE", "2 - 20", "07:55", "8:55")
        self.add_lesson("Martedì", "MATE E COMP", "1 - 05", "8:55", "9:45")
        self.add_lesson("Martedì", "ITALIANO", "2 - 15", "9:55", "10:55")
        self.add_lesson("Martedì", "SISTEMI E RETI", "Lab №2", "10:55", "11:45")
        self.add_lesson("Martedì", "SISTEMI E RETI", "Lab №2", "11:55", "12:55")
        self.add_lesson("Martedì", "SISTEMI E RETI", "Lab №2", "12.55", "13.55")

        self.add_lesson("Mercoledì", "STORIA", "1 - 10", "07:55", "8:55")
        self.add_lesson("Mercoledì", "INFORMATICA", "Lab №4", "8:55", "9:45")
        self.add_lesson("Mercoledì", "COMP.MATE.", "1 - 23", "9:55", "10:55")
        self.add_lesson("Mercoledì", "INGLESE", "2 - 20", "10:55", "11:45")
        self.add_lesson("Mercoledì", "MATE E COMP", "1 - 04", "11:55", "12:55")

        self.add_lesson("Giovedì", "TELE", "Lab ELN & TELE", "07:55", "8:55")
        self.add_lesson("Giovedì", "TELE", "Lab ELN & TELE", "8:55", "9:45")
        self.add_lesson("Giovedì", "T.P.S INFO", "Lab №5", "9:55", "10:55")
        self.add_lesson("Giovedì", "INFORMATICA", "Lab №2", "10:55", "11:45")
        self.add_lesson("Giovedì", "INFORMATICA", "Lab №2", "11:55", "12:55")

        self.add_lesson("Venerdì", "RELIGIONE", "2 - 08", "07:55", "8:55")
        self.add_lesson("Venerdì", "T.P.S INFO", "Lab №5", "8:55", "9:45")
        self.add_lesson("Venerdì", "T.P.S INFO", "2 - 08", "9:55", "10:55")
        self.add_lesson("Venerdì", "TELE", "2 - 08", "10:55", "11:45")
        self.add_lesson("Venerdì", "ITALIANO", "2 - 16", "11:55", "12:55")
        self.add_lesson("Venerdì", "ITALIANO", "2 - 16", "12.55", "13.55")

        self.add_lesson("Sabato", "ITALIANO", "2 - 15", "07:55", "8:55")
        self.add_lesson("Sabato", "INFORMATICA", "Lab №4", "8:55", "9:45")
        self.add_lesson("Sabato", "INFORMATICA", "Lab №4", "9:55", "10:55")
        self.add_lesson("Sabato", "INFORMATICA", "Lab №4", "10:55", "11:55")