from brownie import Wei, accounts, chain, interface, web3


link = interface.ERC20("0x514910771af9ca656af840dff83e8264ecf986ca")


def main():
    accounts.clear()
    account = '0x23c8Fbd5E14A9565707D8D1a88045F2fA5648968'
    from_acc =  accounts.load('chainlink-nya3')
    link_balance = link.balanceOf(account)
    print(f'link balance {link_balance}')
    link.transfer('0xB45A43e998286ab3Be4106b4c381f01dccE772a4', link_balance, {'from': from_acc}) #test

