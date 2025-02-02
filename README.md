# Bidoo Link Opener

Questo script automatizza il login e l'apertura di link da un file di testo su **Bidoo**, un sito di aste online. Utilizza Selenium WebDriver per interagire con il sito e può essere facilmente configurato per operazioni di scraping o navigazione automatica.

## Funzionalità

- **Login automatico**: Accede al sito di **Bidoo** utilizzando le credenziali fornite.
- **Verifica del login**: Controlla se il login è riuscito verificando la presenza di un elemento specifico.
- **Estrazione di URL**: Estrae i link da un file di testo e verifica che siano URL validi.
- **Apertura dei link**: Apre i link uno alla volta, con una pausa casuale tra 2 e 3 secondi per evitare richieste troppo veloci.

## Problemi noti

- **CAPTCHA**: Se il sito **Bidoo** presenta un CAPTCHA durante il login o l'interazione con i link, lo script potrebbe non funzionare correttamente. Il CAPTCHA richiede l'intervento manuale per confermare che l'utente è un essere umano, impedendo la corretta automazione del processo.

## Requisiti

Per eseguire questo script, è necessario avere i seguenti prerequisiti:

- **Python 3.x**
- **Selenium**
- **Edge WebDriver**
- **dotenv** per gestire le variabili d'ambiente

## Installazione

1. Clona il repository:

    ```bash
    git clone https://github.com/xRubby/BidooLinkOpener.git
    cd BidooLinkOpener
    ```

2. Crea un ambiente virtuale (opzionale ma consigliato):

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # su Windows usa venv\Scripts\activate
    ```

3. Installa le dipendenze:

    ```bash
    pip install -r requirements.txt
    ```

4. Scarica il [Microsoft Edge WebDriver](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/) compatibile con la tua versione di Edge.

5. Crea un file `.env` nella directory principale del progetto e aggiungi le seguenti variabili di ambiente:

    ```
    EMAIL=tua_email@example.com
    PASSWORD=tua_password
    ```

## Come Usare

1. Crea un file `links.txt` nella directory principale del progetto, contenente i link che vuoi che lo script apra, uno per riga.
2. Esegui lo script:

    ```bash
    python main.py
    ```

Lo script eseguirà automaticamente il login su **Bidoo** utilizzando le credenziali fornite nel file `.env`, verificherà se il login è stato effettuato correttamente, e aprirà ogni link presente nel file `links.txt`.
