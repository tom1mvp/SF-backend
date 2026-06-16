# 🏆 **SF-5: Sistema de Gestión de Torneos y Alquiler de Canchas de Fútbol 5 (API SaaS)** ⚽

**SF-5** es una plataforma backend integral diseñada para modernizar la operación de los complejos deportivos amateurs y transformar la experiencia de los jugadores. 

Más allá de la reserva estándar de canchas, este proyecto ofrece un **ecosistema dinámico** que acorta la brecha entre la gestión del predio y la interacción de la comunidad, enfocándose en tres pilares principales:

* **Cronograma en tiempo real:** Seguimiento instantáneo de la disponibilidad de las canchas.
* **Generación automática de torneos:** Gestión de llaves complejas para copas dinámicas y etapas de eliminación directa (knockout).
* **Métricas de rendimiento:** Entrega de estadísticas detalladas para el seguimiento de los jugadores.

Esta plataforma transforma los partidos casuales en una experiencia profesional y fluida para amigos que compiten en copas dinámicas y torneos de eliminación directa.

### 📝 Módulos del Sistema
- **Ubication (Ubicación):** Este módulo gestiona todas las operaciones relacionadas con localizaciones geográficas, incluyendo países, provincias y ciudades. Es la base estructural para situar los complejos deportivos.

### ⚙️ Endpoints del Sistema

#### Módulo de Ubicación
| Método | Endpoint | Descripción | Requiere Autenticación |
| :--- | :--- | :--- | :---: |
| `GET` | `/ubication/country/list/` | Obtiene la lista completa de todos los países en la base de datos. | No |
| `GET` | `/ubication/country/name/<str:name>/` | Obtiene los detalles del país que coincida con el nombre especificado en la URL. | No |
| `GET` | `/ubication/province/list/` | Obtiene la lista completa de todas las provincias en la base de datos. | No |
| `GET` | `/ubication/province/name/<str:name>/` | Obtiene los detalles de la provincia que coincida con el nombre especificado en la URL. | No |
| `GET` | `/ubication/province/country/<str:country_name>/` | Obtiene todas las provincias asociadas al nombre del país especificado en la URL. | No |
| `GET` | `/ubication/city/list/` | Obtiene la lista completa de todas las ciudades en la base de datos. | No |
| `GET` | `/ubication/city/name/<str:name>/` | Obtiene los detalles de la ciudad que coincida con el nombre especificado en la URL. | No |
| `GET` | `/ubication/city/province/<str:province_name>/` | Obtiene todas las ciudades asociadas al nombre de la provincia especificado en la URL. | No |

### 📄 Especificaciones Detalladas (Módulo Ubicación)

---

#### 🗺️ Endpoints de Países (Country)

##### 1. Obtener todos los países
* **URL:** `/ubication/country/list/`
* **Método:** `GET`
* **Respuesta Exitosa (200 OK):**
    ```json
    {
        "data": [
            {
                "id": 1,
                "name": "Argentina"
            }
        ]
    }
    ```
* **Respuesta de Error (404 Not Found):**
    ```json
    {
        "error": "NotFound",
        "message": "Country not found"
    }
    ```

##### 2. Obtener país por nombre
* **URL:** `/ubication/country/name/<str:name>/`
* **Método:** `GET`
* **Parámetros de URL:** `name=[string]` (ej: `Argentina`)
* **Respuesta Exitosa (200 OK):**
    ```json
    {
        "data": [
            {
                "id": 1,
                "name": "Argentina"
            }
        ]
    }
    ```
* **Respuesta de Error (400 Bad Request):**
    ```json
    {
        "error": "ValidationError",
        "message": "The country name is required in the URL."
    }
    ```
* **Respuesta de Error (404 Not Found):**
    ```json
    {
        "error": "NotFound",
        "message": "Country not found"
    }
    ```

---

#### 🏛️ Endpoints de Provincias (Province)

##### 3. Obtener todas las provincias
* **URL:** `/ubication/province/list/`
* **Método:** `GET`
* **Respuesta Exitosa (200 OK):**
    ```json
    {
        "data": [
            {
                "id": 2,
                "name": "Ciudad Autonoma de Buenos Aires",
                "country_id": 1,
                "country_name": "Argentina"
            },
            {
                "id": 14,
                "name": "Cordoba",
                "country_id": 1,
                "country_name": "Argentina"
            }
        ]
    }
    ```
* **Respuesta de Error (404 Not Found):**
    ```json
    {
        "error": "NotFound",
        "message": "Provinces not found"
    }
    ```
            
##### 4. Obtener provincia por nombre
* **URL:** `/ubication/province/name/<str:name>/`
* **Método:** `GET`
* **Parámetros de URL:** `name=[string]` (ej: `Cordoba`)
* **Respuesta Exitosa (200 OK):**
    ```json
    {
        "data": [
            {
                "id": 14,
                "name": "Cordoba",
                "country_id": 1,
                "country_name": "Argentina"
            }
        ]
    }
    ```
* **Respuesta de Error (400 Bad Request):**
    ```json
    {
        "error": "ValidationError",
        "message": "The province name is required in the URL."
    }
    ```
* **Respuesta de Error (404 Not Found):**
    ```json
    {
        "error": "NotFound",
        "message": "province not found"
    }
    ```
         
##### 5. Obtener provincias por nombre de país
* **URL:** `/ubication/province/country/<str:country_name>/`
* **Método:** `GET`
* **Parámetros de URL:** `country_name=[string]` (ej: `Argentina`)
* **Respuesta Exitosa (200 OK):**
    ```json
    {
        "data": [
            {
                "id": 2,
                "name": "Ciudad Autonoma de Buenos Aires",
                "country_id": 1,
                "country_name": "Argentina"
            },
            {
                "id": 14,
                "name": "Cordoba",
                "country_id": 1,
                "country_name": "Argentina"
            }
        ]
    }
    ```

---

#### 🏙️ Endpoints de Ciudades (City)

##### 6. Obtener todas las ciudades
* **URL:** `/ubication/city/list/`
* **Método:** `GET`
* **Respuesta Exitosa (200 OK):**
    ```json
    {
        "data": [
            {
                "id": 1,
                "name": "Río Cuarto",
                "province_id": 14,
                "province_name": "Cordoba"
            },
            {
                "id": 2,
                "name": "Villa Maria",
                "province_id": 14,
                "province_name": "Cordoba"
            }
        ]
    }
    ```
* **Respuesta de Error (404 Not Found):**
    ```json
    {
        "error": "NotFound",
        "message": "City not found"
    }
    ```

##### 7. Obtener ciudad por nombre
* **URL:** `/ubication/city/name/<str:name>/`
* **Método:** `GET`
* **Parámetros de URL:** `name=[string]` (ej: `Cordoba`)
* **Respuesta Exitosa (200 OK):**
    ```json
    {
        "data": [
            {
                "id": 1,
                "name": "Río Cuarto",
                "province_id": 14,
                "province_name": "Cordoba"
            }
        ]
    }
    ```
* **Respuesta de Error (400 Bad Request):**
    ```json
    {
        "error": "ValidationError",
        "message": "The city name is required in the URL."
    }
    ```
* **Respuesta de Error (404 Not Found):**
    ```json
    {
        "error": "NotFound",
        "message": "City not found"
    }
    ```

##### 8. Obtener ciudades por nombre de provincia
* **URL:** `/ubication/city/province/<str:province_name>/`
* **Método:** `GET`
* **Parámetros de URL:** `province_name=[string]` (ej: `Cordoba`)
* **Respuesta Exitosa (200 OK):**
    ```json
    {
        "data": [
            {
                "id": 1,
                "name": "Río Cuarto",
                "province_id": 14,
                "province_name": "Cordoba"
            },
            {
                "id": 2,
                "name": "Villa Maria",
                "province_id": 14,
                "province_name": "Cordoba"
            }
        ]
    }
    ```
* **Respuesta de Error (400 Bad Request):**
    ```json
    {
        "error": "ValidationError",
        "message": "The province name is required in the URL."
    }
    ```
* **Respuesta de Error (404 Not Found):**
    ```json
    {
        "error": "NotFound",
        "message": "Province not found"
    }
    ```

---

### 🛠️ Tecnologías y Arquitectura

* **Framework Backend:** Django & Django REST Framework (DRF)
* **Base de Datos:** PostgreSQL (Alojada en Neon Tech)
* **Entorno y Despliegue:** Docker & Docker Compose

### 📁 Arquitectura de la Base de Datos

* **Usuarios y Perfiles:** Modelos de usuario personalizados para gestionar tanto a los Administradores de los Predios como los perfiles de los Jugadores.
* **Alquileres y Reservas:** Gestión de canchas, tarifas por hora, reservas y estados de pago.
* **Torneos (Copas):** Control de torneos, equipos, emparejamientos de llaves y etapas de eliminación directa.
* **Estadísticas y Análisis:** Seguimiento de datos del partido, goles, tarjetas e historial de rendimiento de los jugadores.

---

### 👤 Creador

* **Thomas Elser Bratik** – *Desarrollador Fullstack Junior* – [@tom1mvp](https://github.com/tom1mvp)

---
*¡Conectemos! Si tenés alguna sugerencia o querés saber más sobre el desarrollo de SF-5, no dudes en visitar mi perfil.*