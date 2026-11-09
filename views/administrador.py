import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, 
    QLineEdit, QComboBox, QPushButton, QMessageBox, QGroupBox
)
from PyQt5.QtCore import Qt

class AdminWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("PANEL DE ADMINISTRADOR - EcoRecarga")
        self.resize(520, 500)

        # Aplicando paleta de colores oficial (Fondo Azul Pizarra Oscuro)
        self.setStyleSheet("""
            QWidget {
                background-color: #0F172A;
                color: #F8FAFC;
                font-family: Arial, sans-serif;
                font-size: 13px;
            }
            QGroupBox {
                border: 2px solid #334155;
                border-radius: 8px;
                margin-top: 15px;
                font-weight: bold;
                color: #38BDF8;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                subcontrol-position: top left;
                padding: 0 5px;
            }
            QLineEdit, QComboBox {
                background-color: #1E293B;
                border: 1px solid #475569;
                border-radius: 5px;
                padding: 6px;
                color: #FFFFFF;
            }
            QLineEdit:focus, QComboBox:focus {
                border: 1px solid #00BFA5;
            }
            QPushButton {
                background-color: #00BFA5;
                color: #0F172A;
                font-weight: bold;
                border-radius: 5px;
                padding: 8px;
            }
            QPushButton:hover {
                background-color: #10B981;
            }
            /* Estilo para los botones de la barra de navegación superior */
            #NavButton {
                background-color: #1E293B;
                color: #38BDF8;
                border: 1px solid #334155;
                font-size: 11px;
            }
            #NavButton:hover {
                background-color: #334155;
            }
        """)

        main_layout = QVBoxLayout()

        # --- TÍTULO PRINCIPAL ---
        lbl_titulo = QLabel("🌿 PANEL DE ADMINISTRADOR - EcoRecarga 🌿")
        lbl_titulo.setStyleSheet("font-size: 15px; font-weight: bold; color: #00BFA5;")
        lbl_titulo.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(lbl_titulo)

        # --- BARRA DE NAVEGACIÓN SUPERIOR (Pestañas) ---
        nav_layout = QHBoxLayout()
        
        btn_registro = QPushButton("➕ Registrar Entrega")
        btn_registro.setObjectName("NavButton")
        
        btn_puntos = QPushButton("📍 Gestionar Puntos")
        btn_puntos.setObjectName("NavButton")
        
        btn_reportes = QPushButton("📈 Reportes")
        btn_reportes.setObjectName("NavButton")
        
        nav_layout.addWidget(btn_registro)
        nav_layout.addWidget(btn_puntos)
        nav_layout.addWidget(btn_reportes)
        main_layout.addLayout(nav_layout)

        # --- FORMULARIO DE REGISTRO DE PESAJE ---
        box_pesaje = QGroupBox(" REGISTRAR NUEVO PESAJE DE RECICLAJE ")
        form_layout = QVBoxLayout()

        # Documento / Usuario
        form_layout.addWidget(QLabel("Documento / Usuario:"))
        self.input_usuario = QLineEdit()
        self.input_usuario.setPlaceholderText("Ej: 10548923-2 (Carlos Pérez)")
        form_layout.addWidget(self.input_usuario)

        # Punto de Acopio
        form_layout.addWidget(QLabel("Punto de Acopio:"))
        self.combo_acopio = QComboBox()
        self.combo_acopio.addItems([
            "Centro de Acopio Central (Av. Universitaria)", 
            "EcoPunto Plaza Comercial"
        ])
        form_layout.addWidget(self.combo_acopio)

        # Tipo de Material (Puntos por kg según especificaciones del proyecto)
        form_layout.addWidget(QLabel("Tipo de Material:"))
        self.combo_material = QComboBox()
        self.combo_material.addItem("Plástico (PET) - 10 pts/kg", 10)
        self.combo_material.addItem("Vidrio - 5 pts/kg", 5)
        self.combo_material.addItem("Aluminio - 15 pts/kg", 15)
        self.combo_material.addItem("Papel / Cartón - 8 pts/kg", 8)
        self.combo_material.currentIndexChanged.connect(self.calcular_puntos)
        form_layout.addWidget(self.combo_material)

        # Peso Ingresado
        form_layout.addWidget(QLabel("Peso Ingresado (kg):"))
        self.input_peso = QLineEdit()
        self.input_peso.setPlaceholderText("Ej: 3.5")
        self.input_peso.textChanged.connect(self.calcular_puntos)
        form_layout.addWidget(self.input_peso)

        # Línea divisoria visual dentro del recuadro
        linea = QWidget()
        linea.setFixedHeight(1)
        linea.setStyleSheet("background-color: #334155; margin: 5px 0;")
        form_layout.addWidget(linea)

        # Resultado de Puntos (Con detalle en tono Dorado/Ámbar oficial)
        self.lbl_puntos = QLabel("Puntos a asignar automáticamente: <span style='color: #FBBF24;'><b>0 Puntos</b></span>")
        self.lbl_puntos.setStyleSheet("font-size: 14px; margin-top: 5px;")
        self.lbl_puntos.setAlignment(Qt.AlignCenter)
        form_layout.addWidget(self.lbl_puntos)

        # Botón de Guardar y Acreditar Principal
        btn_guardar = QPushButton("💾 Guardar y Acreditar Puntos")
        btn_guardar.setStyleSheet("""
            QPushButton {
                background-color: #00BFA5;
                color: #0F172A;
                font-weight: bold;
                font-size: 14px;
                padding: 10px;
                margin-top: 8px;
            }
            QPushButton:hover {
                background-color: #10B981;
                color: #FFFFFF;
            }
        """)
        btn_guardar.clicked.connect(self.guardar_pesaje)
        form_layout.addWidget(btn_guardar)

        box_pesaje.setLayout(form_layout)
        main_layout.addWidget(box_pesaje)

        self.setLayout(main_layout)

    def calcular_puntos(self):
        try:
            peso_text = self.input_peso.text().strip().replace(',', '.')
            if not peso_text:
                self.lbl_puntos.setText("Puntos a asignar automáticamente: <span style='color: #FBBF24;'><b>0 Puntos</b></span>")
                return

            peso = float(peso_text)
            factor_puntos = self.combo_material.currentData()
            total_puntos = int(peso * factor_puntos)

            self.lbl_puntos.setText(f"Puntos a asignar automáticamente: <span style='color: #FBBF24;'><b>{total_puntos} Puntos</b></span>")
        except ValueError:
            self.lbl_puntos.setText("Puntos a asignar automáticamente: <span style='color: #EF4444;'><b>Peso inválido</b></span>")

    def guardar_pesaje(self):
        usuario = self.input_usuario.text().strip()
        peso = self.input_peso.text().strip()
        
        if not usuario or not peso:
            QMessageBox.warning(self, "Campos Incompletos", "Por favor completa el documento del usuario y el peso ingresado.")
            return
            
        QMessageBox.information(self, "Éxito - EcoRecarga", f"¡Pesaje registrado y puntos acreditados correctamente al usuario {usuario}!")
        self.input_usuario.clear()
        self.input_peso.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AdminWindow()
    window.show()
    sys.exit(app.exec_())