**CONTRIBUTING.md**

# Contributing to Monthly Missions

First of all, thank you for taking part in the SuperDataScience Monthly Mission. Every month, we provide open challenges so participants can practice their Data Science / Machine Learning / AI skills and build up their project portfolio. This document will guide you through the process of contributing. Please read it before submitting your work.

---

## How Can I Contribute?

### **What is the format for submission?**

In this repository, we use two distinct folders for submissions, depending on whether you’re an SDS community member or an external contributor:

- `submissions/sds-members` – for participants who are **part of the SuperDataScience (SDS) community**.  
- `submissions/external-contributions` – for **all other contributors** outside the SDS community.

Within each folder, you’ll find an example of the folder and file naming structure. For instance, in the `submissions/sds-members` folder, you’ll see a subfolder named `shaheer-airaj`, containing `shaheer_mission_name.ipynb`. This notebook demonstrates the format and includes some helpful markdown information.

Feel free to **copy that notebook** into your own subfolder (named after your first and last name, or your GitHub username) and fill out its markdown sections. You can then build your entire submission within that single notebook.

**Tip**: We encourage contributors to keep all work in one well-organized notebook, with clear comments and markdown sections. This makes it easier for reviewers to follow your reasoning and code.

### **Where do I place my submissions?**

1. **SDS Members**: If you’re part of the SDS community, create a folder inside `submissions/sds-members` using your full name (as displayed on SDS) or your GitHub username. Put all your submissions in this folder.

   Example:
   ```
   submissions
   └── sds-members
       └── shaheer-airaj
           └── shaheer_mission_name.ipynb
   ```

2. **External Participants**: If you’re not an SDS member, please place your submissions under `submissions/external-contributions` in a folder named after your full name or preferred identifier.

   Example:
   ```
   submissions
   └── external-contributions
       └── jane-doe
           └── jane_data_insights.ipynb
   ```

Make sure to follow this folder and file-naming structure—or your submissions may not be considered.

---

## Submitting Pull Requests (PRs)

To submit your solution for the Monthly Mission, follow this workflow:

### Step-by-Step Guide:

1. **Fork the Repository**  
   - Click the “Fork” button at the top of the repository page to create a copy in your GitHub account.

2. **Clone Your Fork**  
   - Clone your fork locally to work on it:
     ```bash
     git clone https://github.com/your-username/repository-name.git
     ```
   - Replace `your-username` and `repository-name` with your actual GitHub username and the name of the forked repository.

3. **Create a Python Virtual Environment**  
   - Navigate into your newly cloned repository:
     ```bash
     cd repository-name
     ```
   - Create a virtual environment (using Python’s built-in `venv`, for example):
     ```bash
     python3 -m venv venv
     ```
   - Activate the virtual environment:
     - **macOS/Linux**:
       ```bash
       source venv/bin/activate
       ```
     - **Windows**:
       ```bash
       venv\Scripts\activate
       ```

4. **Install Dependencies**  
   - You can install the project’s dependencies with:
     ```bash
     pip install -r requirements.txt
     ```

5. **Make Your Changes**  
   - Add your submission in the correct folder (`submissions/sds-members` or `submissions/external-contributions`), and ensure your folder/file naming matches the conventions provided.
   - If you’re writing code, ensure it’s clear, well-documented, and follows any relevant coding standards or style guidelines for this project.

6. **Test Your Changes**  
   - If there are any tests or recommended checks, run them to confirm everything works as expected.

7. **Commit Your Changes**  
   - Write a clear commit message describing what you’ve done:
     ```bash
     git commit -m "Add new mission submission for Jane Doe"
     ```

8. **Push to Your Fork**  
   - Push your changes to the branch on your forked repository:
     ```bash
     git push origin main
     ```

9. **Open a Pull Request**  
   - Go to the original repository (i.e., the SuperDataScience Monthly Mission repo).
   - Open a Pull Request from your branch.
   - Provide a clear description of what the PR does:
     - Reference any relevant issues or previous discussions, if applicable.
     - Explain your solution approach and any design decisions.

### PR Review Process

- A maintainer will review your submission. Please be patient as reviews can sometimes take a bit of time.
- If changes or updates are requested, make the necessary modifications, commit them to the same branch, and push again. Your PR will automatically update.
- Once your submission is approved, it will be merged and become part of the project!

---

## Need Help?

If you have any questions or need assistance:
- Open an issue in the Issues tab.
- Reach out to me using my email shaheer@superdatascience.com.
- Reach out to the maintainers directly on the SDS platform.

We appreciate your contribution and look forward to seeing your solutions!