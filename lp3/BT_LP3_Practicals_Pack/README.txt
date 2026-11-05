BT LP3 PRACTICALS - COMPLETE TEXT AND VIVA PACK
=================================================

PRACTICALS INCLUDED (from your LP3 chit)
----------------------------------------
13. MetaMask installation and study of Ether spending per transaction.
14. Create your own wallet using MetaMask for crypto transactions.
15. Bank smart contract on a test network: Deposit, Withdraw, ShowBalance.
16. Student data smart contract using structures, arrays, fallback/receive;
    deploy and observe transaction fee and gas.
17. Survey report on types of blockchains and real-world use cases.
18. BT Mini Project - a preparation/report template and general viva questions.

FOLDER CONTENTS
---------------
Each Practical_XX folder contains:
- Practical_XX_Notes.txt: aim, explanation, procedure, observation/result.
- Practical_XX_Viva_QA.txt: 10 short questions and answers for that practical.
- Solidity .sol and matching .txt files for the supplied Bank and Student code.

At the root:
- BT_Viva_QA_All_Practicals_13_to_18.txt: all 60 viva questions and answers
  in ONE combined file.
- README.txt: this guide.

IMPORTANT BANK CONTRACT NOTE
-----------------------------
Your uploaded Bank.sol is preserved unchanged as Bank_Original_From_Upload.
Its Withdraw() is payable and subtracts msg.value from the internal balance,
but it does not send Ether to the owner. A separately labelled Bank_Corrected
version is included with Withdraw(amount) that transfers Ether to the owner.
Do not mistake the corrected version for the original submitted code; follow
the code version required by your instructor.

STUDENT CONTRACT NOTE
---------------------
Student.sol is transcribed from your upload. It uses a Student struct, a
dynamic array, duplicate-roll-number checking, require/revert, fallback and
receive. The contract has no Ether-withdraw function, so do not send valuable
funds to it.

HOW TO USE IN REMIX
-------------------
1. Open https://remix.ethereum.org/.
2. Create a new .sol file and paste the required contract.
3. Select a compiler compatible with pragma ^0.8.0 and compile.
4. Use Remix VM for a local test, or connect MetaMask to a test network.
5. Deploy and test the contract functions.
6. Inspect transaction details for gas used and fees.

For Remix, the wallet environment may appear as Browser Extension or
Injected Provider - MetaMask depending on the current Remix interface.

SAFETY
------
- Use test networks and test ETH for practice.
- Never share your Secret Recovery Phrase or private key.
- Do not deploy classroom/demo code with real funds.
- These teaching contracts are not audited for production use.

OFFICIAL REFERENCES
-------------------
MetaMask install:
https://support.metamask.io/start/getting-started-with-metamask

Create a MetaMask wallet:
https://support.metamask.io/start/creating-a-new-wallet

Remix smart contract compile/deploy:
https://github.com/remix-project-org/remix-ide/blob/master/docs/create_deploy.md

Ethereum transaction fee mechanism:
https://eips.ethereum.org/EIPS/eip-1559

SCOPE NOTE
----------
The chit only names Practical 18 as "BT: Mini Project" and does not give a
project title or code. Therefore Practical 18 contains a reusable template
and general viva questions, not an invented project implementation.
