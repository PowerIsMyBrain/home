<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>ControlPanelDmD</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>
    <style>
        .przyklejone-divy {
            position: fixed; /* Określa, żeby elementy były przyklejone do okna przeglądarki */
            top: 0; /* Określa odległość od góry */
            right: 0; /* Określa, że elementy mają być przylepione do prawej strony */
            width: 40%;
            padding-top: 25px;
        }
        .przyklejddoł-divy {
            position: fixed; /* Określa, żeby elementy były przyklejone do okna przeglądarki */
            bottom: 0; /* Określa odległość od góry */
            left: 0; /* Określa, że elementy mają być przylepione do prawej strony */
            padding: 5px;
            font-size: 12px;
        }

        .pagination {
            padding: auto;
        }
        .mainContainer {
            padding: 25px;
        }
        </style>
</head>
<body>
<script>
    const mapa = true;
</script>
    <div class="mainContainer">
        <!-- Navbar -->
        <div>
        <ul class="nav nav-tabs">
            <li class="nav-item">
                <a class="nav-link active" aria-current="page" href="#">Użytkownicy</a>
            </li>
            <li class="nav-item dropdown">
            <a class="nav-link dropdown-toggle" data-bs-toggle="dropdown" href="#" role="button" aria-expanded="true">Opcje</a>
                <ul class="dropdown-menu">
                    <li><a class="dropdown-item"href="admin_dashboard.php">Strona Główna</a></li>
                    <li><hr class="dropdown-divider"></li>
                    <li><a class="dropdown-item" href="brands.php">Zarządzaj Markami</a></li>
                    <li><a class="dropdown-item" href="users.php">Użytkownicy</a></li>
                    <li><a class="dropdown-item" href="permissions.php">Uprawnienia</a></li>
                    <!-- Dodaj inne strony panelu administracyjnego zgodnie z potrzebami -->
                    <li><a class="dropdown-item" href="blog.php">Blog</a></li>
                    <li><a class="dropdown-item" href="media_gallery.php">Galeria Mediów</a></li>
                    <li><a class="dropdown-item" href="market_trends.php">Trendy Rynkowe</a></li>
                    <li><a class="dropdown-item" href="notifications.php">Powiadomienia</a></li>
                    <li><a class="dropdown-item" href="error_reports.php">Raporty Błędów</a></li>
                    <li><hr class="dropdown-divider"></li>
                    <li><a class="dropdown-item" href="#">Ustawienia</a></li>
                </ul>
            </li>
            

        </ul>
        <div class="przyklejone-divy">
            <p maria-disabled="true">Zalogowany jako Mikael | 
                <span>
                    <button type="button" class="btn btn-secondary btn-sm">Wyloguj się</button>
                </span>
            </p>
        </div>
        </div>
            <!-- Right site -->

    
                <!-- Użytkownicy -->
                <div class="col-2 col-sm-7">
                    <!-- <h3>Użytkownicy</h3> -->
                    <table class="table">
                        <thead>
                          <tr>
                            <th scope="col">#</th>
                            <th scope="col">Nazwa użytkownika</th>
                            <th scope="col">Aktywność</th>
                            <th scope="col">Login</th>
                            <th scope="col"><i class="bi bi-person-gear"></i> Akcja</th>
                          </tr>
                        </thead>
                        <tbody>
                          <tr>
                            <th scope="row">1</th>
                            <td>Mark</td>
                            <td>Otto</td>
                            <td>@mdo</td>
                            <td>
                                <a href="#"><i class="bi bi-info-square" style="color: rgb(0, 196, 49) !important;"></i></a>
                                <a href="#"><i class="bi bi-pencil-square" style="color: rgb(0, 180, 204) !important;"></i></a>
                                <a href="#"><i class="bi bi-person-video2" style="color: rgb(255, 145, 0) !important;"></i></a>
                                <a href="#"><i class="bi bi-x-square-fill" style="color: rgb(255, 0, 0) !important;"></i></a>
                            </td>
                          </tr>
                          <tr>
                            <th scope="row">2</th>
                            <td><stong>Jacob</stong></td>
                            <td>Thornton</td>
                            <td>@fat</td>
                            <td>
                                <a href="#"><i class="bi bi-info-square" style="color: rgb(0, 196, 49) !important;"></i></a>
                                <a href="#"><i class="bi bi-pencil-square" style="color: rgb(0, 180, 204) !important;"></i></a>
                                <a href="#"><i class="bi bi-person-video2" style="color: rgb(255, 145, 0) !important;"></i></a>
                                <a href="#"><i class="bi bi-x-square-fill" style="color: rgb(255, 0, 0) !important;"></i></a>    
                            </td>
                          </tr>
                          <tr>
                            <th scope="row">3</th>
                            <td colspan="2">Larry the Bird</td>
                            <td>@twitter</td>
                            <td>
                                <a href="#"><i class="bi bi-info-square" style="color: rgb(0, 196, 49) !important;"></i></a>
                                <a href="#"><i class="bi bi-pencil-square" style="color: rgb(0, 180, 204) !important;"></i></a>
                                <a href="#"><i class="bi bi-person-video2" style="color: rgb(255, 145, 0) !important;"></i></a>
                                <a href="#"><i class="bi bi-x-square-fill" style="color: rgb(255, 0, 0) !important;"></i></a>    
                            </td>
                          </tr>
                        </tbody>
                      </table>
                      <div class="pagination">
                        <nav aria-label="Page navigation example">
                            <ul class="pagination justify-content-center">
                              <li class="page-item disabled">
                                <a class="page-link" href="#" tabindex="-1" aria-disabled="true">Previous</a>
                              </li>
                              <li class="page-item"><a class="page-link" href="#">1</a></li>
                              <li class="page-item"><a class="page-link" href="#">2</a></li>
                              <li class="page-item"><a class="page-link" href="#">3</a></li>
                              <li class="page-item">
                                <a class="page-link" href="#">Next</a>
                              </li>
                            </ul>
                          </nav>      
                      </div>
                </div>
                <!-- Conntent -->
                <div class="przyklejddoł-divy">
                    <p>Copyrights © 2024 DMD DOMY. All Rights Reserved.<p>  
                    <p>Polityka prywatności | Zasady korzystania z witryny | FAQ’s | Pomoc</p>
                </div>

    </div>
</body>
</html>