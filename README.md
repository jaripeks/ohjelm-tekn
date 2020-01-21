# Git: tehtävä 1
## Komentojen ’git log’ ja ’git config –list’ tulostus paikallisesta repostasi
---
### git log
```
commit 869e2063077c44249f8066ad35b33e9a4477556f (HEAD -> master, origin/master)
Author: Jari-Pekka Salo <jari.p.salo@gmail.com>
Date:   Tue Jan 21 12:59:06 2020 +0200

    added link to repo to README.md

commit be630cf3a521c35281f8df913404d36d8743fc4b
Author: Jari-Pekka Salo <jari.p.salo@gmail.com>
Date:   Tue Jan 21 12:41:49 2020 +0200

    Removed index.html and added content to README.md

commit 925ddcc07de954d270fc361f2bc749628030b568
Author: Jari-Pekka Salo <jari.p.salo@gmail.com>
Date:   Tue Jan 21 12:39:02 2020 +0200

    added a README.md

commit 0e60dd5e8901b4f9c8139f66efa294c6ce2f2da5
Author: Jari-Pekka Salo <jari.p.salo@gmail.com>
Date:   Tue Jan 21 12:12:01 2020 +0200

    created a repo for the project
```
### git config --list
```
core.excludesfile=~/.gitignore
core.legacyheaders=false
core.quotepath=false
mergetool.keepbackup=true
push.default=simple
color.ui=auto
color.interactive=auto
repack.usedeltabaseoffset=true
alias.s=status
alias.a=!git add . && git status
alias.au=!git add -u . && git status
alias.aa=!git add . && git add -u . && git status
alias.c=commit
alias.cm=commit -m
alias.ca=commit --amend
alias.ac=!git add . && git commit
alias.acm=!git add . && git commit -m
alias.l=log --graph --all --pretty=format:'%C(yellow)%h%C(cyan)%d%Creset %s %C(white)- %an, %ar%Creset'
alias.ll=log --stat --abbrev-commit
alias.lg=log --color --graph --pretty=format:'%C(bold white)%h%Creset -%C(bold green)%d%Creset %s %C(bold green)(%cr)%Creset %C(bold blue)<%an>%Creset' --abbrev-commit --date=relative
alias.llg=log --color --graph --pretty=format:'%C(bold white)%H %d%Creset%n%s%n%+b%C(bold blue)%an <%ae>%Creset %C(bold green)%cr (%ci)' --abbrev-commit
alias.d=diff
alias.master=checkout master
alias.spull=svn rebase
alias.spush=svn dcommit
alias.alias=!git config --list | grep 'alias\.' | sed 's/alias\.\([^=]*\)=\(.*\)/\1\	 => \2/' | sort
include.path=~/.gitcinclude
include.path=.githubconfig
include.path=.gitcredential
diff.exif.textconv=exif
credential.helper=osxkeychain
user.name=Jari-Pekka Salo
user.email=jari.p.salo@gmail.com
push.default=matching
core.editor=code --wait
diff.tool=default-difftool
difftool.default-difftool.cmd=code --wait --diff $LOCAL $REMOTE
core.repositoryformatversion=0
core.filemode=true
core.bare=false
core.logallrefupdates=true
core.ignorecase=true
core.precomposeunicode=true
remote.origin.url=https://github.com/jaripeks/ohjelm-tekn.git
remote.origin.fetch=+refs/heads/*:refs/remotes/origin/*
branch.master.remote=origin
branch.master.merge=refs/heads/master
```
---
## Linkki GitHub-repoosi
[ohjelm-tekn.git](https://github.com/jaripeks/ohjelm-tekn)

---
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
>### 9. git checkout README.md
>palauttaa tiedoston README.md vastaamaan edellisen commitin tilaa

PS. En käyttänyt yhtään git config --global -komentoa, koska olin jo aiemmin kongfiguroinut käyttäjätietoni jne.