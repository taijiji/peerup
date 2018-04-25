# peerup
Sample Network Automation Tool for BGP Private Peering.

This tool was used in [this presentation](https://speakerdeck.com/taijijiji/ming-ri-karahazimerunetutowakuyun-yong-zi-dong-hua-shi-jian-bian)


<img src="img/system.png" width="1000px">

# How to run

```
python setup.py
```

## Scenario File

```
purpus:  |
  本作業の目的は、ABC社 (AS65002) との BGPプライベートピアするものである。
  The target of operation is BGP private peering with ABC company(AS65002).
operator: Taiji Tsuchiya
operation_date: 20180410
hosts:
  hostname: vsrx1
  os: junos
  username: user1
  password: password1
  mgmt_ipaddress: 192.168.33.2
scenario:
  - check_hostname:
      hostname: vsrx1
  - check_model:
      model: FIREFLY-PERIMETER
  - check_os_version:
      os_version: 12.1X47-D15.4
  - check_interface:
      if_name: ge-0/0/2
      if_status: up
  - set_interface:
      if_name: ge-0/0/2
      if_addr: 192.168.35.1
      if_subnet: 30
  - check_interface:
      if_name: ge-0/0/2
      if_status: up
  - set_bgp_neighbor:
      if_name: ge-0/0/2
      neighbor_asnum: 65002
      neighbor_addr: 192.168.35.2
      neighbor_description: AS65002_peer
  - check_bgp_neighbor:
      neighbor_addr: 192.168.35.2
      neighbor_status: up
  - check_bgp_route_advertised:
      neighbor_addr: 192.168.35.2
      advertised_route_num: 0
  - check_bgp_route_received:
      neighbor_addr: 192.168.35.2
      received_route_num: 1
  - set_bgp_route_advertised:
      policy_name: as65002-out
      advertised_route_addr: 172.16.1.0
      advertised_route_subnet: 24
      if_name: ge-0/0/2
      neighbor_addr: 192.168.35.2
  - check_bgp_route_advertised:
      neighbor_addr: 192.168.35.2
      advertised_route_num: 1
  - set_bgp_route_received:
      policy_name: all-accept
      if_name: ge-0/0/2
      neighbor_addr: 192.168.35.2
  - check_bgp_route_received:
      neighbor_addr: 192.168.35.2
      received_route_num: 1
```


# Result

<img src="img/result_1.png" width="600px">
<img src="img/result_2.png" width="400px">
<img src="img/result_3.png" width="400px">
<img src="img/result_4.png" width="500px">
<img src="img/result_5.png" width="500px">
<img src="img/result_6.png" width="500px">
<img src="img/result_7.png" width="500px">

# Demo

<img src="https://github.com/taijiji/peerup/blob/master/img/peerup_movie_v1.gif" width="1300px">

