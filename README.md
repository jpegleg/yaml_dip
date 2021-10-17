# yaml_dip
An HTTPS client app template in python with requests module, built for the salsa_falcon.

## See https://github.com/jpegleg/salsa_falcon

## This is a template, edit it from here for a real use. 
#### Probably want to make that api token something more useful.
#### Replace mycoolsalsafalcon in the template with your salsa_falcon server DNS name or IP.
#### Replace the URI context /api/encrypt/1 etc, with the URI contexts you configure in your salsa_falcon routes.

This client tempalte takes in a YAML file called struct.yml which defines encryption and decryption salsa falcon endpoints
as well as data to encrypt and decrypt. The program could be expanded to have multiple yaml files loaded and processed etc.

```
$ python yaml_dip.py
2021-10-16 23:19:07.469675 -> Loaded struct.yml for salsa20...
2021-10-16 23:19:07.469765 <- Sending to salsa falcon.
2021-10-16 23:19:07.469789  Hash of encrypt URL:  df017879755179a83a2aa12c7617b7548616ae9554684140ea550283cf01da7e
2021-10-16 23:19:07.473130 -> Loaded struct.yml for salsa20...
2021-10-16 23:19:07.473158 <- Sending to salsa falcon.
2021-10-16 23:19:07.473178  Hash of encrypt URL:  df017879755179a83a2aa12c7617b7548616ae9554684140ea550283cf01da7e
2021-10-16 23:19:07.702469 -> Recv encrypted:  b'43e65ff34e84bc1b3f3d8989'
2021-10-16 23:19:07.702544  Hash of encrypt URL:  df017879755179a83a2aa12c7617b7548616ae9554684140ea550283cf01da7e
2021-10-16 23:19:07.709397 -> Recv encrypted:  b'42dc72125a7b1c8080'
2021-10-16 23:19:07.709446  Hash of encrypt URL:  df017879755179a83a2aa12c7617b7548616ae9554684140ea550283cf01da7e
2021-10-16 23:19:07.867144 -> Recv encrypted:  b'3049370be1bbf62651'
2021-10-16 23:19:07.867189  Hash of encrypt URL:  df017879755179a83a2aa12c7617b7548616ae9554684140ea550283cf01da7e
2021-10-16 23:19:07.874951 -> Recv encrypted:  b'429ddcfdb0627043cc'
2021-10-16 23:19:07.875002  Hash of encrypt URL:  df017879755179a83a2aa12c7617b7548616ae9554684140ea550283cf01da7e
2021-10-16 23:19:08.006999 -> Recv encrypted:  b'65cb383d8e7291a49b7c33cf6de7'
2021-10-16 23:19:08.007045  Hash of encrypt URL:  df017879755179a83a2aa12c7617b7548616ae9554684140ea550283cf01da7e
2021-10-16 23:19:08.015089 -> Recv encrypted:  b'6098f08fe965fcf163'
2021-10-16 23:19:08.015116  Hash of encrypt URL:  df017879755179a83a2aa12c7617b7548616ae9554684140ea550283cf01da7e
2021-10-16 23:19:08.156270 -> Recv encrypted:  b'6a75bcd84c5242374e793a39'
2021-10-16 23:19:08.156381  Hash of encrypt URL:  df017879755179a83a2aa12c7617b7548616ae9554684140ea550283cf01da7e
2021-10-16 23:19:08.165019 -> Recv encrypted:  b'93cc3f772d60b9f00d'
2021-10-16 23:19:08.165071  Hash of encrypt URL:  df017879755179a83a2aa12c7617b7548616ae9554684140ea550283cf01da7e
2021-10-16 23:19:08.303663 -> Recv encrypted:  b'25ecc73353bc4d3b8117c006689f532f71f0200f44230b44e8223180a9547a1878411787cd4308ee011253f05f86e487c900563356b114ac516da8fcb4fe765bbdc18044ac1021cfd8fb7d95'
2021-10-16 23:19:08.308441 -> Recv encrypted:  b'dfbca033298111c5dc'
2021-10-16 23:19:08.308492  Hash of encrypt URL:  df017879755179a83a2aa12c7617b7548616ae9554684140ea550283cf01da7e
2021-10-16 23:19:08.451976 -> Recv encrypted:  b'87f757979a53a4ed0d'
2021-10-16 23:19:08.452019  Hash of encrypt URL:  df017879755179a83a2aa12c7617b7548616ae9554684140ea550283cf01da7e
2021-10-16 23:19:08.596775 -> Recv encrypted:  b'1c47e895529f8bd7b3'
2021-10-16 23:19:08.596828  Hash of encrypt URL:  df017879755179a83a2aa12c7617b7548616ae9554684140ea550283cf01da7e
2021-10-16 23:19:08.741808 -> Recv encrypted:  b'e12791b384afff0909'
2021-10-16 23:19:08.741866  Hash of encrypt URL:  df017879755179a83a2aa12c7617b7548616ae9554684140ea550283cf01da7e
2021-10-16 23:19:08.883197 -> Recv encrypted:  b'cd8094db420dc579d2'
2021-10-16 23:19:08.883268  Hash of encrypt URL:  df017879755179a83a2aa12c7617b7548616ae9554684140ea550283cf01da7e
2021-10-16 23:19:09.033234 -> Recv encrypted:  b'1d7bdfacc479f8bac4'
2021-10-16 23:19:09.033351  Hash of encrypt URL:  df017879755179a83a2aa12c7617b7548616ae9554684140ea550283cf01da7e
2021-10-16 23:19:09.169263 -> Recv encrypted:  b'22dc7e3405c5435710'
2021-10-16 23:19:09.169391  Hash of encrypt URL:  df017879755179a83a2aa12c7617b7548616ae9554684140ea550283cf01da7e
2021-10-16 23:19:09.311297 -> Recv encrypted:  b'36f6d8a8c20b27be3d'
2021-10-16 23:19:09.311367  Hash of encrypt URL:  df017879755179a83a2aa12c7617b7548616ae9554684140ea550283cf01da7e
2021-10-16 23:19:09.458137 -> Recv encrypted:  b'e41401760ec8c978d5'
2021-10-16 23:19:09.458197  Hash of encrypt URL:  df017879755179a83a2aa12c7617b7548616ae9554684140ea550283cf01da7e
2021-10-16 23:19:09.605011 -> Recv encrypted:  b'4e218a3ab771455720'
2021-10-16 23:19:09.605049  Hash of encrypt URL:  df017879755179a83a2aa12c7617b7548616ae9554684140ea550283cf01da7e
2021-10-16 23:19:09.751107 -> Recv encrypted:  b'9d3558472b8b8eb3c0'
2021-10-16 23:19:09.751162  Hash of encrypt URL:  df017879755179a83a2aa12c7617b7548616ae9554684140ea550283cf01da7e
2021-10-16 23:19:09.895037 -> Recv encrypted:  b'04580b6dad73a5decf'
2021-10-16 23:19:09.895097  Hash of encrypt URL:  df017879755179a83a2aa12c7617b7548616ae9554684140ea550283cf01da7e
2021-10-16 23:19:10.036902 -> Recv encrypted:  b'd21e6db47995f2a1a8'
2021-10-16 23:19:10.036956  Hash of encrypt URL:  df017879755179a83a2aa12c7617b7548616ae9554684140ea550283cf01da7e
2021-10-16 23:19:10.178278 -> Recv encrypted:  b'11a10e612d1177c3d1'
2021-10-16 23:19:10.178319  Hash of encrypt URL:  df017879755179a83a2aa12c7617b7548616ae9554684140ea550283cf01da7e
2021-10-16 23:19:10.316991 -> Recv encrypted:  b'eb702f9ac6fb3acc1d'
2021-10-16 23:19:10.317043  Hash of encrypt URL:  df017879755179a83a2aa12c7617b7548616ae9554684140ea550283cf01da7e
2021-10-16 23:19:10.461758 -> Recv encrypted:  b'cd6873bdcac76202fe'
2021-10-16 23:19:10.461810  Hash of encrypt URL:  df017879755179a83a2aa12c7617b7548616ae9554684140ea550283cf01da7e
2021-10-16 23:19:10.606851 -> Recv encrypted:  b'93ae3b64dccd553e2b'
2021-10-16 23:19:10.606905  Hash of encrypt URL:  df017879755179a83a2aa12c7617b7548616ae9554684140ea550283cf01da7e
2021-10-16 23:19:10.751099 -> Recv encrypted:  b'23f42d2b451b5e00ca'
2021-10-16 23:19:10.751151  Hash of encrypt URL:  df017879755179a83a2aa12c7617b7548616ae9554684140ea550283cf01da7e
2021-10-16 23:19:10.896500 -> Recv encrypted:  b'b2a92f53ef49bc58f7'
2021-10-16 23:19:10.896550  Hash of encrypt URL:  df017879755179a83a2aa12c7617b7548616ae9554684140ea550283cf01da7e
2021-10-16 23:19:11.042374 -> Recv encrypted:  b'c15ccc1e71b43f9aad'
2021-10-16 23:19:11.042427  Hash of encrypt URL:  df017879755179a83a2aa12c7617b7548616ae9554684140ea550283cf01da7e
2021-10-16 23:19:11.188841 -> Recv encrypted:  b'd6473e64755e3a5401'
2021-10-16 23:19:11.188895  Hash of encrypt URL:  df017879755179a83a2aa12c7617b7548616ae9554684140ea550283cf01da7e
2021-10-16 23:19:11.331679 -> Recv encrypted:  b'176b6e8c0df7ee4e6e'
2021-10-16 23:19:11.331722  Hash of encrypt URL:  df017879755179a83a2aa12c7617b7548616ae9554684140ea550283cf01da7e
2021-10-16 23:19:11.471022 -> Recv encrypted:  b'26ad56d96d30fcae21'
2021-10-16 23:19:11.471079  Hash of encrypt URL:  df017879755179a83a2aa12c7617b7548616ae9554684140ea550283cf01da7e
2021-10-16 23:19:11.616956 -> Recv encrypted:  b'd15568768b33b3b29a'
2021-10-16 23:19:11.617022  Hash of encrypt URL:  df017879755179a83a2aa12c7617b7548616ae9554684140ea550283cf01da7e
2021-10-16 23:19:11.765071 -> Recv encrypted:  b'1da574931f708b0156'
2021-10-16 23:19:11.765125  Hash of encrypt URL:  df017879755179a83a2aa12c7617b7548616ae9554684140ea550283cf01da7e
2021-10-16 23:19:11.909023 -> Recv encrypted:  b'5231ac5d264cbe5ada'
2021-10-16 23:19:11.909074  Hash of encrypt URL:  df017879755179a83a2aa12c7617b7548616ae9554684140ea550283cf01da7e
2021-10-16 23:19:12.054491 -> Recv encrypted:  b'ed7274172d4e2d2afc'
2021-10-16 23:19:12.054600  Hash of encrypt URL:  df017879755179a83a2aa12c7617b7548616ae9554684140ea550283cf01da7e
2021-10-16 23:19:12.200524 -> Recv encrypted:  b'6cb22d273a0746eee8'
2021-10-16 23:19:12.200585  Hash of encrypt URL:  df017879755179a83a2aa12c7617b7548616ae9554684140ea550283cf01da7e
2021-10-16 23:19:12.346350 -> Recv encrypted:  b'd7e35a82e360feb8f9a3a15934fa'

```

The segments to decrypt are defined as eseg while the data segments to encrypt are labelled datasegment:

```
---
salsamixer:

  name:
    - "do salsa20 on some YAML values"
  executions:
    HONKSET:
      datasegment:
        - "Honk honk honk"
      eseg:
        - 52e323fc8d924e2290f02ceb
      salsafalconE:
        - "https://mycoolsalsafalcon/api/encrypt/1"
      salsafalconD:
        - "https://mycoolsalsafalcon/api/decrypt/funtimeswithuricontexts"
...   
```

You can have any number of executions and it will iterate through them:

```
---
salsamixer:

  name:
    - "do salsa20 on some YAML values"
  executions:
    HONKSET:
      datasegment:
        - "Honk honk honk"
      eseg:
        - 52e323fc8d924e2290f02ceb
      salsafalconE:
        - "https://mycoolsalsafalcon/api/encrypt/1"
      salsafalconD:
        - "https://mycoolsalsafalcon/api/decrypt/funtimeswithuricontexts"
    HONKSET2:
      datasegment:
        - "Honk honk honk honk honk honk 2"
       eseg:
        - 52e323fc8d924e2290f02ce1
       salsafalconE:
        - "https://mycoolsalsafalcon/api/encrypt/2"
       salsafalconD:
        - "https://mycoolsalsafalcon/api/decrypt/funtimeswithuricontexts2"        
...   
```

If you only want to decrypt or only want to encrypt, just leave out the YAML keys you don't need:

```
---
salsamixer:

  name:
    - "do salsa20 on some YAML values"
  executions:
    HONKSET:
      datasegment:
        - "Honk honk honk"
        - "More things, encoded images, whatevs."
        - "Further things we want to send around."
      salsafalconE:
        - "https://mycoolsalsafalcon/api/encrypt/1"
    HONKSET2:
      datasegment:
        - "Honk honk honk honk honk honk 2"
      salsafalconE:
        - "https://mycoolsalsafalcon/api/encrypt/1"
        - "https://mycoolsalsafalcon/api/encrypt/2"     
... 
```
