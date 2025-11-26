# A handmade list of frequent entities picked up by the NER that are inaccurate or provide irrelevant information

undesired_entities = [
    "Venice",           # The city everything happens in, not very interesting
    "Italy",
    "St. Stephen's",    # Markers of time periods an opera was performed in during a certain year
    "St. Martin's",
    "St. Luke's",
    "Ascension",
    "Bonlini",          # Musicologists the opera list is based on
    "Groppo",
    "Groppo MS",
    "Galvani",
    "Galvani SSal",
    "Wiel",
    "Giovanni",         # Not enough information to accurately identify the entities
    "Angelo",
    "Paolo",
    "Gio",
    "Marc",
    "Pietro",
    "Giovanni Rossi",   # Unusable for various reasons
    "Arias",            # Elements wrongly identified as entities
    "US",
    "Performed",
    "Diario",
    "La",
    "pp",
    "Vqs",
    "Cod",
    "GB",
    "Rvat",
    "NV",
    "Suppl",
    "Repertoire",
    "Carteggio da Venezia",
]


# A list of the valid entities that were extracted

probably_good_entities = [
    "Naples",               # Cities/Regions other than Venice
    "Neapolitan",
    "Rome",
    "London",
    "Vienna",
    "Bologna",
    "Mantua",
    "Mantuan",
    "Milan",
    "Florence",
    "Verona",
    "Modena",
    "Paris",
    "Dresden",
    "Padua",
    "Vicenza",
    "England",
    "France",
    "Prague",
    "Pietro Metastasio",    # The composers/librettists of the operas
    "Metastasio",
    "Antonio Vivaldi",
    "Vivaldi",
    "Francesco Silvani",
    "Silvani",
    "Carlo Francesco Pollarolo",
    "Apostolo Zeno",
    "Zeno",
    "Goldoni",
    "Tomaso Albinoni",
    "Albinoni",
    "Grimani",
    "Antonio Ziani",
    "Caldara",
    "Handel",
    "Galuppi",
    "Domenico Lalli",
    "Carlo Pallavicino",
    "Francesco Gasparini",
    "Hasse",
    "San Cassiano",     # The theaters
    "San Salvatore",
    "San Samuele",
]

STOPPED AT HASSE