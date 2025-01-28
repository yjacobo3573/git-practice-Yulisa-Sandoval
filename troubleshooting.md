# Reflection: Assignment Challenges and Solutions

While working on this assignment, I encountered a few challenges that required some troubleshooting and problem-solving:

## Issue with Visual Studio IDE
- The main problem was that Visual Studio automatically added configuration files to my project window. These files were not meant to be tracked by Git.
- When I attempted to push my changes to GitHub, I encountered the following error:  
  **"Read access violation."**

## Solution
To resolve this, I had to:
1. Configure Git to ignore these files by updating the `.gitignore` file.
2. Remove the already tracked files from the repository using the command line.

## Takeaway
Although this process was a bit tricky, especially since I had to use the command line to manually fix the issue, it was a valuable learning experience.  
I now understand more about:
- How Git works.
- Managing IDE-generated files in a repository.

## Reverting commits
I decided to revert a commit where I added some formating to my readme because I didn't like how it looked. It was really easy to do.
