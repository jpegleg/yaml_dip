# yaml_dip
An HTTPS client app template in python with requests module, built for the salsa_falcon.

## See https://github.com/jpegleg/salsa_falcon

## This is a template, edit it from here for a real use. 
#### Probably want to make that api token something more useful.
#### Replace mycoolsalsafalcon in the template with your salsa_falcon server DNS name or IP.
#### Replace the URI context /api/encrypt/1 etc, with the URI contexts you configure in your salsa_falcon routes.

This client tempalte takes in a YAML file called struct.yml which defines encryption and decryption salsa falcon endpoints
as well as data to encrypt and decrypt. The program could be expanded to have multiple yaml files loaded and processed etc.
This example has two client threads to two different salsa_falcon servers, encrypting some strings. Even with the salsa_falcon being remote, the speed is good.

```
$ python yaml_dip.py
2021-10-17 00:14:26.107058 -> Loaded struct1.yml for salsa20...
2021-10-17 00:14:26.107171 <- Sending to salsa falcon.
2021-10-17 00:14:26.111168 -> Loaded struct2.yml for salsa20...
2021-10-17 00:14:26.111194 <- Sending to salsa falcon.
2021-10-17 00:14:26.375488 df0178797551 -> Recv thread 2 output:  b'e96a1c9e2f2d7a3a411eed767b0969d1334885e48def18723d79a628f90f659c525a2b0404c4ae154d4abbdd79fb832b217de087765825fffff23ffff726f53519d15c8ac4eb50f19c0f5a2e'
2021-10-17 00:14:26.519678 df0178797551 -> Recv thread 2 output:  b'1444f0c324cc4f23aa8792642a'
2021-10-17 00:14:26.530474 950d29aeba1a -> Recv thread 1 output:  b'39323963306537366631356431343432323964333230'
2021-10-17 00:14:26.664828 df0178797551 -> Recv thread 2 output:  b'425ed87f679cba4a0189803a508161'
2021-10-17 00:14:26.748891 950d29aeba1a -> Recv thread 1 output:  b'306462366132613437626365626363633638363230306138'
2021-10-17 00:14:26.809334 df0178797551 -> Recv thread 2 output:  b'42012809259659f32f1dc8fdddefcce805cccd3b3786efea251d4cfd1bb7459dc09f5b09ab6fb9b1775bb1aac355d2b415407d72f9bce7767be976eb894782'
2021-10-17 00:14:26.962262 950d29aeba1a -> Recv thread 1 output:  b'366361303938313466633435383335363736336165626130646534393136'
2021-10-17 00:14:27.170391 950d29aeba1a -> Recv thread 1 output:  b'3733623265373031616639393164343966333438'
2021-10-17 00:14:27.385008 950d29aeba1a -> Recv thread 1 output:  b'356337303966613635396331376537643131343337303235396236663831376432356331333931326539633964383162346633336438316138376638376264633335333538393632616364663363336163346234376635613931306134633632346132646535376537356564346134323837303638386565373133313436646266333232643534666661353634303939326364356237353338363961343337633465323663306630'
2021-10-17 00:14:27.599081 950d29aeba1a -> Recv thread 1 output:  b'356339646637373166626661613238366332613139376362616139363033326463386462326530323362323566646239346230386531313664663933366561636433666163653335376564323235373266626239386535393039643561646338316332376130373933356330393937626566623434323265383039323365326563303362633139643838353932343863353963373161323432633731376362616562666437383365'
2021-10-17 00:14:27.814579 950d29aeba1a -> Recv thread 1 output:  b'3838663630656664393236373830386134323461356430353932313434363033333563646130306237646236376439383737396236303635323533353862366330356439303061346236663336343035663739346565643037353963313861646234376631633933363536623738323236613238316562646239306565353031623932333339373666656330306130376464643738663931'
2021-10-17 00:14:28.028348 950d29aeba1a -> Recv thread 1 output:  b'663037393464616430373561366662646163313638633865323830623735303237656366353766396262353364316164313164346566666362336166383261663962393834323131386430313333303634353435666463313139623665626461323263393932313639666332353630646365336632653766303232343233376432323965623239636239303161653730393339616631353739333930633363313966373634396665'
2021-10-17 00:14:28.245654 950d29aeba1a -> Recv thread 1 output:  b'34396635316637656537373164383032326232396162373861626538383666306231653765656337'
2021-10-17 00:14:28.471847 950d29aeba1a -> Recv thread 1 output:  b'38316166356165356430373435633630366539633338313532633066313865336231653536643430383437393036393637646532343235386363626566643732373561633136396162656565636439653337623762633531'
2021-10-17 00:14:28.695111 950d29aeba1a -> Recv thread 1 output:  b'356134356364616366396531323134663037633530653434303333393863343234656464353437346639333736333266353631653631653532356235356665363063626134643335666465313363393935653361353431393436393135613436393233636134323231623664666435353333366563323136643633613838643330356237646533313133643238326237316261333432633061326539623365396238653530346238'
$

```
### Note the second column of the output is a truncated SHA256 of the falcon server URI context used.
### The purpose of this is for tracking and audit, without exposing the URI context of the falcon route to the output.
### That hash is only truncated to save disk space in the output, you can remove the truncate and print the full SHA256 if you like.
#### Change urihash[0:12] to urihash in the code to print the full hash value.

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

The salsa falcon/s used could be local and/or remote. I like to have remote salsa falcons with encrypt only set ups, and put the decrypt api elsewhere.
This creates nice control over the decryption mechanism and more importantly, the secret key is never on the client or build systems.
