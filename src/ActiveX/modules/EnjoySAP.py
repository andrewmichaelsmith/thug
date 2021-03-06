
import logging
log = logging.getLogger("Thug")

def LaunchGui(self, arg0, arg1, arg2):
    if len(arg0) > 1500:
        log.ThugLogging.add_behavior_warn('[EnjoySAP ActiveX] LaunchGUI overflow in arg0')

def PrepareToPostHTML(self, arg):
    if len(arg) > 1000:
        log.ThugLogging.add_behavior_warn('[EnjoySAP ActiveX] PrepareToPostHTML overflow in arg0')

def Comp_Download(self, arg0, arg1):
    log.warning(arg0)
    log.warning(arg1)
    
    url = arg0

    log.ThugLogging.add_behavior_warn("[EnjoySAP ActiveX] Fetching from URL %s" % (url, ))

    try:
        response, content = self._window._navigator.fetch(url)
    except:
        log.ThugLogging.add_behavior_warn('[EnjoySAP ActiveX] Fetch failed')
