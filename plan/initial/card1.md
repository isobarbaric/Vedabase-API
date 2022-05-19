# General

provide access to the following books:
- Bhagavad-gītā As It Is
- Śrīmad-Bhāgavatam (Bhāgavata Purāṇa)
- Śrī Caitanya-caritāmṛta

for all of them, create classes for all of them 

# Bhagavad-gītā As It Is

- deal with these parts of the book individually
    - Setting the Scene
    - Dedication
    - Preface
    - Introduction
    - A Note About the Second Edition
- for the ``Chapter``s:
    - variables
        - chapter number
        - chapter title
        - list of ``Text`` objects
    - API methods unique to ``Chapter`` objects are getters for the first 2 variables mentioned
- for the ``Text``s:
    - variables
        - text number
        - text devanagri
        - text romanization
        - synonyms
        - translation
        - purport
    - API methods unique to ``Text`` objects are getters for the variables mentioned above

for the API itself, have to figure out the routes for the calls themselves individually later and there, can combine calls to these functions

# Śrīmad-Bhāgavatam (Bhāgavata Purāṇa)

- to be dealt with separately from the Canto objects themselves 
    - dedication 
    - preface
    - introduction
- for the ``Canto``'s:
    - variables 
        - list of ``Chapter`` objects
    - API methods unique to ``Canto`` objects are getters for the variables mentioned above

# Śrī Caitanya-caritāmṛta

- variables
    - main book object should contain three ``Lila`` objects
        - Adi-lila
        - Madhya-lila
        - Antya-lila 
- for the ``Lila``s:
    - dedication
    - introduction
    - preface
    - foreword
    - list of ``Chapter`` objects 