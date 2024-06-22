from main import HCaptcha
import json
import tls_client
import secrets
import base64

def pack_msg(data):
    return base64.b64encode(data.encode()).decode()

token = "MTIyNjI2OTc1MzQ0Njg5MTU1Mg.GwG9nE.U6J6Tup2JR49AUbd3YbfEoPhEegoZHoOijYzFY"

headers = {
    "accept": "*/*",
    "accept-language": "en-US,en;q=0.5",
    "authorization": token,
    "content-type": "application/json",
    "sec-ch-ua": "\"Not_A Brand\";v=\"8\", \"Chromium\";v=\"120\", \"Brave\";v=\"120\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.199 Safari/537.36",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "sec-gpc": "1",
    "x-context-properties": pack_msg('{"location":"Invite Button Embed","location_guild_id":null,"location_channel_id":null,"location_channel_type":1,"location_message_id":null"}'),
    "x-debug-options": "bugReporterEnabled",
    "x-discord-locale": "es-ES",
    "x-discord-timezone": "Europe/Copenhagen",
    "x-super-properties": pack_msg('{"os":"Windows","browser":"Chrome","device":"","system_locale":"en-US","browser_user_agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.199 Safari/537.36","browser_version":"119.0.6045.199","os_version":"10","referrer":"","referring_domain":"","referrer_current":"","referring_domain_current":"","release_channel":"stable","client_build_number":259048,"client_event_source":null,"design_id":0}')
}


_data = {"session_id": secrets.token_hex(16)  }

invite_code = "skid".replace("https://discord.gg/", "").replace(".gg/", "").replace("https://discord.com/", "")
ses = tls_client.Session(client_identifier="chrome124")

def req():
    response = ses.post(f"https://discord.com/api/v9/invites/{invite_code}", headers=headers, data=json.dumps(_data))
    if "captcha" in response.text:
        data = response.json()
        code = HCaptcha(data["captcha_sitekey"], "https://discord.gg/" + invite_code).solve(response.json()["captcha_rqdata"])

        if code is None:
            print("Failed to solve captcha :()")
            return req()

        headers["x-captcha-key"] = code
        headers["x-captcha-rqtoken"] = data["captcha_rqtoken"]
        
        #print(json.dumps(headers, indent=4))
        
        response = ses.post(f"https://discord.com/api/v9/invites/{invite_code}", headers=headers, data=json.dumps(_data))
        if "captcha" in response.text:
            print("Failed to solve captcha")
            return req()
        print(response.text, "22")
    else:
        print(response.text, "55")

    
    
req()