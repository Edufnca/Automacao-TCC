Quimica = list()

Elementos_quimicos = {
    "H": {
        "nome": "Hidrogênio",
        "massa_quantica": 1.008,
        "numero_atomico": 1,
        "simbolo": "H",
        "familia": "Não metal",
        "grupo": 1,
        "periodo": 1
    },
    "He": {
        "nome": "Hélio",
        "massa_quantica": 4.0026,
        "numero_atomico": 2,
        "simbolo": "He",
        "familia": "Gases nobres",
        "grupo": 18,
        "periodo": 1
    },
    "Li": {
        "nome": "Lítio",
        "massa_quantica": 6.94,
        "numero_atomico": 3,
        "simbolo": "Li",
        "familia": "Metal alcalino",
        "grupo": 1,
        "periodo": 2
    },
    "Be": {
        "nome": "Berílio",
        "massa_quantica": 9.0122,
        "numero_atomico": 4,
        "simbolo": "Be",
        "familia": "Metal alcalino-terroso",
        "grupo": 2,
        "periodo": 2
    },
    "B": {
        "nome": "Boro",
        "massa_quantica": 10.81,
        "numero_atomico": 5,
        "simbolo": "B",
        "familia": "Semimetais",
        "grupo": 13,
        "periodo": 2
    },
    "C": {
        "nome": "Carbono",
        "massa_quantica": 12.01,
        "numero_atomico": 6,
        "simbolo": "C",
        "familia": "Não metal",
        "grupo": 14,
        "periodo": 2
    },
    "N": {
        "nome": "Nitrogênio",
        "massa_quantica": 14.01,
        "numero_atomico": 7,
        "simbolo": "N",
        "familia": "Não metal",
        "grupo": 15,
        "periodo": 2
    },
    "O": {
        "nome": "Oxigênio",
        "massa_quantica": 16.00,
        "numero_atomico": 8,
        "simbolo": "O",
        "familia": "Não metal",
        "grupo": 16,
        "periodo": 2
    },
    "F": {
        "nome": "Flúor",
        "massa_quantica": 19.00,
        "numero_atomico": 9,
        "simbolo": "F",
        "familia": "Halogênios",
        "grupo": 17,
        "periodo": 2
    },
    "Ne": {
        "nome": "Neônio",
        "massa_quantica": 20.18,
        "numero_atomico": 10,
        "simbolo": "Ne",
        "familia": "Gases nobres",
        "grupo": 18,
        "periodo": 2
    },
        "Na": {
        "nome": "Sódio",
        "massa_quantica": 22.99,
        "numero_atomico": 11,
        "simbolo": "Na",
        "familia": "Metal alcalino",
        "grupo": 1,
        "periodo": 3
    },
    "Mg": {
        "nome": "Magnésio",
        "massa_quantica": 24.31,
        "numero_atomico": 12,
        "simbolo": "Mg",
        "familia": "Metal alcalino-terroso",
        "grupo": 2,
        "periodo": 3
    },
    "Al": {
        "nome": "Alumínio",
        "massa_quantica": 26.98,
        "numero_atomico": 13,
        "simbolo": "Al",
        "familia": "Metal do bloco p",
        "grupo": 13,
        "periodo": 3
    },
    "Si": {
        "nome": "Silício",
        "massa_quantica": 28.09,
        "numero_atomico": 14,
        "simbolo": "Si",
        "familia": "Semimetais",
        "grupo": 14,
        "periodo": 3
    },
    "P": {
        "nome": "Fósforo",
        "massa_quantica": 30.97,
        "numero_atomico": 15,
        "simbolo": "P",
        "familia": "Não metal",
        "grupo": 15,
        "periodo": 3
    },
    "S": {
        "nome": "Enxofre",
        "massa_quantica": 32.06,
        "numero_atomico": 16,
        "simbolo": "S",
        "familia": "Não metal",
        "grupo": 16,
        "periodo": 3
    },
    "Cl": {
        "nome": "Cloro",
        "massa_quantica": 35.45,
        "numero_atomico": 17,
        "simbolo": "Cl",
        "familia": "Halogênios",
        "grupo": 17,
        "periodo": 3
    },
    "Ar": {
        "nome": "Argônio",
        "massa_quantica": 39.95,
        "numero_atomico": 18,
        "simbolo": "Ar",
        "familia": "Gases nobres",
        "grupo": 18,
        "periodo": 3
    },
    "K": {
        "nome": "Potássio",
        "massa_quantica": 39.10,
        "numero_atomico": 19,
        "simbolo": "K",
        "familia": "Metal alcalino",
        "grupo": 1,
        "periodo": 4
    },
    "Ca": {
        "nome": "Cálcio",
        "massa_quantica": 40.08,
        "numero_atomico": 20,
        "simbolo": "Ca",
        "familia": "Metal alcalino-terroso",
        "grupo": 2,
        "periodo": 4
    },
    "Sc": {
        "nome": "Escândio",
        "massa_quantica": 44.96,
        "numero_atomico": 21,
        "simbolo": "Sc",
        "familia": "Metal de transição",
        "grupo": 3,
        "periodo": 4
    },
    "Ti": {
        "nome": "Titânio",
        "massa_quantica": 47.87,
        "numero_atomico": 22,
        "simbolo": "Ti",
        "familia": "Metal de transição",
        "grupo": 4,
        "periodo": 4
    },
    "V": {
        "nome": "Vanádio",
        "massa_quantica": 50.94,
        "numero_atomico": 23,
        "simbolo": "V",
        "familia": "Metal de transição",
        "grupo": 5,
        "periodo": 4
    },
    "Cr": {
        "nome": "Cromo",
        "massa_quantica": 52.00,
        "numero_atomico": 24,
        "simbolo": "Cr",
        "familia": "Metal de transição",
        "grupo": 6,
        "periodo": 4
    },
    "Mn": {
        "nome": "Manganês",
        "massa_quantica": 54.94,
        "numero_atomico": 25,
        "simbolo": "Mn",
        "familia": "Metal de transição",
        "grupo": 7,
        "periodo": 4
    },
    "Fe": {
        "nome": "Ferro",
        "massa_quantica": 55.85,
        "numero_atomico": 26,
        "simbolo": "Fe",
        "familia": "Metal de transição",
        "grupo": 8,
        "periodo": 4
    },
    "Co": {
        "nome": "Cobalto",
        "massa_quantica": 58.93,
        "numero_atomico": 27,
        "simbolo": "Co",
        "familia": "Metal de transição",
        "grupo": 9,
        "periodo": 4
    },
    "Ni": {
        "nome": "Níquel",
        "massa_quantica": 58.69,
        "numero_atomico": 28,
        "simbolo": "Ni",
        "familia": "Metal de transição",
        "grupo": 10,
        "periodo": 4
    },
    "Cu": {
        "nome": "Cobre",
        "massa_quantica": 63.55,
        "numero_atomico": 29,
        "simbolo": "Cu",
        "familia": "Metal de transição",
        "grupo": 11,
        "periodo": 4
    },
    "Zn": {
        "nome": "Zinco",
        "massa_quantica": 65.38,
        "numero_atomico": 30,
        "simbolo": "Zn",
        "familia": "Metal de transição",
        "grupo": 12,
        "periodo": 4
    },
        "Ga": {
        "nome": "Gálio",
        "massa_quantica": 69.72,
        "numero_atomico": 31,
        "simbolo": "Ga",
        "familia": "Metal do bloco p",
        "grupo": 13,
        "periodo": 4
    },
    "Ge": {
        "nome": "Germanio",
        "massa_quantica": 72.63,
        "numero_atomico": 32,
        "simbolo": "Ge",
        "familia": "Semimetais",
        "grupo": 14,
        "periodo": 4
    },
    "As": {
        "nome": "Arsênio",
        "massa_quantica": 74.92,
        "numero_atomico": 33,
        "simbolo": "As",
        "familia": "Semimetais",
        "grupo": 15,
        "periodo": 4
    },
    "Se": {
        "nome": "Selênio",
        "massa_quantica": 78.96,
        "numero_atomico": 34,
        "simbolo": "Se",
        "familia": "Não metal",
        "grupo": 16,
        "periodo": 4
    },
    "Br": {
        "nome": "Bromo",
        "massa_quantica": 79.90,
        "numero_atomico": 35,
        "simbolo": "Br",
        "familia": "Halogênios",
        "grupo": 17,
        "periodo": 4
    },
    "Kr": {
        "nome": "Criptônio",
        "massa_quantica": 83.80,
        "numero_atomico": 36,
        "simbolo": "Kr",
        "familia": "Gases nobres",
        "grupo": 18,
        "periodo": 4
    },
    "Rb": {
        "nome": "Rubídio",
        "massa_quantica": 85.47,
        "numero_atomico": 37,
        "simbolo": "Rb",
        "familia": "Metal alcalino",
        "grupo": 1,
        "periodo": 5
    },
    "Sr": {
        "nome": "Estrôncio",
        "massa_quantica": 87.62,
        "numero_atomico": 38,
        "simbolo": "Sr",
        "familia": "Metal alcalino-terroso",
        "grupo": 2,
        "periodo": 5
    },
    "Y": {
        "nome": "Ítrio",
        "massa_quantica": 88.91,
        "numero_atomico": 39,
        "simbolo": "Y",
        "familia": "Metal de transição",
        "grupo": 3,
        "periodo": 5
    },
    "Zr": {
        "nome": "Zircônio",
        "massa_quantica": 91.22,
        "numero_atomico": 40,
        "simbolo": "Zr",
        "familia": "Metal de transição",
        "grupo": 4,
        "periodo": 5
    },
    "Nb": {
        "nome": "Nióbio",
        "massa_quantica": 92.91,
        "numero_atomico": 41,
        "simbolo": "Nb",
        "familia": "Metal de transição",
        "grupo": 5,
        "periodo": 5
    },
    "Mo": {
        "nome": "Molibdênio",
        "massa_quantica": 95.95,
        "numero_atomico": 42,
        "simbolo": "Mo",
        "familia": "Metal de transição",
        "grupo": 6,
        "periodo": 5
    },
    "Tc": {
        "nome": "Tecnécio",
        "massa_quantica": 98,
        "numero_atomico": 43,
        "simbolo": "Tc",
        "familia": "Metal de transição",
        "grupo": 7,
        "periodo": 5
    },
    "Ru": {
        "nome": "Rutênio",
        "massa_quantica": 101.1,
        "numero_atomico": 44,
        "simbolo": "Ru",
        "familia": "Metal de transição",
        "grupo": 8,
        "periodo": 5
    },
    "Rh": {
        "nome": "Ródio",
        "massa_quantica": 102.9,
        "numero_atomico": 45,
        "simbolo": "Rh",
        "familia": "Metal de transição",
        "grupo": 9,
        "periodo": 5
    },
    "Pd": {
        "nome": "Paládio",
        "massa_quantica": 106.4,
        "numero_atomico": 46,
        "simbolo": "Pd",
        "familia": "Metal de transição",
        "grupo": 10,
        "periodo": 5
    },
    "Ag": {
        "nome": "Prata",
        "massa_quantica": 107.9,
        "numero_atomico": 47,
        "simbolo": "Ag",
        "familia": "Metal de transição",
        "grupo": 11,
        "periodo": 5
    },
    "Cd": {
        "nome": "Cádmio",
        "massa_quantica": 112.4,
        "numero_atomico": 48,
        "simbolo": "Cd",
        "familia": "Metal de transição",
        "grupo": 12,
        "periodo": 5
    },
    "In": {
        "nome": "Indio",
        "massa_quantica": 114.8,
        "numero_atomico": 49,
        "simbolo": "In",
        "familia": "Metal do bloco p",
        "grupo": 13,
        "periodo": 5
    },
    "Sn": {
        "nome": "Estanho",
        "massa_quantica": 118.7,
        "numero_atomico": 50,
        "simbolo": "Sn",
        "familia": "Metal do bloco p",
        "grupo": 14,
        "periodo": 5
    },
    "Sb": {
    "nome": "Antimônio",
    "massa_quantica": 121.8,
    "numero_atomico": 51,
    "simbolo": "Sb",
    "familia": "Semimetais",
    "grupo": 15,
    "periodo": 5
    },
    "Te": {
        "nome": "Telúrio",
        "massa_quantica": 127.6,
        "numero_atomico": 52,
        "simbolo": "Te",
        "familia": "Semimetais",
        "grupo": 16,
        "periodo": 5
    },
    "I": {
        "nome": "Iodo",
        "massa_quantica": 126.9,
        "numero_atomico": 53,
        "simbolo": "I",
        "familia": "Halogênios",
        "grupo": 17,
        "periodo": 5
    },
    "Xe": {
        "nome": "Xenônio",
        "massa_quantica": 131.3,
        "numero_atomico": 54,
        "simbolo": "Xe",
        "familia": "Gases nobres",
        "grupo": 18,
        "periodo": 5
    },
    "Cs": {
        "nome": "Césio",
        "massa_quantica": 132.9,
        "numero_atomico": 55,
        "simbolo": "Cs",
        "familia": "Metal alcalino",
        "grupo": 1,
        "periodo": 6
    },
    "Ba": {
        "nome": "Bário",
        "massa_quantica": 137.3,
        "numero_atomico": 56,
        "simbolo": "Ba",
        "familia": "Metal alcalino-terroso",
        "grupo": 2,
        "periodo": 6
    },
    "La": {
        "nome": "Lantânio",
        "massa_quantica": 138.9,
        "numero_atomico": 57,
        "simbolo": "La",
        "familia": "Lantanídeos",
        "grupo": None,
        "periodo": 6
    },
    "Ce": {
        "nome": "Cério",
        "massa_quantica": 140.1,
        "numero_atomico": 58,
        "simbolo": "Ce",
        "familia": "Lantanídeos",
        "grupo": None,
        "periodo": 6
    },
    "Pr": {
        "nome": "Praseodímio",
        "massa_quantica": 140.9,
        "numero_atomico": 59,
        "simbolo": "Pr",
        "familia": "Lantanídeos",
        "grupo": None,
        "periodo": 6
    },
    "Nd": {
        "nome": "Neodímio",
        "massa_quantica": 144.2,
        "numero_atomico": 60,
        "simbolo": "Nd",
        "familia": "Lantanídeos",
        "grupo": None,
        "periodo": 6
    },
    "Pm": {
        "nome": "Promécio",
        "massa_quantica": 145,
        "numero_atomico": 61,
        "simbolo": "Pm",
        "familia": "Lantanídeos",
        "grupo": None,
        "periodo": 6
    },
    "Sm": {
        "nome": "Samário",
        "massa_quantica": 150.4,
        "numero_atomico": 62,
        "simbolo": "Sm",
        "familia": "Lantanídeos",
        "grupo": None,
        "periodo": 6
    },
    "Eu": {
        "nome": "Európio",
        "massa_quantica": 152,
        "numero_atomico": 63,
        "simbolo": "Eu",
        "familia": "Lantanídeos",
        "grupo": None,
        "periodo": 6
    },
    "Gd": {
        "nome": "Gadolínio",
        "massa_quantica": 157.3,
        "numero_atomico": 64,
        "simbolo": "Gd",
        "familia": "Lantanídeos",
        "grupo": None,
        "periodo": 6
    },
    "Tb": {
        "nome": "Térbio",
        "massa_quantica": 158.9,
        "numero_atomico": 65,
        "simbolo": "Tb",
        "familia": "Lantanídeos",
        "grupo": None,
        "periodo": 6
    },
    "Dy": {
        "nome": "Disprósio",
        "massa_quantica": 162.5,
        "numero_atomico": 66,
        "simbolo": "Dy",
        "familia": "Lantanídeos",
        "grupo": None,
        "periodo": 6
    },
    "Ho": {
        "nome": "Hólmio",
        "massa_quantica": 164.9,
        "numero_atomico": 67,
        "simbolo": "Ho",
        "familia": "Lantanídeos",
        "grupo": None,
        "periodo": 6
    },
    "Er": {
        "nome": "Érbio",
        "massa_quantica": 167.3,
        "numero_atomico": 68,
        "simbolo": "Er",
        "familia": "Lantanídeos",
        "grupo": None,
        "periodo": 6
    },
    "Tm": {
        "nome": "Túlio",
        "massa_quantica": 168.9,
        "numero_atomico": 69,
        "simbolo": "Tm",
        "familia": "Lantanídeos",
        "grupo": None,
        "periodo": 6
    },
    "Yb": {
        "nome": "Itérbio",
        "massa_quantica": 173.1,
        "numero_atomico": 70,
        "simbolo": "Yb",
        "familia": "Lantanídeos",
        "grupo": None,
        "periodo": 6
    },
    "Lu": {
        "nome": "Lutécio",
        "massa_quantica": 175,
        "numero_atomico": 71,
        "simbolo": "Lu",
        "familia": "Lantanídeos",
        "grupo": None,
        "periodo": 6
    },
    "Hf": {
        "nome": "Háfnio",
        "massa_quantica": 178.5,
        "numero_atomico": 72,
        "simbolo": "Hf",
        "familia": "Metal de transição",
        "grupo": 4,
        "periodo": 6
    },
    "Ta": {
        "nome": "Tântalo",
        "massa_quantica": 180.9,
        "numero_atomico": 73,
        "simbolo": "Ta",
        "familia": "Metal de transição",
        "grupo": 5,
        "periodo": 6
    },
    "W": {
        "nome": "Tungstênio",
        "massa_quantica": 183.8,
        "numero_atomico": 74,
        "simbolo": "W",
        "familia": "Metal de transição",
        "grupo": 6,
        "periodo": 6
    },
    "Re": {
        "nome": "Rênio",
        "massa_quantica": 186.2,
        "numero_atomico": 75,
        "simbolo": "Re",
        "familia": "Metal de transição",
        "grupo": 7,
        "periodo": 6
    },
    "Os": {
        "nome": "Ósmio",
        "massa_quantica": 190.2,
        "numero_atomico": 76,
        "simbolo": "Os",
        "familia": "Metal de transição",
        "grupo": 8,
        "periodo": 6
    },
    "Ir": {
        "nome": "Irídio",
        "massa_quantica": 192.2,
        "numero_atomico": 77,
        "simbolo": "Ir",
        "familia": "Metal de transição",
        "grupo": 9,
        "periodo": 6
    },
    "Pt": {
        "nome": "Platina",
        "massa_quantica": 195.1,
        "numero_atomico": 78,
        "simbolo": "Pt",
        "familia": "Metal de transição",
        "grupo": 10,
        "periodo": 6
    },
    "Au": {
        "nome": "Ouro",
        "massa_quantica": 197,
        "numero_atomico": 79,
        "simbolo": "Au",
        "familia": "Metal de transição",
        "grupo": 11,
        "periodo": 6
    },
    "Hg": {
        "nome": "Mercúrio",
        "massa_quantica": 200.6,
        "numero_atomico": 80,
        "simbolo": "Hg",
        "familia": "Metal de transição",
        "grupo": 12,
        "periodo": 6
    },
        "Tl": {
        "nome": "Tálio",
        "massa_quantica": 204.4,
        "numero_atomico": 81,
        "simbolo": "Tl",
        "familia": "Metal do bloco p",
        "grupo": 13,
        "periodo": 6
    },
    "Pb": {
        "nome": "Chumbo",
        "massa_quantica": 207.2,
        "numero_atomico": 82,
        "simbolo": "Pb",
        "familia": "Metal do bloco p",
        "grupo": 14,
        "periodo": 6
    },
    "Bi": {
        "nome": "Bismuto",
        "massa_quantica": 208.9,
        "numero_atomico": 83,
        "simbolo": "Bi",
        "familia": "Metal do bloco p",
        "grupo": 15,
        "periodo": 6
    },
    "Po": {
        "nome": "Polônio",
        "massa_quantica": 209,
        "numero_atomico": 84,
        "simbolo": "Po",
        "familia": "Semimetais",
        "grupo": 16,
        "periodo": 6
    },
    "At": {
        "nome": "Astato",
        "massa_quantica": 210,
        "numero_atomico": 85,
        "simbolo": "At",
        "familia": "Halogênios",
        "grupo": 17,
        "periodo": 6
    },
    "Rn": {
        "nome": "Radônio",
        "massa_quantica": 222,
        "numero_atomico": 86,
        "simbolo": "Rn",
        "familia": "Gases nobres",
        "grupo": 18,
        "periodo": 6
    },
    "Fr": {
        "nome": "Frâncio",
        "massa_quantica": 223,
        "numero_atomico": 87,
        "simbolo": "Fr",
        "familia": "Metal alcalino",
        "grupo": 1,
        "periodo": 7
    },
    "Ra": {
        "nome": "Rádio",
        "massa_quantica": 226,
        "numero_atomico": 88,
        "simbolo": "Ra",
        "familia": "Metal alcalino-terroso",
        "grupo": 2,
        "periodo": 7
    },
    "Ac": {
        "nome": "Actínio",
        "massa_quantica": 227,
        "numero_atomico": 89,
        "simbolo": "Ac",
        "familia": "Actinídeos",
        "grupo": None,
        "periodo": 7
    },
    "Th": {
        "nome": "Tório",
        "massa_quantica": 232.0,
        "numero_atomico": 90,
        "simbolo": "Th",
        "familia": "Actinídeos",
        "grupo": None,
        "periodo": 7
    },
    "Pa": {
        "nome": "Protactínio",
        "massa_quantica": 231.0,
        "numero_atomico": 91,
        "simbolo": "Pa",
        "familia": "Actinídeos",
        "grupo": None,
        "periodo": 7
    },
    "U": {
        "nome": "Urânio",
        "massa_quantica": 238.0,
        "numero_atomico": 92,
        "simbolo": "U",
        "familia": "Actinídeos",
        "grupo": None,
        "periodo": 7
    },
    "Np": {
        "nome": "Netúnio",
        "massa_quantica": 237.0,
        "numero_atomico": 93,
        "simbolo": "Np",
        "familia": "Actinídeos",
        "grupo": None,
        "periodo": 7
    },
    "Pu": {
        "nome": "Plutônio",
        "massa_quantica": 244.0,
        "numero_atomico": 94,
        "simbolo": "Pu",
        "familia": "Actinídeos",
        "grupo": None,
        "periodo": 7
    },
    "Am": {
        "nome": "Amerício",
        "massa_quantica": 243.0,
        "numero_atomico": 95,
        "simbolo": "Am",
        "familia": "Actinídeos",
        "grupo": None,
        "periodo": 7
    },
    "Cm": {
        "nome": "Cúrio",
        "massa_quantica": 247.0,
        "numero_atomico": 96,
        "simbolo": "Cm",
        "familia": "Actinídeos",
        "grupo": None,
        "periodo": 7
    },
    "Bk": {
        "nome": "Berquélio",
        "massa_quantica": 247.0,
        "numero_atomico": 97,
        "simbolo": "Bk",
        "familia": "Actinídeos",
        "grupo": None,
        "periodo": 7
    },
    "Cf": {
        "nome": "Califórnio",
        "massa_quantica": 251.0,
        "numero_atomico": 98,
        "simbolo": "Cf",
        "familia": "Actinídeos",
        "grupo": None,
        "periodo": 7
    },
    "Es": {
        "nome": "Einstênio",
        "massa_quantica": 252.0,
        "numero_atomico": 99,
        "simbolo": "Es",
        "familia": "Actinídeos",
        "grupo": None,
        "periodo": 7
    },
        "Fm": {
        "nome": "Férmio",
        "massa_quantica": 257.0,
        "numero_atomico": 100,
        "simbolo": "Fm",
        "familia": "Actinídeos",
        "grupo": None,
        "periodo": 7
    },
    "Md": {
        "nome": "Mendelévio",
        "massa_quantica": 258.0,
        "numero_atomico": 101,
        "simbolo": "Md",
        "familia": "Actinídeos",
        "grupo": None,
        "periodo": 7
    },
    "No": {
        "nome": "Nobélio",
        "massa_quantica": 259.0,
        "numero_atomico": 102,
        "simbolo": "No",
        "familia": "Actinídeos",
        "grupo": None,
        "periodo": 7
    },
    "Lr": {
        "nome": "Laurêncio",
        "massa_quantica": 266.0,
        "numero_atomico": 103,
        "simbolo": "Lr",
        "familia": "Actinídeos",
        "grupo": None,
        "periodo": 7
    },
    "Rf": {
        "nome": "Rutherfórdio",
        "massa_quantica": 267.0,
        "numero_atomico": 104,
        "simbolo": "Rf",
        "familia": "Metal de transição",
        "grupo": 4,
        "periodo": 7
    },
    "Db": {
        "nome": "Dúbnio",
        "massa_quantica": 270.0,
        "numero_atomico": 105,
        "simbolo": "Db",
        "familia": "Metal de transição",
        "grupo": 5,
        "periodo": 7
    },
    "Sg": {
        "nome": "Seabórgio",
        "massa_quantica": 271.0,
        "numero_atomico": 106,
        "simbolo": "Sg",
        "familia": "Metal de transição",
        "grupo": 6,
        "periodo": 7
    },
    "Bh": {
        "nome": "Bóhrio",
        "massa_quantica": 270.0,
        "numero_atomico": 107,
        "simbolo": "Bh",
        "familia": "Metal de transição",
        "grupo": 7,
        "periodo": 7
    },
    "Hs": {
        "nome": "Hássio",
        "massa_quantica": 277.0,
        "numero_atomico": 108,
        "simbolo": "Hs",
        "familia": "Metal de transição",
        "grupo": 8,
        "periodo": 7
    },
        "Mt": {
        "nome": "Meitnério",
        "massa_quantica": 276.0,
        "numero_atomico": 109,
        "simbolo": "Mt",
        "familia": "Metal de transição",
        "grupo": 9,
        "periodo": 7
    },
    "Ds": {
        "nome": "Darmstádio",
        "massa_quantica": 281.0,
        "numero_atomico": 110,
        "simbolo": "Ds",
        "familia": "Metal de transição",
        "grupo": 10,
        "periodo": 7
    },
    "Rg": {
        "nome": "Roentgênio",
        "massa_quantica": 280.0,
        "numero_atomico": 111,
        "simbolo": "Rg",
        "familia": "Metal de transição",
        "grupo": 11,
        "periodo": 7
    },
    "Cn": {
        "nome": "Copernício",
        "massa_quantica": 285.0,
        "numero_atomico": 112,
        "simbolo": "Cn",
        "familia": "Metal de transição",
        "grupo": 12,
        "periodo": 7
    },
    "Nh": {
        "nome": "Nihônio",
        "massa_quantica": 284.0,
        "numero_atomico": 113,
        "simbolo": "Nh",
        "familia": "Metal do bloco p",
        "grupo": 13,
        "periodo": 7
    },
    "Fl": {
        "nome": "Fleróvio",
        "massa_quantica": 289.0,
        "numero_atomico": 114,
        "simbolo": "Fl",
        "familia": "Metal do bloco p",
        "grupo": 14,
        "periodo": 7
    },
    "Mc": {
        "nome": "Moscóvio",
        "massa_quantica": 288.0,
        "numero_atomico": 115,
        "simbolo": "Mc",
        "familia": "Metal do bloco p",
        "grupo": 15,
        "periodo": 7
    },
    "Lv": {
        "nome": "Livermório",
        "massa_quantica": 293.0,
        "numero_atomico": 116,
        "simbolo": "Lv",
        "familia": "Metal do bloco p",
        "grupo": 16,
        "periodo": 7
    },
    "Ts": {
        "nome": "Tenessino",
        "massa_quantica": 294.0,
        "numero_atomico": 117,
        "simbolo": "Ts",
        "familia": "Halogênios",
        "grupo": 17,
        "periodo": 7
    },
    "Og": {
        "nome": "Oganessônio",
        "massa_quantica": 294.0,
        "numero_atomico": 118,
        "simbolo": "Og",
        "familia": "Gases nobres",
        "grupo": 18,
        "periodo": 7
    }
}

Quimica.append(Elementos_quimicos)

def elementos_grupo(x):
    for elemento in Elementos_quimicos:
        if Quimica[0][elemento]['grupo'] ==x:
            resultado=Quimica[0][elemento]['nome']
            return resultado
def elementos_periodo(x):
    for elemento in Elementos_quimicos:
        if Quimica[0][elemento]['periodo'] ==x:
            resultado=Quimica[0][elemento]['nome']
            return resultado

def elemento_simbolo(x):
    for elemento in Elementos_quimicos:
        if Quimica[0][elemento]['simbolo'] ==x:
            resultado=Quimica[0][elemento]
            return resultado

def elemento_nome(x):
    for elemento in Elementos_quimicos:
        if Quimica[0][elemento]['nome'] ==x:
            resultado = Quimica[0][elemento]
            return resultado

    

