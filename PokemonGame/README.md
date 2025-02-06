

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

flowchart TD
    A[Front-end] --> B[Barcened]
    A --> C[M1]
    
    D[Main backboard] --> E[Backbone]
    D --> F[Process(s)]
    D --> G[decision]
    
    H[Dontabase] --> I[Module Load]
    H --> J[Module Load]

```
