import asyncio
from modules import *
from modules.okx import Okx
from utils.sleeping import sleep
from loguru import logger

async def withdraw_okx(_id, key, recipient):
    """
    Withdraw ETH from OKX
    ______________________________________________________
    min_amount - min amount (ETH)
    max_amount - max_amount (ETH)
    chains - ['zksync', 'arbitrum', 'linea', 'base', 'optimism']
    terminate - if True - terminate program if money is not withdrawn
    """
    token = 'ETH'

    #chains = ['arbitrum', 'zksync', 'linea', 'base', 'optimism']
    chains = ['zksync']

    min_amount = 0.05
    max_amount = 0.08

    terminate = True

    okx_exchange = Okx(_id, key, chains, recipient)
    await okx_exchange.okx_withdraw(min_amount, max_amount, token, terminate)


async def bridge_orbiter_from_scroll(account_id, key, recipient):
    """
    Bridge from orbiter
    ______________________________________________________
    from_chain – ethereum, polygon_zkevm, arbitrum, optimism, zksync | Select one
    to_chain – ethereum, polygon_zkevm, arbitrum, optimism, zksync | Select one

    save_funds - how much eth save on the account (min and max, choose randomly)
    min_required_amount - минимальная требуемая сумма в сети, на которую будет реагировать модуль в eth
    """

    #from_chains = ["arbitrum", "optimism", "base", "scroll", "linea"]
    #to_chain = "zksync"

    from_chains = ["scroll"]
    to_chain = "linea"

    min_amount = 0.005
    max_amount = 0.0051
    decimal = 4

    all_amount = True

    min_percent = 98
    max_percent = 100
    save_funds = [0.0005, 0.0007]

    orbiter = Orbiter(account_id, key, from_chains, recipient)
    await orbiter.bridge(to_chain, min_amount, max_amount, decimal, all_amount, min_percent, max_percent, save_funds)


async def deposit_full_amount_okx(_id, key, recipient):
    """
    Deposit all ETH to OKX
    ______________________________________________________
    min_left_amount - min amount to left on account (ETH)
    max_left_amount - max amount to left on account (ETH)
    chains - ['zksync', 'arbitrum', 'linea', 'base', 'optimism']
    to_address - address to send
    terminate - if True - terminate program if money is not withdrawn
    """
    token = 'ETH'
    to_address = recipient
    chains = ['linea']

    min_left_amount = 0.00035
    max_left_amount = 0.00043

    terminate = True
    if len(recipient) == 0:
        raise ValueError('recipient is null')
    okx_exchange = Okx(_id, key, chains, recipient)
    await okx_exchange.okx_deposit(min_left_amount, max_left_amount, token, to_address, terminate)

async def deposit_scroll(account_id, key, recipient):
    """
    Deposit from official bridge
    ______________________________________________________
    all_amount - bridge from min_percent to max_percent
    """

    min_amount = 0.001
    max_amount = 0.002
    decimal = 4

    all_amount = True

    min_percent = 1
    max_percent = 1

    scroll = Scroll(account_id, key, "ethereum", recipient)
    await scroll.deposit(min_amount, max_amount, decimal, all_amount, min_percent, max_percent)


async def withdraw_scroll(account_id, key, recipient):
    """
    Withdraw from official bridge
    ______________________________________________________
    all_amount - withdraw from min_percent to max_percent
    """

    min_amount = 0.0012
    max_amount = 0.0012
    decimal = 4

    all_amount = True

    min_percent = 10
    max_percent = 10

    scroll = Scroll(account_id, key, "scroll", recipient)
    await scroll.withdraw(min_amount, max_amount, decimal, all_amount, min_percent, max_percent)

async def bridge_orbiter(account_id, key, recipient):
    """
    Bridge from orbiter
    ______________________________________________________
    from_chain – ethereum, polygon_zkevm, arbitrum, optimism, zksync | Select one
    to_chain – ethereum, polygon_zkevm, arbitrum, optimism, zksync | Select one

    save_funds - how much eth save on the account (min and max, choose randomly)
    min_required_amount - минимальная требуемая сумма в сети, на которую будет реагировать модуль в eth
    """

    #from_chains = ["arbitrum", "optimism", "base", "scroll", "linea"]
    #to_chain = "zksync"

    from_chains = ["zksync"]
    to_chain = "scroll"

    min_amount = 0.005
    max_amount = 0.0051
    decimal = 4

    all_amount = True

    min_percent = 98
    max_percent = 100
    save_funds = [0.007, 0.011]

    orbiter = Orbiter(account_id, key, from_chains, recipient)
    await orbiter.bridge(to_chain, min_amount, max_amount, decimal, all_amount, min_percent, max_percent, save_funds)

async def bridge_layerswap(account_id, key, recipient):
    """
    Bridge from Layerswap
    ______________________________________________________
    from_chain - Choose any chain: ethereum, arbitrum, optimism, avalanche, polygon, base, scroll
    to_chain - Choose any chain: ethereum, arbitrum, optimism, avalanche, polygon, base, scroll

    make_withdraw - True, if need withdraw after deposit

    all_amount - deposit from min_percent to max_percent
    """

    from_chain = "zksync"
    to_chain = "scroll"

    min_amount = 0.003
    max_amount = 0.004

    decimal = 5

    all_amount = True

    min_percent = 98
    max_percent = 100
    save_funds = [0.007, 0.011]

    layerswap = LayerSwap(account_id=account_id, private_key=key, chain=from_chain, recipient=recipient)
    await layerswap.bridge(
        from_chain, to_chain, min_amount, max_amount, decimal, all_amount, min_percent, max_percent, save_funds
    )


async def bridge_nitro_to_linea(account_id, key, recipient):
    """
    Bridge from nitro
    ______________________________________________________
    from_chain – ethereum, arbitrum, optimism, zksync, scroll, base, linea | Select one
    to_chain – ethereum, arbitrum, optimism, zksync, scroll, base, linea | Select one
    """

    from_chain = "scroll"
    to_chain = "linea"

    min_amount = 0.005
    max_amount = 0.0051
    decimal = 4

    all_amount = True

    min_percent = 98
    max_percent = 100
    save_funds = [0.0008, 0.001]

    nitro = Nitro(account_id=account_id, private_key=key, chain=from_chain, recipient=recipient)
    await nitro.bridge(to_chain, min_amount, max_amount, decimal, all_amount, min_percent, max_percent, save_funds)


async def bridge_nitro(account_id, key, recipient):
    """
    Bridge from nitro
    ______________________________________________________
    from_chain – ethereum, arbitrum, optimism, zksync, scroll, base, linea | Select one
    to_chain – ethereum, arbitrum, optimism, zksync, scroll, base, linea | Select one
    """

    from_chain = "zksync"
    to_chain = "scroll"

    min_amount = 0.005
    max_amount = 0.0051
    decimal = 4

    all_amount = True

    min_percent = 98
    max_percent = 100
    save_funds = [0.007, 0.011]

    nitro = Nitro(account_id=account_id, private_key=key, chain=from_chain, recipient=recipient)
    await nitro.bridge(to_chain, min_amount, max_amount, decimal, all_amount, min_percent, max_percent, save_funds)


async def wrap_eth(account_id, key, recipient):
    """
    Wrap ETH
    ______________________________________________________
    all_amount - wrap from min_percent to max_percent
    """

    min_amount = 0.001
    max_amount = 0.002
    decimal = 4

    all_amount = True

    min_percent = 5
    max_percent = 10

    scroll = Scroll(account_id, key, "scroll", recipient)
    await scroll.wrap_eth(min_amount, max_amount, decimal, all_amount, min_percent, max_percent)


async def unwrap_eth(account_id, key, recipient):
    """
    Unwrap ETH
    ______________________________________________________
    all_amount - unwrap from min_percent to max_percent
    """

    min_amount = 0.001
    max_amount = 0.002
    decimal = 4

    all_amount = True

    min_percent = 100
    max_percent = 100

    scroll = Scroll(account_id, key, "scroll", recipient)
    await scroll.unwrap_eth(min_amount, max_amount, decimal, all_amount, min_percent, max_percent)


async def swap_skydrome(account_id, key, recipient):
    """
    Make swap on Skydrome
    ______________________________________________________
    from_token – Choose SOURCE token ETH, USDC | Select one
    to_token – Choose DESTINATION token ETH, USDC | Select one

    Disclaimer - You can swap only ETH to any token or any token to ETH!
    ______________________________________________________
    all_amount - swap from min_percent to max_percent
    """

    from_token = "USDC"
    to_token = "ETH"

    min_amount = 0.0001
    max_amount = 0.0002
    decimal = 6
    slippage = 1

    all_amount = True

    min_percent = 100
    max_percent = 100

    skydrome = Skydrome(account_id, key, recipient)
    await skydrome.swap(
        from_token, to_token, min_amount, max_amount, decimal, slippage, all_amount, min_percent, max_percent
    )


async def swap_zebra(account_id, key, recipient):
    """
    Make swap on Zebra
    ______________________________________________________
    from_token – Choose SOURCE token ETH, USDC | Select one
    to_token – Choose DESTINATION token ETH, USDC | Select one

    Disclaimer - You can swap only ETH to any token or any token to ETH!
    ______________________________________________________
    all_amount - swap from min_percent to max_percent
    """

    from_token = "USDC"
    to_token = "ETH"

    min_amount = 0.0001
    max_amount = 0.0002
    decimal = 6
    slippage = 1

    all_amount = True

    min_percent = 100
    max_percent = 100

    zebra = Zebra(account_id, key, recipient)
    await zebra.swap(
        from_token, to_token, min_amount, max_amount, decimal, slippage, all_amount, min_percent, max_percent
    )


async def swap_syncswap(account_id, key, recipient):
    """
    Make swap on SyncSwap

    from_token – Choose SOURCE token ETH, USDC | Select one
    to_token – Choose DESTINATION token ETH, USDC | Select one

    Disclaimer – Don't use stable coin in from and to token | from_token USDC to_token USDT DON'T WORK!!!
    ______________________________________________________
    all_amount - swap from min_percent to max_percent
    """

    from_token = "USDC"
    to_token = "ETH"

    min_amount = 1
    max_amount = 2
    decimal = 6
    slippage = 1

    all_amount = True

    min_percent = 100
    max_percent = 100

    syncswap = SyncSwap(account_id, key, recipient)
    await syncswap.swap(
        from_token, to_token, min_amount, max_amount, decimal, slippage, all_amount, min_percent, max_percent
    )


async def swap_xyswap(account_id, key, recipient):
    """
    Make swap on XYSwap
    ______________________________________________________
    from_token – Choose SOURCE token ETH, WETH, USDC | Select one
    to_token – Choose DESTINATION token ETH, WETH, USDC | Select one

    Disclaimer - If you use True for use_fee, you support me 1% of the transaction amount
    ______________________________________________________
    all_amount - swap from min_percent to max_percent
    """

    from_token = "USDC"
    to_token = "ETH"

    min_amount = 0.0001
    max_amount = 0.0001
    decimal = 6
    slippage = 1

    all_amount = True

    min_percent = 100
    max_percent = 100

    xyswap = XYSwap(account_id, key, recipient)
    await xyswap.swap(
        from_token, to_token, min_amount, max_amount, decimal, slippage, all_amount, min_percent, max_percent
    )


async def deposit_layerbank(account_id, key, recipient):
    """
    Make deposit on LayerBank
    ______________________________________________________
    make_withdraw - True, if need withdraw after deposit

    all_amount - deposit from min_percent to max_percent
    """
    min_amount = 0.0001
    max_amount = 0.0002
    decimal = 5

    sleep_from = 5
    sleep_to = 24

    make_withdraw = True

    all_amount = True

    min_percent = 5
    max_percent = 10

    layerbank = LayerBank(account_id, key, recipient)
    await layerbank.deposit(
        min_amount, max_amount, decimal, sleep_from, sleep_to, make_withdraw, all_amount, min_percent, max_percent
    )


async def deposit_aave(account_id, key, recipient):
    """
    Make deposit on Aave
    ______________________________________________________
    make_withdraw - True, if need withdraw after deposit

    all_amount - deposit from min_percent to max_percent
    """
    min_amount = 0.0001
    max_amount = 0.0002
    decimal = 5

    sleep_from = 5
    sleep_to = 24

    make_withdraw = True

    all_amount = True

    min_percent = 5
    max_percent = 10

    aave = Aave(account_id, key, recipient)
    await aave.deposit(
        min_amount, max_amount, decimal, sleep_from, sleep_to, make_withdraw, all_amount, min_percent, max_percent
    )


async def mint_zerius(account_id, key, recipient):
    """
    Mint + bridge Zerius NFT
    ______________________________________________________
    chains - list chains for random chain bridge: arbitrum, optimism, polygon, bsc, avalanche
    Disclaimer - The Mint function should be called "mint", to make sure of this, look at the name in Rabby Wallet or in explorer
    """

    chains = ["arbitrum"]

    sleep_from = 10
    sleep_to = 20

    zerius = Zerius(account_id, key, recipient)
    await zerius.bridge(chains, sleep_from, sleep_to)


async def mint_l2pass(account_id, key, recipient):
    """
    Mint L2Pass NFT
    """

    contract = "0x0000049f63ef0d60abe49fdd8bebfa5a68822222"

    l2pass = L2Pass(account_id, key, recipient)
    await l2pass.mint(contract)


async def mint_nft(account_id, key, recipient):
    """
    Mint NFT on NFTS2ME
    ______________________________________________________
    contracts - list NFT contract addresses
    """

    contracts = [""]

    minter = Minter(account_id, key, recipient)
    await minter.mint_nft(contracts)


async def mint_zkstars(account_id, key, recipient):
    """
    Mint ZkStars NFT
    """

    contracts = [
        "0x609c2f307940b8f52190b6d3d3a41c762136884e",
        "0x16c0baa8a2aa77fab8d0aece9b6947ee1b74b943",
        "0xc5471e35533e887f59df7a31f7c162eb98f367f7",
        "0xf861f5927c87bc7c4781817b08151d638de41036",
        "0x954e8ac11c369ef69636239803a36146bf85e61b",
        "0xa576ac0a158ebdcc0445e3465adf50e93dd2cad8",
        "0x17863384c663c5f95e4e52d3601f2ff1919ac1aa",
        "0x4c2656a6d1c0ecac86f5024e60d4f04dbb3d1623",
        "0x4e86532cedf07c7946e238bd32ba141b4ed10c12",
        "0x6b9db0ffcb840c3d9119b4ff00f0795602c96086",
        "0x10d4749bee6a1576ae5e11227bc7f5031ad351e4",
        "0x373148e566e4c4c14f4ed8334aba3a0da645097a",
        "0xdacbac1c25d63b4b2b8bfdbf21c383e3ccff2281",
        "0x2394b22b3925342f3216360b7b8f43402e6a150b",
        "0xf34f431e3fc0ad0d2beb914637b39f1ecf46c1ee",
        "0x6f1e292302dce99e2a4681be4370d349850ac7c2",
        "0xa21fac8b389f1f3717957a6bb7d5ae658122fc82",
        "0x1b499d45e0cc5e5198b8a440f2d949f70e207a5d",
        "0xec9bef17876d67de1f2ec69f9a0e94de647fcc93",
        "0x5e6c493da06221fed0259a49beac09ef750c3de1"
    ]

    mint_min = 1
    mint_max = 1

    mint_all = False

    sleep_from = 5
    sleep_to = 10

    zkkstars = ZkStars(account_id, key, recipient)
    await zkkstars.mint(contracts, mint_min, mint_max, mint_all, sleep_from, sleep_to)


async def send_message(account_id, key, recipient):
    """
    Send message with L2Telegraph
    ______________________________________________________
    chain - select need chain to send message, you can specify several, one will be selected randomly

    availiable chaines: bsc, optimism, avalanche, arbitrum, polygon, linea, moonbeam, kava, telos, klaytn, gnosis, moonriver
    """
    use_chain = ["gnosis", "moonriver"]

    l2telegraph = L2Telegraph(account_id, key, recipient)
    await l2telegraph.send_message(use_chain)


async def bridge_nft(account_id, key, recipient):
    """
    Make mint NFT and bridge NFT on L2Telegraph
    ______________________________________________________
    chain - select need chain to send message, you can specify several, one will be selected randomly

    availiable chaines: bsc, optimism, avalanche, arbitrum, polygon, linea
    """
    use_chain = ["polygon"]

    sleep_from = 5
    sleep_to = 20

    l2telegraph = L2Telegraph(account_id, key, recipient)
    await l2telegraph.bridge(use_chain, sleep_from, sleep_to)


async def make_transfer(_id, key, recipient):
    """
    Transfer ETH
    """

    min_amount = 0.0001
    max_amount = 0.0002
    decimal = 5

    all_amount = True

    min_percent = 10
    max_percent = 10

    transfer = Transfer(_id, key, recipient)
    await transfer.transfer(min_amount, max_amount, decimal, all_amount, min_percent, max_percent)


async def swap_tokens(account_id, key, recipient):
    """
    SwapTokens module: Automatically swap tokens to ETH
    ______________________________________________________
    use_dex - Choose any dex: syncswap, skydrome, zebra, xyswap
    """

    use_dex = [
        "syncswap", "skydrome", "zebra"
    ]

    use_tokens = ["USDC"]

    sleep_from = 1
    sleep_to = 5

    slippage = 0.1

    min_percent = 100
    max_percent = 100

    swap_tokens = SwapTokens(account_id, key, recipient)
    await swap_tokens.swap(use_dex, use_tokens, sleep_from, sleep_to, slippage, min_percent, max_percent)


async def swap_multiswap(account_id, key, recipient):
    """
    Multi-Swap module: Automatically performs the specified number of swaps in one of the dexes.
    ______________________________________________________
    use_dex - Choose any dex: syncswap, skydrome, zebra, xyswap
    quantity_swap - Quantity swaps
    ______________________________________________________
    If back_swap is True, then, if USDC remains, it will be swapped into ETH.
    """

    use_dex = ["syncswap", "skydrome", "zebra"]

    min_swap = 3
    max_swap = 4

    sleep_from = 3
    sleep_to = 7

    slippage = 0.1

    back_swap = True

    min_percent = 20
    max_percent = 30

    multi = Multiswap(account_id, key, recipient)
    await multi.swap(
        use_dex, sleep_from, sleep_to, min_swap, max_swap, slippage, back_swap, min_percent, max_percent
    )


async def multibridge(account_id, key, recipient):
    """
    MultriBridge - Makes a bridge from a random network where there is a minimum acceptable balance
    ______________________________________________________
    use_bridge - right now only nitro

    source_chain – ethereum, arbitrum, optimism, zksync, scroll, base, linea | Select one or more
    destination_chain - ethereum, arbitrum, optimism, zksync, scroll, base, linea | Select one

    min_chain_balance - minimum acceptable balance for bridge
    """

    use_bridge = "nitro"

    source_chain = ["optimism", "zksync", "base", "linea"]
    destination_chain = "scroll"

    min_amount = 0.005
    max_amount = 0.006
    decimal = 4

    all_amount = False

    min_percent = 5
    max_percent = 10

    min_chain_balance = 0.006

    multibridge = Multibridge(account_id=account_id, private_key=key, recipient=recipient)
    await multibridge.bridge(use_bridge, source_chain, destination_chain, min_amount, max_amount, decimal, all_amount, min_percent, max_percent, min_chain_balance)


async def custom_routes(account_id, key, recipient):
    """
    BRIDGE:
        – deposit_scroll
        – withdraw_scroll
        – bridge_orbiter
        – bridge_layerswap
        – bridge_nitro
    WRAP:
        – wrap_eth
        – unwrap_eth
    DEX:
        – swap_skydrome
        – swap_syncswap
        – swap_zebra
        – swap_xyswap
    LIQUIDITY:
    LANDING:
        – depost_layerbank
        – withdraw_layerbank
        – deposit_aave
        – withdraw_aave
    NFT/DOMAIN:
        – mint_zerius
        – mint_zkstars
        – create_omnisea
        – mint_nft
        – mint_l2pass
    ANOTHER:
        – swap_multiswap
        – multibridge
        – swap_tokens
        – send_mail (Dmail)
        – create_safe
        – rubyscore_vote
        – deploy_contract
    ______________________________________________________
    Disclaimer - You can add modules to [] to select random ones,
    example [module_1, module_2, [module_3, module_4], module 5]
    The script will start with module 1, 2, 5 and select a random one from module 3 and 4

    You can also specify None in [], and if None is selected by random, this module will be skipped

    You can also specify () to perform the desired action a certain number of times
    example (send_mail, 1, 10) run this module 1 to 10 times
    """

    logger.info(f"[{account_id}][{recipient}] Acc recipient")

    use_modules = [
        mint_zerius,
        swap_multiswap,
        [create_omnisea, None],
        [mint_zkstars, mint_l2pass],
        [deploy_contract, None],
        [send_mail, create_safe, None],
        [deposit_layerbank, deposit_aave]
    ]

    sleep_from = 110
    sleep_to = 200

    random_module = True

    await withdraw_okx(account_id, key, recipient);
    
    await sleep(sleep_from, sleep_to);

    bridge_scroll_actions : list = [
        [bridge_nitro, bridge_layerswap, bridge_orbiter]
    ]
    
    routes = Routes(account_id, key, recipient)

    await routes.start(bridge_scroll_actions, sleep_from, sleep_to, False)

    await routes.start(use_modules, sleep_from, sleep_to, random_module)

    bridge_from_scroll_actions : list = [
        [bridge_nitro_to_linea, bridge_orbiter_from_scroll]
    ]
    
    await routes.start(bridge_from_scroll_actions, sleep_from, sleep_to, False)

    await sleep(160, 200);

    await deposit_full_amount_okx(account_id, key, recipient);
    
    await sleep(200, 250);


#########################################
########### NO NEED TO CHANGE ###########
#########################################

async def withdraw_layerbank(account_id, key, recipient):
    layerbank = LayerBank(account_id, key, recipient)
    await layerbank.withdraw()


async def withdraw_aave(account_id, key, recipient):
    aave = Aave(account_id, key, recipient)
    await aave.withdraw()


async def send_mail(account_id, key, recipient):
    dmail = Dmail(account_id, key, recipient)
    await dmail.send_mail()


async def create_omnisea(account_id, key, recipient):
    omnisea = Omnisea(account_id, key, recipient)
    await omnisea.create()


async def create_safe(account_id, key, recipient):
    gnosis_safe = GnosisSafe(account_id, key, recipient)
    await gnosis_safe.create_safe()


async def deploy_contract(account_id, key, recipient):
    deployer = Deployer(account_id, key, recipient)
    await deployer.deploy_token()


async def rubyscore_vote(account_id, key, recipient):
    rubyscore = RubyScore(account_id, key, recipient)
    await rubyscore.vote()


async def nft_origins(account_id, key, recipient):
    nft = NftOrigins(account_id, key, recipient)
    await nft.mint()


def get_tx_count():
    asyncio.run(check_tx())
