import random

def assign_best_faculty(complaint_text: str, all_faculties: list) -> str:
    """
    Mock AI Agent that analyzes the complaint text and assigns it to the best faculty 
    based on experience / keywords mapping.
    """
    text = complaint_text.lower()
    
    # Simple keyword mappings mapping to standard faculty groups
    expertise_map = {
        "Plumbing & Water": ["water", "leak", "plumbing", "pipe", "drinking", "washroom", "toilet", "tap"],
        "Electrical": ["electric", "power", "light", "fan", "ac", "wiring", "short circuit", "electricity"],
        "IT Support": ["wifi", "internet", "computer", "projector", "network", "login", "portal"],
        "Campus Maintenance": ["cleaning", "garbage", "dust", "road", "building", "furniture", "bench", "desk"],
        "Academic & Examination": ["exam", "results", "marks", "grade", "faculty", "attendance", "syllabus", "lectures"],
        "Hostel & Accommodation": ["hostel", "room", "mess", "food", "warden", "bed", "canteen"],
        "Security & Discipline": ["ragging", "fight", "security", "guard", "id card", "parking", "theft", "stolen"]
    }
    
    # Add actual existing faculties from DB if not in our predefined keys
    faculty_names = [f["name"] for f in all_faculties] if all_faculties else []
    
    # We will score each faculty
    scores = {f: 0 for f in faculty_names}
    for category in expertise_map:
        if category not in scores:
            scores[category] = 0
            
    for category, keywords in expertise_map.items():
        for kw in keywords:
            if kw in text:
                scores[category] += 1
                
    # Also score simple text matching for actual DB faculty names
    for f in faculty_names:
        if f.lower() in text:
            scores[f] += 2
            
    best_match = max(scores, key=scores.get)
    
    if scores[best_match] == 0:
        # Fallback to the first available faculty or a generic one
        return "General Administration"
        
    return best_match
    
