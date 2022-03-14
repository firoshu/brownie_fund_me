from brownie import accounts, config, MockV3Aggregator, FundMe, network

from scripts.helpful_scripts import (
    get_account,
    deploy_mock,
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
)
import os
from web3 import Web3


def deploy_fund_me():
    account = get_account()
    print("Account: ", account)

    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        price_feed_address = config["networks"][network.show_active()][
            "eth_usd_price_feed"
        ]
    else:
        deploy_mock()
        price_feed_address = MockV3Aggregator[-1].address
        # print("printing verify status: ", config["networks"][network.show_active()])

    fund_me = FundMe.deploy(
        price_feed_address,
        {"from": account},
        publish_source=config["networks"][network.show_active()]["verify"],
    )
    return fund_me
    print("Contract deployed to:", fund_me.address)


def main():
    deploy_fund_me()
