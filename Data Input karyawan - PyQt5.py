import sys
import pandas as pd
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QTextEdit, QPushButton, QVBoxLayout, QHBoxLayout, QScrollArea, QSizePolicy


class EmployeeInputWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.employee_data = []
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Input Data Karyawan')

        # Label dan input untuk nama
        self.name_label = QLabel('Nama:')
        self.name_input = QLineEdit()

        # Label dan input untuk alamat
        self.address_label = QLabel('Alamat:')
        self.address_input = QTextEdit()

        # Label dan input untuk jabatan
        self.position_label = QLabel('Jabatan:')
        self.position_input = QLineEdit()

        # Button untuk submit
        self.submit_button = QPushButton('Submit')
        self.submit_button.clicked.connect(self.submit_data)

        # Button untuk simpan ke Excel
        self.save_button = QPushButton('Simpan ke Excel')
        self.save_button.clicked.connect(self.save_to_excel)

        # Button untuk clear data
        self.clear_button = QPushButton('Clear')
        self.clear_button.clicked.connect(self.clear_data)

        # Layout utama
        layout = QVBoxLayout()
        layout.addWidget(self.name_label)
        layout.addWidget(self.name_input)
        layout.addWidget(self.address_label)
        layout.addWidget(self.address_input)
        layout.addWidget(self.position_label)
        layout.addWidget(self.position_input)
        layout.addWidget(self.submit_button)
        layout.addWidget(self.save_button)
        layout.addWidget(self.clear_button)

        # Scroll Area untuk menampilkan data karyawan
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area_widget = QWidget()
        self.scroll_area_layout = QVBoxLayout(scroll_area_widget)
        self.data_label = QLabel('Data Karyawan:')
        self.scroll_area_layout.addWidget(self.data_label)
        scroll_area.setWidget(scroll_area_widget)
        layout.addWidget(scroll_area)

        self.setLayout(layout)

    def submit_data(self):
        # Mengambil nilai input dari widget
        name = self.name_input.text()
        address = self.address_input.toPlainText()
        position = self.position_input.text()

        # Menambahkan data karyawan ke list
        employee = {'Nama': name, 'Alamat': address, 'Jabatan': position}
        self.employee_data.append(employee)

        # Memperbarui tampilan data karyawan di GUI
        self.update_employee_data()

        # Mereset nilai input setelah submit
        self.name_input.clear()
        self.address_input.clear()
        self.position_input.clear()

    def update_employee_data(self):
        # Menghapus semua widget data karyawan sebelumnya
        for i in reversed(range(self.scroll_area_layout.count())):
            self.scroll_area_layout.itemAt(i).widget().setParent(None)

        # Menambahkan widget baru untuk setiap data karyawan
        for employee in self.employee_data:
            data_label = QLabel(f"Nama: {employee['Nama']}, Alamat: {employee['Alamat']}, Jabatan: {employee['Jabatan']}")
            self.scroll_area_layout.addWidget(data_label)

    def save_to_excel(self):
        # Membuat dataframe dari data karyawan
        df = pd.DataFrame(self.employee_data)

        # Menyimpan dataframe ke file Excel
        df.to_excel('data_karyawan.xlsx', index=False)
        print('Data karyawan berhasil disimpan ke Excel.')

    def clear_data(self):
        # Menghapus semua data karyawan
        self.employee_data = []

        # Memperbarui tampilan data karyawan di GUI
        self.update_employee_data()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = EmployeeInputWidget()
    window.show()
    sys.exit(app.exec_())
