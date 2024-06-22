function random_number(A, I) {
  console.log(A,I)
  //return 
  return Math.floor(Math.random() * (I - A + 1)) + A
}

function encrypt(str) {
  var alphabet = "abcdefghijklmnopqrstuvwxyz";
  if (null == str) return null;
  for (var str_2 = 'string' != typeof str ? String(str) : str, list = [], M = 0; M < 13; M += 1)
      list.push(String["fromCharCode"](random_number(65, 90)));

  var list_joined = list.join(''),
      rand = random_number(1, 26),
      a = str_2.split(' ')
          .reverse()
          .join(' ')
          .split('')
          .reverse()
          .map(function (str) {
              if (!str.match(/[a-z]/i)) return str;
              var indx = alphabet.indexOf(str.toLowerCase());
              var rotate = alphabet[(indx + rand) % 26];
              return str === str.toUpperCase() ? rotate.toUpperCase() : rotate;
          })
          .join('');

  var encoded_str = Buffer.from(a, 'utf8').toString('base64').split('').reverse().join(''), // skal være encoded_str = base64.b64encode(a.encode()).decode()[::-1]
      rand_2 = random_number(1, encoded_str.length - 1);

  return [(encoded_str.slice(rand_2, encoded_str.length) + encoded_str.slice(0, rand_2)).replace(new RegExp('['.concat(list_joined).concat(list_joined.toLowerCase(), ']'), 'g'),
      function (str) {
          return str === str.toUpperCase() ? str.toLowerCase() : str.toUpperCase();
      }
  ),
  rand.toString(16),
  rand_2.toString(16),
      list_joined,
  ];
}



function decrypt(arr) {
  console.log(arr); 
  var alphabet = "abcdefghijklmnopqrstuvwxyz"; 
  var encoded_str = arr[0]; // Første ting fra array [ 'wajVxigKldjnMZoZ', '11', '2', 'UTIXCOQKNPTMW' ] som er det der er encoded
  var rand = parseInt(arr[1], 16); // andet ting i array er random værdi (både tal og bostav) brugt til at encrypt
  var rand_2 = parseInt(arr[2], 16); // tredje ting i array er random værdi (både tal og bostav) brugt til at encrypt
  var list_joined = arr[3]; // Fjerde ting i array er en liste af tilfældige bogstaver

  // Decrypt string ved at bytte om på store og små bogstaver
  var decoded_str = encoded_str.replace(new RegExp('['.concat(list_joined).concat(list_joined.toLowerCase(), ']'), 'g'),
      function (str) {
          return str === str.toUpperCase() ? str.toLowerCase() : str.toUpperCase();
      }
  );

  // Omarranger string ved at skifte de to dele omkring rand_2
  var rearranged_str = decoded_str.slice(decoded_str.length - rand_2, decoded_str.length) + decoded_str.slice(0, decoded_str.length - rand_2);
  
  // decrypt string fra base64 og vend den om
  var base64_decoded_str = Buffer.from(rearranged_str.split('').reverse().join(''), 'base64').toString('utf8');
  var base64_decoded_str = decodeURIComponent(base64_decoded_str);
  // decrypt string ved at rotere bogstaverne tilbage i alfabetet
  var decrypted_str = base64_decoded_str.split('')
      .map(function (str) {
          if (!str.match(/[a-z]/i)) return str;
          var indx = alphabet.indexOf(str.toLowerCase());
          var rotate = alphabet[(indx - rand + 26) % 26];
          return str === str.toUpperCase() ? rotate.toUpperCase() : rotate;
      })
      .reverse() // Vend strengen om
      .join('') // Saml tegnene til en streng
      .split(' ') // Opdel strengen ved mellemrum
      .reverse() // Vend ordene om
      .join(' '); // Saml ordene til en streng

  return decrypted_str; // Returner den dekrypterede streng
}


console.log(decrypt(encrypt("nigger nigger")));