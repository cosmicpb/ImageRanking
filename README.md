# ImageRanking

Linux/Windows:

sudo apt update

sudo apt install python3-pip

wget -nc https://dl-ssl.google.com/linux/linux_signing_key.pub 

cat linux_signing_key.pub | gpg --dearmor | sudo tee /etc/apt/trusted.gpg.d/linux_signing_key.gpg  >/dev/null 

sudo sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/chrome.list' 

sudo apt update 

sudo apt install google-chrome-stable 

git clone https://github.com/cosmicpb/ImageRanking.git

cd ImageRanking

pip install -r requirements.txt

python3 imgrank.py -h <YOUR_URL> -t <SLEEP_TIME>




For Dev use, just if you run in Windows (other kind of code to do the same thing, but just in Windows)

python3 imgrank_dev_windows.py -h <YOUR_URL> -t <SLEEP_TIME>

