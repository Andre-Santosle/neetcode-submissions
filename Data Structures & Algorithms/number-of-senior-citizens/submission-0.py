class Solution:
    def countSeniors(self, details: List[str]) -> int:
        nbr_of_seniors = 0

        for ssn in details:
            age = ssn[-4:-2]
            if int(age) > 60:
                nbr_of_seniors += 1


        return nbr_of_seniors

