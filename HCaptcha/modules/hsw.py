from HCaptcha.modules.profile import Profile
import base64
import json
import random



def hsw(ua: str, req: str, href: str, toSubmit: int = False) -> str:
    
    header_encoded, payload_encoded, signature = req.split('.')
    payload_encoded += '=' * (-len(payload_encoded) % 4)
    #print(base64.b64decode(payload_encoded).decode())
    payload = json.loads(base64.b64decode(payload_encoded))
    version = payload.get("l", "").split("/c/")[1]
    
    profile = Profile(useragent=ua, 
                      payload=payload,
                      toSubmit=toSubmit)
    stack_data = []
    

    
    if toSubmit in [3]:
        stack_data = [
            "new Promise (<anonymous>)"
        ]
    
    return {
        "proof_spec": {
            "difficulty": payload.get("s", 2),
            "fingerprint_type": payload.get("f", 0),
            "_type": payload.get("t", "w"),
            "data": payload.get("d", None),
            "_location": payload.get("l", None),
            "timeout_value": float(payload.get("c", 1000))
        },
        "rand": profile.rand,
        "components": {
            "navigator": {
                "user_agent": profile.user_agent,
                "language": "en-US",
                "languages": [
                    "en-US"
                ],
                "platform": "Win32",
                "max_touch_points": 0,
                "webdriver": False,
                "notification_query_permission": None,
                "plugins_undefined": False
            },
            "screen": {
                "color_depth": 24,
                "pixel_depth": 24,
                "width": profile.screen_width,
                "height": profile.screen_height,
                "avail_width": profile.screen_width_avail,
                "avail_height": profile.screen_height_avail,
            },
            "device_pixel_ratio": profile.device_pixel_ratio,
            "has_session_storage": True,
            "has_local_storage": True,
            "has_indexed_db": True,
            "web_gl_hash": "-1",
            "canvas_hash": profile.canvas_hash,
            "has_touch": False,
            "notification_api_permission": "Denied",
            "chrome": "chrome" in profile.user_agent,
            "to_string_length": profile.to_string_length,
            "err_firefox": None,
            "r_bot_score": 0,
            "r_bot_score_suspicious_keys": [],
            "r_bot_score_2": 0,
            "audio_hash": "-1",
            "extensions": [
                False
            ],
            "parent_win_hash": profile.parent_win_hash,
            "webrtc_hash": "-1",
            "performance_hash": profile.performance_hash,
            "unique_keys": profile.unique_keys,
            "inv_unique_keys": profile.inv_unique_keys,
            "common_keys_hash": profile.common_keys_hash,
            "common_keys_tail": profile.common_keys_tail,
            "features": {
                "performance_entries": True,
                "web_audio": True,
                "web_rtc": True,
                "canvas_2d": True,
                "fetch": True
            }
        },
        "events": [],
        "suspicious_events": [],
        "messages": None,
        "stack_data": stack_data,
        "stamp": profile.stamp,
        "href": href if toSubmit [1,2,3] else None,
        "ardata": None,
        "errs": {
            "list": []
        },
        "perf": [
            [
                1,
                float(random.randint(5, 100)) + 0.0
            ],
            [
                2,
                float(random.randint(20, 300)) + 0.0
            ],
            [
                3,
                0.0
            ]
        ]
    }
