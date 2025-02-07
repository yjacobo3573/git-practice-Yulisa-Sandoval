

```mermaid
---
title: User Flow Diagram for Card Management App
---

%% User Flow Diagram
flowchart TD
    A(Open_App) --> B(Home_Screen)
    B --> C(Select_View_Cards)
    C --> D(View_Cards_Screen)
    D --> E(Select_New_Cards)
    E --> F(New_Cards_Screen)
    F --> G(Submit_New_Cards)
    G --> H(Select_Manage_Deck)
    H --> I(Manage_Deck_Screen)
    I --> J(Assemble_Deck)
    J --> K(Logout)  

```




```mermaid
---
title: Admin Flow Diagram for Card Management App
---
%% Admin Flow Diagram
flowchart TD
    A2(Open_App) --> B2(Dashboard)
    B2 --> C2(Approve_User_Submitted_Cards)
    C2 --> D2(Select_Cards_Tab)
    D2 --> E2(Cards_Screen)
    E2 --> F2(Modify_and_Delete_Existing_Cards)
    F2 --> G2(Logout)
```


```mermaid
---
title: Software Architecture Diagram
---

flowchart TD
    A1[User] --> A[Front-end]
    
    A --> B[Manage decks]
    A --> C[Submit new cards]
    
    A --> D[Backend API]
    
    D --> E[Admin-Dashboard]
    
    E --> F[Delete_Card]
    E --> G[Approve_Card]
    E --> H[Modify_Card]

    E --> I[Backend processes decision]
    
    I --> J[Database]


```
| **Endpoint**                         | **Method** | **Description**                                   | **Authentication** |
|--------------------------------------|-----------|-------------------------------------------------|--------------------|
| `/api/cards`                         | `GET`     | Retrieve all Pokémon cards                      | User               |
| `/api/cards/{id}`                     | `GET`     | Retrieve details of a specific card by ID      | User              |
| `/api/cards/submit`                   | `POST`    | Submit a new Pokémon card for approval         | User               |
| `/api/cards/{id}/approve`             | `PUT`     | Approve a user-submitted card                  | Admin              |
| `/api/cards`                          | `POST`    | Add a new Pokémon card                         | Admin              |
| `/api/cards/{id}`                     | `PUT`     | Modify an existing Pokémon card                | Admin              |
| `/api/cards/{id}`                     | `DELETE`  | Delete a Pokémon card                          | Admin              |
| `/api/decks`                          | `GET`     | Retrieve all decks of the logged-in user       | User               |
| `/api/decks/{id}`                     | `GET`     | Retrieve details of a specific deck           | User               |
| `/api/decks`                          | `POST`    | Create a new deck                             | User               |
| `/api/decks/{id}`                     | `PUT`     | Modify an existing deck                       | User               |
| `/api/decks/{id}`                     | `DELETE`  | Delete a deck                                | User               |
| `/api/decks/{id}/add-card`            | `POST`    | Add a card to a deck                         | User               |
| `/api/decks/{id}/remove-card/{cardId}` | `DELETE`  | Remove a card from a deck                    | User               |
| `/api/auth/login`                     | `POST`    | User logins                                  | Admin               |
| `/api/auth/register`                  | `POST`    | Register a new user                          | Admin               |
| `/api/auth/logout`                    | `POST`    | Logout current session                       | Admin               |

```mermaid
---
title: Software Architecture Diagram
---


erDiagram
    USER {
        int User_ID PK
        string Email
        string Password
        string Role "User, Admin"
    }
    
    CARD {
        int Card_ID PK
        string Name
        string Type
        string Stat_Values
        string Status "Pending, Approved"
    }
    
    DECK {
        int Deck_ID PK
        int User_ID FK
        string Deck_Name
        int Deck_Size
    }

    DECK_CARDS {
        int Deck_ID FK
        int Card_ID FK
    }
    
    PENDING_CARDS {
        int Pending_Card_ID PK
        int Card_ID FK
        int User_ID FK
        date Submission_Date
    }
    
    USER ||--o{ DECK : "has"
    USER ||--o{ PENDING_CARDS : "submits"
    CARD ||--o{ PENDING_CARDS : "is pending"
    CARD ||--o{ DECK_CARDS : "is part of"
    DECK ||--o{ DECK_CARDS : "contains"




```
