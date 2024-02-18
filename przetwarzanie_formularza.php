<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Formularz edycji bloga</title>
    <!-- Dodaj tutaj linki do stylów CSS, jeśli są potrzebne -->
</head>
<body>

<h1>Formularz edycji bloga</h1>

<form action="przetwarzanie_formularza.php" method="post" enctype="multipart/form-data">
    <label for="tytul">Tytuł bloga:</label><br>
    <input type="text" id="tytul" name="tytul" required><br><br>

    <label for="tresc">Treść bloga:</label><br>
    <textarea id="tresc" name="tresc" rows="4" cols="50" required></textarea><br><br>

    <label for="zdjecie">Dodaj zdjęcie:</label><br>
    <input type="file" id="zdjecie" name="zdjecie"><br><br>

    <label for="komentarz">Modyfikuj komentarz:</label><br>
    <textarea id="komentarz" name="komentarz" rows="4" cols="50"></textarea><br><br>

    <input type="submit" value="Zapisz zmiany">
</form>

</body>
</html>
