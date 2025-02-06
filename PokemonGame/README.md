

```mermaid
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

%% Admin Flow Diagram
flowchart TD
    A(Open_App) --> B(Dashboard)
    B --> C(Approve_User_Submitted_Cards)
    C --> D(Select_Cards_Tab)
    D --> E(Cards_Screen)
    E --> F(Modify_and_Delete_Existing_Cards)
    F --> G(Logout)
