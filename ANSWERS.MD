# Teorifrågor
Du svara kortfattat på följande frågor i ANSWERS.md för att demonstrera dina kunskaper.
1.	Vad är skillnaden mellan enhetstest, integrationstest, regressionstest och prestandatest?
2.	Beskriv hur det går till när man arbetar med TDD.
3.	Beskriv hur BDD skiljer sig från TDD.
4.	Tänk dig att du skulle göra en webbsida som liknar Läslistan, både frontend och backend. Om du fick välja förutsättningslöst, vilka sorters tester skulle du vilja använda? Motivera ditt val.

## 1 Beskriv skillnaden mellan olika tester
Vad är skillnaden mellan enhetstest, integrationstest, regressionstest och prestandatest?
+ Enhetstest - är en isolerad test för enbart den minsta beståndsdelen av koden. Passar bra att köra ofta. 
Ger exempelvis svar på att en funktion ger rätt resultat, kanske beräkning av en formel som en del av en större programkod.
+ Integrationstest - testar att flera moduler/klasser/delar fungerar tillsammans, 
så att kommunikationen dem emellan ger rätt resultat. Integrationstester upptäcker fel som enhetstester missar. 
Ger exempelvis svar på om det är fel i ett gränssnitt mellan moduler. På en högre nivå, vid systemintegrationstest, så testar man att olika system kommunicerar korrekt och ger rätt resultat. 
+ Regressionstest - testar att befintlig funktionalitet fungerar korrekt efter någon sorts ändring, 
exempelvis bugg-rättning eller tillägg av en ny funktion. Ger svar på frågan om systemet fortfarande fungerar som det ska. 
Jag har jobbat med kundprojekt där man typ vartannat år gjorde ett "lyft" till ny standardversion av kodbasen och då var man tvungen utföra väldigt många regressionstester för att se att kundunika funktioner fortfarande gav önskat resultat.  
+ Prestandatest - är en typ av icke-funktionell test som testar hur ett system beter sig under belastning. 
Ger exempelvis svar på frågan om systemet är stabilt. 
Min erfarenhet är att dessa tester görs sällan, tyvärr mest för att förstå varför något inte funkar som det ska i produktion.
## 2 Beskriv hur man arbetar med TDD
TDD är Test Driven Development, även kallat red-green-refactor eftersom testerna först ska bli röda, 
sedan gröna och sedan successivt refaktoreras och bli ännu bättre.
+ a. Det bygger på att man FÖRST skriver ett test, passar bäst för unittester, som alltså inte har någon kod att köra testen emot och därför alltid kommer att bli röd (failed). 
+ b. Sedan skriver man så pass mycket kod att testen blir grön (passed).
+ c. Sedan förbättrar man den skrivna koden utan att förändra dess beteende (målet är att testet ska fortsätta bli grönt).
+ d. sedan loopar a -b - c tills man är klar med den delen.

## 3 Beskriv hur BDD skiljer sig från TDD
BDD Behaviour Driven Development är en vidareutveckling av TDD. BDD handlar om att utvecklare, testare och verksamheten 
samarbetar för att definiera hur systemet ska bete sig utifrån användarens perspektiv. En skillnad är att man beskriver systemets 
tester som meningar på nära naturligt språk. Genom att man inte behöver vara utvecklare för att förstå testet, 
så kan även en beställare förstå vad som testas och utvecklas och vilka delar som är utförda. 
Det blir lättare att från start verifiera att test och utveckling följer de verkliga kraven som ställs på systemet, 
och man kan få fokus på affärsnyttan och belysa vilka problem som koden löser. <p>
Gherkin är ett vanligt format för att beskriva beteenden med strukturen ”given, when, then”.
+ Given – ett utgångsläge, 
+ When – en händelse eller handling,
+ Then – det förväntade resultatet. <br>

## 4 Tester i egenutvecklat system
Tänk dig att du skulle göra en webbsida som liknar Läslistan, både frontend och backend. 
Om du fick välja förutsättningslöst, vilka sorters tester skulle du vilja använda? Motivera ditt val.
+ a. Vi skulle till att börja med ha tydliga riktlinjer om hur vår produkt utvecklas och testas, så att alla följer de riktlinjer som ges oavsett om man är nyanställd eller jobbat länge. 
Alltför många gamla system lider av att inte ha ordning och kontroll och att anställda i olika perioder gör ”lite som de vill”. 
+ b1. Jag tror att krav-baserad systemutveckling är det som är framtiden. Jag har hört åsikt om IT och AI att det i framtiden är kraven som kommer att vara det värdefulla, inte själva koden. 
Med uppdaterade och omfattande krav så kan man nämligen tänka sig att AI regenerera koden snabbt, om så behövs. I mitt system sker tätt samarbete mellan utvecklare, testare och produktägare för att ta fram systemets beteende. 
Vi skulle i början utföra Event Storming, en samarbetsbaserad metodik inom IT och mjukvaruutveckling, för att snabbt kartlägga och förstå affärsprocessen. 
+ b2. Vi skriver user stories och väljer vilka vi ska börja med att utveckla i denna sprint och vilka som ska ligga kvar i backlog för senare utveckling. 
+ c. För utvalda user stories skrivs Features och acceptanskriterier, och utifrån acceptanskriterierna skapas test-scenarion med Gherkin. 
All scenarion är röda för funktionerna finns inte ännu.
+ d. Utvecklarna arbetar sedan i den ”inre loopen” och skapar unittester och utvecklar tillhörande metoder. 
Här uppstår fler tester för att täcka kantfall som inte hör hemma i Gherkin. Unit-testerna ska köras av utvecklarna innan de checkar in kod, 
men kommer också att köras automatiskt vid incheckning av kod. 
Genom att utvecklarna testat lokalt innan incheckning så är det ganska säkert att alla tester går igenom när de väl checkas in.
+ e. Varje kväll körs även integrationstesterna för att se att alla delar fortfarande samarbetar.
+ f. När enhetstesterna är gröna och funktionen inkopplad i GUI:t går Gherkin-scenarierna gröna också. 
Yttre loop (BDD) och inre loop (TDD) är klara. E2e-testerna med Playwright körs mer sällan, varannan natt, för att inte låta incheckningarna ta för långt tid 
och tester som tar extra lång tid körs något mer sällan för att garantera att e2e-testerna är klara efter natten.
(Jag har hört av utvecklare att det ibland blir ohållbart långa tider för deras e2e-selenium-tester 
failar ofta intermittent och skapar långa köer som knappt hinner köra klart under dagen. Och eftersom de knappt har unittester finns en osäkerhet i om koden är stabil så
 de måste finna sig i att köra dessa flaky tester om och om igen).
+ g. Till sist utförs manuella tester i slutet av sprinten, på de delar av systemet som är klara, med mycket exploratory testing. Det är viktigt med mänskliga tester för att befästa att det är rätt system som utvecklats.
Automationen ger mycket trygghet men det är i slutänden vi människor som kan bedöma om helhet passar oss människor som det är tänkt.
+ h. När systemet är mer färdigt inför leverans sker prestandatester, för att kontrollera att inget oväntat kommer hända när vi släpper på flera användare.