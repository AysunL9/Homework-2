# 2024-Spring-HW2

Please complete the report problem below:

## Problem 1
Provide your profitable path, the amountIn, amountOut value for each swap, and your final reward (your tokenB balance).

> Solution

path: tokenB(amount:5)->tokenA(amount:5.65532199)->tokenD(amount:2.458781318)->tokenC(amount:5.08892727)->tokenB(amount:20.12988895), final reward=20.129889

## Problem 2
What is slippage in AMM, and how does Uniswap V2 address this issue? Please illustrate with a function as an example.

> Solution

In Automated Market Making (AMM) systems like Uniswap, slippage refers to the difference between the expected price of a trade and the price at which the trade is executed. This difference occurs because of the constant price impact that occurs as trades are made against the liquidity pool.

Uniswap V2 addresses slippage by implementing a feature called the constant product formula. In this formula, the product of the quantities of two assets in a liquidity pool remains constant, which results in a linear relationship between the quantity of one asset being traded and the price impact it has on the other asset.

Example:
Suppose we have a Uniswap V2 liquidity pool containing ETH and DAI tokens. The constant product formula is given by:
$\( x \cdot y = k \)$

Where:
-  $x$  is the quantity of ETH in the pool
-  $y$  is the quantity of DAI in the pool
-  $k$  is the constant product of the two quantities

Now, let's say the initial quantities in the pool are:
-  $x = 1000$  ETH
-  $y = 20000$  DAI

So,  $k = 1000 \times 20000 = 20,000,000 $

Now, a trader wants to swap 10 ETH for DAI. Before the swap, the price of DAI in terms of ETH can be calculated as  $y / x$ , which is  $20000 / 1000 = 20$ DAI/ETH .

After the swap, the new quantities of ETH and DAI in the pool will be:
-  $x' $= 990 ETH (10 ETH were removed)
-  $y'$ =  (let's calculate it)

Using the constant product formula:

 $x' \times y' = k $

 $990 \times y' = 20,000,000 $

 $y' = \frac{20,000,000}{990}$

Now, let's calculate the new price of DAI in terms of ETH:

$\( \frac{y'}{x'} = \frac{\frac{20,000,000}{990}}{990} \approx 20.2020 \)$

So, after the swap, the price of DAI in terms of ETH increased slightly due to slippage.

Uniswap V2's constant product formula ensures that the more a trader tries to swap, the more the price will move against them, discouraging large trades that could significantly impact the market.

## Problem 3
Please examine the mint function in the UniswapV2Pair contract. Upon initial liquidity minting, a minimum liquidity is subtracted. What is the rationale behind this design?

> Solution

The rationale behind subtracting a minimum liquidity amount during the initial liquidity minting in the UniswapV2Pair contract is to prevent users from adding extremely small amounts of liquidity that could be disproportionately costly to the efficiency of the liquidity pool.
1. **Efficiency and Cost-effectiveness**: Liquidity provision involves gas costs, which can be significant, especially for small transactions. If there were no minimum liquidity requirement, users could add tiny amounts of liquidity to the pool, resulting in many small liquidity positions. Managing a large number of small positions can be inefficient and costly both in terms of gas fees and computational resources.

2. **Improving Liquidity Depth**: By enforcing a minimum liquidity requirement, the protocol ensures that liquidity providers add a meaningful amount of liquidity to the pool. This helps to deepen the liquidity pool, making it more resilient to price fluctuations and providing better execution for traders.

3. **Reducing Arbitrage Opportunities**: A minimum liquidity requirement can also help mitigate potential arbitrage opportunities that arise from small imbalances in the pool. If users could add minuscule amounts of liquidity without restriction, it could lead to more frequent and exploitable price disparities between Uniswap and external markets.

Overall, enforcing a minimum liquidity requirement helps to maintain the efficiency, stability, and integrity of the Uniswap liquidity pools. It encourages users to provide liquidity in meaningful amounts, ultimately benefiting both liquidity providers and traders on the platform.

## Problem 4
Investigate the minting function in the UniswapV2Pair contract. When depositing tokens (not for the first time), liquidity can only be obtained using a specific formula. What is the intention behind this?

> Solution

Investigate the minting function in the UniswapV2Pair contract. When depositing tokens (not for the first time), liquidity can only be obtained using a specific formula. What is the intention behind this?
ChatGPT
The specific formula used for minting liquidity tokens in UniswapV2Pair contract is designed to ensure that liquidity providers receive their fair share of the pool's assets based on the relative value of the tokens they are depositing.

In Uniswap V2, the liquidity provision mechanism involves users depositing equal values of two different tokens into a liquidity pool. When they deposit tokens into the pool, they receive liquidity tokens in return, representing their share of the pool's assets. However, the exact amount of liquidity tokens they receive is calculated using a formula that takes into account the current balances of the tokens in the pool.

The intention behind using this formula is to maintain a balanced and efficient liquidity pool where the value of the assets deposited by liquidity providers accurately reflects their share of the pool. This helps to prevent manipulation or unfair advantage by liquidity providers and ensures that the liquidity pool operates effectively to facilitate trades with minimal slippage.

By using a specific formula to determine the amount of liquidity tokens issued to liquidity providers, Uniswap V2 aims to create a fair and transparent mechanism for participating in liquidity provision while maintaining the integrity and efficiency of the decentralized exchange.

## Problem 5
What is a sandwich attack, and how might it impact you when initiating a swap?

> Solution
> A sandwich attack is a type of manipulation in decentralized exchanges (DEXs) like Uniswap where an attacker exploits the predictable price movement caused by their own transactions to profit at the expense of other traders.

Here's how a sandwich attack typically works:

1. **Identifying the Target Transaction**: The attacker monitors the pending transactions in the mempool, waiting for a large trade to be submitted.

2. **Front-Running**: The attacker quickly submits two transactions—one before the target transaction and one after it. The first transaction is typically a small trade that slightly moves the price against the target trader. The second transaction is the attacker's main trade, which takes advantage of the price movement caused by the first transaction.

3. **Profit Extraction**: By executing their trade between the target trader's transactions, the attacker can buy at a slightly lower price and sell at a slightly higher price, profiting from the price difference caused by their own actions.

The impact of a sandwich attack on an individual initiating a swap can be significant:

1. **Slippage**: The price movement caused by the attacker's transactions can result in increased slippage for the target trader. Slippage refers to the difference between the expected price of a trade and the price at which it is executed. Higher slippage means the trader gets a worse deal.

2. **Loss of Funds**: The target trader may end up paying a higher price for their trade or receiving a lower price for their assets, leading to financial losses.

3. **Frustration and Trust Issues**: Encountering a sandwich attack can lead to frustration and loss of trust in the decentralized exchange platform, potentially driving traders away from using it in the future.

To mitigate the risk of sandwich attacks, traders can consider using strategies such as setting appropriate slippage tolerance, using decentralized finance (DeFi) aggregators that implement anti-front-running measures, or waiting for periods of lower network congestion to reduce the likelihood of being targeted by attackers. Additionally, decentralized exchange protocols can implement measures to prevent or mitigate the impact of sandwich attacks, such as implementing anti-front-running mechanisms or increasing the cost of executing multiple transactions within a short period.
