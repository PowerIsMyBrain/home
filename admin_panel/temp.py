usersDB = {
    'michal': 'h8double',
    'piotr': 'pisanki1',
    'informatyk@dmdbudownictwo.pl': '1234'
}

userDataDB = [
    {
        'id': 1, 
        'username': 'michal',
        'password': '50e0ba9650b53f2b8627849578f5a93be4fca8f5c023a94bddf5b3c5194fc38e', 
        'salt' : 'f87449159daaaf40e2b4631395801ce4', 
        'email':'michal@wp.pl',
        'name':'Michał Jankiewicz', 
        'stanowisko': 'kierownik',
        'opis': 'Michał pełni rolę kierownika w naszej firmie. Jego zaangażowanie i skuteczność zostały docenione, gdy został uznany za Pracownika Roku. ',
        'status': '1',
        'avatar': 'https://www.kindpng.com/picc/m/57-579010_wolf-png-logo-wolf-logo-transparent-background-png.png',
        'uprawnienia': {
            'users': 1,
            'brands': 1,
            'blog': 1,
            'subscribers': 1,
            'commnets': 1,
            'team': 1,
            'permissions': 1,
            'settings': 1,
            'newsletter': 1
            },
        'brands': {
            'domy': 1,
            'budownictwo': 1,
            'elitehome': 1,
            'inwestycje': 1,
            'instalacje': 0,
            'development': 1
            }
    },
    {
        'id': 2, 
        'username': 'pawell',  
        'password': '50e0ba9650b53f2b8627849578f5a93be4fca8f5c023a94bddf5b3c5194fc38e', 
        'salt' : 'f87449159daaaf40e2b4631395801ce4',  
        'email':'pawell@wp.pl',
        'name':'Paweł Nowak', 
        'stanowisko': 'kierownik',
        'opis': 'Pracownik roku',
        'status': '0',
        'avatar': 'https://dmddomy.pl/images/team/tm-01-460x460-pawel_perlinski.png',
        'uprawnienia': {
            'users': 0,
            'brands': 0,
            'blog': 0,
            'subscribers':0,
            'commnets': 0,
            'team': 0,
            'permissions': 0,
            'settings': 1,
            'newsletter': 1
            },
        'brands': {
            'domy': 0,
            'budownictwo': 0,
            'elitehome': 0,
            'inwestycje': 0,
            'instalacje': 0,
            'development': 0
            }
    },
]

subsDataDB = [
    {'id': 1, 'email':'michal@wp.pl','name':'Michał', 'status': '1', 
        'comments': {
                1: {
                    'message': "Super! Takie domy są jak najlepiej.",
                    'post_title': 'Willa Floryda',
                    'data-time': '18 lutego 2024'
                },
                2: {
                    'message': "Widzę to już w nowych projektach...",
                    'post_title': 'Willa Floryda',
                    'data-time': '1 marca 2024'
                },
                3: {
                    'message': "To tak naprawdę ciekawo! Dzięki",
                    'post_title': 'Willa Floryda',
                    'data-time': '1 marca 2024'
                }
            }    
    },
    {'id': 2, 'email':'piotrek@wp.pl','name':'Piotr',   'status': '0', 
        'comments': {
                1: {
                    'message': "Super! Takie domy są jak najlepiej.",
                    'post_title': 'Willa Floryda',
                    'data-time': '18 lutego 2024'
                },
                2: {
                    'message': "Widzę to już w nowych projektach...",
                    'post_title': 'Willa Floryda',
                    'data-time': '1 marca 2024'
                },
                3: {
                    'message': "To tak naprawdę ciekawo! Dzięki",
                    'post_title': 'Willa Floryda',
                    'data-time': '1 marca 2024'
                }
            }
    },
    {'id': 3, 'email':'marek@wp.pl','name':'Marek',   'status': '1', 
        'comments': {
                1: {
                    'message': "Super! Takie domy są jak najlepiej.",
                    'post_title': 'Willa Floryda',
                    'data-time': '18 lutego 2024'
                },
                2: {
                    'message': "Widzę to już w nowych projektach...",
                    'post_title': 'Willa Floryda',
                    'data-time': '1 marca 2024'
                },
                3: {
                    'message': "To tak naprawdę ciekawo! Dzięki",
                    'post_title': 'Willa Floryda',
                    'data-time': '1 marca 2024'
                }
            }
    },
]

daneDBList = [
            {
            'id': 1,
            'title': "Dom Lustrzany: Alucobond w Grze Świateł i Natury",
            'introduction': "Zapraszamy do fascynującej podróży do podwarszawskiego Izabelina, gdzie w otulinie Puszczy Kampinoskiej powstał wyjątkowy Lustrzany Dom. Projekt tego jednorodzinnego budynku, autorstwa Marcina Tomaszewskiego z pracowni REFORM Architekt, to połączenie nowoczesności z naturą, gdzie alucobond odgrywa główną rolę w kreowaniu niezwykłej atmosfery.",
            'highlight': "“ Dom Lustrzany to nie tylko budynek mieszkalny, to interaktywna forma sztuki, w której alucobond staje się magią odbić, łącząc nowoczesność z otaczającym krajobrazem. ”",
            'mainFoto': "https://dmddomy.pl/images/blog/bl-00-1920x750-DomLustrzany.png",
            'contentFoto': "https://dmddomy.pl/images/blog/bl-01-750x430-DomLustrzany-1.png",
            'additionalList': "Alucobond: Lustrzane Odbicie Natury: Dom Lustrzany, o powierzchni 400 m² na dwóch kondygnacjach, opiera się na dwóch bryłach, które płynnie łączą się poziomo. Elewacja dolnej części, niemal w całości pokryta alucobondem - aluminiową płytą kompozytową, nadaje budynkowi charakter lustra. Marcin Tomaszewski, opowiadając o swoim projekcie, podkreśla zalety alucobondu, który imituje lustro, zachowując jednocześnie trwałość i wytrzymałość.#splx#Zanurzenie w Naturze: Alucobond sprawia, że dom staje się niemal niewidoczny, odbijając otaczający las i zlewając się z przyrodą. Biała bryła piętra zdaje się unosić w powietrzu, dzięki czemu granice między budynkiem a naturą stają się nieostrzejsze. To nie tylko dom, ale także interaktywna przestrzeń, gdzie światło i odbicia nadają mu dynamiczną formę.#splx#Trwałość i Niski Wymiar Utrzymania: Alucobond, jako materiał niezwykle twardy i trwały, nie wymaga regularnych odnawiania ani odświeżania. Prosta pielęgnacja, polegająca na umyciu powierzchni czystą wodą, sprawia, że budynek zachowuje swoją estetykę na długie lata.",
            'tags': "#DomLustrzany, #Alucobond, #REFORMArchitekt, #ArchitekturaNowoczesna",
            'category': "Architektura Nowoczesna",
            'data': "22 stycznia 2024",
            'author': 'Michał Kowalski',
            'comments': {
                1: {
                    'message': "Super! Takie domy są jak najlepiej.",
                    'user': 'Mariusz Nowak',
                    'e-mail': 'mariusz@nowak.com',
                    'data-time': '18 lutego 2024'
                },
                2: {
                    'message': "Widzę to już w nowych projektach...",
                    'user': 'Jan Kowalski',
                    'e-mail': 'jan@gmail.com',
                    'data-time': '1 marca 2024'
                },
                3: {
                    'message': "To tak naprawdę ciekawo! Dzięki",
                    'user': 'Roh Kowalski',
                    'e-mail': 'rohk@gmail.com',
                    'data-time': '1 marca 2024'
                }
            }
        },
        {
            'id': 2,
            'title': "Dom Lustrzany",
            'introduction': "Zapraszamy do fascynującej podróży do podwarszawskiego Izabelina.",
            'highlight': "“ Dom Lustrzany to nie tylko budynek mieszkalny, to interaktywna forma sztuki. ”",
            'mainFoto': "https://dmddomy.pl/images/blog/bl-00-1920x750-DomLustrzany.png",
            'contentFoto': "https://dmddomy.pl/images/blog/bl-01-750x430-DomLustrzany-1.png",
            'additionalList': "Alucobond: Lustrzane Odbicie Natury: Dom Lustrzany, o powierzchni 400 m²#splx#Zanurzenie w Naturze: Alucobond sprawia, że dom staje się niemal niewidoczny.#splx#Trwałość i Niski Wymiar Utrzymania: Alucobond, jako materiał niezwykle twardy .",
            'tags': "#DomLustrzany, #ArchitekturaNowoczesna",
            'category': "Architektura Nowoczesna",
            'data': "20 luty 2024",
            'author': 'Piotr Walec',
            'comments': {
                1: {
                    'message': "Jestem zaszokowany! Czy na pewno?",
                    'user': 'Mariusz Kot',
                    'e-mail': 'mariusz@kot.com',
                    'data-time': '18 lutego 2024'
                },
                2: {
                    'message': """Fascynujący projekt! Dom Lustrzany wydaje się być nie tylko miejscem do życia, ale prawdziwym arcydziełem sztuki architektonicznej. Zaskakujące, jak alucobond potrafi połączyć nowoczesność z otaczającym krajobrazem, sprawiając, że budynek staje się niemal częścią natury. Jestem pod wrażeniem tego, jak biała bryła piętra zdaje się unosić w powietrzu, tworząc dynamiczną formę.""",
                    'user': 'Jan Kowalski',
                    'e-mail': 'jan@gmail.com',
                    'data-time': '1 marca 2024'
                },
            }
        },
        {
            'id': 3,
            'title': "Dom Lustrzany",
            'introduction': "Zapraszamy do fascynującej podróży do podwarszawskiego Izabelina.",
            'highlight': "“ Dom Lustrzany to nie tylko budynek mieszkalny, to interaktywna forma sztuki. ”",
            'mainFoto': "https://dmddomy.pl/images/blog/bl-00-1920x750-DomLustrzany.png",
            'contentFoto': "https://dmddomy.pl/images/blog/bl-01-750x430-DomLustrzany-1.png",
            'additionalList': "Alucobond: Lustrzane Odbicie Natury: Dom Lustrzany, o powierzchni 400 m²#splx#Zanurzenie w Naturze: Alucobond sprawia, że dom staje się niemal niewidoczny.#splx#Trwałość i Niski Wymiar Utrzymania: Alucobond, jako materiał niezwykle twardy .",
            'tags': "#DomLustrzany, #ArchitekturaNowoczesna",
            'category': "Architektura Nowoczesna",
            'data': "20 luty 2024",
            'author': 'Piotr Walec',
            'comments': {
                1: {
                    'message': "Jestem zaszokowany! Czy na pewno?",
                    'user': 'Mariusz Kot',
                    'e-mail': 'mariusz@kot.com',
                    'data-time': '18 lutego 2024'
                },
                2: {
                    'message': """Fascynujący projekt! Dom Lustrzany wydaje się być nie tylko miejscem do życia, ale prawdziwym arcydziełem sztuki architektonicznej. Zaskakujące, jak alucobond potrafi połączyć nowoczesność z otaczającym krajobrazem, sprawiając, że budynek staje się niemal częścią natury. Jestem pod wrażeniem tego, jak biała bryła piętra zdaje się unosić w powietrzu, tworząc dynamiczną formę.""",
                    'user': 'Jan Kowalski',
                    'e-mail': 'jan@gmail.com',
                    'data-time': '1 marca 2024'
                },
            }
        },
        {
            'id': 4,
            'title': "Dom Lustrzany",
            'introduction': "Zapraszamy do fascynującej podróży do podwarszawskiego Izabelina.",
            'highlight': "“ Dom Lustrzany to nie tylko budynek mieszkalny, to interaktywna forma sztuki. ”",
            'mainFoto': "https://dmddomy.pl/images/blog/bl-00-1920x750-DomLustrzany.png",
            'contentFoto': "https://dmddomy.pl/images/blog/bl-01-750x430-DomLustrzany-1.png",
            'additionalList': "Alucobond: Lustrzane Odbicie Natury: Dom Lustrzany, o powierzchni 400 m²#splx#Zanurzenie w Naturze: Alucobond sprawia, że dom staje się niemal niewidoczny.#splx#Trwałość i Niski Wymiar Utrzymania: Alucobond, jako materiał niezwykle twardy .",
            'tags': "#DomLustrzany, #ArchitekturaNowoczesna",
            'category': "Architektura Nowoczesna",
            'data': "20 luty 2024",
            'author': 'Piotr Walec',
            'comments': {
                1: {
                    'message': "Jestem zaszokowany! Czy na pewno?",
                    'user': 'Mariusz Kot',
                    'e-mail': 'mariusz@kot.com',
                    'data-time': '18 lutego 2024'
                },
                2: {
                    'message': """Fascynujący projekt! Dom Lustrzany wydaje się być nie tylko miejscem do życia, ale prawdziwym arcydziełem sztuki architektonicznej. Zaskakujące, jak alucobond potrafi połączyć nowoczesność z otaczającym krajobrazem, sprawiając, że budynek staje się niemal częścią natury. Jestem pod wrażeniem tego, jak biała bryła piętra zdaje się unosić w powietrzu, tworząc dynamiczną formę.""",
                    'user': 'Jan Kowalski',
                    'e-mail': 'jan@gmail.com',
                    'data-time': '1 marca 2024'
                },
            }
        },
        {
            'id': 5,
            'title': "Dom Lustrzany",
            'introduction': "Zapraszamy do fascynującej podróży do podwarszawskiego Izabelina.",
            'highlight': "“ Dom Lustrzany to nie tylko budynek mieszkalny, to interaktywna forma sztuki. ”",
            'mainFoto': "https://dmddomy.pl/images/blog/bl-00-1920x750-DomLustrzany.png",
            'contentFoto': "https://dmddomy.pl/images/blog/bl-01-750x430-DomLustrzany-1.png",
            'additionalList': "Alucobond: Lustrzane Odbicie Natury: Dom Lustrzany, o powierzchni 400 m²#splx#Zanurzenie w Naturze: Alucobond sprawia, że dom staje się niemal niewidoczny.#splx#Trwałość i Niski Wymiar Utrzymania: Alucobond, jako materiał niezwykle twardy .",
            'tags': "#DomLustrzany, #ArchitekturaNowoczesna",
            'category': "Architektura Nowoczesna",
            'data': "20 luty 2024",
            'author': 'Piotr Walec',
            'comments': {
                1: {
                    'message': "Jestem zaszokowany! Czy na pewno?",
                    'user': 'Mariusz Kot',
                    'e-mail': 'mariusz@kot.com',
                    'data-time': '18 lutego 2024'
                },
                2: {
                    'message': """Fascynujący projekt! Dom Lustrzany wydaje się być nie tylko miejscem do życia, ale prawdziwym arcydziełem sztuki architektonicznej. Zaskakujące, jak alucobond potrafi połączyć nowoczesność z otaczającym krajobrazem, sprawiając, że budynek staje się niemal częścią natury. Jestem pod wrażeniem tego, jak biała bryła piętra zdaje się unosić w powietrzu, tworząc dynamiczną formę.""",
                    'user': 'Jan Kowalski',
                    'e-mail': 'jan@gmail.com',
                    'data-time': '1 marca 2024'
                },
            }
        },
        {
            'id': 6,
            'title': "Dom Lustrzany",
            'introduction': "Zapraszamy do fascynującej podróży do podwarszawskiego Izabelina.",
            'highlight': "“ Dom Lustrzany to nie tylko budynek mieszkalny, to interaktywna forma sztuki. ”",
            'mainFoto': "https://dmddomy.pl/images/blog/bl-00-1920x750-DomLustrzany.png",
            'contentFoto': "https://dmddomy.pl/images/blog/bl-01-750x430-DomLustrzany-1.png",
            'additionalList': "Alucobond: Lustrzane Odbicie Natury: Dom Lustrzany, o powierzchni 400 m²#splx#Zanurzenie w Naturze: Alucobond sprawia, że dom staje się niemal niewidoczny.#splx#Trwałość i Niski Wymiar Utrzymania: Alucobond, jako materiał niezwykle twardy .",
            'tags': "#DomLustrzany, #ArchitekturaNowoczesna",
            'category': "Architektura Nowoczesna",
            'data': "20 luty 2024",
            'author': 'Piotr Walec',
            'comments': {
                1: {
                    'message': "Jestem zaszokowany! Czy na pewno?",
                    'user': 'Mariusz Kot',
                    'e-mail': 'mariusz@kot.com',
                    'data-time': '18 lutego 2024'
                },
                2: {
                    'message': """Fascynujący projekt! Dom Lustrzany wydaje się być nie tylko miejscem do życia, ale prawdziwym arcydziełem sztuki architektonicznej. Zaskakujące, jak alucobond potrafi połączyć nowoczesność z otaczającym krajobrazem, sprawiając, że budynek staje się niemal częścią natury. Jestem pod wrażeniem tego, jak biała bryła piętra zdaje się unosić w powietrzu, tworząc dynamiczną formę.""",
                    'user': 'Jan Kowalski',
                    'e-mail': 'jan@gmail.com',
                    'data-time': '1 marca 2024'
                },
            }
        },
        {
            'id': 7,
            'title': "Dom Lustrzany",
            'introduction': "Zapraszamy do fascynującej podróży do podwarszawskiego Izabelina.",
            'highlight': "“ Dom Lustrzany to nie tylko budynek mieszkalny, to interaktywna forma sztuki. ”",
            'mainFoto': "https://dmddomy.pl/images/blog/bl-00-1920x750-DomLustrzany.png",
            'contentFoto': "https://dmddomy.pl/images/blog/bl-01-750x430-DomLustrzany-1.png",
            'additionalList': "Alucobond: Lustrzane Odbicie Natury: Dom Lustrzany, o powierzchni 400 m²#splx#Zanurzenie w Naturze: Alucobond sprawia, że dom staje się niemal niewidoczny.#splx#Trwałość i Niski Wymiar Utrzymania: Alucobond, jako materiał niezwykle twardy .",
            'tags': "#DomLustrzany, #ArchitekturaNowoczesna",
            'category': "Architektura Nowoczesna",
            'data': "20 luty 2024",
            'author': 'Piotr Walec',
            'comments': {
                1: {
                    'message': "Jestem zaszokowany! Czy na pewno?",
                    'user': 'Mariusz Kot',
                    'e-mail': 'mariusz@kot.com',
                    'data-time': '18 lutego 2024'
                },
                2: {
                    'message': """Fascynujący projekt! Dom Lustrzany wydaje się być nie tylko miejscem do życia, ale prawdziwym arcydziełem sztuki architektonicznej. Zaskakujące, jak alucobond potrafi połączyć nowoczesność z otaczającym krajobrazem, sprawiając, że budynek staje się niemal częścią natury. Jestem pod wrażeniem tego, jak biała bryła piętra zdaje się unosić w powietrzu, tworząc dynamiczną formę.""",
                    'user': 'Jan Kowalski',
                    'e-mail': 'jan@gmail.com',
                    'data-time': '1 marca 2024'
                },
            }
        },
    ]