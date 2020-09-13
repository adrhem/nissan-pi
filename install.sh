sudo cp ./service /lib/systemd/system/nissan.service
sudo chmod 644 /lib/systemd/system/nissan.service
chmod -R +x ./
sudo systemctl daemon-reload
sudo systemctl enable nissan.service
sudo systemctl start nissan.service