# Examination Testverktyg NBI

Skriv ner i README.md: 
1) vad du har testat, och 
2) hur man startar projektet. 

Nu kan du lämna in:    
Använd PyCharm eller VS Code för att skapa en textfil med namnet "exam_mitt_namn.txt" som innehåller länk till ditt projekt på GitHub. (Om du kompletterar ska filen heta "komplettering_mitt_namn.txt".) Denna textfil ska du lämna in på Teams. Kom ihåg att göra ditt projekt publikt. Skriv gärna om du har arbetat med bara G-krav eller även VG-kraven.

Tips  
Flera element på sidan har ett test-id som du kan använda med Playwright.  
Använd headless när du kommit en bit och när du lämnar in uppgiften.  
Kom ihåg att testa navigeringen också, inte bara innehållet i vyerna.  
Rekommenderad mappstruktur för projektet (se även senaste kodexemplet, här)  

## Att köra filen
Skriv pytest



## KOM IHÅG: KÖRAS HEADLESS VID INLÄMNINGEN
Skriv pytest
används biblioteket workflows - siktar du på VG?
används filen .pre-commit-config.yaml för att testa innan github?
används filen python_ci.yml?
kontrollera markers i pytest.ini!
GÖR SNYGGARE LAYOUT FÖR MD-filen!!
kontrollera behave.ini - innehåll i den?

## För G krävs
A.	Det finns enhetstester och integrationstester för BookStore och FavoriteBooks.  
B.	Det finns user stories som täcker all funktionalitet i vyerna Katalog, Lägg till bok samt Mina böcker.  
C.	Alla user stories har minst en feature. Alla features har minst ett scenario. Alla steg implementeras i någon step-fil. (betyder att ingen user story ska vara UTAN feature, men det kan vara så att en feature täcker in två user stories)  
D.	Det går att starta ditt projekt, med hjälp av instruktionerna du har skrivit i README.md.  
E.	Alla test är gröna.  

## För VG krävs
F.	Högre kvalitet och kod som återanvänds.  
G.	User stories som täcker in vyn Statistik.  
H.	Du använder designmönstret Page Object.  
I.	Du använder Scenario Outline.  
J.	Dina features försöker täcka alla meningsfulla möjligheter för motsvarande user story.