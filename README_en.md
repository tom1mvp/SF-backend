# 🏆 **SF-5: 5-a-Side Soccer Field Rental & Tournament System (SAAS API)** ⚽

**SF-5** is a comprehensive backend platform designed to modernize how amateur sports complexes operate and how players experience the game. 

Beyond standard field booking, this project delivers a **dynamic ecosystem** that bridges the gap between venue management and player engagement by focusing on three core pillars:

* **Live scheduling:** Tracking real-time field availability.
* **Automated tournament generation:** Handling complex brackets for dynamic cups and knockout stages.
* **Performance analytics:** Delivering detailed statistics for players.

This platform transforms casual matches into a professional, seamless experience for friends competing in dynamic cups and knockout tournaments.

### 📝 Modules
- **Ubication**: This module handles all operations related to geographic locations, including countries, provinces, and cities.
    
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

### 🛠️ Tech Stack & Architecture

* **Backend Framework**: Django & Django REST Framework (DRF)
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