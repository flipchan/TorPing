# TorPing
a simple script to check if a hiddenservice is active

Noone had created a ping script for hiddenservices so i wrote this 
this does not send a icmp requests it checks if the .onion is in the DHT for hidden services 

This is a simple to use script that checks The Hidden service directory with the help of stem(https://stem.torproject.org/)




## how to:
Testing with duckduckgo(http://3g2upl4pq6kufc4m.onion)
and an invalid one
```console
root@sb0x# python ping_it.py http://3g2upl4pq6kufc4m.onion advanced
checking http://3g2upl4pq6kufc4m.onion
checked:
3g2upl4pq6kufc4m
the hiddenservice is up
Public Key: -----BEGIN RSA PUBLIC KEY-----
MIGJAoGBAJ/SzzgrXPxTlFrKVhXh3buCWv2QfcNgncUpDpKouLn3AtPH5Ocys0jE
aZSKdvaiQ62md2gOwj4x61cFNdi05tdQjS+2thHKEm/KsB9BGLSLBNJYY356bupg
I5gQozM65ENelfxYlysBjJ52xSDBd8C4f/p9umdzaaaCmzXG/nhzAgMBAAE=
-----END RSA PUBLIC KEY-----
Publication time: 2017-07-14 13:00:00
Signature: -----BEGIN SIGNATURE-----
PeiJS2Pqc8txXYVgXMYoA5xrrj7a1tXNJeOpCRPvpkkOvbhsEKQfVKhCse4wXy8X
7amzzAYNkqnmXdXP0GMfIe/S8eppQj5+RPA3aJ2jN5EDiwrRR8BqP88e4hk9TfxN
1yihuwx2K7LrAynuqJRWJcoNurEGSxmNtRY/a95j21w=
-----END SIGNATURE-----
rendezvous service descriptor: (u'a4vzrmrsh6m3hok364eabxhlpjvgpmkg', None, None)
Version: 2

root@b0x:# python ping_it.py http://3g2upl4pq6kufc4m.onion simple
checking http://3g2upl4pq6kufc4m.onion
checked:
3g2upl4pq6kufc4m
the hiddenservice is up


root@b0x:# python ping_it.py http://3g2upl4pq6kufc43.onion simple
checking http://3g2upl4pq6kufc43.onion
No running hidden service at 3g2upl4pq6kufc43.onion
the hidden service is down

```

