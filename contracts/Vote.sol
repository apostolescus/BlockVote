// SPRX-License-Identifier: MIT

pragma solidity 0.8.7;

contract Voting {
    uint256 public candidatesNumber = 0;
    string[] public candidatesName;
    uint256[] private candidatesResults;

    uint256[][] private votes;
    uint256 private voteCounter;
    bool private voteState = false;
    address[] public votersAddress;

    uint256 private nsquare;
    bool private clearRes = true;

    address private owner;

    constructor() {
        owner = msg.sender;
    }

    // Init voting session

    function startVote() public {
        require(msg.sender == owner, "You can not start voting session");
        require(clearRes, "You have to clear previous vote results before");

        voteState = true;
        clearRes = false;
    }

    function clearResults() private {
        delete candidatesResults;
        delete votersAddress;
        delete candidatesName;
        clearRes = true;
        candidatesNumber = 0;
        voteCounter = 0;
        delete votes;
    }

    function endVote() public returns (uint256[] memory) {
        // clear vote specific variables
        voteState = false;

        for (uint256 i = 0; i < candidatesNumber; i++) {
            uint256 sum = votes[0][i];
            for (uint256 j = 1; j < voteCounter; j++) {
                sum = addPaillier(sum, votes[j][i]);
            }
            candidatesResults.push(sum);
        }
        return candidatesResults;
    }

    function resetVote(uint256 _nsquare) public {
        require(msg.sender == owner, "You are not allowed to update!");
        require(!voteState, "Vote is started. You have to stop it first");

        nsquare = _nsquare;
        clearResults();
    }

    function addCandidate(string memory _candidate) public {
        require(msg.sender == owner, "You can not define any candidates");
        require(clearRes, "Clear previous results!");
        require(!voteState, "Vote started, you can not add candidates");
        require(checkCandidate(_candidate), "Candidate already exist!");

        candidatesName.push(_candidate);
        candidatesNumber++;
    }

    function vote(uint256[] memory _votes) public {
        // check if vote is started
        require(voteState, "Vote is closed!");

        // check for double voting
        require(checkAddress(), "You already voted.");

        // check array size
        require(
            _votes.length == candidatesNumber,
            "Candidates number missmatch!"
        );
        require(!checkVoteCorrectitude(_votes), "Incorrect vote!");

        votes.push(_votes);

        voteCounter = voteCounter + 1;

        // Save the current voters address
        votersAddress.push(msg.sender);
    }

    // View Functions

    function viewCandidates() public view returns (string[] memory) {
        return candidatesName;
    }

    // Get Functions

    function getFinalResults() public view returns (uint256[] memory) {
        return candidatesResults;
    }

    function getOwner() public view returns (address) {
        return owner;
    }

    function getVotes(uint256 _number) public view returns (uint256[] memory) {
        require(
            msg.sender == owner,
            " You are not allowed to check the results!"
        );
        return votes[_number];
    }

    // Utilities

    function checkVoteCorrectitude(uint256[] memory _votes)
        public
        view
        returns (bool)
    {
        uint256 counter = 0;
        for (uint256 i = 0; i < candidatesNumber; i++) {
            counter = counter + _votes[i];
        }
        if (counter > 1) {
            return false;
        }
        return true;
    }

    function compareStrings(string memory a, string memory b)
        public
        pure
        returns (bool)
    {
        return (keccak256(abi.encodePacked((a))) ==
            keccak256(abi.encodePacked((b))));
    }

    function checkAddress() private view returns (bool) {
        for (uint256 i; i < votersAddress.length; i++) {
            if (msg.sender == votersAddress[i]) {
                return false;
            }
        }
        return true;
    }

    function checkCandidate(string memory _candidate)
        private
        view
        returns (bool)
    {
        for (uint256 i; i < candidatesName.length; i++) {
            if (compareStrings(_candidate, candidatesName[i])) {
                return false;
            }
        }
        return true;
    }

    function addPaillier(uint256 num1, uint256 num2)
        private
        view
        returns (uint256)
    {
        return (num1 * num2) % nsquare;
    }

    function strToUint(string memory _str)
        public
        pure
        returns (uint256 res, bool err)
    {
        for (uint256 i = 0; i < bytes(_str).length; i++) {
            if (
                (uint8(bytes(_str)[i]) - 48) < 0 ||
                (uint8(bytes(_str)[i]) - 48) > 9
            ) {
                return (0, false);
            }
            res +=
                (uint8(bytes(_str)[i]) - 48) *
                10**(bytes(_str).length - i - 1);
        }

        return (res, true);
    }
}
