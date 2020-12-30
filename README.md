# arm-library-generator
> Docker Ubuntu 컨테이너 내에서 작업하였다.
> ARM Linux 에서 사용할 Library 를 tarball 을 다운로드 받아서 라이브러리 생성하는 것을 자동화하였다.

## 생성
> wget 을 통해서 tarball 다운로드 및 arm-linux-gcc 로 빌드 및 라이브러리 생성 과정을 .py 파이썬 파일에 정의하여 사용한다.
> 이 부분은 직접 해당 과정을 잘 알고 있으면서 정의하여야 하며 미리 로컬 OS(macOS 나 Ubuntu 추천)에서 생성해본 후 정의한다.
>
> docker-compose.yml 에 새로 라이브러리 생성을 실행할 서비스를 생성한다.

## 실행
> 터미널에서 현재 프로젝트로 이동 후 `docker-compose run glibc` 이런 식으로 docker-compose.yml 에 정의된 서비스 이름으로 
> run 을 하면 docker-entrypoint.py 가 실행되면서 
> 