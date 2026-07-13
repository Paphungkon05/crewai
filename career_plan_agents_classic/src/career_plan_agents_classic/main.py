from career_plan_agents_classic.crew import CareerPlanAgentsClassic


def run():
    inputs = {
        "learner_profile": (
            "A Computer Science student with basic skills in Python, HTML, "
            "JavaScript, and databases. Interested in becoming a Software Developer, "
            "but needs improvement in real-world project experience, teamwork, "
            "Git/GitHub, and system design."
        ),
        "target_career": "Software Developer",
        "self_assessment": (
            "Python 3/5, HTML 3/5, JavaScript 2/5, Database 2/5, "
            "Git/GitHub 1/5, Web Development 2/5, Software Engineering 2/5, "
            "System Design 1/5, Problem Solving 3/5, Teamwork 3/5, Communication 3/5."
        ),
        "required_qualifications": (
            "Programming in Python or JavaScript, database knowledge, Git/GitHub, "
            "web application development, SDLC understanding, problem-solving, "
            "basic system design, teamwork, communication, and real-world project "
            "development skills."
        ),
    }

    result = CareerPlanAgentsClassic().crew().kickoff(inputs=inputs)
    print(result)


if __name__ == "__main__":
    run()
