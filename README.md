# Generador de Contraseñas Seguras - Python

![Python](https://img.shields.io/badge/Python-3.6+-3776AB?style=for-the-badge&logo=python&logoColor=white)

> **Un generador de contraseñas seguro e interactivo desarrollado en Python**  
> *Crea contraseñas robustas y personalizables con facilidad*

<img width="620" height="272" alt="image1" src="https://github.com/user-attachments/assets/b2961620-e9d6-495e-9981-bebc5c73ddf9" />

<img width="992" height="687" alt="image2" src="https://github.com/user-attachments/assets/8c5345b3-d9f9-4db4-b17e-4628ad891ff0" />

## Tabla de Contenidos
- [Sobre este proyecto](#sobre-este-proyecto)
- [Características](#características)
- [Instalación y uso](#instalacion-y-uso)
- [Explicación del código](#explicación-del-código)
- [Autor](#autor)

## Sobre este proyecto
Este proyecto es un generador de contraseñas seguro e interactivo desarrollado en Python. 
Utiliza el módulo secrets para generar contraseñas criptográficamente seguras, a diferencia del módulo random que es menos seguro para este propósito.

### Características principales:
- Configuración interactiva: El usuario puede personalizar longitud y tipos de caracteres
- Múltiples modos: Generación individual o múltiple
- Validaciones: Longitud mínima y selección obligatoria de caracteres
- Interfaz amigable: Menú claro con opciones numeradas
- Seguridad: Uso de secrets para generación criptográficamente segura

### Tecnologías implementadas:
- Python 3.6+: Lenguaje base
- Módulo secrets: Generación segura de contraseñas
- Módulo string: Conjuntos de caracteres predefinidos
- Módulo random: Mezcla de caracteres (solo para ordenamiento)

## Características

|Característica|	Descripción|
|--------------|-------------|
|Generación segura|	Usa secrets en lugar de random para seguridad criptográfica|
|Configurable	|Longitud, mayúsculas, minúsculas, números y símbolos|
|Múltiples contraseñas|	Genera varias contraseñas a la vez|
|Menú interactivo	|5 opciones para diferentes necesidades|
|Validación|	Mínimo 4 caracteres y al menos un tipo seleccionado|
|Resumen visual	|Muestra la configuración actual|
|Sin dependencias|	Solo usa módulos estándar de Python|

## Instalación y uso

### Requisitos
- Python 3.6 o superior
- No requiere dependencias externas

### Instalación 

```bash
# 1. Clonar el repositorio
git clone https://github.com/tu-usuario/generador-contrasenas.git
cd generador-contrasenas

# 2. Ejecutar el programa
python generador.py
```

### Menú de opciones

|Opción|	Función|
|------|---------|
|1	|Configurar y generar una contraseña|
2	|Configurar y generar múltiples contraseñas|
3	|Usar configuración actual y generar|
4	|Ver configuración actual|
5	|Salir del programa|

## Explicación del código

### Clase principal: GeneradorContrasenas

| Método | Función | Descripción |
|--------|---------|-------------|
| `__init__()` | Constructor | Inicializa configuración por defecto |
| `generar()` | Generación | Crea una contraseña segura |
| `generar_multiple()` | Múltiple | Genera varias contraseñas |
| `configurar()` | Configuración | Establece parámetros personalizados |
| `pedir_configuracion()` | Interactivo | Pide configuración al usuario |
| `_preguntar_si_no()` | Auxiliar | Maneja entrada de sí/no |
| `_mostrar_resumen()` | Visual | Muestra configuración actual |

### Conceptos clave aplicados

| Concepto | Implementación |
|----------|----------------|
| **Seguridad criptográfica** | `secrets.choice()` en lugar de `random.choice()` |
| **Programación orientada a objetos** | Clase `GeneradorContrasenas` |
| **Manejo de excepciones** | `try/except` para entradas inválidas |
| **Validación de datos** | Longitud mínima y tipos de caracteres |
| **Interfaz de usuario** | Menú interactivo en consola |
| **Módulos estándar** | `string`, `secrets`, `random` |

## Autor

**Humberto Isaac Padilla Contreras**
- GitHub: [@LovecraftianCode](https://github.com/LovecraftianCode)
- LinkedIn: [Humberto Isaac Padilla Contreras](https://www.linkedin.com/in/humberto-isaac-padilla-contreras-3527aa3b7)
- Proyecto inspirado en necesidades de seguridad digital
