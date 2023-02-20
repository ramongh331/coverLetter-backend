# Cover Letter Writer

## Purpose
This API will store the information needed to add into the cover letter. 

## Technologies To Be Used
- Python
- Django
- To Be Deployed on Render.com

## Model
<img src="https://i.imgur.com/avYFwVU.png" alt="Cover Letter Writer ERD"/>

### Schema
- Your Name (name)
- Job Position (position)
- Date (date)
- Name of Company (company)
- Number of years of experience (yoe)
- Skill(s) (skill)
- Expertise (expertise)
- Relevant passion (passion)
- Company's products/services (products)


## The Route Table
| Endpoint | Method | Description|
|----------|--------|------------|
| /coverletters | GET | returns all cover letters |
| /coverletters/:id | GET | returns a single cover letter |
| /coverletters | POST | creates a cover letter |
| /coverletters/:id | PUT | updates a cover letter based on id |
| /coverletters/:id | DELETE | deletes a cover letter based on id |



## Live API
[Live Site](https://coverletter-backend.onrender.com/coverletters/)

## Cover Letter Template

Dear [Hiring Manager],

I am writing to express my interest in the [Position] role at [Company]. As an experienced [your profession or job title], I am excited to apply my [relevant skills or experience] to make a valuable contribution to your team.

In my [Number of Years] years of experience, I have honed my skills in [relevant skills or technologies] and worked on a variety of projects that have enabled me to develop [relevant expertise]. I have also collaborated with cross-functional teams and stakeholders to deliver projects on time and within budget.

Additionally, I have a passion for [relevant field or industry] and am committed to staying up-to-date with the latest developments and trends. I am confident that my skills in [relevant skills or experience] and passion for [relevant field or industry] make me an ideal candidate for the [Position] role at [Company].

I am excited about the opportunity to join a dynamic and innovative company like [Company] and to be a part of a team that is committed to delivering high-quality [relevant products or services]. I am confident that my skills, experience, and passion will enable me to make a valuable contribution to your team and to help drive the success of your business.

Thank you for considering my application. I look forward to the opportunity to discuss my qualifications further and to learn more about the [Position] role at [Company].

Sincerely,
[Your Name]