# umamusume-auto

This project is for automation of a smartphone application called *Umamusume Pretty Derby* by Cygames.  
https://umamusume.jp/

## Prerequisite
* pyenv
* Pipenv
* adb (Android Debug Bridge)

## How to start
```
cd umamusume-auto
pipenv install
pipenv run python main.py umamusume_name
```

## What this Python script can do
* Start *Umamusume* application
* Start *Aoharu* training(アオハルトレーニング) with random parents(継承ウマ娘) and random support cards
* Going out in all the training so that the training can finish ASAP and increment the training count to complete missions
* Playable character: *Mejiro McQueen(メジロマックイーン)*

```
pipenv run python main.py mejiro_mcqueen
``` 
