"""
PS: I am open to ways I could optimize this code.

Program simply takes each letter of your name
and creates a different mnemonic at every instance.
e.g:
R - resounding
A - altitude
L - like
P - progress
H - hearty
"""

import random

"""
I collected a bunch of words(trash_collect)
from the internet and needed to clean it up
and make a list from them thus the function
"""
def create_list(trash):
    trash_replace = trash.replace('|', '')
    new_list = trash_replace.split()
    return new_list


trash_collect = "absolutely | adorable | accepted | acclaimed | accomplish | accomplishment | " \
                "achievement | action | active | admire | adventure | affirm | affirmative | " \
                "affluent | agree | agreeable | amazing | angelic | appealing | approve | " \
                "aptitude | attractive | awesome | able | acceptance | accepting | activate " \
                "| add | addition | advantage | aid | aim | accuracy | abundance | appreciate | " \
                "appreciative | assertive | assertiveness | audacity | aware | awareness | authentic | " \
                "accountable | accountability | acknowledgement | adventure | adventurous | adaptability | " \
                "agility | alertness | affection | affectionate | ambition | amazed | attentiveness | " \
                "anticipation | authenticity | animated | awe | awed | adore | awesomeness | amusing | " \
                "astonished | angel | admirable | altruism | absolutely | advantageous | affinity," \
                " amazement | approval | applaud | attitude | altitude | ardor | accolade | admirer " \
                "| amicable | accommodating | awake | awaken | amplify | aligned | alignment | assured | " \
                "articulate | astounding | approachable | amiable | alert | adept | alluring | "\
                "beaming | beautiful | believe | beneficial | bliss | bountiful | " \
                "bounty | brave | bravo | bubbly | blessing" \
                " | blessed | blissful | bloom | balance | blossom | balanced | brilliant | beloved | best | " \
                "better | bold | boldness | bright | brightness | breezy | brilliance | bravery | belonging | " \
                "breathtaking | blazing | beauty | benevolent |"\
                "calm | celebrated | certain | champ | champion | charming " \
                "| cheery | choice | classic | clean | commend | " \
                "composed |congratulations | constant | cool | creative | cute " \
                "| care | caring | create | charm | " \
                "charming | capable | creativity | celebration | " \
                "certainty | charity | cuddle | comfort | comfortable | " \
                "clean | cuddly | cheerful | clarity | commitment | collaboration " \
                "| curiosity | conscious | change | challenge | communication | " \
                "community | compassion | connection | connected | centered | " \
                "courage | courageous | conviction | competent | consistent | " \
                "contribution | courtesy | cooperation | closeness | curiosity |" \
                " consideration | communion | collected | conquer | charisma | congruence | " \
                "companionship | consistency | cordial | cozy | content | " \
                "compliment | carefree | credible | clever | contemplative | congenial | " \
                "compassionate | considerate | cautious | captivating | " \
                "confident | courteous | curious | constructive | committed |"\
                "dazzling | delight | delightful | distinguished | divine | " \
                "direction | delicious | dream | do | dreamy | daring | " \
                "decisive | delighted | dreamy | dynamic | delicate | deserving " \
                "| decent | desire | devotion | dignity | " \
                "dazzled | devoted | drive | diversity | dependability | dedication | " \
                "discovery | deep | determined | diligent | dedicated | detailed | " \
                "discreet | direct | decorous | debonair | dependable | diplomatic |"\
                "earnest | easy | ecstatic | effective | effervescent | efficient | effortless | " \
                "electrifying | elegant | enchanting | encouraging | endorsed | " \
                "energetic | energized | engaging | essential | esteemed | ethical | " \
                "excellent | excellence | exciting | exquisite | empathy | empathic | ease | easily | education | " \
                "empowered | encouraged | enable | elated | encouragement | " \
                "engaged | energy | educated | elegance | effective | " \
                "excited | excitement | enjoy | endurance | experience | expertise | " \
                "enjoyment | eager | elevate | evolve | expression | empowering | enchanted | " \
                "exhilarating | enthusiastic | ecstatic | equality | exemplary | enlivened | " \
                "extraordinary | expectant | earnest | enduring | expansive | exalted | " \
                "effortless | easy-going | exuberant  | entertaining | endearing | enterprising | "\
                "fabulous | fair | familiar | fantastic | favorable | fitting | free | fresh | " \
                "flourishing | fortunate | friendly | fun | funny| flowing | faith | " \
                "faithful | favorite | family | flexibility | focus | fulfilled | " \
                "forgiving | fascinating | fancy | fearless | festive | fit | fortitude | freedom | frank | "\
                "generous | genius | genuine | giving | glamorous | glow | glowing | good | " \
                "graceful | great | grin | growing | generosity | genius | " \
                "gift | genial | generate | giddy | glad | growth | guidance " \
                "| guide | give | giving | good | goodness | God | grand | " \
                "great | goddess | gorgeous | grounded | glory | " \
                "grow | gratitude | gratefulness | gratitude | goodwill | gentle | " \
                "happy | harmonious | healing | healthy | heartwarming | heartfelt | " \
                "heart | hearty | heavenly | honest | honorable | honored | hug | " \
                "hope | humble | happily | human | honesty | harmony | health | hopeful | hope | " \
                "humor | hero | holy | harness | holiness | honor | hospitality | helpful | " \
                "holistic | hot | humorous | handsome | hard-working | hilarious | " \
                "idea | ideal | imaginative | imagine | imagination | impressive | independent | " \
                "innovate | innovative | instant | instinctive | intuitive | intellectual | intelligent | " \
                "inventive | inspired | inspiration | interesting | improvement | influence | inner peace | " \
                "insight | integrity | invigorating | involvement | intention | intentional | illumination | " \
                "intrepid | innocence | intense | intimacy | investment | incomparable | invincible | " \
                "interconnected | incredible | ingenious | insightful | inspiring | " \
                "inquisitive | introspective | industrious | impartial | "\
                "jovial | joy | jubilant | joyful | joyous | jolly | justice | just | "\
                "kind | kindness | knowing | knowledgeable | kiss | keen | laugh | " \
                "light | legendary | learned | lively | lovely | lucid | lucky | luminous | " \
                "like | love | leader | loving | liberty | luxury | life | longevity | " \
                "lesson | logical | lovable | loyal | "\
                "marvelous | masterful | meaningful | merit | meritorious | miraculous | " \
                "motivating | moving |  meaning | more | magnificent | mastery | modesty | " \
                "motivation | mercy | mindfulness | mindful | miracle | magic | maturity | " \
                "meditation | mastermind | magnetism | movement | memorable | mesmerizing | " \
                "majestic | methodical | motivated | magnetic | modest | "\
                "natural | nice | now | nurturing | nutritious | noble | namaste | nourishment | " \
                "neat | nirvana | nourish | new | one | open | optimistic | onwards | openly | " \
                "outstanding | order | overcome | oneness | outgoing | organized | opportunity | " \
                "original | open-minded | objective | observant | outspoken | positive | paradise | " \
                "phenomenal | pleasurable | plentiful | pleasant | poised | polished | powerful | " \
                "prepared | principled | productive | progress | prominent | protected | proud | " \
                "passion | persistent | peace | prosperity | prosper | persistence | precision | " \
                "proactive | punctual | patience | power | perseverance | playful | play | " \
                "playfulness | pleased | pleasing | purpose | prepared | present | polite | " \
                "possibility | promptness | priceless | participant | progress | privacy | " \
                "privilege | patient | persuasive | protective | passionate | "\
                "quality | quick | quiet | quickening | queen | queenly | quietness | " \
                "qualified | quest-ful | ready | reassuring | refined | refreshing | " \
                "rejoice | relaxed | respect | reliable | remarkable | resounding | " \
                "respected | restored | reward | rewarding | right | robust | " \
                "recommend | relieve | relieved | refreshed | resourceful | responsible | " \
                "renewed | resilient | reverence | romance | rainbow | risk | relationship | " \
                "revived | revelation | rest | rested | righteous | release | resplendent | " \
                "respectful | resolute | reflective | receptive | "\
                "safe | satisfactory | secure | simple | simplicity | simplify | skilled | " \
                "skillful | smile | soulful | sparkling | special | spirited | " \
                "spiritual | stirring | stupendous | stunning | success | successful | " \
                "sunny | super | superb | supporting | surprising | sacred | selfless | " \
                "self-esteem | serene | serenity | security | sustained | soulful | " \
                "self-love | self-compassion | self-care | service | stimulating | " \
                "satisfying | still | surprised | soul | shelter | space | save | " \
                "sincere | sympathetic | strive | spontaneous | splendid | supreme | " \
                "smart | spectacular | shine | sublime | steadfastness | sunny | " \
                "strong | strength | sentimental | shift | synchronicity | synergy | " \
                "serendipity | stretch | stellar | supercharged | self-assured | " \
                "supportive | self-reliant | steadfast | sensitive | steady | spunky | sensible | selective | "\
                "terrific | thorough | thrilling | thriving | top | tranquil | " \
                "transforming | transformational | trusting | truthful | true | " \
                "truth | trust | tact | teaching | teachable | team | thankful | " \
                "thankfulness | truthfulness | tolerance | tranquility | " \
                "transparency | tender | touch | thriving | tenacity | triumph | " \
                "tender | tradition | timely | trustworthy | timing | thrill | " \
                "transformation | tough | tenacious | talkative | talented | tolerant | " \
                "thoughtful | unleashed | uplift | unconditional | ultimate | unwavering | " \
                "up | upbeat | upright | upstanding | useful | understanding | unity | " \
                "unbelievable | up-leveled | understood | unparalleled | uncompromising | " \
                "unbiased | unique | unconventional | unassuming | "\
                "valued | vibrant | victorious | victory | vigorous | virtuous | vitality | " \
                "vivacious | vitality | value | valuable | variety | versatility | vulnerable | " \
                "vulnerability | validation | virtue | venturous | versatile | "\
                "wealthy | welcome | well | whole  | wholesome | willing | wonderful | " \
                "wondrous | worthy | wow | warm | wonder | worthiness | win | willingness | " \
                "wellness | wholehearted | wise | xoxo | yes | yummy | yay | " \
                "you | zeal | zealous | zest | zing | zestful | zen"

words = create_list(trash_collect)
user_name = input()

for letter in user_name:
    choices = []
    if letter == ' ':
        print('')
        continue
    for word in words:
        if word[0].upper() == letter.upper():
            choices.append(word)
    # print(choices)
    try:
        print(f'{letter.upper()} - {random.choice(choices)}')
    except IndexError:
        print(f'{letter} - not a letter')
