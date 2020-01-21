# Git: tehtävä 1
## Komentojen ’git log’ ja ’git config –list’ tulostus paikallisesta repostasi
```

```

## Linkki GitHub-repoosi
[ohjelm-tekn.git](https://github.com/jaripeks/ohjelm-tekn)
## Listaa käyttämäsi git-komennot ja kerro lyhyesti, mitä ne tekevät
>### 1.	git init
>luo repositoryn
>### 2.	git status
>Kertoo hakemiston (working directory) ja staging arean (en tiedä miten suomentaisin) tilan
>### 3.	git add .
>lisää hakemistossa olevat tiedostot ja hakemistot repositoryyn ja merkitsee ne otettavaksi seuraavaan committiin (Staged)
>### 4.	git commit -m ”created repo for the project”
>tallentaa muutokset kommentilla: ”created repo for the project”
>### 5.	git remote add origin https://github.com/jaripeks/ohjelm-tekn.git
>Konfiguroi hakemiston repositoryn etärepositoryksi ohjelm-tekn.git-repositoryn nimelle origin
>### 6.	git push -u origin master
>puskee origin nimiseen etärepositoryyn paikallisen repositoryn master haara
>### 7. git commit
>Avaa oletuseditoriksi konfiguroidun tekstieditorin muutoksien tallentamiseen liittyvän kommentin lisäämistä varten. Kun tekstieditori suljetaan (kommentin syöttämisen jälkeen), tallentaa muutokset repositoryyn
>### 8. git reset README.md
>palauttaa tiedoston README.md Staged vaiheesta vaiheeseen jossa sitä ei oteta mukaan seuraavaan committiin (modified)