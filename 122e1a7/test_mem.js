console.clear()

console.log("MEMORIES -------------------")

for(let i = 0; i<69; i++) {
    try {
    const uint8Array = new Uint8Array(memories.$$a.buffer, eval(`$var${i}.value`), 250);
    const decoder = new TextDecoder();
    const decodedString = decoder.decode(uint8Array);
    const cleanedString = decodedString.replace(/\u0000/g, '');
    console.log(cleanedString)
    console.log(i)
    } catch {}
}

console.log("STACK -------------------")

for(let i = 0; i<69; i++) {
    try {
    const uint8Array = new Uint8Array(memories.$$a.buffer, eval(`stack[${i}].value`), 100);
    const decoder = new TextDecoder();
    const decodedString = decoder.decode(uint8Array);
    const cleanedString = decodedString.replace(/\u0000/g, '');
    console.log(i, cleanedString)
    } catch {}
}



"6z6", [Object.getOwnPropertyNames(window["chrome"] || {}), null === (I = window.prompt) || void 0 === I ? void 0 : I.toString().length, null === (g = window["close"]) 
|| void 0 === g ? void 0 : g.toString().length, null === (B = window["process"]) || void 0 === B ? void 0 : B.type, 
"ContentIndex" in window, "ContactsManager"in window, "SharedWorker" in window, 
Function.toString().length, "flat" in [] ? "ReportingObserver" in window : null,
"onrejectionhandled" in window ? "RTCRtpTransceiver" in window : null, 
"MediaDevices" in window, 
'PerformanceObserver' in window && 'takeRecords' in PerformanceObserver.prototype ? "Credential" in window : null, 
"supports"in (window.CSS || {}) && CSS.supports('border-end-end-radius: initial'), 
EA, 
(C = [],
    Object[BA(u)](document)[BA(547)]((function(A) {
        var I = BA;
        if (!weirdchk(document, A)) {
            var g = document[A];
            if (g) {
                var B = Object.getPrototypeOf(g) || {};
                C.push([A, K(K([], Object.keys(g), true), Object.keys(B), true).slice(0, 5)])
            } else
                C[I(b)]([A])
        }
    }
    )),
    C[BA(d)](0, 5)), gI(window), "Symbol" in window && "description" in Symbol.prototype ? "PaymentManager "in window : null]

)

matchMedia('(device-width: '.concat(screen.width, 'px) and (device-height: ').concat(screen.height, 'px)')).matches
matchMedia(G(w)[G(o)](F, ")")).matches

matchMedia("(resolution: ".concat(window.devicePixelRatio, "dppx)")).matches


function time() {
    return "undefined" != typeof performance && "function" == typeof performance.now ? performance[I(A)]() : Date.now()
}