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
2021-10-17 00:00:40.778003 -> Loaded struct.yml for salsa20...
2021-10-17 00:00:40.778125 <- Sending to salsa falcon.
2021-10-17 00:00:40.782197 -> Loaded struct.yml for salsa20...
2021-10-17 00:00:40.782220 <- Sending to salsa falcon.
2021-10-17 00:00:41.089902 df0178797551 -> Recv thread 2 output:  b'e9641dd7d803a5f1db2e6482b7bf4d6727b9882bdd7e5f510f61389b42ca6f3127823c08572f2d01e09c2f541b6f8f8d0505ec3ee3fed6007eb202698ef98e476684fd01696a4f991f31135d'
2021-10-17 00:00:41.095300 df0178797551 -> Recv thread 1 output:  b'4aefafde0d916454ed2ee6'
2021-10-17 00:00:41.310947 df0178797551 -> Recv thread 1 output:  b'bd6d056e28693cd27003b23b'
2021-10-17 00:00:41.317323 df0178797551 -> Recv thread 2 output:  b'18bbfb92953dc82220cdd7e6c8'
2021-10-17 00:00:41.457001 df0178797551 -> Recv thread 1 output:  b'81558f2738112a79c57bce5ae4ec7e'
2021-10-17 00:00:41.492855 df0178797551 -> Recv thread 2 output:  b'106fd428aea458b31c97253a8e6c1d'
2021-10-17 00:00:41.625267 df0178797551 -> Recv thread 1 output:  b'a172865eac6d631c7b07'
2021-10-17 00:00:41.631063 df0178797551 -> Recv thread 2 output:  b'7078f886325e0d1c747b040f6e5b9fbc22506d31327ca75fd863d3c65b58e2d3c172436b48b18a80d2c3be76664e4b8d2008c7e055a1ab5511009f61fbefff'
2021-10-17 00:00:41.776727 df0178797551 -> Recv thread 1 output:  b'6acd3ac92ea08d7db1889198c8742f1be7d506c7484b9eb78e76b8e736b08243d923cbcf1815a29ce74ae1d1fd9b89d4a693a39aa207c8683d0e475e56acb2a0da12b80f8989099cd38fccf5'
2021-10-17 00:00:41.912456 df0178797551 -> Recv thread 1 output:  b'673192f700a6aabfd85e8566715d4e9627578da1'
2021-10-17 00:00:42.047188 df0178797551 -> Recv thread 1 output:  b'd5398a9f4d9dd80fc1'
$

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
