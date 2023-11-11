import libtorrent as lt

class Session:
    def __init__(self, libtorrent):
        self._user_agent = 'python client v0.1'
        self._listen_interfaces = '0.0.0.0'
        self._port = '6881'
        self._lt = libtorrent
        self._session = None

    def create_session(self):
        # Membuat dan mengonfigurasi sesi libtorrent
        settings = {
            'user_agent': self._user_agent,
            'listen_interfaces': f'{self._listen_interfaces}:{self._port}',
            'download_rate_limit': 0,
            'upload_rate_limit': 0
        }
        self._session = self._lt.session(settings)
        return self._session

    def set_download_limit(self, rate=0):
        # Mengatur batas kecepatan unduhan
        rate_limit = int(rate * 1024) if rate > 0 else -1
        self._session.set_download_rate_limit(rate_limit)

    def set_upload_limit(self, rate=0):
        # Mengatur batas kecepatan unggahan
        rate_limit = int(rate * 1024) if rate > 0 else -1
        self._session.set_upload_rate_limit(rate_limit)

    def get_upload_limit(self):
        # Mendapatkan batas kecepatan unggahan saat ini
        return self._session.upload_rate_limit()

    def get_download_limit(self):
        # Mendapatkan batas kecepatan unduhan saat ini
        return self._session.download_rate_limit()

    def __str__(self):
        return "Session for torrent client."

    def __repr__(self):
        return "Session for torrent client."

    def __call__(self):
        return self.create_session()
