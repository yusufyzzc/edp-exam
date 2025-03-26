class Company:
    def __init__(self):
        self.applicants = []
        self.event_queue = []

    def register_applicant(self, applicant):
        self.applicants.append(applicant)
        print(f"Applicant {applicant.name} registered successfully")

    def notify_applicants(self, message):
        for applicant in self.applicants:
            applicant.receive_notification(message)

    def add_event(self, event):
        self.event_queue.append(event)
        print(f"Event added: {event}")

    def process_events(self):
        while self.event_queue:
            event = self.event_queue.pop(0)
            print(f"Processing event: {event}")
            self.notify_applicants(event)


class Applicant:
    def __init__(self, name, surname, birthday, address, id_number):
        self.name = name
        self.surname = surname
        self.birthday = birthday
        self.address = address
        self.id_number = id_number

    def receive_notification(self, message):
        print(f"Notification for {self.name}: {message}")


if __name__ == "__main__":
    company = Company()

    applicant_1 = Applicant("Mark", "White", "01-01-2001", "Berlin-Germany", "12345")
    applicant_2 = Applicant("Mike", "Terrain", "02-01-2004", "Hamburg-Germany", "12987")

    company.register_applicant(applicant_1)
    company.register_applicant(applicant_2)

    company.add_event("Your application number is 02")
    company.add_event("Congratulations, Select Interview date")
    company.process_events()
