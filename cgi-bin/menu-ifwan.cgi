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
</style>
</head>
<body>
<h4><a href="/cgi-bin/ifwan.cgi?comand=start&" target="body">Ifwan start</a></h4>
<h4><a href="/cgi-bin/ifwan.cgi?comand=stop&" target="body">Ifwan stop</a></h4>
<h4><a href="/cgi-bin/ifwan.cgi?comand=status&" target="body">Ifwan status</a></h4>
<h4><a href="/cgi-bin/configura-ifwan.cgi?"target="body">Ifwan config</a></h4>
</body>
</html>

EOM


