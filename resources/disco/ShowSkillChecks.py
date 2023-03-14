import json
import csv
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

'''
Difficulty checks are coded in the following format:

[3]
0 Field data
 1 string title = "DifficultyPass"
 1 string value = "2"
 0 int type = 1
 1 string typeString = "CustomFieldType_Number"
[4]
0 Field data
 1 string title = "Actor"
 1 string value = "386"
 0 int type = 5
 1 string typeString = "CustomFieldType_Actor"
[5]

The value under the "DifficultyPass" sets the difficulty of the check
The value below "Actor" sets the skill which is checked, in this case "Suggestion" (see ACTOR_DICT)

'''

#mapping of actor codes to in-game skills, note that there are 5 different perception checks!
#('normal', smell, hearing, taste, sight)
ACTOR_DICT = {
    389: 'Conceptualization',
    390: 'Logic',
    391: 'Encyclopedia',
    392: 'Rhetoric',
    393: 'Drama',
    394: 'Visual Calculus',
    395: 'Empathy',
    396: 'Inland Empire',
    397: 'Volition',
    398: 'Authority',
    399: 'Suggestion',
    400: 'Esprit de Corps',
    401: 'Endurance',
    402: 'Physical Instrument',
    403: 'Shivers',
    404: 'Pain Threshold',
    405: 'Electro-Chemistry',
    406: 'Half Light',
    407: 'Hand-Eye Coordination',
    408: 'Reaction Speed',
    409: 'Savoir Faire',
    410: 'Interfacing',
    411: 'Composure',
    412: 'Perception',
    413: 'Perception',
    414: 'Perception',
    415: 'Perception',
    416: 'Perception',
}

#map of DifficultyPass values to in-game difficulty
DIFF_MAP = {
    0: 6,
    1: 8,
    2: 10,
    3: 12,
    4: 14,
    5: 16,
    6: 18,
    7: 20,
    8: 7,
    9: 9,
    10: 11,
    11: 13,
    12: 15,
    13: 17,
    14: 19
}

#in-game skill order
DISPLAY_ORDER = [
'Logic',
'Encyclopedia',
'Rhetoric',
'Drama',
'Conceptualization',
'Visual Calculus',
'Volition',
'Inland Empire',
'Empathy',
'Authority',
'Esprit de Corps',
'Suggestion',
'Endurance',
'Pain Threshold',
'Physical Instrument',
'Electro-Chemistry',
'Shivers',
'Half Light',
'Hand-Eye Coordination',
'Perception',
'Reaction Speed',
'Savoir Faire',
'Interfacing',
'Composure'
]

#highest check value is 14
HIGH_CHECK = 15

#-------------------------------------------#
#    extract check counts from game code    #
#-------------------------------------------#

#check count arrays
passive_checks = {k: [0] * HIGH_CHECK for k in ACTOR_DICT.values()}
antipassive_checks = {k: [0] * HIGH_CHECK for k in ACTOR_DICT.values()}


# Open and read in dialogue JSON data (I extracted it using AssetStudio by Perfare)
with open("Disco Elysium.json", encoding="utf-8") as disco_data_json:
    disco_data = json.load(disco_data_json)

# Go through each conversation.
for conversation in disco_data["conversations"]:
    # Go through each piece of dialogue within a conversation.
    for dialogue in conversation["dialogueEntries"]:
    
        # Construct a dictionary of this dialogue block with the dialogue's speaker
        # and, if it has them, difficulty and antipassiveness.
        # (We do this as dialogue entries are weirdly formatted and difficult to
        # manipulate otherwise).
        dialogue_field_dict = {}
        dialogue_field_dict["Antipassive"] = False
        for dialogue_field in dialogue["fields"]:
            if dialogue_field["title"] == "Antipassive":
                dialogue_field_dict["Antipassive"] = True
            elif dialogue_field["title"] == "Actor":
                dialogue_field_dict["Actor"] = int(dialogue_field["value"])
            elif dialogue_field["title"] == "DifficultyPass":
                dialogue_field_dict["DifficultyPass"] = int(dialogue_field["value"])
        
        # If this dialogue block is a skill check, add it to the count(s).
        if "DifficultyPass" in dialogue_field_dict:
            if dialogue_field_dict["Antipassive"]:
                antipassive_checks[ACTOR_DICT[dialogue_field_dict["Actor"]]][dialogue_field_dict["DifficultyPass"]] += 1
            else:
                passive_checks[ACTOR_DICT[dialogue_field_dict["Actor"]]][dialogue_field_dict["DifficultyPass"]] += 1

#--------------------#
#Write result tables #
#--------------------#

# Write a table of tallied difficulty checks for both passives and antipassives for each skill.
for tup in [('Passive Checks', passive_checks), ('Antipassive Checks', antipassive_checks)]:
    # The table will have the skill's name and sum of checks as first two columns.
    header = ["Skill", "Total"] + list(range(HIGH_CHECK))
    data = []
    title = tup[0]
    checks = tup[1]
    
    for skill in DISPLAY_ORDER:
        # The +2 is for the skill name and sum of checks.
        skill_checks = [0] * (HIGH_CHECK + 2)
        skill_checks[0] = skill
        skill_checks[1] = sum(checks[skill])
        
        for i, value in enumerate(checks[skill]):
            skill_checks[DIFF_MAP[i] - 6 + 2] = value
        
        data.append(skill_checks)
    
    # Write to file.
    with open(title + ".csv", 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(data)
        
#--------------------#
#    Plot results    #
#--------------------#

#skill grid dimensions
X = 6
Y = 4

#chart colours
ROW_COLOURS = ['skyblue', 'orchid', 'indianred', 'gold']
BG_COLOUR = 'black'
SPINE_COLOUR = 'white'

for tup in [('Passive Checks', passive_checks), ('Antipassive Checks', antipassive_checks)]:
    #unpack tuple
    title = tup[0]
    checks = tup[1]

    #setup all Y*X subplopts
    fig, ax = plt.subplots(nrows=Y, ncols=X, sharex=True)
    ax[0,0].set_xticks(list(range(6,20+1,2)))

    #set figure title, size and, background colour
    fig.suptitle(title, color=SPINE_COLOUR, fontsize=22)
    fig.set_size_inches(24, 13.5)
    fig.set_facecolor('black')

    #go through all skills
    for y in range(0,Y):
        for x in range(0, X):
            #skill being drawn
            skill = DISPLAY_ORDER[x + X*y]

            #calculate total number of skill checks and find highest skill check
            count = sum(checks[skill])
            max_skill = max(map(lambda dc: DIFF_MAP[dc], [ j for (i,j) in zip(checks[skill], range(15)) if i > 0 ]), default=0)
            
            #style chart
            col = ROW_COLOURS[y]
            ax[y, x].set_title(DISPLAY_ORDER[X*y+x], color=col)
            ax[y, x].set_facecolor(BG_COLOUR)
            for spine in ax[y,x].spines.values():
                spine.set_color(SPINE_COLOUR)            
            ax[y, x].tick_params(colors=SPINE_COLOUR)
            #allow max of 5 y ticks and only use integer values
            ax[y, x].yaxis.set_major_locator(ticker.MaxNLocator(nbins=5, integer=True))
            #remove y ticks if there is no data
            if count == 0:                
                ax[y,x].tick_params(axis='y',which='both', left=False, labelleft=False)
##            else:
##                ax[y,x].set_yscale('log')
                
            #draw bar chart
            ax[y, x].bar(list(map(lambda d: DIFF_MAP[d], range(0,15))), checks[skill], color=col)

            #add stat data
            ax[y, x].text(0.75, 0.85, f'Σ={count}', color=SPINE_COLOUR, transform = ax[y, x].transAxes)
            ax[y, x].text(0.75, 0.75, f'M={max_skill}', color=SPINE_COLOUR, transform = ax[y, x].transAxes)

    #save figures with max window size
    mng = plt.get_current_fig_manager()
    mng.window.state('zoomed')
    fig.savefig(title + ".png", facecolor=fig.get_facecolor(), transparent=False)
 
plt.show()
