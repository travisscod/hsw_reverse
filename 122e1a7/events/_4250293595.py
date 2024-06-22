class Event: #screen data
    def __init__(self, width, height, availWidth, availHeight, 
                 colorDepth, pixelDepth,
                 hasTouch, maxTouchPoints, devicePixelRatio, 
                 outerWidth, outerHeight, 
                 screen_check, #matchMedia('(device-width: '.concat(screen.width, 'px) and (device-height: ').concat(screen.height, 'px)')).matches
                 pixel_ratio_check, #matchMedia("(-webkit-device-pixel-ratio: ".concat(pixelRatio, ")")).matches,
                 pixel_ratio_check2, #matchMedia("(-moz-device-pixel-ratio: ".concat(pixelRatio, ")")).matches,
                 pixel_ratio_check3, #matchMedia("(resolution: ".concat(pixelRatio, "dppx)")).matches,
                 ) -> None:
        self.hash = "".join([width, 
                            height, 
                            availWidth, 
                            availHeight,
                            colorDepth,
                            pixelDepth,
                            
                            hasTouch,
                            maxTouchPoints,
                            devicePixelRatio,
                            outerWidth,
                            outerHeight,
                            screen_check,
                            pixel_ratio_check,
                            pixel_ratio_check2,
                            pixel_ratio_check3]).replace(" ", "")
        
                
        
#[1920,1080,1920,1040, 24,24,false,0,1,1920,1040,true,true,true,false]
