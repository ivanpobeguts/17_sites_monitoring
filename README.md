# Sites Monitoring Utility

The script analyzes file with urls and shows if url's HTTP status is 200
and if there are more than 30 days until expiration date. 

# Instalation

Script requires Python 3.5 and some dependencies. You can instal it whith the following command:

```bash
$ pip instal -r requirements.txt
```   

# Example

Script waits for one parameter - path to file with urls. Example:

**urls:**
https://stackoverflow.com/questions/9381463/how-to-create-a-file-in-linux-from-terminal-window
https://www.aton.ru/
https://github.com/ivanpobeguts
http://sdfsdf.sdf/sdf
https://www.livelib.ru/
iofdupa

```bash
$ python check_sites_health.py urls.txt

url: https://stackoverflow.com/questions/9381463/how-to-create-a-file-in-linux-from-terminal-window
Is url ok:  yes
Is domain expired:  yes
------------------------------
url: https://www.aton.ru/
Is url ok:  yes
Is domain expired:  yes
------------------------------
url: https://github.com/ivanpobeguts
Is url ok:  yes
Is domain expired:  yes
------------------------------
url: http://sdfsdf.sdf/sdf
Is url ok:  no
Is domain expired:  no
------------------------------
url: https://www.livelib.ru/
Is url ok:  yes
Is domain expired:  yes
------------------------------
url: iofdupa
Is url ok:  no
Is domain expired:  no
------------------------------

```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
