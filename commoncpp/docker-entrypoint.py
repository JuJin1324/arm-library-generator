# 참조사이트 https://wiki.beyondlogic.org/index.php?title=Cross_Compiling_BusyBox_for_ARM
import os

work_dir = os.environ['WORK_DIR']


def download_library(lib_version: str, after_download):
    download_filename = f'commoncpp2-{lib_version}.tar.gz'
    download_url = f'https://ftp.gnu.org/gnu/commoncpp/{download_filename}'
    os.system(f'wget {download_url}')
    os.system(f'tar -xvf {download_filename}')
    after_download(lib_version)


def make_library(lib_version: str):
    build_dir = f'{work_dir}/commoncpp2-build'
    os.system(f'mkdir {build_dir}')

    os.system(f'cd {build_dir}; ../commoncpp2-{lib_version}/configure arm-linux-gnueabi '
              f'--target=arm-linux-gnueabi '
              f'--build=i686-pc-linux-gnu '
              f'--prefix= '
              f'--enable-add-ons')
    os.system(f'cd {build_dir}; make -j4')
    os.system(f'cd {build_dir}; make install install_root=/home/export/{lib_version}')


def main():
    commoncpp_version = os.environ['COMMONCPP_VERSION']
    download_library(commoncpp_version, make_library)


if __name__ == '__main__':
    main()
