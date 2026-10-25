# Examination Testverktyg NBI

Denna inlämning siktar på betyg G. Jag har även använt Page Objekt.

## Vad som testas
För filen fav_book.py unit-testas metoderna
- add(book)
- remove(book)

För filen book_store.py unit-testas metoderna
- add_book(book)
- toggle_favorite(book) - både till True och till False

Integration mellan objekten testas med avseende på toggle True och False.

Med Playwright testas angivna user stories enligt filen STORIES.md där features-filer tagits fram utifrån dessa. 

## Att köra projektet
Jag kör mina tester från projektets root "examination_testverktyg_lena", då räcker det att skriva
- pytest
- behave
- flake8

## CI
I biblioteket workflows körs vid CI:
- unittester
- integrationstester
- flake8-tester
- playwright-tester

## Lokala tester
Lokalt kör jag pytest och behave vid commit, enligt filen .pre-commit-config.yaml.

## Angivna kriterier enligt examen
För G krävs<br>
A.	Det finns enhetstester och integrationstester för BookStore och FavoriteBooks.  
B.	Det finns user stories som täcker all funktionalitet i vyerna Katalog, Lägg till bok samt Mina böcker.  
C.	Alla user stories har minst en feature. Alla features har minst ett scenario. Alla steg implementeras i någon step-fil. 
D.	Det går att starta ditt projekt, med hjälp av instruktionerna du har skrivit i README.md.  
E.	Alla test är gröna.  

För VG krävs<br>
F.	Högre kvalitet och kod som återanvänds.  
G.	User stories som täcker in vyn statistik.  
H.	Du använder designmönstret Page Object.  
I.	Du använder Scenario Outline.  
J.	Dina features försöker täcka alla meningsfulla möjligheter för motsvarande user story.