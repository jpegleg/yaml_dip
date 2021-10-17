# yaml_dip
An HTTPS client app template in python with requests module, built for the salsa_falcon.

## See https://github.com/jpegleg/salsa_falcon

## This is a template, edit it from here for a real use. 
#### Probably want to make that api token something more useful.
#### Replace mycoolsalsafalcon in the template with your salsa_falcon server DNS name or IP.
#### Replace the URI context /api/encrypt/1 etc, with the URI contexts you configure in your salsa_falcon routes.

This client tempalte takes in a YAML file called struct.yml which defines encryption and decryption salsa falcon endpoints
as well as data to encrypt and decrypt. The program could be expanded to have multiple yaml files loaded and processed etc.
This example has two client threads encrypting 80 strings. Even with the salsa_falcon being remote, the speed is good.

```
$ python yaml_dip.py
2021-10-16 23:29:50.462398 -> Loaded struct.yml for salsa20...
2021-10-16 23:29:50.462473 <- Sending to salsa falcon.
2021-10-16 23:29:50.462501  Hash of encrypt URL:  df017879755179a83a2aa12c7617b7548616ae9554684140ea550283cf01da7e
2021-10-16 23:29:50.471154 -> Loaded struct.yml for salsa20...
2021-10-16 23:29:50.471177 <- Sending to salsa falcon.
2021-10-16 23:29:50.471194  Hash of encrypt URL:  df017879755179a83a2aa12c7617b7548616ae9554684140ea550283cf01da7e
2021-10-16 23:29:50.626966 -> Recv encrypted:  b'f659e339c63cf59c183d94'
2021-10-16 23:29:50.627022  Hash of encrypt URL:  df017879755179a83a2aa12c7617b7548616ae9554684140ea550283cf01da7e
2021-10-16 23:29:50.634214 -> Recv encrypted:  b'dd61a14b8a22a53185c12c31f17395c02d388d03c1fdcbe0faac77f6d17ec8be5fc922e1dc5b668'
2021-10-16 23:29:50.780141 -> Recv encrypted:  b'43bcd96429d609fa07d0bdd1'
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
