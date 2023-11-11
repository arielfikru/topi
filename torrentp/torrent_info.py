import libtorrent as lt

class TorrentInfo:
    def __init__(self, path_or_magnet, libtorrent):
        self._lt = libtorrent
        if path_or_magnet.startswith("magnet:"):
            self._info = self._lt.parse_magnet_uri(path_or_magnet)
        else:
            self._info = self._lt.torrent_info(path_or_magnet)

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
