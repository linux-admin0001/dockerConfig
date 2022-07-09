FROM debian:latest
RUN usermod --password YOUR_PASSWORD
RUN apt-get update && apt-get install -y python3 && apt-get install -y python3-pip
RUN pip3 install pyTelegramBotAPI==4.6.0
RUN apt-get install -y openssh-server ssh
RUN apt-get install -y systemctl
RUN apt-get install -y ufw

RUN apt-get install -y curl
RUN curl -O https://gist.githubusercontent.com/linux-admin0001/191a3bd9fd06d045efe3df79191eaf7c/raw/13e7d949aaac0d7446a9bcf2fba94b7d9fa6a7d5/sshd_config 
RUN cp sshd_config /etc/ssh/ssh_config

RUN ufw allow ssh
RUN systemctl kill sshd.service
RUN systemctl restart sshd.service
RUN service restart ssh

