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
2021-10-16 18:04:58.404194 -> Loaded struct.yml for salsa20...
2021-10-16 18:04:58.404258 <- Sending to salsa falcon.
2021-10-16 18:04:58.404282  Hash of input API URL:  df017879755179a83a2aa12c7617b7548616ae9554684140ea550283cf01da7e
2021-10-16 18:04:58.557214 -> Recv output:  b'32cad2115922c71197af23f30a71374383cdd80c090c'
2021-10-16 18:04:58.565548 <- Sending to salsa falcon.
2021-10-16 18:04:58.565592  Hash of input API URL:  b32429a1b4f156f30c5d4ccc0d066d91cb3301b445c9ca3c881098844b4f3aca
2021-10-16 18:04:58.708676 -> Recv output:  b'My message that was encrypted in the YAML is decrypted here as example.'
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
