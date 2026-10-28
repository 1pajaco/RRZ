# morfoloske operacije
rabimo kernal, ki je pravokoten array

kalsicen setup je double for loop
glede na operacijo (erozijo ali pa dialacijo) bomo uporabili nas min oziroma max 

Dialation
D(i, j) = max(I(i,j), I((i-1),j), I((i+1),j), I(i,(j-1), I(i,(j+1))))

center kernala postane pixel ce je kateri koli vrednost ne 0 potem nastavimo center na 1

erozija 
E(i, j) = min(I(i,j), I((i-1),j), I((i+1),j), I(i,(j-1), I(i,(j+1))))

odstranili bomo tisti piksel ki je centralni element v kernal na sredini in vsi stranski so nekaj torej vse vrednosti so 1

torej se ohrani sredina ostalo gre proc

invertana slika je operacija erode inverzna dialate
operacije so destruktivne in nemoremo reversat

razlozil je odprtje/opening D(E(I)), zaprtje/closing E(D(I))

# uporabit erozije da se izbrise celotno stvar, kernal ki ima najmanj aktivnih elementov 3x3

najdi 3x3 kernal da izbrisemo celotno sliko z erozijo

[
    [1, 1, 1],
    [1, x, 0],
    [1, 0, 0]
]

[
    [1, 0, 0],
    [0, x, 0],
    [1, 0, 0]
]

[
    [0, 0 ,0 ,0 ,0, 0, 0],
    [0, 0, 0, 1, 1, 1, 0],
    [0, 0, 1, 1, 0, 0, 0],
    [0, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 0],
    [0, 0, 0, 0, 1, 0, 0],
    [0, 0 ,0 ,0 ,0, 0, 0],
]

# regije
stats, labels ~ pogosto se ozadje steje kot ena velika komponenta,
centroid ~ povprecje vseh koodrinat vseh piksolov znotraj objekta
bounding box ~ obroba komponenta, 


# kalibracija kamere
K [f 0 cx]
  [0 f cy]
  [0 0 1]

in D = [k1, k2, ...]

uporabimo sahovnico za kalibracijo

parametri distorzije ~ radialna distrozije ki ukrivi ravne crte
