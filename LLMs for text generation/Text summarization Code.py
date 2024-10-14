import pandas as pd
import random
from transformers import T5ForConditionalGeneration, T5Tokenizer

# Load the data
file_path = r"C:\Users\saksh\OneDrive\Desktop\LLMs for text generation\Responces.csv"
data = pd.read_csv(file_path)

# Initialize T5 model and tokenizer
model_name = "t5-small"
t5_tokenizer = T5Tokenizer.from_pretrained(model_name)
t5_model = T5ForConditionalGeneration.from_pretrained(model_name)


# Function to generate a review using T5
def generate_t5_review(row):
    project_type = row['What type of elevator project did Horizon Elevators complete for you?']
    responsiveness = row[' How responsive has Horizon Elevators been to your inquiries or concerns?']
    communication = row[' How well did Horizon Elevators keep you informed throughout the process (sales, installation, etc.)?']
    pricing = row['Compared to other elevator companies; did Horizon Elevators offer competitive pricing?']
    amc_satisfaction = row['How satisfied are you with the Annual Maintenance Contract (AMC) service provided by Horizon Elevators?']
    installation_professionalism = row[' How professional and efficient was the installation process conducted by Horizon Elevators?']
    overall_satisfaction = row["How satisfied are you with the overall quality, reliability, and safety of Horizon Elevators' installations (if applicable) or maintenance services?"]
    recommendation = row['Would you recommend Horizon Elevators to others looking for elevator installation or maintenance services?']


    question_1 = [
        (""),
        (f"I had a {project_type} with Horizon Elevators completed on Monday."),
        (f"My experience with Horizon Elevators was for a {project_type} project completed on Tuesday. "),
        (f"Had a {project_type} completed by Horizon Elevators on Wednesday."),
        (f"The {project_type} project completed by Horizon Elevators on Thursday."),
        (f"On Friday we have completed a {project_type} with Horizon Elevators."),
        (f"Horizon Elevators completed a {project_type} for me on Saturday."),]
    # Choose a random template
    q1temp = random.choice(question_1)

    question_2 = [
        (""),
        (f"They were {responsiveness} to my inquiries and concerns."),
        (f"They showed {responsiveness} to my concerns and inquiries. "),
        (f"It was a {responsiveness} experience regarding my inquiries and concerns. "),
        (f"They were {responsiveness} responsiveness to my inquiries and concerns. "),
        (f"Their {responsiveness} nature in handling my inquiries and concerns stood out. "),
        (f"Their responsiveness to my concerns was {responsiveness}")]
    # Choose a random template

    q2temp = random.choice(question_2)

    question_3 = [
        (""),
        (f"Throughout the process, I was {communication}."),
        (f"From start to finish, their communication was {communication}."),
        (f"Throughout, they kept me {communication}. "),
        (f"Throughout the process, their communication was {communication}, "),
        (f"During the entire process, I found their communication to be {communication}. "),
        (f"and they kept me {communication} throughout the entire process. "),]
    # Choose a random template
    q3temp = random.choice(question_3)


    question_4 = [
        (""),
        (f"Their pricing was {pricing}. "),
        (f"Their pricing strategy was {pricing}, "),
        (f"In terms of pricing, they were {pricing}. "),
        (f"Pricing-wise, they were {pricing}. "),
        (f"and their pricing was {pricing}. "),
        (f"I found their pricing to be {pricing}. "),]
    # Choose a random template
    q4temp = random.choice(question_4)


    question_5 = [
        (""),
        (f"I am {amc_satisfaction} with the Annual Maintenance Contract (AMC) service. "),
        (f"and I am {amc_satisfaction} with their AMC service. "),
        (f"The AMC service left me feeling {amc_satisfaction}. "),
        (f"The AMC service has been {amc_satisfaction}. "),
        (f"I am {amc_satisfaction} with their Annual Maintenance Contract service. "),
        (f"Their AMC service left me {amc_satisfaction}. "),]
    # Choose a random template
    q5temp = random.choice(question_5)


    question_6 = [
        (""),
        (f"The installation was {installation_professionalism}."),
        (f"The installation process was {installation_professionalism}. "),
        (f"The professionalism during installation was {installation_professionalism}. "),
        (f"Their installation process was {installation_professionalism}. "),
        (f"The installation was {installation_professionalism}."),
        (f" The installation process was {installation_professionalism}."),]
    # Choose a random template
    q6temp = random.choice(question_6)


    question_7 = [
        (""),
        (f" I am {overall_satisfaction} with the quality, reliability, and safety of their installations."),
        (f"I am {overall_satisfaction} with their service quality, reliability, and safety standards. "),
        (f"All in all, I'm {overall_satisfaction} with the quality, reliability, and safety of their work."),
        (f"The {project_type} project completed by Horizon Elevators on Thursday."),
        (f" I am {overall_satisfaction} with the quality, reliability, and safety of their installations."),
        (f"I am {overall_satisfaction} with the quality, reliability, and safety of their service."),]
    # Choose a random template
    q7temp = random.choice(question_7)


    question_8 = [
        (""),
        (f"I would {recommendation} Horizon Elevators to others."),
        (f"I would {recommendation} Horizon Elevators to others. "),
        (f"I would {recommendation} Horizon Elevators."),
        (f"I would {recommendation} them to others."),
        (f"I would {recommendation} Horizon Elevators to others."),
        (f"I would {recommendation} Horizon Elevators to anyone in need of elevator services."),]
    # Choose a random template
    q8temp = random.choice(question_8)


    review_template = f"{q1temp}{q2temp}{q3temp}{q4temp}{q5temp}" #{q6temp}{q7temp}{q8temp}


    return review_template

print(data.apply(generate_t5_review, axis=1)[0])
# Generate Google reviews
data['Google Review'] = data.apply(generate_t5_review, axis=1)

# Save the generated reviews to a new CSV file
output_file_path = r"C:\Users\saksh\OneDrive\Desktop\LLMs for text generation\Generated responces form.csv"
data.to_csv(output_file_path, index=False)
print(f"Generated Google reviews saved to {output_file_path}")