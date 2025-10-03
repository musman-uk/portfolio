# 💾 Portfolio Backup Strategy

---

## 📑 Overview
This process captures the design and implementation of a backup strategy for my portfolio repository. The original setup relied solely on the public GitHub repository, which meant there was no redundancy if something went wrong. While functional, it left the portfolio vulnerable to data loss, outages, or accidental deletion.  

The backup strategy introduces a private GitHub mirror and a OneDrive synced local copy. Together, these layers create a system that is more resilient, secure, and clear. The portfolio is no longer just a single point of truth but a distributed, multi layered workflow that reflects principles of reliability and maintainability.

---

## 📌 Purpose
The backup strategy was guided by a set of clear aims:  

- **Redundancy**: to ensure the portfolio is always recoverable from multiple independent sources.  
- **Security**: to avoid over exposed tokens and reduce risks in automation.  
- **Resilience**: to protect against GitHub outages, accidental deletions, or sync errors.  
- **Transparency of process**: to document the backup workflow itself as part of the portfolio, showing that reliability is a deliberate design choice.  

---

## 📝 Approach
- Implemented automation using GitHub Actions to mirror the public repository into a private backup repository.  
- Encountered blockers with push based mirroring and switched to a pull based model where the private repository pulls from the public source.  
- Created a local clone inside the OneDrive synced folder and refreshed it with `git pull` using the Git CLI, which then synced automatically to the cloud.  
- Explored automation options such as Task Scheduler and Power Automate but kept manual pulls for visibility and control.  
- Documented the blockers and trade offs to ensure clarity for future improvements.  

---

## 🎯 Rationale
- A pull based mirror simplified authentication and reduced token scope risks compared to pushing into the private repository.  
- OneDrive integration added a non GitHub cloud layer, diversifying backup locations.  
- Layered redundancy ensures no single point of failure.  
- Manual first, automate later balances control with scalability, leaving room for future automation.  

---

## 🚧 Blockers

The blockers below highlight the main challenges faced during implementation. Supporting screenshots are at the bottom of this section for visual reference.

- **Push to Private Repository Unsuccesful**  
  Attempted push based mirroring did not succeed due to token scope and permission issues. The resolution was to invert the flow so the private repository pulls from the public source instead.  

- **OneDrive Limitations**  
  OneDrive cannot directly integrate with GitHub. It requires manual or scheduled `git pull` to refresh the local clone.  

- **Automation Trade offs**  
  Task Scheduler requires the laptop to be on, while Power Automate produces zip snapshots rather than full Git clones with history.  

- **Accidental Files**   
  Stray files such as `-l` created during testing required manual cleanup.

- **Additional Security Concerns**          
  Backups could be exposed to exploitation or attacks if left unprotected, hence caution was applied and they are now secured with device PIN, strong passwords, and private repositiory visibility to prevent unauthorized access.

For Visual references to blockers encountered, please view screenshots in the outcome section.

---

## 🏁 Outcome

The portfolio backup strategy transformed from a single‑point setup into a layered, resilient system. The tree structure below illustrates the change, whilst the screenshots visually reference blockers encountered.

<details>
<summary><strong>🌳 View Tree Structures</strong></summary>

<pre>
📂 portfolio (before)
└── 📄 Public GitHub Repostiory (main)
</pre>

<pre>
📂 portfolio (after)
├── 📄 Public GitHub Repository (main)
├── 🔒 Private GitHub Backup Repository (automated pull from public)
├── 💻 Local Folder In Laptop That Syncs to OneDrive Cloud
└── ☁️ OneDrive Cloud Copy (local clone synced to OneDrive cloud)
</pre>

</details>

<details>
<summary><strong>📸 View Screenshots</strong></summary>

- ![Token Setup – Deleted Token, Name Only](https://github.com/musman-uk/portfolio/blob/main/workflow-process/portfolio-backup-strategy/Portfolio%20Backup%20%20Tokens.png)  
  *Example of the token created for testing (now deleted, no secret visible).*

- ![Push Failure – Authentication Error](https://github.com/musman-uk/portfolio/blob/main/workflow-process/portfolio-backup-strategy/Portfolio%20Backup%20Blocker.png)  
  *Authentication failure encountered when attempting to push directly into the private repository.*

- ![Debugging Push Issue](https://github.com/musman-uk/portfolio/blob/main/workflow-process/portfolio-backup-strategy/Portfolio%20Backup%20Debug.png)  
  *Debug output isolating the failure to the push step, confirming the issue was authentication related.*

- ![Push Success](https://github.com/musman-uk/portfolio/blob/main/workflow-process/portfolio-backup-strategy/Portfolio%20Backup%20Strategy%20-%20Success.png)  
  *Successful push confirming the backup workflow was functioning correctly after adjustments.*

</details>


---

## 💭 Reflections
Designing and implementing the backup strategy was as much about mindset as it was about technical execution. At first I assumed that pushing directly into the private backup repository would be the most straightforward solution, but the authentication failures and token scope issues quickly revealed the hidden complexity of that approach. This prompted me to step back and reconsider the problem, and in doing so I discovered that a pull based model was not only simpler but also more secure. That shift in perspective was a reminder that the obvious path is not always the most sustainable one, and that resilience often comes from reframing the problem rather than forcing a brittle solution.  

The addition of a OneDrive synced local clone introduced another layer of learning. While it may seem redundant at first glance, it provided a valuable safeguard outside of GitHub, diversifying the backup strategy and reducing reliance on a single platform. The manual git pull step, although less elegant than full automation, gave me a sense of visibility and control that was reassuring during the early stages. It also highlighted the trade off between convenience and oversight. Automation can save time, but it can also obscure what is happening under the hood.  

Each blocker along the way, from failed pushes to stray files, became an opportunity to deepen my understanding of GitHub Actions, authentication scopes, and workflow maintainability. Instead of treating these as setbacks, I began to see them as checkpoints that tested the robustness of the system. The final outcome is not just a backup strategy but a reflection of the principles I want my work to embody: adaptability, security, clarity, and transparency. Looking ahead, I see room to refine the process further, particularly by automating the OneDrive sync in a way that preserves the integrity of the Git history. Even in its current form, the system provides peace of mind and demonstrates that reliability is not an afterthought. It is something that must be designed, tested, and documented with the same care as the portfolio itself.
