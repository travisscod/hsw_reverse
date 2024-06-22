# dont know yet

class Event:
    def __init__(self, object_getOwnPropertyNames_chrome, 
                 prompt_tostring_len, close_tostring_len, 
                 process_type, content_index, contacts_manager, shared_worker,
                 function_tostring_len, reporting_observer,
                 onreject_rtctp, media_devices, performance_observer,
                 border_end_end_check, odd_vars, random_dict, document_vars, symbols) -> None:
        self.hash = [
            object_getOwnPropertyNames_chrome, #Object.getOwnPropertyNames(window["chrome"]
            
            prompt_tostring_len, #window.prompt.toString().length
            close_tostring_len, #window.close.toString().length
            process_type, #window["process"].type but is null for some reason because of browser
            content_index, #"ContentIndex" in window
            contacts_manager, #"ContactsManager"in window
            shared_worker, # "SharedWorker" in window
            function_tostring_len, #Function.toString().length
            reporting_observer,  #"flat" in [] ? "ReportingObserver" in window : null
            onreject_rtctp, #"onrejectionhandled" in window ? "RTCRtpTransceiver" in window : null
            media_devices, #"MediaDevices" in window
            performance_observer, #'PerformanceObserver' in window && 'takeRecords' in PerformanceObserver.prototype ? "Credential" in window : null, 
            border_end_end_check, #"supports"in (window.CSS || {}) && CSS.supports('border-end-end-radius: initial'), 
            odd_vars, #This the window get propnames last 25 and then compraed to some regex /[_$]/
            random_dict, #this seems to be empty every time
            document_vars, #seems to take document functions and check them with random II func
            symbols, #"Symbol" in window && "description" in Symbol.prototype ? "PaymentManager "in window : null
        ]