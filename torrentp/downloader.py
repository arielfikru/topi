import sys
import time

class Downloader:
    def __init__(self, session, torrent_info, save_path, libtorrent, is_magnet):
        self._session = session
        self._torrent_info = torrent_info
        self._save_path = save_path
        self._file = None
        self._status = None
        self._name = ''
        self._state = ''
        self._lt = libtorrent
        self._add_torrent_params = None
        self._is_magnet = is_magnet

    def status(self):
        if not self._is_magnet:
            self._file = self._session.add_torrent({'ti': self._torrent_info, 'save_path': f'{self._save_path}'})
            self._status = self._file.status()
        else:
            self._add_torrent_params = self._torrent_info
            self._add_torrent_params.save_path = self._save_path
            self._file = self._session.add_torrent(self._add_torrent_params)
            self._status = self._file.status()
        return self._status

    def download(self):
        print(f'Start downloading {self.name}')
        while not self._status.is_seeding:
            s = self.status()
            print('\r%.2f%% complete (down: %.1f kB/s up: %.1f kB/s peers: %d) %s' % (
                s.progress * 100, s.download_rate / 1000, s.upload_rate / 1000,
                s.num_peers, s.state), end=' ')
            sys.stdout.flush()
            time.sleep(1)
        print(self._status.name, 'downloaded successfully.')

    def download_specific_file(self, file_id):
        """Download a specific file by its ID."""
        if self._is_magnet:
            self._wait_for_metadata()

        file_priorities = [0] * len(self._file.get_torrent_info().files())
        if 0 <= file_id < len(file_priorities):
            file_priorities[file_id] = 1  # Download only the file with the given ID

        self._file.prioritize_files(file_priorities)
        self.download()

    def _wait_for_metadata(self):
        """Wait for metadata to be available."""
        while not self._file.has_metadata():
            time.sleep(1)

    @property
    def name(self):
        self._name = self.status().name
        return self._name

    def __str__(self):
        return f"Downloader(name={self._name}, state={self._state})"

    def __repr__(self):
        return f"Downloader(name={self._name}, state={self._state})"

    def __call__(self):
        pass
