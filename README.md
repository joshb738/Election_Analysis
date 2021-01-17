# Election_Analysis

## Project Overview
Analysis of a local congressional election was performed to provide the Colorado Board of Elections with the following details:

1. A total count of votes cast in the election.
2. A complete list of all candidates that received votes.
3. The percentage of total votes and total number of votes cast from each county in the precinct.
4. The county with the largest voter turnout.
5. The percentage of votes each candidate won as well as the total number of votes each candidate received.
6. The election winner based on popular vote.

## Resources 
- Data Sources: [election_results.csv](resources/election_results.csv)
- Software: Python 3.9.1, Visual Studio Code, 1.52.1

## Election Audit Results
The Analysis of the election show that:

1. A total of **369,711** votes were cast in this election.

2. The following candidates received votes:
   - Charles Casper Stockham
   - Diana DeGette
   - Raymon Anthony Doane

3. The voter turnout for each county were as follows:
   - The county of Jefferson cast **10.5%** of the total vote with **38,855** votes.
   - The county of Denver cast **82.8%** of the total vote with **306,055** votes.
   - The county of Arapahoe cast **6.7%** of the total vote with **24,801** votes.
   
4. Based on the results the county of **Denver** was responsible for the largest voter turnout with **82.8%** of the total vote and **306,055** votes.

5. Candidate Results were as follows:
   - Charles Casper Stockham received **23.0%** of the total vote with **85,213** votes.
   - Diana DeGette received **73.8%** of the total vote with **272,892** votes.
   - Raymon Anthony Doane received **3.1%** of total vote with **11,606** votes.

6. Based on the popular vote, **Diane DeGette** was the winner of the election with **73.8%** of the total vote and **272,892** votes.

## Election Audit summarry
With several minor modifications the Python script for this analysis can be reused to analyze other electoral datasets:
1. Edit line **#8** of the script to ensure the new data source file is being used.
   - file_to_load = os.path.join("resources", "***election_results.csv***")
2. Edit lines **#47 & 50** to match the correct column indexes to the candidates names and countys in the new data source.
   - candidate_name = row[***2***]
   - county_name = row[***1***]
