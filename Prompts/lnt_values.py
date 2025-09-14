LNT_VALUES = [
    # Core 7 Leave No Trace Principles
    "Plan Ahead & Prepare",
    "Travel & Camp on Durable Surfaces",
    "Dispose of Waste Properly", 
    "Leave What You Find",
    "Minimize Campfire Impacts",
    "Respect Wildlife",
    "Be Considerate of Others",
    
    # Plan Ahead & Prepare - The Basics
    "Know the regulations and special concerns for the area you'll visit",
    "Prepare for extreme weather, hazards, and emergencies",
    "Schedule your trip to avoid times of high use",
    "Visit in small groups. Split larger parties into smaller groups",
    "Repackage food to minimize waste",
    "Use a map and compass to eliminate the use of rock cairns, flagging, or marking paint",
    
    # Travel & Camp on Durable Surfaces - The Basics
    "Durable surfaces include established trails, campsites, rock, gravel, and dry grasses or snow",
    "Protect riparian areas by camping at least 200 feet from lakes and streams",
    "Good campsites are found, not made. Altering a site is not necessary",
    "Concentrate use on existing trails and campsites",
    "Walk single file in the middle of the trail, even when wet or muddy",
    "Keep campsites small. Focus activity in areas where vegetation is absent",
    "Disperse use to prevent the creation of campsites and trails",
    "Avoid places where impacts are just beginning",
    
    # Dispose of Waste Properly - The Basics
    "Pack it in, pack it out. Inspect your campsite and rest areas for trash or spilled food",
    "Deposit solid human waste in catholes dug 6-8 inches deep at least 200 feet from water, camp, and trails",
    "Bury toilet paper deep in a cathole or pack the toilet paper out along with hygiene products",
    "To wash yourself or your dishes, carry water 200 feet away from streams or lakes and use small amounts of biodegradable soap. Scatter strained dishwater",
    
    # Leave What You Find - The Basics  
    "Preserve the past: observe cultural or historic structures and artifacts, but do not touch them",
    "Leave rocks, plants, and other natural objects as you find them",
    "Avoid introducing or transporting non-native species",
    "Do not build structures, furniture, or dig trenches",
    
    # Minimize Campfire Impacts - The Basics
    "Campfires can cause lasting impacts on the environment. Use a lightweight stove for cooking and enjoy a candle lantern for light",
    "Use established fire rings, pans, or mound fires where fires are permitted",
    "Keep fires small. Use only sticks from the ground that can be broken by hand",
    "Burn all wood and coals to ash, put out campfires completely, then scatter cool ashes",
    
    # Respect Wildlife - The Basics
    "Observe wildlife from a distance. Do not follow or approach them",
    "Never feed animals. Feeding wildlife damages their health, alters natural behaviors, and exposes them to predators and other dangers",
    "Control pets at all times, or leave them at home",
    "Avoid wildlife during sensitive times: mating, nesting, raising young, or winter",
    
    # Be Considerate of Others - The Basics
    "Respect others and protect the quality of their experience",
    "Be courteous. Yield to other users on the trail",
    "Greet riders and ask which side of the trail to move to when encountering pack stock",
    "Take breaks and camp away from trails and others",
    "Let nature's sounds prevail. Avoid loud voices and noises"
]

LNT_PROMPT_TEMPLATE = """
You are analyzing a Reddit comment for Leave No Trace (LNT) outdoor ethics values.

IMPORTANT: Leave No Trace principles only apply to outdoor recreation contexts (camping, hiking, backpacking, fishing, hunting, climbing, wilderness activities, national parks, nature areas, trails, etc.). If the post and comment do not involve outdoor recreation scenarios, respond with:
EXHIBITED: NA
INCENTIVIZED: NA

REDDIT POST:
Title: {title}
Body: {body}

COMMENT TO ANALYZE:
{comment}

Only proceed with the analysis below if this content involves outdoor recreation activities. Otherwise, return NA as instructed above.

Please identify which of these Leave No Trace values are EXHIBITED (directly shown) and INCENTIVIZED (encouraged in others) in the comment:

{values_list}

OUTPUT FORMAT: For each value, output 0 (not present) or 1 (present) for EXHIBITED and INCENTIVIZED:

EXHIBITED:
[List each value: 0 or 1]

INCENTIVIZED:
[List each value: 0 or 1]
"""