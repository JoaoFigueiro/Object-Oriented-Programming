import abc
from datetime import datetime

"""
Objectives
    - Creation of abstract classes and abstract methods;
    - multiple inheritance of abstract classes;
    - overriding abstract methods;
    - delivering multiple child classes.
"""

class Scanner(abc.ABC):
    @abc.abstractmethod
    def scan_document(self):
        pass

    @abc.abstractmethod
    def get_scanner_status(self):
        pass


class Printer(abc.ABC):
    @abc.abstractmethod
    def print_document(self):
        pass

    @abc.abstractmethod
    def get_printer_status(self):
        pass


class MFD1(Scanner, Printer):
    def __init__(self):
        self.serial_number = "ABC" + datetime.now().strftime("%Y%m%d%H%M%S")
        self.max_resolution = 100

        self.printer_serial_number = "CBA" + datetime.now().strftime("%H%M%S%Y%m%d")
        self.printer_max_resolution = 100

    def scan_document(self):
        return "Scanning Document in Low Resolution..."

    def get_scanner_status(self):
        return f"""
            Scanner Serial Number: {self.serial_number}
            Scanner Max Resolution: {self.max_resolution}
            """

    def print_document(self):
        return "Printing document..."

    def get_printer_status(self):
        return f"""
            Printer Serial Number: {self.serial_number}
            Printer Max Resolution: {self.max_resolution}
            """

class MFD2(Scanner, Printer):
    print_history = []

    def __init__(self):
        self.serial_number = "DEF" + datetime.now().strftime("%Y%m%d%H%M%S")
        self.max_resolution = 200

        self.printer_serial_number = "FED" + datetime.now().strftime("%H%M%S%Y%m%d")
        self.printer_max_resolution = 200

    def scan_document(self):
        return "Scanning Document in Medium Resolution..."

    def get_scanner_status(self):
        return f"""
            Scanner Serial Number: {self.serial_number}
            Scanner Max Resolution: {self.max_resolution}
            """

    @classmethod
    def print_document(cls):
        print_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        cls.print_history.append(
            f"Print operation at: {print_time}"
        )

        return "Printing document..."

    def get_printer_status(self):
        return f"""
            +--------------------------------------------+ 
            Printer Serial Number: {self.serial_number}
            Printer Max Resolution: {self.max_resolution}
            +--------------------------------------------+
            """

    @classmethod
    def print_operation_history(cls):
        for history in cls.print_history: print(history)


class MFD3(Scanner, Printer):
    print_history = []

    def __init__(self):
        self.serial_number = "DEF" + datetime.now().strftime("%Y%m%d%H%M%S")
        self.max_resolution = 300

        self.printer_serial_number = "FED" + datetime.now().strftime("%H%M%S%Y%m%d")
        self.printer_max_resolution = 300

    def scan_document(self):
        return "Scanning Document in Medium Resolution..."

    def get_scanner_status(self):
        return f"""
            Welcome to the top! 
            ==============================================
            Scanner Serial Number: {self.serial_number}
            Scanner Max Resolution: {self.max_resolution}
            ==============================================
            """

    @classmethod
    def print_document(cls):
        print_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        cls.print_history.append(
            f"Print operation at: {print_time}"
        )

        return "Printing document..."

    def get_printer_status(self):
        return f"""
            Printer Serial Number: {self.serial_number}
            Printer Max Resolution: {self.max_resolution}
            """

    @classmethod
    def print_operation_history(cls):
        for history in cls.print_history: print(history)

    def fax_machine(self):
        print("Fax Machine")


def demonstrate_methods(mfd):
    print(f"Demonstrating methods of {type(mfd).__name__}")

    if not isinstance(mfd, Printer):
        return

    if not isinstance(mfd, Scanner):
        return

    print(mfd.scan_document())
    print(mfd.get_scanner_status())
    print(mfd.print_document())
    print(mfd.get_printer_status())

    if isinstance(mfd, MFD3):
        print(mfd.fax_machine())


mfd1 = MFD1()
mfd2 = MFD2()
mfd3 = MFD3()

for device in [mfd1, mfd2, mfd3]:
    demonstrate_methods(device)

print("Demonstrating class methods of MFD2: ")

MFD2.print_operation_history()

print("Demonstrating class methods of MFD2: ")

MFD3.print_operation_history()





