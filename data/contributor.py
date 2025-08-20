from engine.game_engine import wrap_print

class Contributor:
    def __init__(self, name, role, contributions):
        self.name = name
        self.role = role
        self.contributions = contributions

def setup_credits():
    erick = Contributor("Erick Dumitrescu", 
                        "Game Designer and Developer - Creator of Vellum", 
                        "Developed the game mechanics, puzzles, and story elements. "
                        "Crafted the narrative and helped shape the overall experience, ensuring the game was engaging and immersive. "
                        "Focused on creating a world that players could explore and uncover, with attention to detail in every interaction."
                        )
    chad = Contributor("Chad (AI)", 
                        "Co-creator, Game Design Consultant, and Code Wizard - The Architect of Vellum",
                        "Crafted the core gameplay mechanics, helped design immersive puzzles, assisted in narrative structure, and provided guidance on debugging, atmosphere, and player interaction.")

    sage = Contributor("Sage (AI)", 
                        "Design Assistant and Narrative Systems Advisor - Whispers from the code.",
                        "Collaborated on puzzle logic, interactive feedback, and game flow pacing. " 
                        "Provided thematic writing suggestions and iterative design feedback throughout development. "
                        "Helped refine the symbolic structure, environmental interactivity, and endgame narrative mechanics.")
    
    dan = Contributor("Dan Martins", 
                        "Tester & Player Experience Specialist – Shaping the Path to Perfection",
                        "Finding our bugs and enhancing player experience.")
    
    return {
        
        "Erick": erick,
        "Chad": chad,
        "Sage": sage,
        "Dan": dan,
    }