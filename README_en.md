# 🏆 **SF-5: 5-a-Side Soccer Field Rental & Tournament System (SAAS API)** ⚽

**SF-5** is a comprehensive backend platform designed to modernize how amateur sports complexes operate and how players experience the game. 

Beyond standard field booking, this project delivers a **dynamic ecosystem** that bridges the gap between venue management and player engagement by focusing on three core pillars:

* **Live scheduling:** Tracking real-time field availability.
* **Automated tournament generation:** Handling complex brackets for dynamic cups and knockout stages.
* **Performance analytics:** Delivering detailed statistics for players.

This platform transforms casual matches into a professional, seamless experience for friends competing in dynamic cups and knockout tournaments.

### 📝 Modules
- **Ubication**: This module handles all operations related to geographic locations, including address, countries, provinces, and cities.
- **People**: This module handles all operations related to managing personal identity records, including full names, contact info, and demographic details.
- **Users**: This module manages authentication, user accounts, authorization levels (JWT Tokens), and independent email verification/reactivation workflows.
    
### ⚙️ Endpoints
* **Ubication Module**:
    | Method | Endpoint | Description | Auth Required |
    | :--- | :--- | :--- | :---: |
    | `GET` | `/ubication/country/list/` | Retrieves a complete list of all countries in the database. | No |
    | `GET` | `/ubication/country/name/<str:name>/` | Retrieves the country details that match the name specified in the URL. | No |
    | `GET` | `/ubication/province/list/` | Retrieves a complete list of all provinces in the database. | No |
    | `GET` | `/ubication/province/name/<str:name>/` | Retrieves the province details that match the name specified in the URL. | No |
    | `GET` | `/ubication/province/country/<str:country_name>/` | Retrieves all provinces associated with the country name specified in the URL. | No |
    | `GET` | `/ubication/city/list/` | Retrieves a complete list of all cities in the database. | No |
    | `GET` | `/ubication/city/name/<str:name>/` | Retrieves the city details that match the name specified in the URL. | No |
    | `GET` | `/ubication/city/province/<str:province_name>/` | Retrieves all cities associated with the province name specified in the URL. | No |
    | `GET` | `/ubication/address/list/` | Retrieves a complete list of all adresses in the database | No |
    | `GET` | `/ubication/address/street/<str:street>/` | Retrives the address details that match the street specified in the URL. | No |
    | `GET` | `/ubication/address/city/<str:city_name>/` | Retrives all adresses associated with the city name specified in the URL. | No |
    | `POST`| `/ubication/address/create/` | Creates a new address record associated with a specific city. | No |
    | `PUT`| `/ubication/address/update/<int:id>/` | Updates an existing address record matching the specified ID. | No |
    
* **People Module**:
    | Method | Endpoint | Description | Auth Required |
    | :--- | :--- | :--- | :---: |
    | `GET` | `/person/document/type/list/` | Retrieves a complete list of all document types in the database. | No |
    | `GET` | `/person/document/type/name/<str:name>/` | Retrieves the document type details that match the name specified in the URL. | No |
    | `GET` | `/person/genre/list/` | Retrieves a complete list of all genres in the database. | No |
    | `GET` | `/person/genre/name/<str:name>/` | Retrieves the genre details that match the name specified in the URL. | No |
    | `GET` | `/person/list/` | Retrieves a complete list of all registered people in the database. | No |
    | `GET` | `/person/name/<str:last_name>/` | Retrieves all people matching the last name specified in the URL. | No |
    | `GET` | `/person/document/<str:document_number>/` | Retrieves the details of a person matching the specified document number. | No |
    | `POST` | `/person/create/` | Registers a new person record with their identification data. | No |
    | `PUT` | `/person/update/<int:id>/` | Updates an existing person record matching the specified ID. | No |

* **Users Module**:
    | Method | Endpoint | Description | Auth Required |
    | :--- | :--- | :--- | :---: |
    | `GET` | `/user/list/` | Retrieves a list of all system users. | Yes (Admin) |
    | `GET` | `/username/<str:username>/` | Retrieves user account detailed information by username. | No |
    | `GET` | `/email/<str:email>/` | Retrieves user account detailed information by email. | No |
    | `POST` | `/login/` | Authenticates user credentials and returns a secure access token. | No |
    | `POST` | `/register/` | Registers a new user account linked to role and personal information. | No |
    | `PUT` | `/update/<int:id>/` | Modifies an existing user's data matching the specified ID. | No |
    | `PATCH` | `/delete/<int:id>/` | Performs a logical deactivation of a user profile. | No |
    | `PATCH` | `/recover/<str:email>/` | Re-enables a previously deactivated account logically. | No |
    | `PATCH` | `/recover/password/<int:id>/` | Resets and updates the account password for the given user ID. | No |
    | `POST` | `/email/reset/password/<str:username>/<str:email>/` | Triggers a secure, automated link to recover password using a unique token. | No |
    | `POST` | `/email/reactivation/user/<str:username>/<str:email>/` | Triggers a secure email containing an activation link to reactivate a user account. | No |

### 📄 Detailed Specifications

---

#### 🗺️ Country Endpoints

##### 1. Get all countries
* **URL:** `/ubication/country/list/`
* **Method:** `GET`
* **Success Response (200 OK):**
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
* **Error Response (404 Not Found):**
```json
    {
        "error": "NotFound",
        "message": "Country not found"
    }
    ```

##### 2. Get country by name
* **URL:** `/ubication/country/name/<str:name>/`
* **Method:** `GET`
* **URL Params:** `name=[string]` (e.g., `Argentina`)
* **Success Response (200 OK):**
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
* **Error Response (400 Bad Request):**
```json
    {
        "error": "ValidationError",
        "message": "The country name is required in the URL."
    }
    ```
* **Error Response (404 Not Found):**
```json
    {
        "error": "NotFound",
        "message": "Country not found"
    }
    ```

---

#### 🏛️ Province Endpoints

##### 3. Get all provinces
* **URL:** `/ubication/province/list/`
* **Method:** `GET`
* **Success Response (200 OK):**
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
* **Error Response (404 Not Found):**
```json
    {
        "error": "NotFound",
        "message": "Provinces not found"
    }
    ```
            
##### 4. Get province by name
* **URL:** `/ubication/province/name/<str:name>/`
* **Method:** `GET`
* **URL Params:** `name=[string]` (e.g., `Cordoba`)
* **Success Response (200 OK):**
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
* **Error Response (400 Bad Request):**
```json
    {
        "error": "ValidationError",
        "message": "The province name is required in the URL."
    }
    ```
* **Error Response (404 Not Found):**
```json
    {
        "error": "NotFound",
        "message": "province not found"
    }
    ```
         
##### 5. Get provinces by country name
* **URL:** `/ubication/province/country/<str:country_name>/`
* **Method:** `GET`
* **URL Params:** `country_name=[string]` (e.g., `Argentina`)
* **Success Response (200 OK):**
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

#### 🏙️ City Endpoints

##### 6. Get all cities
* **URL:** `/ubication/city/list/`
* **Method:** `GET`
* **Success Response (200 OK):**
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
* **Error Response (404 Not Found):**
```json
    {
        "error": "NotFound",
        "message": "City not found"
    }
    ```

##### 7. Get city by name
* **URL:** `/ubication/city/name/<str:name>/`
* **Method:** `GET`
* **URL Params:** `name=[string]` (e.g., `Cordoba`)
* **Success Response (200 OK):**
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
* **Error Response (400 Bad Request):**
```json
    {
        "error": "ValidationError",
        "message": "The city name is required in the URL."
    }
    ```
* **Error Response (404 Not Found):**
```json
    {
        "error": "NotFound",
        "message": "City not found"
    }
    ```

##### 8. Get cities by province name
* **URL:** `/ubication/city/province/<str:province_name>/`
* **Method:** `GET`
* **URL Params:** `province_name=[string]` (e.g., `Cordoba`)
* **Success Response (200 OK):**
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
* **Error Response (400 Bad Request):**
```json
    {
        "error": "ValidationError",
        "message": "The province name is required in the URL."
    }
    ```
* **Error Response (404 Not Found):**
```json
    {
        "error": "NotFound",
        "message": "Province not found"
    }
    ```

---

#### 🏠 Address Endpoints

##### 9. Get all adresses
* **URL:** `/ubication/address/list/`
* **Method:** `GET`
* **Success Response (200 OK):**
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
                "comment": "Main home",
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
                "comment": "Main Home",
                "is_apartment": true,
                "city_id": 2687,
                "city_name": "Río Cuarto"
            }
        ]
    }
    ```
* **Error Response (404 Not Found):**
```json
    {
        "error": "NotFound",
        "message": "Address not found"
    }
    ```

#### 10. Get address by street
* **URL:** `/ubication/address/street/<str:street>/`
* **Method:** `GET`
* **URL Params:** `street=[string]` (e.g., `Lorem ipsum`)
* **Success Response (200 OK):**
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
                "comment": "Main home",
                "is_apartment": false,
                "city_id": 2687,
                "city_name": "Río Cuarto"
            }
        ]
    }
    ```
* **Error Response (400 Bad Request):**
```json
    {
        "error": "ValidationError",
        "message": "The street name is required in the URL."
    }
    ```
* **Error Response (404 Not Found):**
```json
    {
        "error": "NotFound",
        "message": "Street not found"
    }
    ```

#### 11. Get address by city
* **URL:** `/ubication/address/city/<str:city_name>/`
* **Method:** `GET`
* **URL Params:** `city_name=[string]` (e.g., `Río Cuarto`)
* **Success Response (200 OK):**
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
                "comment": "Main home",
                "is_apartment": false,
                "city_id": 2687,
                "city_name": "Río Cuarto"
            }
        ]
    }
    ```
* **Error Response (400 Bad Request):**
```json
    {
        "error": "ValidationError",
        "message": "The city name is required in the URL."
    }
    ```
* **Error Response (404 Not Found):**
```json
    {
        "error": "NotFound",
        "message": "City not found"
    }
    ```

#### 12. Create an address
* **URL:** `/ubication/address/create/`
* **Method:** `POST`
* **Headers:** `Content-Type: application/json`
* **Request Body (JSON):**
```json
    {
        "street_main": "Lorem",
        "street_complement": "Ipsum",
        "street_number": "0000",
        "apartment_number": "",
        "floor": "",
        "comment": "Main Home",
        "is_apartment": false,
        "city_id": 2687
    }
    ```
* **Success Response (201 Created):**
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
            "comment": "Main Home",
            "is_apartment": false,
            "city_id": 2687,
            "city_name": "Río Cuarto"
        }
    }
    ```
* **Error Response (400 Bad Request):**
```json
    {
        "Error": "Sensitive data is missing"
    }
    ```

#### 13. Update an address
* **URL:** `/ubication/address/update/<int:id>/`
* **Method:** `PUT`
* **URL Params:** `id=[integer]` (e.g., `2`)
* **Headers:** `Content-Type: application/json`
* **Request Body (JSON):**
```json
    {
        "street_main": "Lore Lore",
        "street_complement": "Ipsum",
        "street_number": "9000",
        "apartment_number": "1",
        "floor": "2",
        "comment": "Main Home",
        "is_apartment": true,
        "city_id": 2687
    }
    ```
* **Success Response (200 OK):**
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
            "comment": "Main Home",
            "is_apartment": true,
            "city_id": 2687,
            "city_name": "Río Cuarto"
        }
    }
    ```
* **Error Response (400 Bad Request):**
```json
    {
        "Error": "Sensitive data is missing"
    }
    ```
* **Error Response (404 Not Found):**
```json
    {
        "Error": "Address not found"
    }
    ```

---

### 👤 People Endpoints

##### 14. Get all genres
* **URL:** `/person/genre/list/`
* **Method:** `GET`
* **Success Response (200 OK):**
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
* **Error Response (404 Not Found):**
```json
    {
        "error": "NotFound",
        "message": "Genres not found"
    }
    ```

#### 15. Get genre by name
* **URL:** `/person/genre/name/<str:name>/`
* **Method:** `GET`
* **URL Params:** `name=[string]` (e.g., `Female`)
* **Success Response (200 OK):**
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
* **Error Response (400 Bad Request):**
```json
    {
        "error": "ValidationError",
        "message": "The genre name is required in the URL."
    }
    ```
* **Error Response (404 Not Found):**
```json
    {
        "error": "NotFound",
        "message": "Genre not found"
    }
    ```

##### 16. Get all document type
* **URL:** `/person/document/type/list/`
* **Method:** `GET`
* **Success Response (200 OK):**
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
* **Error Response (404 Not Found):**
```json
    {
        "error": "NotFound",
        "message": "Document Types not found"
    }
    ```

#### 17. Get document type by name
* **URL:** `/person/document/type/name/<str:name>/`
* **Method:** `GET`
* **URL Params:** `name=[string]` (e.g., `DNI`)
* **Success Response (200 OK):**
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

#### 18. Get all people
* **URL:** `/person/list/`
* **Method:** `GET`
* **Success Response (200 OK):**
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

#### 19. Get people by last name
* **URL:** `/person/name/<str:last_name>/`
* **Method:** `GET`
* **URL Params:** `last_name=[string]` (e.g., `Doe`)
* **Success Response (200 OK):**
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

#### 20. Create a person
* **URL:** `/person/create/`
* **Method:** `POST`
* **Headers:** `Content-Type: application/json`
* **Request Body (JSON):**
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

#### 🔒 Users Endpoints

##### 21. Trigger Password Reset Email
* **URL:** `/email/reset/password/<str:username>/<str:email>/`
* **Method:** `POST`
* **URL Params:** `username=[string]`, `email=[string]`
* **Success Response (200 OK):**
```json
    {
        "message": "The email recover was successfully sent."
    }
    ```
* **Error Response (400 Bad Request):**
```json
    {
        "error": "BadRequest",
        "message": "We were unable to send the recovery email"
    }
    ```

##### 22. User Login (JWT Generation)
* **URL:** `/login/`
* **Method:** `POST`
* **Request Body (JSON):**
```json
    {
        "username": "thomas",
        "password": "secure_password"
    }
    ```
* **Success Response (200 OK):**
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

##### 23. Logical User Deactivation
* **URL:** `/delete/<int:id>/`
* **Method:** `PATCH`
* **URL Params:** `id=[integer]` (e.g., `1`)
* **Success Response (200 OK):**
```json
    {
        "message": "The user was successfully deactivated."
    }
    ```

---

### 🛠️ Tech Stack & Architecture

* **Backend Framework**: Django & Django REST Framework (DRF)
* **Authentication**: Simple JWT & Secure Token Generator (`secrets` module)
* **Database**: PostgreSQL (Hosted on Neon Tech)
* **Environment & Deployment**: Docker & Docker Compose

### 📁 Database Architecture

* **Users & Profiles**: Custom User models managing both Complex Administrators and Player profiles.
* **Bookings**: Handling Fields, hourly rates, reservations, and payment statuses.
* **Tournaments (Cups)**: Managing Tournaments, Teams, Matchmaking Brackets, and Knockout Stages.
* **Analytics**: Tracking Match Statistics, Goals, Cards, and Player Performance History.

### 👤 Creator

* **Thomas Elser Bratik** – *Junior Fullstack Developer* – [@tom1mvp](https://github.com/tom1mvp)

---
*Let's connect! If you have any suggestions or want to know more about the development of SF-5, feel free to check out my profile.*