
for (let i = 0; i <= 71; i++) {
    try {
    var offset = eval(`$var${i}.value`);
    var _length = 25;
    
    
    const uint8Array = new Uint8Array(memories.$$a.buffer, offset, _length);
    const decoder = new TextDecoder();
    const decodedString = decoder.decode(uint8Array);
    const cleanedString = decodedString.replace(/\u0000/g, '');
    
    console.log(JSON.stringify(cleanedString));
    } catch {}

}
