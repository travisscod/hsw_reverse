from HCaptcha.modules.stamp import get_stamp
from random import choice
from HCaptcha.modules.hash import *
from HCaptcha.modules.encode import encrypt
import json

class Profile:
    # ON SUBMIT CAPTCHA OONLY

    

    COMMON_KEYS_TAIL = "chrome,caches,cookieStore,ondevicemotion,ondeviceorientation,ondeviceorientationabsolute,launchQueue,documentPictureInPicture,onbeforematch,getScreenDetails,queryLocalFonts,originAgentCluster,speechSynthesis,oncontentvisibilityautostatechange,onscrollend,webkitRequestFileSystem,webkitResolveLocalFileSystemURL,Raven",
    SCREEN_SIZES = [{
        "width": 1920,
        "height": 1080,
    }, {
        "width": 1680,
        "height": 1050,
    }, {
        "width": 1440,
        "height": 900,
    }, {
        "width": 1366,
        "height": 768,
    }, {
        "width": 1280,
        "height": 800,
    }, {
        "width": 1280,
        "height": 720,
    }, {
        "width": 1024,
        "height": 768,
    }, {
        "width": 800,
        "height": 600,
    }, {
        "width": 640,
        "height": 480,
    }]
    
    
    AVAIL_SCREEN_SIZES = [{
        "width": 1920,
        "height": 1040,
    }, {
        "width": 1680,
        "height": 1010,
    }, {
        "width": 1440,
        "height": 870,
    }, {
        "width": 1366,
        "height": 728,
    }, {
        "width": 1280,
        "height": 780,
    }, {
        "width": 1280,
        "height": 700,
    }, {
        "width": 1024,
        "height": 748,
    }, {
        "width": 800,
        "height": 580,
    }, {
        "width": 640,
        "height": 460,
    }]
    #TODO: 
    #fix hashne
    #fix hele fp
    
    
    def __init__(self, useragent, payload, toSubmit=False):
        self.user_agent = useragent
        self.stamp = get_stamp(payload.get("s", 2), payload.get("d", None))
        self.rand = [choice(range(100000000000, 999999999999)) / 1000000000000]
        self.version = payload.get("l", "").split("/c/")[1]
        
        screen_index = 0#choice(range(len(self.SCREEN_SIZES)))
        
        self.screen_width = self.SCREEN_SIZES[screen_index]["width"]
        self.screen_height = self.SCREEN_SIZES[screen_index]["height"]
        self.screen_width_avail = self.AVAIL_SCREEN_SIZES[screen_index]["width"]
        self.screen_height_avail = self.AVAIL_SCREEN_SIZES[screen_index]["height"]        
        self.device_pixel_ratio = 0.8999999761581421#choice([1, 1.25, 1.5, 0.7])

        self.to_string_length = 33
        self.canvas_hash = random_hash(19)
        self.parent_win_hash = random_hash(20) if toSubmit else None
        self.performance_hash = random_hash(19)
        
        self.unique_keys = self.get_unq(toSubmit) if toSubmit in [1,2,3] else None
        self.inv_unique_keys = self.get_inv(toSubmit) if toSubmit in [1,2,3] else None
        self.common_keys_hash = random_hash(10) if toSubmit in [1,2,3] else None
        self.common_keys_tail = self.COMMON_KEYS_TAIL if toSubmit in [1,2,3] else None
        
        self.events = [
            [
                3070040703,
                #"6981242729856591669"
                random_hash(19)
            ],
            [
                3756317564,
                #"2337666753322697468"
                random_hash(19)
            ],
            [
                334928754,
                #"11162578751185176535"
                random_hash(20)
            ],
            [
                873741287,
                "[-21.69165302782324,10457,16567]"
            ],
            [
                3719249172,
                #"9763902456468889070"
                random_hash(19)
            ],
            [
                2998564779,
                "[60,71,65536,245760,245759]"
            ],
            [
                2371850788, # FALSE WHATEVER IDK
                "false"
            ],
            [
                1068771096, # NO IDEA EITHER
                "623"
            ],
            [
                3498175614, 
                json.dumps(json.dumps(encrypt("2200263562"))) # RANDOM HASH
            ],
            [
                3916977893, # 669213918 MEN ENCODED
                json.dumps([json.dumps(encrypt("Google Inc. (Google)")), json.dumps(encrypt("ANGLE (Google, Vulkan 1.3.0 (SwiftShader Device (Subzero) (0x0000C0DE)), SwiftShader driver)"))])
            ],
            [
                748900772,
                #"8383473043360077444"
                random_hash(19)
            ],
            [
                1587819988,
                #"3313549113868922289"
                random_hash(19)
            ],
            [
                3957763561,
                "[\"Windows\",\"10.0.0\",null,\"64\",\"x86\",\"119.0.0.0\"]"
            ],
            [
                137519462,
            # "16849396538752381139"
                random_hash(20)
            ],
            [
                3311072794,
                "1096"
            ],
            [
                669213918, # WEBGL YE
                "[\"Google Inc. (Google)\",\"ANGLE (Google, Vulkan 1.3.0 (SwiftShader Device (Subzero) (0x0000C0DE)), SwiftShader driver)\"]"
            ],
            [
                3952131478,
                "[20]"
            ],
            [
                2571358880, # TID WHATEVER
                "[\"Europe/Copenhagen\",-60,-60,-3203646808000,\"Central European Standard Time\",\"en-US\"]"
            ],
            [
                1373138784, #IMG ?
                "[[\"img:imgs3.hcaptcha.com\",0,116.5],[\"navigation:newassets.hcaptcha.com\",0,15],[\"script:newassets.hcaptcha.com\",33,9],[\"xmlhttprequest:api.hcaptcha.com\",0,194.5]]"
            ],
            [
                255383392, # NOK WEBGL HASH AF IDK HAR IKKE TJEKKET ENDNU
                "[2147483647,2147483647,4294967294]"
            ],
            [
                872174808, #HEADERS?
                "[\"5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36\",\"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36\",4,6,\"en-US\",[\"en-US\"],\"Win32\",null,[\"Brave 119\",\"Chromium 119\",\"Not?A_Brand 24\"],false,\"Windows\",2,4,true,false,null,false,false,true,\"null\",true,false]"
            ],
            [
                338869435,
            # "15814981228744257825"
                random_hash(20)
            ],
            [
                2691352878,
                "17514"
            ],
            [
                3913991343, # STRING LEN ?
                "33"
            ],
            [
                1877814445, # NOK STATIC VILLE JEG GÆTTE
                "[1,2,3,4]"
            ],
            [
                2881608941, #NOGET PERFORMANCE TID NOGET LIGESOM ohr
                "57"
            ],
            [
                143592240, #VILLE GÆTT MOUSEMOV MEN IDK
                "[[105,[104,105,104,255,104,104,105,255,104,104,104,255,105,104,105,255]],[[11,0,0,95.96875,15,4,96.765625],[[12,0,-1,113.125,17,4,113],[11,0,0,111,12,4,111],[11,0,0,95.96875,15,4,96.765625],[11,0,0,95.96875,15,4,96.765625],[11,0,0,95.96875,15,4,96.765625],[11,0,0,95.96875,15,4,96.765625],[11,0,0,95.96875,15,4,96.765625],[11,0,0,95.96875,15,4,96.765625],[12,0,0,109.640625,14,3,110.1953125]]],[0,2,4,5,6,8,9,12,13,15,17,18,19,21,22,23,28,29,30,31,33,34,35,37,39,42,47,48,49,66,67,69,71,72,75,76,77,78,79,81,82],[0,0,0,0,14,3,0]]"
            ],
            [
                2460707167,
                "[1,4,5,7,9,12,20,21,24,25,29,32]"
            ],
            [
                2906236335, # JS 
                f"[[[\"https://newassets.hcaptcha.com/captcha/v1/18fa736/hcaptcha.js\",0,5]],[[\"*\",84,9]]]"
            ],
            [
                1587180961,
                #"1715020872265"
                random_hash(13)
            ],
            [
                1350382849, # 8w6 HASH AF TING NOKJ
                "[[277114314453,277114314460,277114314451,357114314456,277114314452,554228628898,57114314443,717114314371391,554228628897,277114314456,1108457257862,277114314450,554228628919,277114314460,277114314451],false]"
            ],
            [
                2622130410,
                "[8192,64,16384,2048,15,2048]"
            ],
            [
                137955265,
                "\"Europe/Copenhagen\""
            ],
            [
                1335970363,
                #"8618185792084308427"
                random_hash(19)
            ],
            [
                3827436525,
                #"15307345790125003576"
                random_hash(20)
            ],
            [
                4086018371,
                "[[true,\"en-US\",true,\"Microsoft David - English (United States)\",\"Microsoft David - English (United States)\"],[false,\"en-US\",true,\"Microsoft Mark - English (United States)\",\"Microsoft Mark - English (United States)\"],[false,\"en-US\",true,\"Microsoft Zira - English (United States)\",\"Microsoft Zira - English (United States)\"]]"
            ],
            [
                531197711,
                "107"
            ],
            [
                1421982308,
                "[2147483648,2200263562,null,null,4294705152,true,true,true,null]"
            ],
            [
                2151859767,
                "[[\"loadTimes\",\"csi\",\"app\"],35,34,null,false,false,true,37,false,true,true,true,true,[\"Raven\",\"_sharedLibs\",\"hsw\",\"__wdata\",\"image_label_binary\"],[[\"getElementsByClassName\",[]],[\"getElementById\",[]],[\"querySelector\",[]],[\"querySelectorAll\",[]]],[],true]"
            ],
            [
                690142092,
                "[8192,8192,8192,8,8,4]"
            ],
            [
                3082579163,
                #"10070449724236879769"
                random_hash(20)
            ],
            [
                2115854713, # Europe/Copenhagen
                json.dumps(json.dumps(encrypt("Europe/Copenhagen")))
            ],
            [
                443486963,
                #"12358398885081326346"
                random_hash(20)
            ],
            [
                2854298529,
                "60"
            ],
            [
                2275435905,
                #"4631229088072584217"
                random_hash(19)
            ],
            [
                1311261287,
                "[4,128,4]"
            ],
            [
                1613898511,
                #"17002384262467705698"
                random_hash(20)
            ],
            [
                3497821731,
                "[1,1023,1,1,4]"
            ],
            [
                694616987, # SCREEN SIZE STUFF 
                "[1920,1040,1920,1040,24,24,false,0,0.8999999761581421,1920,1040,false,true,true,false]"
            ],
            [
                2232178856,
                "[2147483647,2147483647,2147483647,2147483647]"
            ],
            [
                1405859696,
                "[16,4096,31,32,16383,123,14,127,[23,127,127]]"
            ],
            [
                3725196262,
                "[32,4096,16384,7,14,127,[23,127,127]]"
            ],
            [
                414144794,
                "[-6.172841548919678,-20.71068000793457,120.71069145202637,-20.71068000793457,141.42137145996094,120.71069145202637,-20.71068000793457,141.42137145996094,-20.71068000793457,-20.71068000793457,0,0,400.0000305175781,600,true]"
            ]
        ]
        self.events = random.shuffle(self.events)
        
        
        #print(self.canvas_hash)
    def get_unq(self, submit_type):
        if submit_type == 1:
            return "__localeData__,regeneratorRuntime,__isReactDndBackendSetUp,0,__BILLING_STANDALONE__,webpackChunkdiscord_app,platform,__SECRET_EMOTION__,__SENTRY__,hcaptcha,hcaptchaOnLoad,__timingFunction,DiscordErrors,clearImmediate,__OVERLAY__,grecaptcha,DiscordSentry,GLOBAL_ENV,setImmediate,1,IntlPolyfill,_ws,__DISCORD_WINDOW_ID"
        elif submit_type == 2:
            return "GLOBAL_ENV,_ws,0,__OVERLAY__,hcaptcha,__localeData__,IntlPolyfill,__timingFunction,grecaptcha,DiscordSentry,1,hcaptchaOnLoad,clearImmediate,setImmediate,DiscordErrors,__BILLING_STANDALONE__,__DISCORD_WINDOW_ID,webpackChunkdiscord_app,__SECRET_EMOTION__,regeneratorRuntime,platform,__isReactDndBackendSetUp,__SENTRY__"
        elif submit_type == 3:
            return "__SECRET_EMOTION__,IntlPolyfill,regeneratorRuntime,__isReactDndBackendSetUp,DiscordErrors,1,__localeData__,hcaptchaOnLoad,_ws,DiscordSentry,grecaptcha,__BILLING_STANDALONE__,clearImmediate,hcaptcha,platform,__timingFunction,webpackChunkdiscord_app,__DISCORD_WINDOW_ID,0,__SENTRY__,GLOBAL_ENV,__OVERLAY__,setImmediate"
        else:
            print("ERRROR???" + str(submit_type))
            return "ERROR"
        
    def get_inv(self, submit_type):
        if submit_type == 1:
            return "__wdata,sessionStorage,localStorage,hsw,_sharedLibs,_length,offset"
        elif submit_type == 2:
            return "sessionStorage,hsw,image_label_binary,offset,__wdata,_length,_sharedLibs,localStorage"
        elif submit_type == 3:
            return "__wdata,text_free_entry,hsw,offset,image_label_binary,localStorage,_length,_sharedLibs,sessionStorage"
        else:
            print("ERRRO2R???" + str(submit_type))
            return "ERROR"
        
        
        