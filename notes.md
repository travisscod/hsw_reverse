index 0 function er nop virker det som, så jeg hra bare erstattet den med console.log.
Den får scraped hele fp_raw lige inden den sender det frem og tilbage mellem wasm delen og så js. 

exports:
(export "$a" (memory 0))
(export "ab" (func 271))
(export "bb" (func 314))
(export "cb" (func 315))
(export "db" (func 322))
(export "eb" (func 331))
(export "fb" (table 0))
(export "gb" (func 338))
(export "hb" (func 295))
(export "ib" (func 341))
(export "jb" (func 356))
(export "kb" (func 339))


date = Math.round(Date.now() / 1e3);

return Ng(JSON.stringify(C), date, g)


raw_fp sendt til wasm
function WI(A, I, g, B) {
    G.gb(A, I, PI(g), PI(B))
}



Ville jeg gætte til at være der de generer deres crypto key på 256 bits med AES-GCM
local.set $var3
i32.const 256
call $a.Ra
local.set $var2

ic6 er fingerprint_events



rand generation

call $func319
f64.convert_i32_u
f64.const 2.3283064365386963e-10
f64.mul



//HACK

                                                    ;;inject
                                                    local.get 4
                                                    local.get 6
                                                    i32.load offset=8
                                                    i32.const 300
                                                    
                                                    call 106

                                                    ;;set pointer to new fp ptr
                                                    i32.const 50
                                                    call 26
                                                    local.set 4

                                                    ;;set len to new fp len
                                                    i32.const 75
                                                    call 26
                                                    i32.store offset=8

                                                    ;; test bp
                                                    ;;local.get 4
                                                    ;;local.get 6
                                                    ;;i32.load offset=8
                                                    
                                                    

call $func360 hash function??