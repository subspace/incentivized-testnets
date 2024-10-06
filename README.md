# Subspace Incentivized Testnets Archive
## Farming Reward Allocations
Final farming reward allocations (excluding Stake Wars 1) can be found in the [CSV file](https://github.com/subspace/incentivized-testnets/blob/main/Final_farming_rewards.csv)
Detailed breakdown of all incentivized testnets and exact calculation formulas can be found in the [XLSX file](https://github.com/subspace/incentivized-testnets/blob/main/Subspace%20Testnet%20Token%20Distribution%20List_calculations_FINAL.xlsx) which was created as follows:
1. Calculate all tokens that were generated during each testnet period Gemini 1,2, 3F and 3G  (total number of tokens)
2. Calculate all rewards that were generated during each testnet period  3H Pool 1 and 3H Pool 2  (total number of rewards)
3. Create a pivot table to list each wallet's participation in each testnet category
4. Calculate the relative reward for each wallet for each testnet ( reward / total number of rewards)
   
### Gemini 1
1. Calculate the relative reward for each wallet
    1. Distribute the allocation of 0.3% to all wallets proportional to their relative reward
    2. Count all wallets that have participated in Gemini 1 (reported number 13'106) and divide 0.2% by the number of wallets
2. Add this amount to all wallets that have participated in Gemini 1
   
### Gemini 2
**First Incentive:**
1. Calculate the relative reward for each wallet
2. Distribute the allocation of 0.05% to all wallets proportional to their relative reward

**Second Incentive (only wallets with 3 tSSC balance are qualified):**
1. Calculate the relative reward for each wallet
2. Distribute the allocation of 0.5% to all wallets (only above 3tSSC) proportional to their relative reward

### Gemini 3:
1. Determine the proportions of each testnet for 3F-3H Pool 1 (numbers of blocks generated during the testnet divided by the number of all blocks)
2. Determine the total relative reward during 3F-3H pool 1 proportional to the testnet block count for each wallet
3. Determine the relative reward during 3H pool 2 for each wallet
4. Determine the aggregated token allocation for each testnet period (e.g., 0.1% * number of weeks for 3F-3H Pool 1 and 0.05% * number of weeks for 3H Pool 2)
5. Multiply the relative reward of each wallet with the aggregated token allocation for each testnet period
6. Multiply the relative allocation of each wallet with the token supply (1B token) to get the absolute number of tokens per wallet"

**Incentivized Phases**

![Gemini 3 Incentivized Phases](<Testnet Reward Phases.png>)

## Stake Wars 1 Allocations
Can be found in the [XLSX File](https://github.com/subspace/incentivized-testnets/blob/main/Stake%20Wars%201.xlsx). An explanation of the rewards structure can be found on [the Autonomys forum](https://forum.autonomys.xyz/t/stake-wars-introduction/2060#rewards-9).

## Node Archives
Archive of Subspace incentivized testnets node databases includes:
- 2 Farmnet networks: pre-stress test (usable with 2022-jan-05 snapshot), and stress test
- 5 Gemini networks (only incentivized): 1b, 2a, 3f, 3g, 3h

Magnet Link:
magnet:?xt=urn:btih:17fea42d965c34553889a207d8945e44834f0187&xt=urn:btmh:1220f926295fb0a3e117c771627290f59ef5844dd59fbc7041626b9f59f22d9d4fe2&dn=Subspace%20Testnet%20Archive

The archive contains a separate file per network, weighing 256.03 GiB total.
