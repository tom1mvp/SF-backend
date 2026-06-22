# 🏆 **SF-5: Sistema de Gestión de Torneos y Alquiler de Canchas de Fútbol 5 (API SaaS)** ⚽

**SF-5** es una plataforma backend integral diseñada para modernizar la operación de los complejos deportivos amateurs y transformar la experiencia de los jugadores con el juego. 

Más allá de la reserva estándar de canchas, este proyecto ofrece un **ecosistema dinámico** que acorta la brecha entre la gestión del predio y la interacción de los jugadores, enfocándose en tres pilares principales:

* **Cronograma en tiempo real:** Seguimiento instantáneo de la disponibilidad de las canchas.
* **Generación automática de torneos:** Gestión de llaves complejas para copas dinámicas y etapas de eliminación directa (knockout).
* **Métricas de rendimiento:** Entrega de estadísticas detalladas para el seguimiento de los jugadores.

Esta plataforma transforma los partidos casuales en una experiencia profesional y fluida para amigos que compiten en copas dinámicas y torneos de eliminación directa.

### 📝 Módulos
- **Ubication (Ubicación):** Este módulo gestiona todas las operaciones relacionadas con localizaciones geográficas, incluyendo direcciones, países, provincias y ciudades.
- **People (Personas):** Este módulo maneja todas las operaciones relacionadas con la gestión de registros de identidad personal, incluyendo nombres completos, información de contacto y detalles demográficos.
- **Users (Usuarios):** Este módulo gestiona la autenticación, cuentas de usuario, niveles de autorización (Tokens JWT) y flujos independientes de verificación/reactivación por correo electrónico.
    
### ⚙️ Endpoints

* **Módulo de Ubicación**:
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
    | `GET` | `/ubication/address/list/` | Obtiene la lista completa de todas las direcciones en la base de datos. | No |
    | `GET` | `/ubication/address/street/<str:street>/` | Obtiene los detalles de la dirección que coincida con la calle especificada en la URL. | No |
    | `GET` | `/ubication/address/city/<str:city_name>/` | Obtiene todas las direcciones asociadas al nombre de la ciudad especificado en la URL. | No |
    | `POST`| `/ubication/address/create/` | Crea un nuevo registro de dirección asociado a una ciudad específica. | No |
    | `PUT`| `/ubication/address/update/<int:id>/` | Actualiza un registro de dirección existente que coincida con el ID especificado. | No |
    
* **Módulo de Personas**:
    | Método | Endpoint | Descripción | Requiere Autenticación |
    | :--- | :--- | :--- | :---: |
    | `GET` | `/person/document/type/list/` | Obtiene la lista completa de todos los tipos de documento en la base de datos. | No |
    | `GET` | `/person/document/type/name/<str:name>/` | Obtiene los detalles del tipo de documento que coincida con el nombre especificado en la URL. | No |
    | `GET` | `/person/genre/list/` | Obtiene la lista completa de todos los géneros en la base de datos. | No |
    | `GET` | `/person/genre/name/<str:name>/` | Obtiene los detalles del género que coincida con el nombre especificado en la URL. | No |
    | `GET` | `/person/list/` | Obtiene la lista completa de todas las personas registradas en la base de datos. | No |
    | `GET` | `/person/name/<str:last_name>/` | Obtiene todas las personas que coincidan con el apellido especificado en la URL. | No |
    | `GET` | `/person/document/<str:document_number>/` | Obtiene los detalles de una persona que coincida con el número de documento especificado. | No |
    | `POST` | `/person/create/` | Registra un nuevo registro de persona con sus datos de identificación. | No |
    | `PUT` | `/person/update/<int:id>/` | Actualiza un registro de persona existente que coincida con el ID especificado. | No |

* **Módulo de Usuarios**:
    | Método | Endpoint | Descripción | Requiere Autenticación |
    | :--- | :--- | :--- | :---: |
    | `GET` | `/user/list/` | Obtiene una lista de todos los usuarios del sistema. | Sí (Admin) |
    | `GET` | `/username/<str:username>/` | Obtiene información detallada de la cuenta de usuario por su nombre de usuario. | No |
    | `GET` | `/email/<str:email>/` | Obtiene información detallada de la cuenta de usuario por su correo electrónico. | No |
    | `POST` | `/login/` | Autentica las credenciales del usuario y devuelve un token de acceso seguro. | No |
    | `POST` | `/register/` | Registra una nueva cuenta de usuario vinculada a un rol e información personal. | No |
    | `PUT` | `/update/<int:id>/` | Modifica los datos de un usuario existente que coincida con el ID especificado. | No |
    | `PATCH` | `/delete/<int:id>/` | Realiza una desactivación lógica de un perfil de usuario. | No |
    | `PATCH` | `/recover/<str:email>/` | Vuelve a habilitar de forma lógica una cuenta previamente desactivada. | No |
    | `PATCH` | `/recover/password/<int:id>/` | Restablece y actualiza la contraseña de la cuenta para el ID de usuario indicado. | No |
    | `POST` | `/email/reset/password/<str:username>/<str:email>/` | Dispara un enlace seguro y automatizado para recuperar la contraseña mediante un token único. | No |
    | `POST` | `/email/reactivation/user/<str:username>/<str:email>/` | Dispara un correo electrónico seguro que contiene un enlace de activación para reactivar una cuenta de usuario. | No |

### 📄 Especificaciones Detalladas

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
                "id": 6,
                "name": "Buenos Aires",
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

#### 🏠 Endpoints de Direcciones (Address)

##### 9. Obtener todas las direcciones
* **URL:** `/ubication/address/list/`
* **Método:** `GET`
* **Respuesta Exitosa (200 OK):**
```json
    {
        "data": [
            {
                "id": 1,
                "street_main": "Lorem ipsum",
                "street_complement": "Lorem ipsum ipsum",
                "street_number": "1880",
                "apartment_number": "",
                "floor": "",
                "comment": "Casa principal",
                "is_apartment": false,
                "city_id": 2687,
                "city_name": "Río Cuarto"
            },
            {
                "id": 2,
                "street_main": "Lorem ipsum",
                "street_complement": "Lorem ipsum",
                "street_number": "0000",
                "apartment_number": "8",
                "floor": "4",
                "comment": "Departamento principal",
                "is_apartment": true,
                "city_id": 2687,
                "city_name": "Río Cuarto"
            }
        ]
    }
    ```
* **Respuesta de Error (404 Not Found):**
```json
    {
        "error": "NotFound",
        "message": "Address not found"
    }
    ```

#### 10. Obtener dirección por calle
* **URL:** `/ubication/address/street/<str:street>/`
* **Método:** `GET`
* **Parámetros de URL:** `street=[string]` (ej: `Lorem ipsum`)
* **Respuesta Exitosa (200 OK):**
```json
    {
        "data": [
            {
                "id": 1,
                "street_main": "Lorem ipsum",
                "street_complement": "Lorem ipsum ipsum",
                "street_number": "1880",
                "apartment_number": "",
                "floor": "",
                "comment": "Casa principal",
                "is_apartment": false,
                "city_id": 2687,
                "city_name": "Río Cuarto"
            }
        ]
    }
    ```
* **Respuesta de Error (400 Bad Request):**
```json
    {
        "error": "ValidationError",
        "message": "The street name is required in the URL."
    }
    ```
* **Respuesta de Error (404 Not Found):**
```json
    {
        "error": "NotFound",
        "message": "Street not found"
    }
    ```

#### 11. Obtener direcciones por ciudad
* **URL:** `/ubication/address/city/<str:city_name>/`
* **Método:** `GET`
* **Parámetros de URL:** `city_name=[string]` (ej: `Río Cuarto`)
* **Respuesta Exitosa (200 OK):**
```json
    {
        "data": [
            {
                "id": 1,
                "street_main": "Lorem ipsum",
                "street_complement": "Lorem ipsum ipsum",
                "street_number": "1880",
                "apartment_number": "",
                "floor": "",
                "comment": "Casa principal",
                "is_apartment": false,
                "city_id": 2687,
                "city_name": "Río Cuarto"
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

#### 12. Crear una dirección
* **URL:** `/ubication/address/create/`
* **Método:** `POST`
* **Encabezados (Headers):** `Content-Type: application/json`
* **Cuerpo de la Petición (JSON Request Body):**
```json
    {
        "street_main": "Lorem",
        "street_complement": "Ipsum",
        "street_number": "0000",
        "apartment_number": "",
        "floor": "",
        "comment": "Casa principal",
        "is_apartment": false,
        "city_id": 2687
    }
    ```
* **Respuesta Exitosa (201 Created):**
```json
    {
        "Message": "The address has been successfully created",
        "data": {
            "id": 1,
            "street_main": "Lorem",
            "street_complement": "Ipsum",
            "street_number": "0000",
            "apartment_number": "",
            "floor": "",
            "comment": "Casa principal",
            "is_apartment": false,
            "city_id": 2687,
            "city_name": "Río Cuarto"
        }
    }
    ```
* **Respuesta de Error (400 Bad Request):**
```json
    {
        "Error": "Sensitive data is missing"
    }
    ```

#### 13. Actualizar una dirección
* **URL:** `/ubication/address/update/<int:id>/`
* **Método:** `PUT`
* **Parámetros de URL:** `id=[integer]` (ej: `2`)
* **Encabezados (Headers):** `Content-Type: application/json`
* **Cuerpo de la Petición (JSON Request Body):**
```json
    {
        "street_main": "Lore Lore",
        "street_complement": "Ipsum",
        "street_number": "9000",
        "apartment_number": "1",
        "floor": "2",
        "comment": "Departamento principal",
        "is_apartment": true,
        "city_id": 2687
    }
    ```
* **Respuesta Exitosa (200 OK):**
```json
    {
        "Message": "The address has been successfully updated",
        "data": {
            "id": 2,
            "street_main": "Lore lore",
            "street_complement": "Ipsum",
            "street_number": "9000",
            "apartment_number": "1",
            "floor": "2",
            "comment": "Departamento principal",
            "is_apartment": true,
            "city_id": 2687,
            "city_name": "Río Cuarto"
        }
    }
    ```
* **Respuesta de Error (400 Bad Request):**
```json
    {
        "Error": "Sensitive data is missing"
    }
    ```
* **Respuesta de Error (404 Not Found):**
```json
    {
        "Error": "Address not found"
    }
    ```

---

#### 👤 Endpoints de Personas (People)

##### 14. Obtener todos los géneros
* **URL:** `/person/genre/list/`
* **Método:** `GET`
* **Respuesta Exitosa (200 OK):**
```json
    {
        "data": [
            {
                "id": 1,
                "name": "Male"
            },
            {
                "id": 2,
                "name": "Female"
            }
        ]
    }
    ```
* **Respuesta de Error (404 Not Found):**
```json
    {
        "error": "NotFound",
        "message": "Genres not found"
    }
    ```

#### 15. Obtener género por nombre
* **URL:** `/person/genre/name/<str:name>/`
* **Método:** `GET`
* **Parámetros de URL:** `name=[string]` (ej: `Female`)
* **Respuesta Exitosa (200 OK):**
```json
    {
        "data": [
            {
                "id": 2,
                "name": "Female"
            }
        ]
    }
    ```
* **Respuesta de Error (400 Bad Request):**
```json
    {
        "error": "ValidationError",
        "message": "The genre name is required in the URL."
    }
    ```
* **Respuesta de Error (404 Not Found):**
```json
    {
        "error": "NotFound",
        "message": "Genre not found"
    }
    ```

##### 16. Obtener todos los tipos de documento
* **URL:** `/person/document/type/list/`
* **Método:** `GET`
* **Respuesta Exitosa (200 OK):**
```json
    {
        "data": [
            {
                "id": 1,
                "name": "DNI"
            },
            {
                "id": 2,
                "name": "Passport"
            }
        ]
    }
    ```
* **Respuesta de Error (404 Not Found):**
```json
    {
        "error": "NotFound",
        "message": "Document Types not found"
    }
    ```

#### 17. Obtener tipo de documento por nombre
* **URL:** `/person/document/type/name/<str:name>/`
* **Método:** `GET`
* **Parámetros de URL:** `name=[string]` (ej: `DNI`)
* **Respuesta Exitosa (200 OK):**
```json
    {
        "data": [
            {
                "id": 1,
                "name": "DNI"
            }
        ]
    }
    ```

#### 18. Obtener todas las personas
* **URL:** `/person/list/`
* **Método:** `GET`
* **Respuesta Exitosa (200 OK):**
```json
    {
        "data": [
            {
                "id": 1,
                "first_name": "John",
                "last_name": "Doe",
                "document_number": "12345678",
                "birth_date": "1995-05-20",
                "phone": "5551234567",
                "email": "johndoe@example.com",
                "document_type_id": 1,
                "genre_id": 1,
                "address_id": 1
            }
        ]
    }
    ```

#### 19. Obtener personas por apellido
* **URL:** `/person/name/<str:last_name>/`
* **Método:** `GET`
* **Parámetros de URL:** `last_name=[string]` (ej: `Doe`)
* **Respuesta Exitosa (200 OK):**
```json
    {
        "data": [
            {
                "id": 1,
                "first_name": "John",
                "last_name": "Doe",
                "document_number": "12345678",
                "birth_date": "1995-05-20",
                "phone": "5551234567",
                "email": "johndoe@example.com",
                "document_type_id": 1,
                "genre_id": 1,
                "address_id": 1
            }
        ]
    }
    ```

#### 20. Crear una persona
* **URL:** `/person/create/`
* **Método:** `POST`
* **Encabezados (Headers):** `Content-Type: application/json`
* **Cuerpo de la Petición (JSON Request Body):**
```json
    {
        "first_name": "Jane",
        "last_name": "Smith",
        "document_number": "87654321",
        "birth_date": "1992-10-10",
        "phone": "5559876543",
        "email": "janesmith@example.com",
        "document_type_id": 1,
        "genre_id": 2,
        "address_id": 2
    }
    ```

---

#### 🔒 Endpoints de Usuarios (Users)

##### 21. Disparar correo de restablecimiento de contraseña
* **URL:** `/email/reset/password/<str:username>/<str:email>/`
* **Método:** `POST`
* **Parámetros de URL:** `username=[string]`, `email=[string]`
* **Respuesta Exitosa (200 OK):**
```json
    {
        "message": "The email recover was successfully sent."
    }
    ```
* **Respuesta de Error (400 Bad Request):**
```json
    {
        "error": "BadRequest",
        "message": "We were unable to send the recovery email"
    }
    ```

##### 22. Inicio de sesión de usuario (Generación de JWT)
* **URL:** `/login/`
* **Método:** `POST`
* **Cuerpo de la Petición (JSON Request Body):**
```json
    {
        "username": "thomas",
        "password": "secure_password"
    }
    ```
* **Respuesta Exitosa (200 OK):**
```json
    {
        "Message": "Welcome, user",
        "data": {
            "id": 1,
            "username": "thomas",
            "is_active": true,
            "person_id": 1
        },
        "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
    }
    ```

##### 23. Desactivación lógica de usuario
* **URL:** `/delete/<int:id>/`
* **Método:** `PATCH`
* **Parámetros de URL:** `id=[integer]` (ej: `1`)
* **Respuesta Exitosa (200 OK):**
```json
    {
        "message": "The user was successfully deactivated."
    }
    ```

---

### 🛠️ Tecnologías y Arquitectura

* **Framework Backend:** Django & Django REST Framework (DRF)
* **Autenticación:** Simple JWT & Generador de Tokens Seguro (módulo `secrets`)
* **Base de Datos:** PostgreSQL (Alojada en Neon Tech)
* **Entorno y Despliegue:** Docker & Docker Compose

### 📁 Arquitectura de la Base de Datos

* **Usuarios y Perfiles:** Modelos de usuario personalizados para gestionar tanto a los Administradores de los Predios como los perfiles de los Jugadores.
* **Reservas:** Gestión de canchas, tarifas por hora, reservas y estados de pago.
* **Torneos (Copas):** Control de torneos, equipos, emparejamientos de llaves y etapas de eliminación directa.
* **Estadísticas y Análisis:** Seguimiento de datos de los partidos, goles, tarjetas e historial de rendimiento de los jugadores.

### 👤 Creador

* **Thomas Elser Bratik** – *Desarrollador Fullstack Junior* – [@tom1mvp](https://github.com/tom1mvp)

---
*¡Conectemos! Si tenés alguna sugerencia o querés saber más sobre el desarrollo de SF-5, no dudes en visitar mi perfil.*