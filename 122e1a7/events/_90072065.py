import json

class Event:
    def __init__(self, appVersion, userAgent, deviceMemory, hardwareConcurrency, language, languages, platform, oscpu, connection, brands, mobile, mimetype_lenght, plugin_lenght, pdfViewerEnabled, unknown, rtt, webdriver, webdriver2, has_share, keyboard, isBrave, isDuckDuckGo):
        self.hash = json.dumps([
            appVersion,
            userAgent,
            deviceMemory,
            hardwareConcurrency,
            language,
            languages,
            platform,
            oscpu,
            connection, # undefined
            brands, # useragentdata in navigator only brands wihtout version
            
            mobile, # navigator.webdriver
            platform, # navigatorUAdata.platform
            
            mimetype_lenght, # navigator.mimeTypes.length
            plugin_lenght, # navigator.plugins.length
            pdfViewerEnabled, # navigator.pdfViewerEnabled
        
            unknown, #https://developer.mozilla.org/en-US/docs/Web/API/NetworkInformation/downlinkMax
            rtt,  #?
            webdriver ,# navigator.webdriver
            webdriver2 ,# navigator.hasClientInformation
            has_share ,# navigator.share
            keyboard ,# navigator.keyboard
            
            isBrave, 
            isDuckDuckGo

        ])
"""
["5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
 "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
 8,
 12,
 "en-US",
 ["en-US","en"],
 "Win32",
 null,
 ["Brave 119",
  "Chromium 119",
  "Not?A_Brand 24"],
 false,
 "Windows",2,2,true,false,null,false,false,true,"[object Keyboard]",true,false]"""     