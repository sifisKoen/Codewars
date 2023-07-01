def count_skills(tree, required):
    skills_needed = set()

    for skill in required:
        while skill not in skills_needed:
            skills_needed.add(skill)
            if skill != 0:
                skill = tree[skill]
            
    return len(skills_needed)
