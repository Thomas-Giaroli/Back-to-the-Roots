# Vous pouvez placer le script de votre jeu dans ce fichier.

# Déclarez sous cette ligne les images, avec l'instruction 'image'
# ex: image eileen heureuse = "eileen_heureuse.png"
image classe = "classe.jpg"
image MentorImg = "mentor.png"
image chapitre3_img = "rueResize (1).jpg"
image scene1 = "route.jpg"
image mentor = "Mentor.png"
image scene2 = "route2.jpg"
image loose_chapter2_back = "loose_chapter_2.jpg"
image chapter6 = "chatper6 (1).jpg"
image representant_img = "representant.png"
image etrangerImg = "etranger.jpg"
image c1 = "1.png"
image c2 = "2.png"
image c3 = "3.png"
image c4 = "4.png"
image c5 = "5.png"
image c6 = "6.png"

define stab = "stab.mp3"

define scenev1 = "zoulette.ogg"
# Déclarez les personnages utilisés dans le jeu.
define e = Character('Eileen', color="#c8ffc8")
define ppi = Character('Théo', color = "#c8ffc8")
define ppa = Character('Alex', color = "#c8ffc8")
define Mentor = Character('Mentor', color="#c8ffc8")
define representant = Character('representant', color="#c8ffc8")
define etranger_mysterieux = Character('Etranger', color="#c8ffc8")
$ choix1 = False
$ choix2 = False
$ choix3 = False
$ choix4 = False
$ choix5 = False
$ choix6 = False 
# Le jeu commence ici
label start:
    scene c1
    with fade
    ""
    show classe
    with fade
    ppi "Encore une journée horrible à l'orphelinat..."
    ppa "Ouais..."
    ppi "*regarde par la fenêtre* Je me sens si seul ici. Je veux savoir d'où je viens et qui je suis."
    ppa "Je me demande toujours pourquoi nos parents nous ont abandonnés. Tu penses qu'on le saura un jour ?"
    menu:
        "Partager ses questionnements à son ami":
            ppi "Je ne le sais pas, et ca me rend fou, nous devrions fuir pour le découvrir."
            ppa "Tu as raison, partons."
            jump chapter2
        "Changer de sujet":
            ppi "Aucune idée, mais ca me met mal à l'aise, parlons d'autre chose."
            ppa "oh, ok..."
            jump lose

    show rue
    with fade

    return

label chapter2:
    scene c2
    with fade
    ""
    scene chapitre3_img
    ppi "Je ne sais pas où je vais. Je suis épuisé et je ne sais pas quoi faire."
    show MentorImg at headright
    Mentor "Tu as besoin d'aide, mon enfant. Je peux te montrer la voie."
    menu:
        ppi "J'aurai vraiment besoin d'aide ..."
        "Refuser l'aide du mentor":
            ppi "Je ne peux pas faire confiance à un étranger. Je vais continuer mon voyage seul."
            Mentor "Comme tu le souhaites..."
            jump loose_chapter2
        "Accepter l'aide du mentor":
            $ choix2 = True
            ppi "Je suis à bout de force et j'ai besoin d'aide. Merci."
            jump chapter3
    
label chapter3:
    scene c3
    with fade
    ""
    scene chapitre3_img
    $ choix3 = False
    
    show MentorImg at headright
    Mentor "Tu dois apprendre à faire confiance en toi et à croire en ta propre force intérieure. Je vais t'enseigner les outils pour le faire."
    #ppi  "Je vais faire de mon mieux pour apprendre."
    menu :
        "Abandonner l'apprentissage":
            ppi "Je ne pense pas être capable de faire ça. Je dois retourner à l'orphelinat."
            jump lose
        "Continuer à apprendre":
            ppi "Je suis déterminé à découvrir mes racines et à comprendre qui je suis. Je vais continuer à apprendre avec vous."
            $ choix3 = True
            jump chapter4
    return

label chapter4:
    scene c4
    with fade
    ""
    scene scene1
    #voice scenev1
    ppi "Je suis enfin libre de partir à la découverte de moi-même et de mon passé. Mais les défis ne vont pas manquer sur ma route."
    ppi "La route va être dur ..."
    show mentor at right
    Mentor "Salut jeune ! Pour pouvoir passer tu devras me donner le nom du meilleur EIP de la promo de 3ème année à Epitech."
    menu:
        "Abandonner et rentrer chez soi" :
            hide mentor
            $ choix4 = False
            ppi "Je suis si déçus ... Je suis fatigué je ne réfléchis pas trop bien actuellement ..."
            jump lose
        "Affronter le défis sans aucune aide" :
            $ choix4 = True
            ppi "Je veux prouver que je suis capable de faire face à tout ce qui se dresse sur ma route. Je vais affronter ces défis seul."
            if renpy.input("Quel est la meilleur équipe ?", length=32) == "GreyStock" :
                Mentor "Parfait ! Tu es digne de passer, tu es digne !"
                scene scene2
                "Après avoir parcouru du chemin vous n'avez rien découvert sur votre passé"
                ppi "la route va être longue ... Comment faire je n'ai pas énormément de provision."
                jump chapter5
            else :
                Mentor "Grosse flèche t'y est pas un bon"
                jump lose
    return

label chapter5:
    scene c5
    with fade
    ""
    scene route
    #show screen minimap()
    #show carrefour
    "Le personnage principal est maintenant un jeune adulte, voyageant dans le monde et en apprenant davantage sur lui-même et son passé."
    "Il rencontre de nouvelles personnes et affronte de nouveaux défis, mais retrouve également certains vieux amis."
    ppi "Je n'arrive pas à croire que ça fait cinq ans que j'ai quitté l'orphelinat. Tellement de choses se sont passées depuis."
    ppi "J'ai appris tellement, vu tellement, et changé tellement. Mais il y a encore des choses que je ne sais pas, et je veux les découvrir."
    menu:
        "Continuer sur la route" :
            #show route
            ppi "Je suis venu jusqu'ici, je ne veux prendre aucun risque inutile. Je vais rester sur la route."
            "Le personnage principal continue sur la route et rencontre finalement un étranger mystérieux."
            show etranger_mysterieux
            etranger_mysterieux "Bonjour jeune homme, tu ressemble fortement à un enfant que je connais, ne serais tu pas Théo par hasard ?"
            ppi "D'ou me conaissez-vous ?"
            etranger_mysterieux "Oh..."
            etranger_mysterieux "Tu es spécial Théo, tu es différent."
            ppi "Qu'est ce que vous voulez dire par cela?"
            etranger_mysterieux "Suis moi, tu mérite amplement de découvrir la vérité.."
            jump chapter6

        "Prendre le détour par la forêt" :
            show foret
            ppi "Je me sens aventureux. Peut-être que le détour me mènera à quelque chose d'important."
            ppi "Oh voila un village !"
            villageois "Bonjour Théo, tu es enfin de retour."
            ppi "Qui êtes vous? Ou-suis je?"
            villageois "Ne t'en fais pas, tu es ici à ta place."
            jump chapter6
    return

label chapter6:
    scene c6
    with fade
    ""
    scene chapter6
    ppi "Je n'arrive pas à croire que je vais finalement découvrir la vérité. C'était un long et difficile voyage, mais cela en valait la peine."
    show representant_img
    representant "Je suis le représentant de l'organisation qui a créé l'expérience qui t'a créé."
    representant "Je t'offre ce choix :"
    representant "Soit tu retourne à l'organisation et tu nous aide à poursuivre notre travail,"
    representant "Soit tu peut partir et commencer une nouvelle vie. Libre..."
    menu:
        "Retourner à l'organisation":
            ppi "Je veux aider à faire une différence. Je retournerai à l'organisation et utiliserai mes connaissances et mes capacités pour le bien commun."
            jump join_orga
        "Commencer une nouvelle vie en solo":
            ppi "J'ai assez appris. Je veux juste commencer une nouvelle vie et tout laisser derrière moi."
            jump solo_end
    return

label join_orga:
    scene black
    "Théo retourna à l'organisation et commenca à travailler pour améliorer la vie des autres."
    "Il devient un leader de sa communauté et travailla pour que d'autres aient les mêmes opportunités que lui."
    "Il finit sa vie. Heureux de ce qu'il avait accompli."
    return

label solo_end:
    scene black
    "Théo quitta l'organisation et décida de commencer une nouvelle vie, comme il l'entendait."
    "Il trouva un endroit où il pouvais être lui-même et vivre une vie libre du contrôle des autres."
    "Il continue de grandir et de mûrir, et devient finalement un mentor pour d'autres personnes comme lui, les aidant à trouver leur propre chemin dans la vie."
    return

label lose:
    scene loose_chapter2_back
    "Le jeune orphelin, épuisé et affamé, s'effondra au pied d'un grand arbre."
    "Il avait parcouru de nombreux kilomètres dans l'espoir de retrouver ses parents, mais malheureusement, il n'avait trouvé aucune trace d'eux."
    "La faim qui le taraudait depuis plusieurs jours avait finalement eu raison de lui et il s'éteignit tragiquement, sans avoir trouvé ce qu'il cherchait le plus au monde."
    "L'arbre veilla sur lui en silence, témoin muet de sa quête infructueuse."
    "Une voix appelle Théo une dernière fois."
    ppa "Non Théo !"
    ppa "Ne meurs pas je t'en prie !"
    ppa "Théooooooo !"
    "En vain."
    return