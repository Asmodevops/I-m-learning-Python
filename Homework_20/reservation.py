import datetime as dt 
import json



class Reservation:
    def __init__(self, first_name, last_name, start_date, end_date, room_type):
        self.first_name = first_name
        self.last_name = last_name
        self.start_date = dt.datetime.strptime(start_date, "%Y-%m-%d")
        self.end_date = dt.datetime.strptime(end_date, "%Y-%m-%d")
        self.room_type = room_type
        self.reservations = self.load_reservations()


    def load_reservations(self):
        try:
            with open('reservations.json', 'r', encoding='utf-8') as file:
                reservations = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            reservations = []
        return reservations


    def save_reservations(self):
        with open('reservations.json', 'w', encoding='utf-8') as file:
            json.dump(self.reservations, file, indent=4, ensure_ascii=False)


    def add_reservation(self):
        if self.is_room_available(str(self.start_date.date())):
            reservation_info = {
                'first_name': self.first_name,
                'last_name': self.last_name,
                'start_date': str(self.start_date.date()),
                'end_date': str(self.end_date.date()),
                'room_type': self.room_type
            }
            self.reservations.append(reservation_info)
            self.save_reservations()
            print('Номер успешно забронирован.')

        else:
            print(f"Данный номер занят до {self.end_date.date()}. Попробуйте выбрать другой номер или перенести заезд.")
           

    def del_reservation(self):
        for i, reservation in enumerate(self.reservations):
            if (
                reservation['first_name'] == self.first_name
                and reservation['last_name'] == self.last_name
                and reservation['start_date'] == str(self.start_date.date())
                and reservation['end_date'] == str(self.end_date.date())
                and reservation['room_type'] == self.room_type
            ):
                del self.reservations[i]
                self.save_reservations()
                print("Бронирование указанного номера отменено.")
                return True
        print("Данная бронь не найдена.")
        return False


    def is_room_available(self, date):
        date = dt.datetime.strptime(date, "%Y-%m-%d")
        for reservation in self.reservations:
            start_reservation = dt.datetime.strptime(reservation['start_date'], "%Y-%m-%d")
            end_reservation = dt.datetime.strptime(reservation['end_date'], "%Y-%m-%d")
            
            if (
                reservation['room_type'] == self.room_type
                and start_reservation <= date < end_reservation
            ):
                return False
        return True
