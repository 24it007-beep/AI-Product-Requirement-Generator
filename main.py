from business_analyst import analyze_business_idea
from product_manager import create_product_requirements


def clean_output(text):

    if text is None:
        return "No output generated."

    return (
        str(text)
        .replace("**", "")
        .replace("#", "")
        .replace("`", "")
    )


print("AI Product Requirement Generator Started!")

idea = input("Enter your business idea: ")

print("\nAnalyzing business idea...\n")

business_analysis = analyze_business_idea(idea)

print("--- BUSINESS ANALYSIS ---\n")

print(clean_output(business_analysis))


print("\nCreating Product Requirements...\n")

product_requirements = create_product_requirements(business_analysis)

print("--- PRODUCT REQUIREMENTS ---\n")

print(clean_output(product_requirements))