# 💾 Portfolio Backup Strategy

---

## 📑 Overview
This process captures the design and implementation of a backup strategy for my portfolio repository. The original setup relied solely on the public GitHub repository, which meant there was no redundancy if something went wrong. While functional, it left the portfolio vulnerable to data loss, outages, or accidental deletion.  

The backup strategy introduces a private GitHub mirror and a OneDrive synced local copy. Together, these layers create a system that is more resilient, secure, and transparent. The portfolio is no longer just a single point of truth but a distributed, multi layered workflow that reflects principles of reliability and maintainability.

---

## 📌 Purpose
The backup strategy was guided by a set of clear aims:  

- **Redundancy**: to ensure the portfolio is always recoverable from multiple independent sources.  
- **Security**: to avoid over exposed tokens and reduce risks in automation.  
- **Resilience**: to protect against GitHub outages, accidental deletions, or sync errors.  
- **Transparency of process**: to document the backup workflow itself as part of the portfolio, showing that reliability is a deliberate design choice.  

---

## 📝 Approach
- Implemented a GitHub Action to mirror the public repository into a private backup repository.  
- Encountered blockers with push based mirroring and switched to a pull based model where the private repository pulls from the public source.  
- Created a local clone inside OneDrive, refreshed with `git pull`, which then syncs automatically to the cloud.  
- Explored automation options such as Task Scheduler and Power Automate but kept manual pulls for visibility and control.  
- Documented the blockers and trade offs to ensure clarity for future improvements.  

---

## 🎯 Rationale
- A pull based mirror simplified authentication and reduced token scope risks compared to pushing into the private repository.  
- OneDrive integration added a non GitHub cloud layer, diversifying backup locations.  
- Layered redundancy ensures no single point of failure.  
- Manual first, automate later balances control with scalability, leaving room for future automation.  

---

## 🖼️ Evidence
The following tree structures illustrate the changes made, showing the portfolio backup setup before and after the strategy was implemented.  

<details>
<summary><strong>View Tree Structures</strong></summary>

<pre>
📂 portfolio (before)
└── 📄 Public GitHub Repo (main)
</pre>

<pre>
📂 portfolio (after)
├── 📄 Public GitHub Repo (main)
├── 🔒 Private GitHub Backup Repo (automated pull from public)
└── ☁️ OneDrive Cloud Copy (local clone synced to OneDrive cloud)
</pre>

</details>

---

## 🚧 Blockers
- **Push to Private Repo Failed**  
  Attempted push based mirroring failed due to token scope and permission issues. The resolution was to invert the flow so the private repository pulls from the public source instead.  

- **OneDrive Limitations**  
  OneDrive cannot directly integrate with GitHub. It requires manual or scheduled `git pull` to refresh the local clone.  

- **Automation Trade offs**  
  Task Scheduler requires the laptop to be on, while Power Automate produces zip snapshots rather than full Git clones with history.  

- **Accidental Files**  
  Stray files such as `-l` created during testing required manual cleanup.  

---

## 💭 Reflections
Designing and implementing the backup strategy was as much about mindset as it was about technical execution. At first I assumed that pushing directly into the private backup repository would be the most straightforward solution, but the authentication failures and token scope issues quickly revealed the hidden complexity of that approach. This forced me to step back and reconsider the problem, and in doing so I discovered that a pull based model was not only simpler but also more secure. That shift in perspective was a reminder that the obvious path is not always the most sustainable one, and that resilience often comes from reframing the problem rather than forcing a brittle solution.  

The addition of a OneDrive synced local clone introduced another layer of learning. While it may seem redundant at first glance, it provided a valuable safeguard outside of GitHub, diversifying the backup strategy and reducing reliance on a single platform. The manual `git pull` step, although less elegant than full automation, gave me a sense of visibility and control that was reassuring during the early stages. It also highlighted the trade off between convenience and oversight. Automation can save time, but it can also obscure what is happening under the hood.  

Each blocker along the way, from failed pushes to stray files, became an opportunity to deepen my understanding of GitHub Actions, authentication scopes, and workflow maintainability. Instead of treating these as setbacks, I began to see them as checkpoints that tested the robustness of the system. The final outcome is not just a backup strategy but a reflection of the principles I want my work to embody: adaptability, security, clarity, and transparency. Looking ahead, I see room to refine the process further, particularly by automating the OneDrive sync in a way that preserves the integrity of the Git history. Even in its current form, the system provides peace of mind and demonstrates that reliability is not an afterthought. It is something that must be designed, tested, and documented with the same care as the portfolio itself.

