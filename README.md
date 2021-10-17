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
2021-10-16 23:51:18.620326 -> Loaded struct.yml for salsa20...
2021-10-16 23:51:18.620392 <- Sending to salsa falcon.
2021-10-16 23:51:18.622786 -> Loaded struct.yml for salsa20...
2021-10-16 23:51:18.622807 <- Sending to salsa falcon.
2021-10-16 23:51:18.774221 df017879755179a83a2aa12c7617b7548616ae9554684140ea550283cf01da7e -> Recv encrypted:  b'74dc667ba350d790718719'
2021-10-16 23:51:18.783873 df017879755179a83a2aa12c7617b7548616ae9554684140ea550283cf01da7e -> Recv encrypted:  b'1e166d0962d9ae7a345e6d14d17ae80f91c9163d15cc67f58bd0848e76130dc0a99f26e385bb3decb0e5e65cc4fabab88135df67ed12211826b1aa7a060eb7c123498502575a98b4e25bb074'
2021-10-16 23:51:18.924400 df017879755179a83a2aa12c7617b7548616ae9554684140ea550283cf01da7e -> Recv encrypted:  b'e6cd738eda2b2b6d824edb18'
2021-10-16 23:51:19.072273 df017879755179a83a2aa12c7617b7548616ae9554684140ea550283cf01da7e -> Recv encrypted:  b'3a7eb8c67d1da85e853ce0fbff5b0c'
2021-10-16 23:51:19.222270 df017879755179a83a2aa12c7617b7548616ae9554684140ea550283cf01da7e -> Recv encrypted:  b'c89cea2f5026c3d155f9'
2021-10-16 23:51:19.370099 df017879755179a83a2aa12c7617b7548616ae9554684140ea550283cf01da7e -> Recv encrypted:  b'7d301ddcba9c0a2a5e311b77aae249f4892a38a6193dc917807e571506ab0a915148e32ecf520ef6f3802ef467c69c094fb078ea5edbab6b421c501b70e8af378c45041083701dc6a965288d'
2021-10-16 23:51:19.521451 df017879755179a83a2aa12c7617b7548616ae9554684140ea550283cf01da7e -> Recv encrypted:  b'31df4a35bb25ce253d973ea040eb1bc08ae56ba6'
2021-10-16 23:51:19.670869 df017879755179a83a2aa12c7617b7548616ae9554684140ea550283cf01da7e -> Recv encrypted:  b'e66174e8537e16cb7a'

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
