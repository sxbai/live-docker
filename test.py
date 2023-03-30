from downloader import Downloader
from aliyundrive import AliyunDrive

class Test():
    def proxy_download_file(self):
        base_headers = {
            'User-Agent':
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.54 Safari/537.36',
            'Referer': 'https://www.aliyundrive.com/',
        }
        token = '3e374496576f4207892601fb18010d84'
        share_id = 'bK2yk6nHWhi'
        file_id = '6401fa3e5762fc021b374837b6339f3bc1e719f0'
        headers = base_headers.copy()
        connection = 15
        def get_url_and_headers():
            return AliyunDrive()._get_download_url(share_id, file_id, token), headers.copy()

        headers.update({'Range': 'bytes=0-'})
        downloader = Downloader(
            get_url_and_headers=get_url_and_headers,
            headers=headers,
            connection=connection,
        )
        res_headers = downloader.start()
        with open('tmp/a.mkv', 'wb') as f:
            while True:
                chunk = downloader.read()
                if chunk is None:
                    print('eof')
                    break
                print(len(chunk), '?')
                f.write(chunk)

            #print(chunk)

if __name__ == '__main__':
    res = Test().proxy_download_file()
    print(res)