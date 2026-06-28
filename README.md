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
• **Players & Stats**: This module handles all operations related to soccer players, managing their physical attributes, positioning, team associations, and comprehensive historical match performance analytics.
    
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
    | `GET` | `/auth/user/list/` | Retrieves a list of all system users. | Yes (Admin) |
    | `GET` | `/auth/username/<str:username>` | Retrieves user account detailed information by username. | No |
    | `GET` | `/auth/email/<str:email>` | Retrieves user account detailed information by email. | No |
    | `POST` | `/auth/login/` | Authenticates user credentials and returns a secure access token. | No |
    | `POST` | `/auth/register/` | Registers a new user account linked to role and personal information. | No |
    | `PUT` | `/auth/update/<int:id>` | Modifies an existing user's data matching the specified ID. | No |
    | `PATCH` | `/auth/delete/<int:id>` | Performs a logical deactivation of a user profile. | No |
    | `PATCH` | `/auth/recover/<str:email>` | Re-enables a previously deactivated account logically. | No |
    | `PATCH` | `/auth/recover/password/<int:id>` | Resets and updates the account password for the given user ID. | No |
    | `POST` | `/auth/email/reset/password/<str:username>/<str:email>` | Triggers a secure, automated link to recover password using a unique token. | No |
    | `POST` | `/auth/email/reactivation/user/<str:username>/<str:email>` | Triggers a secure email containing an activation link to reactivate a user account. | No |

• **Players & Stats Module**:
    | Method | Endpoint | Description | Auth Required |
    | :--- | :--- | :--- | :---: |
    | `GET` | `/player/list/` | Retrieves a complete list of all registered players with their user and personal details. | No |
    | `GET` | `/player/username/<str:username>/` | Retrieves player detailed profile information matching the specified username. | No |
    | `POST` | `/player/create/` | Registers a new player profile linked to an existing system user ID. | No |
    | `PUT` | `/player/update/<int:id>/` | Modifies physical and tactical data for an existing player profile matching the ID. | No |
    | `GET` | `/player/stat/list/` | Retrieves a global list of historical performance statistics for all players. | No |
    | `GET` | `/player/stat/nickname/<str:nickname>/` | Retrieves performance metrics using the unique player nickname specified in the URL. | No |
    | `GET` | `/player/stat/id/<int:id>/` | Retrieves performance metrics matching the specific player ID. | No |
    | `POST` | `/player/stat/create/` | Initializes a statistics tracker record for a specific player profile. | No |
    | `PUT` | `/player/stat/update/<int:id>/` | Updates match history records (goals, cards, MVPs) for a given stat ID. | No |

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
            },
            {
                "id": 3,
                name: "Other"
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
* **Error Response (400 Bad Request):**
```json
    {
        "error": "ValidationError",
        "message": "The document type name is required in the URL."
    }
    ```
* **Error Response (404 Not Found):**
```json
    {
        "error": "NotFound",
        "message": "Document type not found"
    }

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
* **Error Response (404 Not Found):**
```json
    {
        "error": "NotFound",
        "message": "People not found"
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
* **Error Response (400 Bad Request):**
```json
    {
        "error": "ValidationError",
        "message": "The last name is required in the URL."
    }
    ```
* **Error Response (404 Not Found):**
```json
    {
        "error": "NotFound",
        "message": "Last name not found"
    }

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
* **Success Response (200 OK):**
```json
    {
        "message": "The person has been created successfully.",
        "data": {
            "id": 7,
            "first_name": "Jane",
            "last_name": "Casas",
            "document_number": "42900761",
            "document_type_name": "DNI",
            "phone_number": "5559876543",
            "email": "janesmith@example.com",
            "genre_name": "Female",
            "address_street": "Avenida italia",
            "address_street_number": "4500",
            "date_birth": "1992-10-10",
            "creation_date": "2026-06-23T11:17:57.787377Z"
        }
    }
```
* **Error Response (400 Bad Request):**
```json
    {
        "Error": "Sensitive data is missing"
    }
```

#### 21. Update a person
* **URL:** `/person/update/<int:id>`
**Method:** `PUT`
* **URL Params:** `id=[integer]` (e.g., `2`)
* **Headers:** `Content-Type: application/json`
* **Request Body (JSON):**
```json
    {
        "first_name": "Jane",
        "last_name": "Smith",
        "document_number": "87654321",
        "birth_date": "1992-10-10",
        "phone": "5551239876",
        "email": "jane.smith.updated@example.com",
        "document_type_id": 1,
        "genre_id": 2,
        "address_id": 5
    }
```
* **Success Response (200 OK):**
```json
   {
        "Message": "The person has been successfully updated",
        "data": {
            "id": 7,
            "first_name": "Jane",
            "last_name": "Smith",
            "document_number": "87654321",
            "document_type_name": "DNI",
            "phone_number": "5551239876",
            "email": "jane.smith.updated@example.com",
            "genre_name": "Female",
            "address_street": "Avenida italia",
            "address_street_number": "4500",
            "date_birth": "1992-10-10",
            "creation_date": "2026-06-23T11:17:57.787377Z"
        }
    }
```
* **Error Response (400 Bad Request):**
```json
    {
        "Error": "Sensitive data is missing"
    }
```

---

### 🔒 Users Endpoints

#### 22. Get all users
* **URL:** `/auth/user/list/`
* **Method:** `GET`
* **Success Response (200 OK):**
```json
{
    "data": [
        {
            "id": 1,
            "username": "jane_smith92",
            "role_name": "Admin",
            "person_id": 7,
            "first_name": "Jane",
            "last_name": "Smith",
            "document_number": "87654321",
            "email": "jane.smith.updated@example.com",
            "phone_number": "5551239876"
        },
        {
            "id": 2,
            "username": "JhonSmith",
            "role_name": "Player",
            "person_id": 8,
            "first_name": "Jhon Williams",
            "last_name": "Smith",
            "document_number": "42900761",
            "email": "JhonSmith@jhon.com",
            "phone_number": "8865268993"
        }
    ]
}
```
* **Error Response (404 Not Found):**
```json
    {
        "error": "NotFound",
        "message": "Users not found"
    }
```

#### 23. Get user by username
* **URL:** `/auth/username/<str:username>`
* **Method:** `GET`
* **URL Params:** `username=[string]` (e.g., `jane_smith92`)
* **Success Response (200 OK):**
```json
    {
        "data": {
            "id": 1,
            "username": "jane_smith92",
            "role_name": "Admin",
            "person_id": 7,
            "first_name": "Jane",
            "last_name": "Smith",
            "document_number": "87654321",
            "email": "jane.smith.updated@example.com",
            "phone_number": "5551239876"
        }
    }
```
* **Error Response (400 Bad Request):**
```json
    {
        "error": "ValidationError",
        "message": "The username is required in the URL."
    }
```
* **Error Response (404 Not Found):**
```json
    {
        "error": "NotFound",
        "message": "Username not found"
    }
```
#### 24. Get user by email
* **URL:** `/auth/email/<str:email>`
* **Method:** `GET`
* **URL Params:** `email=[string]` (e.g., `jane.smith.updated@example.com`)
* **Success Response (200 OK):**
```json
{
    "data": {
        "id": 1,
        "username": "jane_smith92",
        "role_name": "Admin",
        "person_id": 7,
        "first_name": "Jane",
        "last_name": "Smith",
        "document_number": "87654321",
        "email": "jane.smith.updated@example.com",
        "phone_number": "5551239876"
    }
}
```
* **Error Response (400 Bad Request):**
```json
    {
        "error": "ValidationError",
        "message": "The email is required in the URL."
    }
```
* **Error Response (404 Not Found):**
```json
    {
        "error": "NotFound",
        "message": "Email not found"
    }
```
#### 25. Login
* **URL:** `/auth/login/`
* **Method:** `POST`
* **Headers:** `Content-Type: application/json`
* **Request Body (JSON):**
```json
    {
        "username": "jane_smith92",
        "password": "fictitiousPassword1234"
    }
```
* **Success Response (200 OK):**
```json
    {
        "Message": "Welcome, user",
        "data": {
            "id": 1,
            "username": "jane_smith92",
            "role_name": "Admin",
            "person_id": 7,
            "first_name": "Jane",
            "last_name": "Smith",
            "document_number": "87654321",
            "email": "jane.smith.updated@example.com",
            "phone_number": "5551239876"
        },
        "Token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzgxODc1ODg0LCJpYXQiOjE3ODE4NzU1ODQsImp0aSI6IjUxZDY0Y2E0YTRmNzRhYTBhZjYyZWIzNzJkNmQ3MDNmIiwidXNlcl9pZCI6IjIifQ.Lu3607AE1QrrXSeecwpkyPZJFIvMnq-SLlcZoFtl_04"
}
```
* **Error Response (400 Bad Request):**
```json
    {
        "Error": "Sensitive data is missing"
    }
```

#### 26. Register
* **URL:** `/auth/register/`
* **Method:** `POST`
* **Headers:** `Content-Type: application/json`
* **Request Body (JSON):**
```json
{
    "username": "jane_smith92",
    "password": "fictitiousPassword1234",
    "confirm_password": "fictitiousPassword1234",
    "first_name": "Jane",
    "last_name": "Smith",
    "document_number": "87654321",
    "birth_date": "1992-10-10",
    "phone": "5551239876",
    "email": "jane.smith.updated@example.com",
    "document_type_id": 1,
    "genre_id": 2,
    "address_id": 5
}
```

#### 27. Update user
* **URL:** `/auth/update/<int:id>`
**Method:** `PUT`
* **URL Params:** `id=[integer]` (e.g., `2`)
* **Headers:** `Content-Type: application/json`
* **Request Body (JSON):**
```json
{
    "username": "jane_smith92",
    "password": "NewPassword2026*",
    "first_name": "Jane",
    "last_name": "Smith",
    "document_number": "87654321",
    "birth_date": "1992-10-10",
    "phone": "3584999999",
    "email": "jane.smith.nueva@example.com",
    "document_type_id": 1,
    "genre_id": 2,
    "address_id": 5
}
```
* **Success Response (200 OK):**
```json
{
    "Message": "The user has been successfully updated",
    "data": {
        "id": 1,
        "username": "jane_smith92",
        "role_name": "Admin",
        "person_id": 7,
        "first_name": "Jane",
        "last_name": "Smith",
        "document_number": "87654321",
        "email": "jane.smith.nueva@example.com",
        "phone_number": "3584999999"
    }
}
```
* **Error Response (400 Bad Request):**
```json
    {
        "Error": "Sensitive data is missing"
    }
```

##### 28. Delete user (soft)
* **URL:** `/auth/delete/<int:id>`
* **Method:** `PATCH`
* **URL Params:** `id=[integer]` (e.g., `2`)
* **Success Response (200 OK):**
```json
    {
        "Message": "The user has been successfully deactivated."
    }
```

##### 29. Recover user
* **URL:** `/auth/recover/<int:id>`
* **Method:** `PATCH`
* **URL Params:** `id=[integer]` (e.g., `2`)
* **Success Response (200 OK):**
```json
    {
        "Message": "The user has been successfully recovered."
    }
```

##### 29. Recover password
* **URL:** `/auth/password/recover/<int:id>`
* **Method:** `PATCH`
* **URL Params:** `id=[integer]` (e.g., `2`)
* **Request Body (JSON):**
```json
    {
        "password": "newpasswordsecret123",
        "confirm_password": "newpasswordsecret123"
    }
```
* **Success Response (200 OK):**
```json
    {
        "Message": "The password was successfully recovered."
    }
```
* **Error Response (400 Bad Request):**
```json
    {
        "Error": "Sensitive data is missing"
    }
```

##### 30. Send email recover password
* **URL:** `/auth/email/reset/password/<str:username>/<str:email>/`
* **Method:** `POST`
* **URL Params:** `username=[string]` (e.g., `jane_smith92`), `email=[string]` (e.g., `jane.smith.nueva@example.com`)
* **Success Response (200 OK):** 
```json
    {
        "message": "The email recover was successfully sender."
    }
```
* **Error Response (400 Bad Request):**
```json
    {
        "error": "BadRequest",
        "message": "We were unable to send the recovery email"
    }
```

##### 31. Send email reactive user
* **URL:** `/auth/email/reactivation/user/<str:username>/<str:email>`
* **Method:** `POST`
* **URL Params:** `username=[string]` (e.g., `jane_smith92`), `email=[string]` (e.g., `jane.smith.nueva@example.com`)
* **Success Response (200 OK):** 
```json
    {
        "message": "The email recover was successfully sender."
    }
```
* **Error Response (400 Bad Request):**
```json
    {
        "error": "BadRequest",
        "message": "We were unable to send the recovery email"
    }
```

### 🏃‍♂️ Player Endpoints

#### 32. Get all players
* **URL:** `/player/list/`
* **Method:** `GET`
* **Success Response (200 OK):**
```json
    {
        "data": [
            {
                "id": 1,
                "user_id": 2,
                "first_name": "John",
                "last_name": "Doe",
                "profile_picture": null,
                "jersey_number": "10",
                "position": "Foo",
                "preferred_foot": "Bar",
                "weight": "70.00",
                "height": "1.75",
                "nickname": "Dummy1"
            },
            {
                "id": 2,
                "user_id": 3,
                "first_name": "Jane",
                "last_name": "Doe",
                "profile_picture": null,
                "jersey_number": "2",
                "position": "Baz",
                "preferred_foot": "Qux",
                "weight": "65.00",
                "height": "1.68",
                "nickname": "Dummy2"
            },
            {
                "id": 3,
                "user_id": 4,
                "first_name": "Alice",
                "last_name": "Smith",
                "profile_picture": null,
                "jersey_number": "12",
                "position": "FooBar",
                "preferred_foot": "Bar",
                "weight": "60.00",
                "height": "1.70",
                "nickname": "Dummy3"
            },
            {
                "id": 4,
                "user_id": 5,
                "first_name": "Bob",
                "last_name": "Johnson",
                "profile_picture": null,
                "jersey_number": "8",
                "position": "Test",
                "preferred_foot": "Qux",
                "weight": "80.00",
                "height": "1.82",
                "nickname": "Dummy4"
            },
            {
                "id": 5,
                "user_id": 6,
                "first_name": "Eve",
                "last_name": "Brown",
                "profile_picture": null,
                "jersey_number": "7",
                "position": "Example",
                "preferred_foot": "Baz",
                "weight": "55.00",
                "height": "1.60",
                "nickname": "Dummy5"
            }
    ]
}
```
* **Error Response (404 Not Found):**
```json
    {
        "error": "NotFound",
        "message": "Players not found"
    }
```

#### 33. Get user by username
* **URL:** `/player/username/<str:username>`
* **Method:** `GET`
* **URL Params:** `username=[string]` (e.g., `jane_smith92`)
* **Success Response (200 OK):**
```json
    {
        "data": [
            {
                "id": 2,
                "user_id": 3,
                "first_name": "Jhon Alexis",
                "last_name": "Doe",
                "profile_picture": null,
                "jersey_number": "2",
                "position": "Central derecho",
                "preferred_foot": "Derecho",
                "weight": "80.00",
                "height": "1.75",
                "nickname": "Jhon"
            }
        ]
    }
```
* **Error Response (400 Bad Request):**
```json
    {
        "error": "ValidationError",
        "message": "The username is required in the URL."
    }
```
* **Error Response (404 Not Found):**
```json
    {
        "error": "NotFound",
        "message": "Username not found"
    }
```

#### 34. Create player
* **URL:** `/player/create/`
* **Method:** `POST`
* **Headers:** `Content-Type: application/json`
* **Request Body (JSON):**
```json
    {
        "jersey_number": "10",
        "position": "Left Winger",
        "prefed_foot": "Left-footed",
        "weight": 60.00,
        "height": 1.52,
        "nickname": "JhonDoe",
        "user_id": 5
    }
```
* **Success Response (200 OK):**
```json
    {
        "message": "The player has been created successfully.",
        "data": [
            "jersey_number": "10",
            "position": "Left Winger",
            "prefed_foot": "Left-footed",
            "weight": 60.00,
            "height": 1.52,
            "nickname": "JhonDoe",
            "user_id": 5
        ]
    }
```
* **Error Response (400 Bad Request):**
```json
    {
        "Error": "Sensitive data is missing"
    }
```

#### 35. Update player
* **URL:** `/player/update/<int:id>`
* **Method:** `PUT`
* **URL Params:** `id=[integer]` (e.g., `2`)
* **Headers:** `Content-Type: application/json`
* **Request Body (JSON):**
```json
    {
        "jersey_number": "12",
        "position": "Left Winger",
        "prefed_foot": "Left-footed",
        "weight": 60.00,
        "height": 1.52,
        "nickname": "JhonDoe",
        "user_id": 5
    }
```
* **Success Response (200 OK):**
```json
    {
        "message": "The player has been updated successfully.",
        "data": [
            "jersey_number": "12",
            "position": "Left Winger",
            "prefed_foot": "Left-footed",
            "weight": 60.00,
            "height": 1.52,
            "nickname": "JhonDoe",
            "user_id": 5
        ]
    }
```
* **Error Response (400 Bad Request):**
```json
    {
        "Error": "Sensitive data is missing"
    }
```

### 📈 Player Stat Endpoints

#### 36. Get all stats
* **URL:** `/player/stat/list/`
* **Method:** `GET`
* **Success Response (200 OK):**
```json
    {
        "data": [
            {
                "id": 1,
                "player_id": 1,
                "nickname": "Foo",
                "goals": 3,
                "assists": 1,
                "matches_played": 5,
                "yellow_cards": 0,
                "red_cards": 0,
                "total_mvps": 1
            },
            {
                "id": 2,
                "player_id": 2,
                "nickname": "Bar",
                "goals": 0,
                "assists": 4,
                "matches_played": 8,
                "yellow_cards": 2,
                "red_cards": 0,
                "total_mvps": 0
            },
            {
                "id": 3,
                "player_id": 3,
                "nickname": "Baz",
                "goals": 6,
                "assists": 2,
                "matches_played": 12,
                "yellow_cards": 1,
                "red_cards": 1,
                "total_mvps": 2
            },
            {
                "id": 4,
                "player_id": 4,
                "nickname": "Qux",
                "goals": 1,
                "assists": 0,
                "matches_played": 3,
                "yellow_cards": 0,
                "red_cards": 0,
                "total_mvps": 0
            },
            {
                "id": 5,
                "player_id": 5,
                "nickname": "Dummy",
                "goals": 2,
                "assists": 2,
                "matches_played": 4,
                "yellow_cards": 1,
                "red_cards": 0,
                "total_mvps": 0
            }
        ]
    }
```
* **Error Response (404 Not Found):**
```json
    {
        "error": "NotFound",
        "message": "Player stats not found"
    }
```

#### 37. Get stat by nickname
* **URL:** `/player/stat/nickname/<str:nickname>`
* **Method:** `GET`
* **URL Params:** `nickname=[string]` (e.g., `Dummy`)
* **Success Response (200 OK):**
```json
    {
        "id": 5,
        "player_id": 5,
        "nickname": "Dummy",
        "goals": 2,
        "assists": 2,
        "matches_played": 4,
        "yellow_cards": 1,
        "red_cards": 0,
        "total_mvps": 0
    }
```
* **Error Response (400 Bad Request):**
```json
    {
        "error": "ValidationError",
        "message": "The nickname is required in the URL."
    }
```
* **Error Response (404 Not Found):**
```json
    {
        "error": "NotFound",
        "message": "Nickname not found"
    }
```

#### 38. Get stat by ID
* **URL:** `/player/stat/id/<int:id>`
* **Method:** `GET`
* **URL Params:** `id=[integer]` (e.g., `5`)
* **Success Response (200 OK):**
```json
    {
        "id": 5,
        "player_id": 5,
        "nickname": "Dummy",
        "goals": 2,
        "assists": 2,
        "matches_played": 4,
        "yellow_cards": 1,
        "red_cards": 0,
        "total_mvps": 0
    }
```
* **Error Response (400 Bad Request):**
```json
    {
        "error": "ValidationError",
        "message": "The player ID is required in the URL."
    }
```
* **Error Response (404 Not Found):**
```json
    {
        "error": "NotFound",
        "message": "Player not found"
    }
```

#### 39. Create stat
* **URL:** `/player/stat/create/`
* **Method:** `POST`
* **Headers:** `Content-Type: application/json`
* **Request Body (JSON):**
```json
    {
        "goals": 2,
        "assists": 0,
        "matches_played": 4,
        "yellow_cards": 0,
        "red_cards": 0,
        "total_mvps": 0,
        "player_id": 1
    }
```
* **Success Response (200 OK):**
```json
    {
        "message": "The player has been created successfully.",
        "data": {
            "id": 5,
            "player_id": 1,
            "nickname": "JoeDo",
            "goals": 2,
            "assists": 0,
            "matches_played": 4,
            "yellow_cards": 0,
            "red_cards": 0,
            "total_mvps": 0
        }
    }
```
* **Error Response (400 Bad Request):**
```json
    {
        "Error": "Sensitive data is missing"
    }
```

#### 40. Update stat
* **URL:** `/player/stat/update/<int:id>`
* **Method:** `PUT`
* **URL Params:** `id=[integer]` (e.g., `2`)
* **Headers:** `Content-Type: application/json`
* **Request Body (JSON):**
```json
    {
        "goals": 1,
        "assists": 1,
        "matches_played": 1,
        "yellow_cards": 0,
        "red_cards": 0,
        "total_mvps": 0
    }
```
* **Success Response (200 OK):**
```json
    {
        "message": "The player stat has been updated successfully.",
        "data": [
            "id": 5,
            "player_id": 1,
            "nickname": "JoeDo",
            "goals": 1,
            "assists": 1,
            "matches_played": 1,
            "yellow_cards": 0,
            "red_cards": 0,
            "total_mvps": 0
        ]
    }
```
* **Error Response (400 Bad Request):**
```json
    {
        "Error": "Sensitive data is missing"
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