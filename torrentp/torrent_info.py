import libtorrent as lt

class TorrentInfo:
    def __init__(self, path_or_magnet, libtorrent, session):
        self._lt = libtorrent
        self._session = session
        self._info = None
        if path_or_magnet.startswith("magnet:"):
            self._info = self._download_metadata(path_or_magnet)
        else:
            self._info = self._lt.torrent_info(path_or_magnet)

    def _download_metadata(self, magnet_uri):
        magnet_handle = self._lt.add_magnet_uri(self._session, magnet_uri, {'save_path': '.'})
        while not magnet_handle.has_metadata():
            time.sleep(1)
        return magnet_handle.get_torrent_info()

    def list_files(self):
        """ List files in the torrent """
        file_list = []
        for file_index, file in enumerate(self._info.files()):
            file_list.append({"id": file_index, "file": file.path})
        return file_list

    def create_torrent_info(self):
        self._info = self._lt.torrent_info(self._path)
        return self._info

    def __str__(self):
        return f"TorrentInfo(path={self._path})"

    def __repr__(self):
        return f"TorrentInfo(path={self._path})"

    def __call__(self):
        return self.create_torrent_info()
