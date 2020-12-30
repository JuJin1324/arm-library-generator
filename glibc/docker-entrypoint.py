# 참조사이트 https://wiki.beyondlogic.org/index.php?title=Cross_Compiling_BusyBox_for_ARM
import os

work_dir = os.environ['WORK_DIR']


def download_library(lib_version: str, after_download):
    download_filename = f'glibc-{lib_version}.tar.xz'
    download_url = f'http://ftp.gnu.org/gnu/libc/{download_filename}'
    os.system(f'wget {download_url}')
    os.system(f'tar -xJf {download_filename}')
    after_download(lib_version)


def make_library(lib_version: str):
    build_dir = f'{work_dir}/glibc-build'
    os.system(f'mkdir {build_dir}')

    os.system(f'cd {build_dir}; ../glibc-{lib_version}/configure arm-linux-gnueabi '
              f'--target=arm-linux-gnueabi '
              f'--build=i686-pc-linux-gnu '
              f'--prefix= '
              f'--enable-add-ons')
    os.system(f'cd {build_dir}; make -j4')
    os.system(f'cd {build_dir}; make install install_root=/home/export/{lib_version}')


def main():
    glibc_version = os.environ['GLIBC_VERSION']
    download_library(glibc_version, make_library)


if __name__ == '__main__':
    main()
