# LRB-Decisioner

This decision making model enables you to predict the outcome of a pokemon duel

It works by computing a win coefficient from the difference in stats of the two pokemon and the type effectiveness chart 

## How to use

1. Clone this repository on your local machine

2. Install dependencies 

    ```bash
    pip install -r requirements.txt
    ```

3. Run the main program

    ```bash
    python3 main.py
    ```

4. Use the in-terminal menu to run the desired program 

```markdown
Choose a program to run:
  1. Display match matrix for all pokemon (may take a while)
  2. Display match matrix of a given team
  3. Predict match team vs single pokemon
  4. Predict match single pokemon vs single pokemon
  5. Exit
```

## Authors

**Team LRB**
Damien Goupil: made the stats coefficient program
Ewan Lansonneur: made the type effectiveness program
Maxime Perrot: made the main program
