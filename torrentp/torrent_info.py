import libtorrent as lt

class TorrentInfo:
    def __init__(self, path, libtorrent):
        self._path = path
        self._lt = libtorrent
        self._info = self._lt.torrent_info(self._path)

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
