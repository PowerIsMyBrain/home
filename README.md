# Admin Panel

Aplikacja "Admin Panel" stanowi kompleksowe narzędzie do zarządzania wieloma witrynami internetowymi skupionymi pod marką DMD. Została stworzona w oparciu o framework Flask, co pozwala na łatwe dostosowywanie i obsługę. Aplikacja oferuje intuicyjny interfejs użytkownika, umożliwiający administratorom efektywne zarządzanie różnymi aspektami stron. Oto kluczowe funkcje dostępne w panelu:

1. **Strona Główna**:
   - Monitorowanie podstawowych statystyk dotyczących witryny.
   - Dostęp do aktualności i informacji związanych z panelem administracyjnym.

2. **Zarządzanie Użytkownikami (kadrą)**:
   - Dodawanie, edycja i usuwanie kont użytkowników (pracowników).
   - Zarządzanie poziomami uprawnień i rolami użytkowników.

3. **Zarządzanie Blogiem**:
   - Dodawanie nowych wpisów bloga.
   - Edycja i usuwanie istniejących wpisów.
   - Moderowanie komentarzy.

4. **Zarządzanie Newsletterem**:
   - Zarządzanie wysyłką i harmonogramem newsletterów.

5. **Zarządzanie Subskrybentami**:
   - Przeglądanie i zarządzanie listą subskrybentów.
   - Analiza danych subskrybentów i ich preferencji.
   - Moderowanie komentarzy subskrybentów.

6. **Ustawienia**:
   - Dostosowywanie ustawień aplikacji, takich jak konfiguracja SMTP, powiadomienia e-mail, itp.
   - Zarządzanie ustawieniami dostępu i bezpieczeństwa.

## Struktura katalogów aplikacji

admin_panel/
|-- static/
| |-- css/
| | |-- style.css
| |-- js/
| |-- script.js
|-- templates/
| |-- home.html
| |-- user_management.html
| |-- blog_management.html
| |-- newsletter_management.html
| |-- subscriber_management.html
| |-- settings.html
|-- app/
| |-- init.py
| |-- models.py
| |-- routes/
| | |-- init.py
| | |-- home_routes.py
| | |-- user_routes.py
| | |-- blog_routes.py
| | |-- newsletter_routes.py
| | |-- subscriber_routes.py
| | |-- settings_routes.py
| |-- templates/
| | |-- email_templates/
| | |-- newsletter_template.html
| | |-- subscriber_comment_template.html
| | |-- admin_notification_template.html
| |-- static/
| | |-- admin_panel_logo.png
| |-- utils/
| | |-- init.py
| | |-- authentication.py
| | |-- email.py
| | |-- permissions.py
|-- config.py
|-- requirements.txt
|-- run.py
