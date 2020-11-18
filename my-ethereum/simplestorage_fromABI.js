var ABI=[{"constant":false,"inputs":[{"name":"x","type":"uint256"}],"name":"set","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"get","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"}];

var address = "0xfe09fc60f7da0ca181575c1695e815c84f3f9b84";

eth.defaultAccount=eth.coinbase;

var simplestorage = eth.contract(ABI).at(address);