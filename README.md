🔐 Password Generator - Regular Expressions Project
Una aplicación robusta de generación de contraseñas seguras construida con Python y expresiones regulares.

🚀 Características
Generación Segura: Utiliza el módulo secrets para criptografía segura

Personalización Avanzada: Control total sobre la composición de contraseñas

Validación con Regex: Implementación de expresiones regulares para validación

Arquitectura Modular: Código limpio y mantenible

📋 Requisitos
Python 3.8+

Módulos estándar: secrets, string, re

🛠️ Instalación
bash
# Clonar el repositorio
git clone https://github.com/0000MAILY1111/scientific-python-arithmetic
# Navegar al directorio
cd password-generator

# Ejecutar el generador
python password_generator.py
💻 Uso Básico
python
# Generar contraseña con parámetros personalizados
from password_generator import generate_password

# Parámetros: length, nums, special_chars, uppercase, lowercase
secure_password = generate_password(12, 2, 2, 3, 5)
print(f"Contraseña generada: {secure_password}")
🔧 API Reference
generate_password(length, nums, special_chars, uppercase, lowercase)
Genera una contraseña segura con restricciones específicas.

Parámetros:

length (int): Longitud total de la contraseña

nums (int): Número mínimo de dígitos requeridos

special_chars (int): Número mínimo de caracteres especiales

uppercase (int): Número mínimo de letras mayúsculas

lowercase (int): Número mínimo de letras minúsculas

Retorna:

str: Contraseña generada que cumple con todas las restricciones

🏗️ Arquitectura del Proyecto
text
password-generator/
│
├── password_generator.py    # Implementación principal
├── validators.py           # Módulo de validación con regex
├── tests/                  # Suite de pruebas
│   ├── test_generator.py
│   └── test_validators.py
└── requirements.txt        # Dependencias del proyecto
🔍 Validación con Expresiones Regulares
El sistema implementa múltiples patrones regex para garantizar la seguridad:

python
# Ejemplo de patrones de validación
PATTERNS = {
    'digits': re.compile(r'\d'),                    # Validar dígitos
    'special_chars': re.compile(r'[!@#$%^&*()]'),   # Caracteres especiales
    'uppercase': re.compile(r'[A-Z]'),              # Letras mayúsculas
    'lowercase': re.compile(r'[a-z]')               # Letras minúsculas
}
🧪 Testing
bash
# Ejecutar pruebas unitarias
python -m pytest tests/

# Ejecutar con cobertura
python -m pytest --cov=password_generator tests/
📊 Métricas de Seguridad
Entropía alta: Utiliza CSPRNG (Cryptographically Secure PRNG)

Resistente a ataques: Generación impredecible

Validación exhaustiva: Múltiples capas de verificación

🔒 Mejores Prácticas Implementadas
Seguridad: Uso de secrets en lugar de random

Validación: Verificación con expresiones regulares

Flexibilidad: Parámetros configurables

Mantenibilidad: Código modular y documentado

🚀 Roadmap
Interfaz gráfica de usuario (GUI)

API REST para generación remota

Plugin para navegadores

Integración con gestores de contraseñas

🤝 Contribución
Fork el proyecto

Crear una rama feature (git checkout -b feature/AmazingFeature)

Commit cambios (git commit -m 'Add AmazingFeature')

Push a la rama (git push origin feature/AmazingFeature)

Abrir un Pull Request

📄 Licencia
Distribuido bajo la Licencia MIT. Ver LICENSE para más información.

👨‍💻 Autor
Tu 0000MAILY1111

GitHub: [@000MAILY1111](https://github.com/0000MAILY1111)

🙏 Agradecimientos
FreeCodeCamp por el proyecto educativo

Comunidad Python por las mejores prácticas

Contribuidores y testers

⭐ Si este proyecto te fue útil, por favor dale una estrella en GitHub!"# scientific-python-arithmetic" 
