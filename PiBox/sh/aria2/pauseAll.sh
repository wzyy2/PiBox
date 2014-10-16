#!/bin/sh

echo "aria2.pauseAll"
curl -d "{\"jsonrpc\":\"2.0\",\"method\":\"aria2.pauseAll\",\"id\":1,\"params\":[]}" "http://127.0.0.1:6800/jsonrpc"
echo '\ndone'
