// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.0;

contract Bank {
    uint256 private balance;
    address public accOwner;

    constructor() {
        accOwner = msg.sender;
    }

    modifier onlyOwner() {
        require(msg.sender == accOwner, "You are not an account owner");
        _;
    }

    // Deposit Ether into the contract
    function Deposit() public payable onlyOwner {
        require(msg.value > 0, "Amount should be greater than 0!");
        balance += msg.value;
    }

    // Withdraw a specified amount of Ether to the owner
    function Withdraw(uint256 amount) public onlyOwner {
        require(amount > 0, "Withdrawal amount should be greater than 0!");
        require(amount <= balance, "Insufficient deposited balance!");

        // Update state before making the external call
        balance -= amount;

        (bool success, ) = payable(accOwner).call{value: amount}("");
        require(success, "Ether transfer failed!");
    }

    // Show the owner's recorded balance (in wei)
    function ShowBalance() public view onlyOwner returns (uint256) {
        return balance;
    }

    // Show the actual Ether held by this contract (in wei)
    function ShowContractEtherBalance() public view returns (uint256) {
        return address(this).balance;
    }
}
