# January 2025 print chapter, v0.2: content (American style).
COVERS = 'Edited from five reconstructed weeks, covering January 1–February 2.'

SOURCES = {
 'mediamgr': ('TechCrunch', 'OpenAI failed to deliver the opt-out tool it promised by 2025', 'January 1, 2025',
              'https://techcrunch.com/2025/01/01/openai-failed-to-deliver-the-opt-out-tool-it-promised-by-2025/'),
 'russia': ('Reuters', 'Putin orders Russian government and top bank to develop AI cooperation with China', 'January 1, 2025',
            'https://www.reuters.com/technology/putin-orders-russian-government-top-bank-develop-ai-cooperation-with-china-2025-01-01/'),
 'msft': ('Microsoft', 'The golden opportunity for American AI', 'January 3, 2025', 'https://blogs.microsoft.com/on-the-issues/2025/01/03/the-golden-opportunity-for-american-ai/'),
 'meta': ('CNN, via KTVZ', 'Meta scrambles to delete its own AI accounts after backlash intensifies', 'January 3, 2025',
          'https://ktvz.com/money/cnn-business-consumer/2025/01/03/meta-scrambles-to-delete-its-own-ai-accounts-after-backlash-intensifies/'),
 'altman1': ('Sam Altman', 'Reflections', 'January 5, 2025, Pacific time; feed timestamp January 6, 01:37 UTC', 'https://blog.samaltman.com/reflections'),
 'altman2': ('Sam Altman', 'Atom feed: publication timestamp for Reflections', 'January 6, 2025, 01:37:29 UTC', 'https://blog.samaltman.com/posts.atom'),
 'nvidia': ('Nvidia', 'CES 2025: AI Advancing at “Incredible Pace,” NVIDIA CEO Says', 'January 6, 2025', 'https://blogs.nvidia.com/blog/ces-2025-jensen-huang/'),
 'anthropic': ('TechCrunch', 'Anthropic reportedly in talks to raise $2B at $60B valuation, led by Lightspeed', 'January 7, 2025',
               'https://techcrunch.com/2025/01/07/anthropic-reportedly-in-talks-to-raise-2b-at-60b-valuation-led-by-lightspeed/'),
 'phi1': ('Shital Shah', 'Phi-4 Now On HuggingFace with MIT Licence!', 'January 8, 2025', 'https://shital.com/blog/tweets/thread/202501082332-phi-4-official-release/'),
 'phi2': ('Microsoft, via Hugging Face', 'Phi-4 model card', 'model repository; accessed October 24, 2026', 'https://huggingface.co/microsoft/phi-4'),
 'grok': ('MacRumors', 'Grok Now Available as Standalone App in the US', 'January 9, 2025', 'https://www.macrumors.com/2025/01/09/grok-now-available-as-standalone-app-in-the-us/'),
 'zuck1': ('TheTVDB', 'The Joe Rogan Experience #2255 – Mark Zuckerberg', 'episode of January 10, 2025', 'https://thetvdb.com/series/joe-rogan-experience/episodes/10901587'),
 'zuck2': ('ITPro', 'Mark Zuckerberg says AI will be doing the work of mid-level engineers this year', 'January 20, 2025',
           'https://www.itpro.com/software/development/a-sign-of-things-to-come-in-software-development-mark-zuckerberg-says-ai-will-be-doing-the-work-of-mid-level-engineers-this-year-and-hes-not-the-only-big-tech-exec-predicting-the-end-of-the-profession'),
 'sfdc': ('Salesforce', 'Salesforce Unveils Agentforce for Retail to Boost Productivity with Digital Labor and Retail Cloud to Unite In-Store and Digital Shopping', 'January 10, 2025',
          'https://www.salesforce.com/news/press-releases/2025/01/10/agentforce-retail-cloud-pos-announcement/'),
 'diffusion': ('US Bureau of Industry and Security, Federal Register', 'Framework for Artificial Intelligence Diffusion', 'January 15, 2025; effective January 13',
               'https://www.federalregister.gov/documents/2025/01/15/2025-00636/framework-for-artificial-intelligence-diffusion'),
 'uk': ('UK Government', 'AI Opportunities Action Plan: government response', 'January 13, 2025',
        'https://www.gov.uk/government/publications/ai-opportunities-action-plan-government-response/ai-opportunities-action-plan-government-response'),
 'tasks': ('OpenAI', 'ChatGPT release notes: Tasks', 'January 14, 2025 entry', 'https://help.openai.com/en/articles/6825453-chatgpt-release-notes'),
 'eo14141': ('Executive Office of the President, preserved by the American Presidency Project', 'Executive Order 14141—Advancing United States Leadership in Artificial Intelligence Infrastructure',
             'January 14, 2025', 'https://www.presidency.ucsb.edu/documents/executive-order-14141-advancing-united-states-leadership-artificial-intelligence'),
 'minimax': ('MiniMax', 'MiniMax-01 is Now Open-Source: Scaling Lightning Attention for the AI Agent Era', 'January 15, 2025', 'https://www.minimax.io/news/minimax-01-series-2'),
 'apple': ('TechCrunch', 'Apple pauses AI notification summaries for news after generating false alerts', 'January 16, 2025',
           'https://techcrunch.com/2025/01/16/apple-pauses-ai-notification-summaries-for-news-after-generating-false-alerts/'),
 'r1': ('DeepSeek', 'DeepSeek-R1 Release', 'January 20, 2025', 'https://deepseek.com/en/news/deepseek-r1/'),
 'stargate': ('OpenAI', 'Announcing The Stargate Project', 'January 21, 2025', 'https://openai.com/index/announcing-the-stargate-project/'),
 'flashthink': ('Google for Developers', 'Gemini API release notes', 'January 21, 2025 entry', 'https://ai.google.dev/gemini-api/docs/changelog'),
 'operator': ('OpenAI', 'Introducing Operator', 'January 23, 2025', 'https://openai.com/index/introducing-operator/'),
 'eo': ('The White House', 'Removing Barriers to American Leadership in Artificial Intelligence', 'January 23, 2025',
        'https://www.whitehouse.gov/presidential-actions/2025/01/removing-barriers-to-american-leadership-in-artificial-intelligence/'),
 'metacapex': ('Reuters', 'Meta to spend up to $65 billion this year to power AI goals, Zuckerberg says', 'January 24, 2025',
               'https://www.reuters.com/technology/meta-invest-up-65-bln-capital-expenditure-this-year-2025-01-24/'),
 'selloff': ('Reuters', 'DeepSeek sparks AI stock selloff; Nvidia posts record market-cap loss', 'January 27, 2025',
             'https://www.reuters.com/technology/chinas-deepseek-sets-off-ai-market-rout-2025-01-27/'),
 'janus': ('DeepSeek', 'Janus: Janus-Pro release and model repository', 'January 27, 2025 release entry', 'https://github.com/deepseek-ai/Janus'),
 'qwen': ('Qwen Team', 'Qwen2.5-Max: Exploring the Intelligence of Large-scale MoE Model', 'January 28, 2025', 'https://qwenlm.github.io/blog/qwen2.5-max/'),
 'azure': ('SD Times', 'DeepSeek R1 is now available on Azure AI Foundry', 'January 30, 2025', 'https://sdtimes.com/ai/deepseek-r1-is-now-available-on-azure-ai-foundry/'),
 'tulu': ('Allen Institute for AI', 'Scaling the Tülu 3 post-training recipes to surpass the performance of DeepSeek V3', 'January 30, 2025', 'https://allenai.org/blog/tulu-3-405b'),
 'garante': ('Garante per la protezione dei dati personali', 'Artificial Intelligence: The Italian Data Protection Authority blocks DeepSeek', 'January 30, 2025',
             'https://www.garanteprivacy.it/home/docweb/-/docweb-display/docweb/10097450'),
 'nasa': ('CNBC (via NBC New York)', "NASA becomes latest federal agency to block China's DeepSeek on security and privacy concerns", 'January 31, 2025',
          'https://www.nbcnewyork.com/news/business/money-report/nasa-becomes-latest-federal-agency-to-block-chinas-deepseek-on-security-and-privacy-concerns/6130603/'),
 'o3mini': ('OpenAI', 'OpenAI o3-mini', 'January 31, 2025', 'https://openai.com/index/openai-o3-mini/'),
 'deepres': ('OpenAI', 'Introducing deep research', 'February 2, 2025 launch announcement', 'https://openai.com/index/introducing-deep-research/'),
 'aiact': ('European Commission', 'First rules of the Artificial Intelligence Act are now applicable', 'February 3, 2025 notice on provisions applicable from February 2',
           'https://digital-strategy.ec.europa.eu/en/news/first-rules-artificial-intelligence-act-are-now-applicable'),
}

THEME = ('Capability, Access', [
 ('Capability', " took several forms in January: reasoning models, browser agents, image systems and tools for scheduled work. DeepSeek's R1 drew "
  "attention to downloadable reasoning models, while OpenAI tested ways for assistants to act on a user's behalf. Each release posed a practical "
  'question: what could the system reliably do?'),
 ('Access', ' depended on more than a release announcement. Model weights, licenses, subscriptions and computing resources determined who could use '
  'or adapt a system. Large infrastructure plans appeared alongside smaller downloadable models. Export controls, privacy orders and government bans '
  'added another boundary: a service available in one place could face limits in another.'),
])

NOTE = ('Reconstructed in October 2026. ChatGPT had read Claude’s draft. Grok received suggested stories for weeks 1–3 and compiled weeks 4–5 '
        'independently. DeepSeek used sources supplied by the collection. Overlap between selections is therefore not a measure of independent agreement.')
R = 'Reconstructed in October 2026'
C = 'Claude (Opus 5.5)'; G = 'ChatGPT (GPT-6)'; D = 'DeepSeek V4.1-Flash-1017'; Kp = 'Grok 4 (prompted)'; K = 'Grok 4'

WEEKS = [
 (1, 'January 1–5', NOTE, [
  ('OpenAI misses its own date for a creator opt-out tool', 'Reported January 1',
   ["OpenAI had said in May 2024 that Media Manager, a tool to let creators specify how their work could be used in AI training, would be in place "
    "“by 2025.” As the year began, it had not appeared, and the company had given no public update since a spokesperson said in August that it was "
    "still in development.{mediamgr}",
    "The tool was meant to answer creators' objections at a time when OpenAI faced several copyright suits over its training data."],
   [C, G], ['2025-W01-L1-4', '2025-W01-L2-4']),
  ('Russia seeks closer AI cooperation with China', 'January 1: instructions reported',
   ["Instructions published on the Kremlin's website called on Russia's government and Sberbank to develop AI cooperation with China, Reuters reported. "
    "The direction concerned joint research and development.{russia}",
    "The proposal placed international cooperation alongside domestic investment as a route to developing AI capacity."],
   [C, G], ['2025-W01-L1-5', '2025-W01-L2-5']),
  ('Microsoft plans $80 billion for AI data centers', 'January 3',
   ["Microsoft said it expected to invest approximately $80 billion during its 2025 fiscal year in data centers for training AI models and deploying "
    "AI and cloud applications.{msft}",
    "The announcement, a spending plan for the year, placed computing capacity at the center of the company's AI strategy."],
   [C, G, Kp], ['2025-W01-L1-1', '2025-W01-L2-1', '2025-W01-L4-1']),
  ('Meta removes AI character profiles', 'January 3',
   ["Meta removed company-created AI character accounts after renewed attention and criticism from users. CNN reported the removals and the "
    "difficulties users encountered when trying to block the accounts.{meta}",
    "The episode exposed a practical problem for synthetic identities on social platforms: users needed clear information and working controls over their interactions."],
   [C, G], ['2025-W01-L1-3', '2025-W01-L2-3']),
  ('Altman sets out expectations for AI agents', 'January 5, Pacific time',
   ["In “Reflections,” Sam Altman expressed confidence that OpenAI knew how to build AGI as the company had traditionally understood it. He also "
    "suggested that AI agents could enter the workforce during 2025.{altman1}{altman2}",
    "His forecast made the performance of agents in actual work the test of the company's ambitions for the year."],
   [C, G, D], ['2025-W01-L1-2', '2025-W01-L2-2', '2025-W01-L3-1']),
 ]),
 (2, 'January 6–12', R, [
  ('Nvidia brings AI hardware and world models to CES', 'January 6',
   ["At CES, Nvidia introduced the Cosmos platform for developing physical AI, alongside GeForce RTX 50-series graphics processors and Project DIGITS, "
    "a desktop AI system. Cosmos combined world foundation models with tools intended to support robotics and autonomous-vehicle development.{nvidia}",
    "The announcements connected model development to simulation, consumer hardware and local computing beyond a hosted chatbot."],
   [C, G, D, Kp], ['2025-W02-L1-1', '2025-W02-L2-1', '2025-W02-L3-1', '2025-W02-L4-1']),
  ('Anthropic is reported to seek $2 billion at a $60 billion valuation', 'Reported January 7',
   ["The *Wall Street Journal* reported that Anthropic was in talks to raise $2 billion at a $60 billion valuation, in a round led by Lightspeed Venture Partners.{anthropic}",
    "The talks put a price on investors' expectations for one of OpenAI's main rivals at the start of the year."],
   [C, G], ['2025-W02-L1-2', '2025-W02-L2-3']),
  ('Microsoft releases Phi-4 weights', 'January 8',
   ["Microsoft made the official Phi-4 model weights available on Hugging Face under the MIT license. The 14-billion-parameter text model had been "
    "introduced in December; January's development was the public release of its weights.{phi1}{phi2}",
    "Downloadable weights let developers run and adapt the model on their own computing resources."],
   [C, G], ['2025-W02-L1-3', '2025-W02-L2-2']),
  ('Grok reaches US users through a standalone app', 'January 9',
   ["Grok became available as a standalone iOS app in the United States. The release gave users a separate mobile interface for the assistant, which "
    "had previously been associated with the X platform.{grok}",
    "Distribution was part of the competition among assistants: a dedicated app could reach users through a different entry point."],
   [C, G], ['2025-W02-L1-4', '2025-W02-L2-4']),
  ('Salesforce announces retail agents', 'January 10',
   ["Salesforce announced Agentforce capabilities for retail tasks including guided shopping, order management, appointments and loyalty programs. "
    "Availability was scheduled in stages during February and March.{sfdc}",
    "The product plans applied agents to defined commercial workflows, where usefulness could be judged against specific customer and staff tasks."],
   [G], ['2025-W02-L2-5']),
  ('Zuckerberg predicts AI coding agents at the level of mid-level engineers', 'January 10',
   ["On The Joe Rogan Experience, Mark Zuckerberg said that “probably in 2025” Meta and other companies would “have an AI that can effectively be a sort "
    "of mid-level engineer that you have at your company that can write code.”{zuck1}{zuck2}",
    "The remark tied AI's progress in coding directly to the work of human engineers."],
   [C], ['2025-W02-L1-5']),
 ]),
 (3, 'January 13–19', R, [
  ('US rule sets new controls on AI diffusion', 'January 13; published January 15',
   ["The US government issued an interim final rule controlling exports of advanced computing chips and certain AI model weights. The rule took effect "
    "on January 13 and set May 15 as the compliance date for most changes.{diffusion}",
    "The framework treated access to computing and model weights as matters of national security."],
   [C, G, D, Kp], ['2025-W03-L1-1', '2025-W03-L2-1', '2025-W03-L3-1', '2025-W03-L4-1']),
  ('UK adopts an AI action plan', 'January 13',
   ["The UK government published its response to the AI Opportunities Action Plan. Commitments covered public computing capacity, AI Growth Zones, "
    "skills and adoption in public services.{uk}",
    "The plan joined investment in technical resources to changes in public administration, setting an agenda for implementation."],
   [C, G], ['2025-W03-L1-3', '2025-W03-L2-2']),
  ('ChatGPT adds scheduled tasks', 'January 14',
   ["OpenAI began a beta rollout of Tasks for ChatGPT Plus, Pro and Team users. Users could ask ChatGPT to carry out a request later, either once or on "
    "a recurring schedule.{tasks}",
    "The feature extended the assistant beyond an immediate question-and-answer session; scheduling offered a limited, concrete form of delegation."],
   [C, G], ['2025-W03-L1-4', '2025-W03-L2-3']),
  ('Biden directs federal support for AI infrastructure', 'January 14',
   ["President Joe Biden signed Executive Order 14141 on AI infrastructure. It directed federal action to support AI data centers and associated "
    "clean-energy infrastructure, including the use of federal sites.{eo14141}",
    "The order linked AI development to land, electricity and construction."],
   [C, G], ['2025-W03-L1-2', '2025-W03-L2-5']),
  ('MiniMax releases long-context models', 'January 15',
   ["MiniMax introduced the MiniMax-01 family, including a text model and a vision-language model, and released model weights. The company reported "
    "support for contexts of up to four million tokens.{minimax}",
    "The larger context window expanded the amount of material a model could receive in one request."],
   [C, G], ['2025-W03-L1-5', '2025-W03-L2-4']),
  ('Apple pauses AI summaries of news alerts', 'January 16',
   ["Apple paused Apple Intelligence notification summaries for news and entertainment apps in developer previews of its next software updates, after "
    "complaints that summaries had misrepresented news reports, including a BBC complaint about a false alert. Summaries would be shown in italics and "
    "marked as a beta feature that might contain errors.{apple}",
    "The pause showed the risk of generated summaries appearing under a news organization's name."],
   [D], ['2025-W03-L3-2']),
 ]),
 (4, 'January 20–26', R, [
  ('DeepSeek releases R1 reasoning models', 'January 20',
   ["DeepSeek released R1 and six smaller distilled models, making their weights available for download. The company reported results competitive "
    "with OpenAI's o1 on specified reasoning benchmarks.{r1}",
    "The release widened access to reasoning models and gave researchers systems they could inspect and run themselves."],
   [C, G, D, K], ['2025-W04-L1-1', '2025-W04-L2-1', '2025-W04-L3-1', '2025-W04-L4-1']),
  ('Stargate announces a large US infrastructure plan', 'January 21',
   ["OpenAI announced Stargate, a company intending to invest $500 billion over four years in US AI infrastructure. It said $100 billion would begin "
    "to be deployed immediately. Initial equity funders included SoftBank, OpenAI, Oracle and MGX.{stargate}",
    "The announcement set out investment intentions and deployment plans, to be funded by its equity partners."],
   [C, G, D, K], ['2025-W04-L1-2', '2025-W04-L2-2', '2025-W04-L3-2', '2025-W04-L4-2']),
  ('Google updates Gemini Flash Thinking', 'January 21',
   ["Google released an updated experimental preview of Gemini 2.0 Flash Thinking, identified as gemini-2.0-flash-thinking-exp-01-21. It followed the "
    "first public preview in December 2024.{flashthink}",
    "The update kept reasoning models in active development across several providers, still under an experimental label."],
   [K], ['2025-W04-L4-3']),
  ('Operator begins a browser-agent preview', 'January 23',
   ["OpenAI introduced Operator as a research preview for ChatGPT Pro users in the United States. It could interact with websites through a browser, "
    "using actions such as clicking, typing and scrolling, while handing certain steps back to the user.{operator}",
    "The preview moved assistance from generating instructions toward carrying out actions, with the user kept in control of key steps."],
   [C, G, D, K], ['2025-W04-L1-4', '2025-W04-L2-3', '2025-W04-L3-4', '2025-W04-L4-4']),
  ('Trump orders a new AI action plan', 'January 23',
   ["President Donald Trump signed an executive order directing officials to produce an AI action plan within 180 days. It also called for a review "
    "of actions taken under the revoked Executive Order 14110 of October 2023, the previous administration's AI order.{eo}",
    "The directive began the policy process that produced America's AI Action Plan in July."],
   [C, G, D], ['2025-W04-L1-3', '2025-W04-L2-4', '2025-W04-L3-3']),
  ('Meta raises its planned capital spending', 'January 24',
   ["Mark Zuckerberg said Meta planned capital expenditure of $60 billion to $65 billion in 2025 as it expanded its AI infrastructure.{metacapex}",
    "The plan added another large commitment to the month's infrastructure announcements."],
   [C, G], ['2025-W04-L1-5', '2025-W04-L2-5']),
 ]),
 (5, 'January 27–February 2', R, [
  ('DeepSeek concerns trigger a sharp Nvidia selloff', 'January 27',
   ["Nvidia lost roughly $590 billion in market value in a single trading day as DeepSeek's models prompted investors to reassess expectations for AI "
    "spending, Reuters reported.{selloff}",
    "The record one-day loss measured how much investors' expectations rested on the cost of computing."],
   [C, G, D, K], ['2025-W05-L1-1', '2025-W05-L2-1', '2025-W05-L3-1', '2025-W05-L4-1']),
  ('Janus-Pro combines image understanding and generation', 'January 27',
   ["DeepSeek released Janus-Pro, a multimodal model family combining visual understanding with image generation. Its design used separate visual "
    "encoding paths for the two tasks within a shared framework, and model weights were made available.{janus}",
    "The release extended the month's downloadable-model activity beyond text and reasoning."],
   [K], ['2025-W05-L4-2']),
  ('Qwen2.5-Max enters hosted competition', 'January 28',
   ["Alibaba's Qwen team introduced Qwen2.5-Max, a large mixture-of-experts model offered through its hosted services. The team published comparisons "
    "with other models on selected benchmarks.{qwen}",
    "The release broadened the choice of hosted services, offered through an API and chat interface rather than as downloadable weights."],
   [C, G], ['2025-W05-L1-3', '2025-W05-L2-2']),
  ('Microsoft makes DeepSeek R1 available on its cloud', 'Reported January 30',
   ["Microsoft made DeepSeek R1 available through Azure AI Foundry and GitHub, saying it had run red-teaming and safety evaluations and applied content "
    "filtering by default.{azure}",
    "A US cloud provider began offering the Chinese model to business customers within days of the market's reaction to it."],
   [D], ['2025-W05-L3-2']),
  ('Ai2 scales its open post-training work', 'January 30',
   ["Ai2 released Tülu 3 405B, extending its post-training work to a 405-billion-parameter model. The release described training methods, including "
    "reinforcement learning with verifiable rewards, and provided resources for reproducing and studying the work.{tulu}",
    "The contribution included the training process as well as the resulting model, for researchers examining how post-training changes model behavior."],
   [K], ['2025-W05-L4-3']),
  ("Italy restricts DeepSeek's processing of personal data", 'January 30',
   ["Italy's data protection authority ordered an immediate restriction on the processing of Italian users' personal data by the companies providing "
    "DeepSeek's service. It also opened an investigation after finding the companies' response to its information request insufficient.{garante}",
    "The intervention brought European data-protection law to bear on the month's most discussed model."],
   [C], ['2025-W05-L1-2']),
  ('NASA blocks DeepSeek on agency systems', 'January 31',
   ["NASA's chief AI officer told staff that DeepSeek was blocked on agency devices and networks, citing national-security and privacy concerns because "
    "its servers operated outside the United States. The US Navy had already told its members to avoid the model.{nasa}",
    "Government restrictions on DeepSeek spread across agencies within a week of its rise to prominence."],
   [D], ['2025-W05-L3-3']),
  ('OpenAI releases o3-mini', 'January 31',
   ["OpenAI released o3-mini in ChatGPT and its API, emphasizing mathematics, science and coding. The model offered different reasoning-effort settings, "
    "and ChatGPT's free users received a way to try it.{o3mini}",
    "The release brought reasoning capability to a smaller model and a wider audience."],
   [C, G, D, K], ['2025-W05-L1-4', '2025-W05-L2-3', '2025-W05-L3-4', '2025-W05-L4-4']),
  ('Deep research produces sourced reports', 'February 2',
   ["OpenAI introduced deep research in ChatGPT, initially for Pro users. The feature searched and analyzed material from the web to produce reports with citations.{deepres}",
    "The service combined information gathering and synthesis in a longer workflow, with citations that made its sources easier to inspect."],
   [G], ['2025-W05-L2-4']),
  ('The first AI Act obligations begin to apply', 'February 2',
   ["The first provisions of the EU AI Act began to apply, including rules on prohibited AI practices and AI literacy. This was one stage in the law's "
    "phased application.{aiact}",
    "The milestone turned parts of the legislation into applicable requirements, with later stages on their own timetable."],
   [C, G], ['2025-W05-L1-5', '2025-W05-L2-5']),
 ]),
]
