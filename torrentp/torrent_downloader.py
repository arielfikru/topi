from .session import Session
from .torrent_info import TorrentInfo
from .downloader import Downloader
import libtorrent as lt

class TorrentDownloader:
    def __init__(self, path_or_magnet, save_path):
        self._file_path = path_or_magnet
        self._file_path = file_path
        self._save_path = save_path
        self._downloader = None
        self._torrent_info = None
        self._lt = lt
        self._file = None
        self._add_torrent_params = None
        self._session = Session(self._lt)

    def start_download(self, download_speed=0, upload_speed=0):
        if self._file_path.startswith('magnet:'):
            self._add_torrent_params = self._lt.parse_magnet_uri(self._file_path)
            self._add_torrent_params.save_path = self._save_path
            self._downloader = Downloader(session=self._session(), torrent_info=self._add_torrent_params,
                                          save_path=self._save_path, libtorrent=lt, is_magnet=True)

        else:
            self._torrent_info = TorrentInfo(self._file_path, self._lt)
            self._downloader = Downloader(session=self._session(), torrent_info=self._torrent_info(),
                                          save_path=self._save_path, libtorrent=None, is_magnet=False)

        self._session.set_download_limit(download_speed)
        self._session.set_upload_limit(upload_speed)

        self._file = self._downloader
        self._file.download()

    def list_torrent_files(self):
        """ List files in the torrent """
        torrent_info = TorrentInfo(self._file_path, self._lt)
        return torrent_info.list_files()

    def __str__(self):
        return f"TorrentDownloader(file_path={self._file_path}, save_path={self._save_path})"

    def __repr__(self):
        return f"TorrentDownloader(file_path={self._file_path}, save_path={self._save_path})"

    def __call__(self):
        pass
