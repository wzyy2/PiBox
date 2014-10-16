#!/bin/sh

echo "aria2.unpauseAll"
curl -d "{\"jsonrpc\":\"2.0\",\"method\":\"aria2.unpauseAll\",\"id\":1,\"params\":[]}" "http://127.0.0.1:6800/jsonrpc"
echo '\ndone'
