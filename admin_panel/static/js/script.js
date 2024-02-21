// Pobierz dane z bazy danych jako jeden string, gdzie pola są oddzielone przez #splx#
// var daneZBazyDanych = "Alucobond: Lustrzane Odbicie Natury: Dom Lustrzany, o powierzchni 400 m² na dwóch kondygnacjach, opiera się na dwóch bryłach, które płynnie łączą się poziomo. Elewacja dolnej części, niemal w całości pokryta alucobondem - aluminiową płytą kompozytową, nadaje budynkowi charakter lustra. Marcin Tomaszewski, opowiadając o swoim projekcie, podkreśla zalety alucobondu, który imituje lustro, zachowując jednocześnie trwałość i wytrzymałość.#splx#Zanurzenie w Naturze: Alucobond sprawia, że dom staje się niemal niewidoczny, odbijając otaczający las i zlewając się z przyrodą. Biała bryła piętra zdaje się unosić w powietrzu, dzięki czemu granice między budynkiem a naturą stają się nieostrzejsze. To nie tylko dom, ale także interaktywna przestrzeń, gdzie światło i odbicia nadają mu dynamiczną formę.#splx#Trwałość i Niski Wymiar Utrzymania: Alucobond, jako materiał niezwykle twardy i trwały, nie wymaga regularnych odnawiania ani odświeżania. Prosta pielęgnacja, polegająca na umyciu powierzchni czystą wodą, sprawia, że budynek zachowuje swoją estetykę na długie lata.";

// Rozdziel dane na tablicę używając separatora #splx#
// var pola_listy = daneZBazyDanych.split("#splx#");

// Funkcja do dodawania pól do formularza
function addListFields(daneZBazyDanych, id, sep) {
    var pola_listy = daneZBazyDanych.split(sep); // przeniesione z poza ciała funkcji
    // Iteruj przez pola_listy
    pola_listy.forEach(function(value) {
        // Tworzymy nowy element textarea
        var inputElement = document.createElement("textarea");
        inputElement.name = "dynamicField"+id; // Nazwa pola, którą możesz obsłużyć po stronie serwera
        inputElement.value = value; // Ustaw wartość z pola_listy

        // Ustaw style dla textarea
        inputElement.className = "form-control bg-dark formatuj-maly-font";
        inputElement.style.color = "#6d6d6d";
        inputElement.style.border = "#6a6a6a solid 1px";
        inputElement.id = "additionalList" + id;
        inputElement.rows = "4";
        inputElement.required = true;

        // Tworzymy nowy element div, który zawiera textarea i przycisk usuwania
        var listItem = document.createElement("div");
        listItem.className = "no-border formatuj-margin form-control bg-dark formatuj-right";
        listItem.appendChild(inputElement);

        // Przycisk usuwania
        var removeButton = document.createElement("button");
        removeButton.textContent = "Usuń pole";
        removeButton.type = "button";
        removeButton.className = "btn btn-outline-danger formatuj-maly-font formatuj-margin"
        inputElement.style.marginTop = "10px";
        removeButton.onclick = function() {
        listItem.remove();
        };

        listItem.appendChild(removeButton);

        // Dodajemy nowy element listy do kontenera
        // document.getElementById("list-container" + id).appendChild(listItem);
        var listContainer = document.getElementById("list-container" + id);

        if (listContainer) {
            listContainer.appendChild(listItem);
        } else {
            console.error("Element o identyfikatorze 'list-container" + id + "' nie istnieje.");
        }
    });
}

// Funkcja do dodawania nowego pola do listy
function addListItem(id) {
    // Tworzymy nowy element textarea
    var textareaElement = document.createElement("textarea");
    textareaElement.name = "dynamicField"+id; // Nazwa pola, którą możesz obsłużyć po stronie serwera

    // Ustaw style dla textarea
    textareaElement.className = "form-control bg-dark formatuj-maly-font";
    textareaElement.style.color = "#6d6d6d";
    textareaElement.style.border = "#6a6a6a solid 1px";
    textareaElement.id = "additionalList";
    textareaElement.rows = "4";
    textareaElement.required = true;

    // Tworzymy nowy element div, który zawiera textarea i przycisk usuwania
    var listItem = document.createElement("div");
    listItem.className = "no-border formatuj-margin form-control bg-dark formatuj-right";
    listItem.appendChild(textareaElement);

    // Przycisk usuwania
    var removeButton = document.createElement("button");
    removeButton.textContent = "Usuń pole";
    removeButton.type = "button";
    removeButton.className = "btn btn-outline-danger formatuj-maly-font formatuj-margin";
    removeButton.onclick = function() {
        listItem.remove();
    };

    listItem.appendChild(removeButton);

    // Dodajemy nowy element listy do kontenera
    document.getElementById("list-container"+id).appendChild(listItem);
}

// Funkcja do złączania zawartości pól listy w jeden string
function joinListFields(id, sep) {
    var inputElements = document.getElementsByName("dynamicField"+id);
    var values = [];

    // Iteruj przez wszystkie elementy input i dodaj ich wartości do tablicy
    for (var i = 0; i < inputElements.length; i++) {
        values.push(inputElements[i].value);
    }

    // Złącz tablicę w jeden string używając separatora #splx#
    var resultString = values.join(sep);

    // Wyświetl wynik w konsoli (możesz zmienić to na zapis do bazy danych)
    console.log(resultString);
}

// Przykład wywołania funkcji joinListFields
// Możesz umieścić to w odpowiednim miejscu w kodzie, np. po wciśnięciu przycisku "Zapisz"
// joinListFields();