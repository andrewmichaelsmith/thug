# jetAudio "DownloadFromMusicStore()" Arbitrary File Download Vulnerability
# CVE-2007-4983

import logging
log = logging.getLogger("Thug")

def DownloadFromMusicStore(self, url, dst, title, artist, album, genere, size, param1, param2):
    log.ThugLogging.add_behavior_warn('[JetAudio ActiveX] Downloading from URL %s (saving locally as %s)' % (url, dst, ))

    try:
        response, content = self._window._navigator.fetch(url)
    except:
        log.ThugLogging.add_behavior_warn('[JetAudio ActiveX] Fetch failed')
