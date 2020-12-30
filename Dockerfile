# 참조사이트 https://wiki.beyondlogic.org/index.php?title=Cross_Compiling_BusyBox_for_ARM

FROM ubuntu
LABEL maintainer="jujin1324@edaum.net"

RUN apt-get update && apt-get install -y gcc-arm-linux-gnueabi \
g++-arm-linux-gnueabi \
libncurses5-dev \
libc6-dev-i386 \
libstdc++-9-dev \
gawk \
wget \
xz-utils \
make \
bison \
python3

WORKDIR /home/app



