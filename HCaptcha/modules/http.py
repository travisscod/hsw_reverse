import tls_client
import requests

class Request:
    
    def __init__(self) -> None:
        
        tls_data = requests.get("https://tls.peet.ws/api/all").json()
        self.session = tls_client.Session(
            client_identifier = "chrome120",
            ja3_string = tls_data["tls"]["ja3"],
            h2_settings={
                "HEADER_TABLE_SIZE": 65536,
                "MAX_CONCURRENT_STREAMS": 1000,
                "INITIAL_WINDOW_SIZE": 6291456,
                "MAX_HEADER_LIST_SIZE": 262144
            },
            h2_settings_order=[
                "HEADER_TABLE_SIZE",
                "MAX_CONCURRENT_STREAMS",
                "INITIAL_WINDOW_SIZE",
                "MAX_HEADER_LIST_SIZE"
            ],
            supported_signature_algorithms=[
                "ECDSAWithP256AndSHA256",
                "PSSWithSHA256",
                "PKCS1WithSHA256",
                "ECDSAWithP384AndSHA384",
                "PSSWithSHA384",
                "PKCS1WithSHA384",
                "PSSWithSHA512",
                "PKCS1WithSHA512",
            ],
            supported_versions=["GREASE", "1.3", "1.2"],
            key_share_curves=["GREASE", "X25519"],
            cert_compression_algo="brotli",
            pseudo_header_order=[
                ":method",
                ":authority",
                ":scheme",
                ":path"
            ],
            connection_flow=15663105,
            header_order=[
                "accept",
                "user-agent",
                "accept-encoding",
                "accept-language"
            ],
            debug = True)

    def post(self, url, data, headers):
        return self.session.post(url, data=data, headers=headers)
    
    def get(self, url, headers):
        return self.session.get(url, headers=headers)
    
    def close(self):
        self.session.close()