#!/bin/bash

source /usr/local/JSBach/conf/variables.txt


/bin/cat << EOM

<html>
<head>
<meta http-equiv=Content-Type content="text/html; charset=windows-1252">
<meta content="MSHTML 6.00.2900.3660" name=GENERATOR> 

<style type="text/css">
<!--
.estado {
	font-size: 18px;
	font-style: normal;
	color: #e9ab17;
	font-weight: bold;
	font-family: Georgia, "Times New Roman", Times, serif;
}
.cabecera {
	font-family: Verdana, Arial, Helvetica, sans-serif;
	color: #2A5B45;
}
.Estilo1 {color: #FF00FF}
.Estilo2 {color: #000000}
-->
h4{
  background: #f2f6fa;
  border-left: 5px solid #003366;
  margin-bottom: 10px;
  padding: 10px;
  border-radius: 5px;
}
h4:hover {
  background: #d0e4f5;
  cursor: pointer;
  border-left-color: #0055aa;
}
h4:active {
  background: #a6c8e0;
  border-left-color: #002244;
}
h4 a {
  text-decoration: none;
  color: #003366;
  display: block; 
}
h4 a:hover {
  color: #001f3f;
}
</style>
</head>
<body>
<h4><a href="/cgi-bin/bridge.cgi?comand=start&" target="body">Bridge Start</a></h4>
<h4><a href="/cgi-bin/bridge.cgi?comand=stop&" target="body">Bridge Stop</a></h4>
<h4><a href="/cgi-bin/bridge.cgi?comand=status&" target="body">Bridge Status</a></h4>
<h4><a href="/cgi-bin/bridge-configurar.cgi?" target="body">Bridge Configurar VLAN</a></h4>
<h4><a href="/cgi-bin/bridge-configurar-taguntag.cgi?" target="body">Bridge Configurar TAG/UNTAG</a></h4>
</body>
</html>

EOM


