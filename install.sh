if ! command -v pip &> /dev/null
then
    sudo apt install python-pip
fi

sudo cp ./service /lib/systemd/system/nissan.service
sudo chmod 644 /lib/systemd/system/nissan.service
chmod -R +x ./
sudo python -m pip install -r requirements.txt
sudo systemctl daemon-reload
sudo systemctl enable nissan.service
sudo systemctl start nissan.service
