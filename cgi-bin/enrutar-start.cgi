#!/bin/bash
echo "Content-type: text/html; charset=utf-8"
echo ""

/bin/cat << EOM
<html>
<head>
  <meta charset="utf-8">
  <title>Iniciar Enrutamiento</title>
  <style>
pre {
  background: white;
  padding: 20px;
  border: 1px solid #ccc;
  box-shadow: 0 0 5px rgba(0,0,0,0.2);
  white-space: pre-wrap;
  font-family: monospace;
}
body {
  font-family: monospace;
  padding: 20px;
}
.btn-group {
  display: flex;
  gap: 12px;
  margin-bottom: 20px;
}
.btn {
  padding: 10px 20px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 14px;
  font-family: monospace;
  font-weight: bold;
  color: white;
  text-decoration: none;
  display: inline-block;
}
.btn-start { background-color: #003366; }
.btn-start:hover { background-color: #002244; }
.btn-nat   { background-color: #1a6b3c; }
.btn-nat:hover { background-color: #145230; }
.btn-enr   { background-color: #8b4513; }
.btn-enr:hover { background-color: #6a340f; }
  </style>
</head>
<body>
<h2>Iniciar Enrrutamiento</h2>
<div class="btn-group">
  <a class="btn btn-start" href="/cgi-bin/enrutar.cgi?comand=start"   target="body">Start (NAT + ENR)</a>
  <a class="btn btn-nat"   href="/cgi-bin/enrutar.cgi?comand=startNAT" target="body">Start NAT</a>
  <a class="btn btn-enr"   href="/cgi-bin/enrutar.cgi?comand=startENR" target="body">Start ENR</a>
</div>
</body>
</html>
EOM
