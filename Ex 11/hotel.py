import threading
import time

class Table:
    def __init__(self, table_number, seats):
        self.table_number = table_number
        self.seats = seats
        self.status = "available"

class ReservationSystem:
    def __init__(self, num_tables):
        self.tables = [Table(table_number=i, seats=4) for i in range(1, num_tables + 1)]
        self.lock = threading.Lock()

    def display_availability(self):
        with self.lock:
            for table in self.tables:
                print(f"Table {table.table_number}: {table.status}")

    def reserve_table(self, seats_required, client_name):
        with self.lock:
            for table in self.tables:
                if table.status == "available" and table.seats >= seats_required:
                    table.status = "occupied"
                    print(f"Reserved Table {table.table_number} for {client_name}")
                    # Send reservation notification to client and manager (not implemented)

                    return True
            print(f"Sorry, no available table for {client_name}")
            return False

    def pay_bill(self, table_number):
        with self.lock:
            table = self.tables[table_number - 1]
            table.status = "available"
            print(f"Table {table_number} bill paid. Status changed to available.")
            # Send bill payment notification to client and manager (not implemented)


def reservation_worker(reservation_system, seats_required, client_name):
    reservation_system.reserve_table(seats_required, client_name)

def payment_worker(reservation_system, table_number):
    time.sleep(2)  # Simulating time taken to pay the bill
    reservation_system.pay_bill(table_number)


if __name__ == "__main__":
    num_tables = 5
    reservation_system = ReservationSystem(num_tables)

    # Demonstrate reservation
    threads = []
    for i in range(1, 8):
        client_name = f"Client_{i}"
        seats_required = 3
        reservation_thread = threading.Thread(target=reservation_worker, args=(reservation_system, seats_required, client_name))
        threads.append(reservation_thread)
        reservation_thread.start()

    for thread in threads:
        thread.join()

    # Display table availability after reservations
    reservation_system.display_availability()

    # Demonstrate bill payment
    payment_threads = []
    for i in range(1, 4):
        table_number = i
        payment_thread = threading.Thread(target=payment_worker, args=(reservation_system, table_number))
        payment_threads.append(payment_thread)
        payment_thread.start()

    for thread in payment_threads:
        thread.join()

    # Display table availability after bill payments
    reservation_system.display_availability()
