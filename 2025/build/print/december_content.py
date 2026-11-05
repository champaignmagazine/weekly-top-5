# December 2025 print chapter, v0.2: content (American style).
COVERS = 'Edited from four posts published in December 2025, covering December 1–28, and the December 29–31 excerpts of the January 4, 2026 post.'

SOURCES = {
 'v32': ('DeepSeek', 'DeepSeek-V3.2 Release', 'December 1, 2025', 'https://api-docs.deepseek.com/news/news251201/'),
 'apple': ('Apple', 'John Giannandrea to retire from Apple', 'December 1, 2025', 'https://www.apple.com/newsroom/2025/12/john-giannandrea-to-retire-from-apple/'),
 'gen45': ('Runway', 'Introducing Runway Gen-4.5', 'December 1, 2025', 'https://runway.com/research/introducing-runway-gen-4.5'),
 'codered': ('The National News Desk, citing The Wall Street Journal', "OpenAI declares 'code red' to improve ChatGPT, report says", 'December 2, 2025',
             'https://newschannel9.com/news/nation-world/openai-ceo-sam-altman-declares-code-red-memo-to-improve-chatgpt-chatbot-wall-street-journal-report-says'),
 'deepthink': ('Google', 'Gemini 3 Deep Think is now available in the Gemini app', 'December 4, 2025',
               'https://blog.google/products-and-platforms/products/gemini/gemini-3-deep-think/'),
 'limitless': ('Reuters, via Investing.com', 'Meta acquires AI-wearables startup Limitless', 'December 5, 2025',
               'https://ca.investing.com/news/stock-market-news/meta-acquiresaiwearables-startup-limitless-4351782'),
 'accenture': ('Anthropic', 'Accenture and Anthropic launch multi-year partnership to move enterprises from AI pilots to production', 'December 9, 2025',
               'https://www.anthropic.com/news/anthropic-accenture-partnership'),
 'adobe': ('Adobe', 'Adobe Makes Creativity Accessible for Everyone with Adobe Photoshop, Adobe Express and Adobe Acrobat in ChatGPT', 'December 10, 2025',
           'https://news.adobe.com/news/2025/12/adobe-photoshop-express-acrobat-chatgpt'),
 'chip3d': ('Stanford Engineering', 'Scientists and U.S. foundry achieve 3D chip breakthrough to accelerate AI', 'December 10, 2025',
            'https://engineering.stanford.edu/news/scientists-and-us-foundry-achieve-3d-chip-breakthrough-accelerate-ai'),
 'gpt52': ('OpenAI', 'Introducing GPT-5.2', 'December 11, 2025', 'https://openai.com/index/introducing-gpt-5-2/'),
 'eo': ('The White House', 'Ensuring a National Policy Framework for Artificial Intelligence', 'December 11, 2025',
        'https://www.whitehouse.gov/presidential-actions/2025/12/eliminating-state-law-obstruction-of-national-artificial-intelligence-policy/'),
 'deepres': ('Google', 'Build with Gemini Deep Research', 'December 11, 2025',
             'https://blog.google/innovation-and-ai/technology/developers-tools/deep-research-agent-gemini-api/'),
 'gwm': ('Runway', 'Introducing GWM-1', 'December 11, 2025', 'https://runway.com/research/introducing-runway-gwm-1'),
 'disney1': ('OpenAI and The Walt Disney Company', 'The Walt Disney Company and OpenAI reach landmark agreement to bring beloved characters from across Disney’s brands to Sora',
             'December 11, 2025', 'https://openai.com/index/disney-sora-agreement/'),
 'disney2': ('CNN Newsource, via NBC Palm Springs', 'Disney invests $1 billion in OpenAI and licenses 200 iconic characters for Sora', 'December 11, 2025',
             'https://www.nbcpalmsprings.com/2025/12/11/disney-invests-1-billion-in-openai-and-licenses-200-iconic-characters-for-sora'),
 'schedmd': ('Nvidia', 'NVIDIA Acquires Open-Source Workload Management Provider SchedMD', 'December 15, 2025', 'https://blogs.nvidia.com/blog/nvidia-acquires-schedmd/'),
 'nemotron': ('Nvidia', 'NVIDIA Debuts Nemotron 3 Family of Open Models', 'December 15, 2025',
              'https://investor.nvidia.com/news/press-release-details/2025/NVIDIA-Debuts-Nemotron-3-Family-of-Open-Models/default.aspx'),
 'images': ('OpenAI', 'The new ChatGPT Images is here', 'December 16, 2025', 'https://openai.com/index/new-chatgpt-images-is-here/'),
 'flash': ('Google', 'Gemini 3 Flash: frontier intelligence built for speed', 'December 17, 2025',
           'https://blog.google/products-and-platforms/products/gemini/gemini-3-flash/'),
 'skills': ('Anthropic', 'Equipping agents for the real world with Agent Skills', 'October 16, 2025; open-standard update December 18, 2025',
            'https://www.anthropic.com/research/equipping-agents-for-the-real-world-with-agent-skills'),
 'codex': ('OpenAI', 'Introducing GPT-5.2-Codex', 'December 18, 2025', 'https://openai.com/index/introducing-gpt-5-2-codex/'),
 'genesis': ('US Department of Energy', 'Energy Department Announces Collaboration Agreements with 24 Organizations to Advance the Genesis Mission', 'December 18, 2025',
             'https://www.energy.gov/articles/energy-department-announces-collaboration-agreements-24-organizations-advance-genesis'),
 'aisi': ('UK AI Security Institute', 'AI Security Institute – Frontier AI Trends report factsheet', 'December 18, 2025',
          'https://www.gov.uk/government/publications/ai-security-institute-frontier-ai-trends-report-factsheet/ai-security-institute-frontier-ai-trends-report-factsheet'),
 'glm1': ('Z.ai', 'GLM-4.7 model card', 'December 2025 release; live model card', 'https://huggingface.co/zai-org/GLM-4.7'),
 'glm2': ('Z.ai, via PR Newswire', 'Z.ai Releases GLM-4.7 Designed for Real-World Development Environments', 'December 27, 2025; confirms December 22 release',
          'https://www.prnewswire.com/news-releases/zai-releases-glm-4-7-designed-for-real-world-development-environments-cementing-itself-as-chinas-openai-302649821.html'),
 'groq': ('Groq', 'Groq and Nvidia Enter Non-Exclusive Inference Technology Licensing Agreement to Accelerate AI Inference at Global Scale', 'December 24, 2025',
          'https://groq.com/newsroom/groq-and-nvidia-enter-non-exclusive-inference-technology-licensing-agreement-to-accelerate-ai-inference-at-global-scale'),
 'cac': ('Cyberspace Administration of China', 'Notice seeking public comments on draft interim measures for AI anthropomorphic interaction services [translated title]',
         'December 27, 2025', 'https://www.cac.gov.cn/2025-12/27/c_1768571207311996.htm'),
 'nhs': ('UK Department for Science, Innovation and Technology and Department of Health and Social Care', 'Faster treatments and support for health workers as AI tackles A&E bottlenecks',
         'December 28, 2025', 'https://www.gov.uk/government/news/faster-treatments-and-support-for-health-workers-as-ai-tackles-ae-bottlenecks'),
 'hinton': ('Fortune', "Geoffrey Hinton says AI has 'progressed even faster than I thought'", 'December 28, 2025',
            'https://fortune.com/2025/12/28/geoffrey-hinton-godfather-of-ai-2026-prediction-human-worker-replacement/'),
 'manus': ('Manus', 'Manus Joins Meta for Next Era of Innovation', 'December 29, 2025', 'https://manus.im/blog/manus-joins-meta-for-next-era-of-innovation'),
 'grokbiz': ('xAI', 'Introducing Grok Business and Grok Enterprise', 'December 30, 2025', 'https://x.ai/news/grok-business'),
 'softbank': ('SoftBank Group', 'Completion of Additional $22.5 Billion Investment in OpenAI', 'December 31, 2025', 'https://group.softbank/en/news/press/20251231'),
 'forecast': ('Nikhil Chandak and colleagues', 'Scaling Open-Ended Reasoning to Predict the Future', 'December 31, 2025; arXiv version 1', 'https://arxiv.org/abs/2512.25070v1'),
 'adagres': ('Chao Peng and colleagues', 'AdaGReS: Adaptive Greedy Context Selection via Redundancy-Aware Scoring for Token-Budgeted RAG', 'December 31, 2025; arXiv submission',
             'https://arxiv.org/abs/2512.25052'),
 'rair': ('Chenji Lu and colleagues', 'RAIR: A Rule-Aware Benchmark Uniting Challenging Long-Tail and Visual Salience Subset for E-commerce Relevance Assessment',
          'December 31, 2025; arXiv version 1', 'https://arxiv.org/abs/2512.24943v1'),
}

THEME = ('Agents, Accountability', [
 ('Agents', ' were built into more of the places people work. Research agents opened to developers, creative applications ran inside chat, coding models '
  'were designed to sustain long tasks, and a shared format for agent skills became an open standard. The model race tightened as the year closed: '
  'OpenAI declared a “code red” over Google’s lead and answered within 10 days with GPT-5.2, while Google, DeepSeek, Z.ai and Nvidia released models '
  'of their own.'),
 ('Accountability', ' took several forms. Washington moved against state AI laws, Britain published its first public account of frontier-model testing, '
  'and China proposed rules for AI that imitates human companionship. Agreements set the terms of access to technology, characters, staff and capital, and '
  'Geoffrey Hinton ended the year more worried than when he left Google. The final days added research on forecasting, retrieval and product search.'),
])

C = 'Claude Sonnet 4.5'; CP5 = 'Copilot Smart (GPT-5)'; CP = 'Copilot Smart'; G3T = 'Gemini 3 Pro Thinking'; GF = 'Gemini Fast'; G3F = 'Gemini 3 Fast'
K = 'Kimi K2'; Q = 'Qwen3-Next-80B-A3B'; K41 = 'Grok 4.1'; CHATGPT = 'ChatGPT'

WEEKS = [
 (49, 'December 1–7', 'Original post published December 7, 2025', [
  ('DeepSeek releases V3.2 and a specialized reasoning variant', 'December 1',
   ["DeepSeek released V3.2 through its app, website and API, alongside the reasoning-focused V3.2-Speciale. The standard version combined reasoning "
    "with tool use. Speciale was initially offered through a temporary API endpoint and did not support tool calls.{v32}",
    "The pair separated two uses: a model that spends more computation on difficult reasoning, and one built to act through tools."],
   [C], ['2025-W49-L3-5']),
  ('Apple reorganizes its AI leadership', 'December 1',
   ["Apple announced that John Giannandrea would step down as senior vice president for machine learning and AI strategy, serve as an adviser and retire "
    "in spring 2026. Amar Subramanya joined as vice president of AI, reporting to Craig Federighi, with responsibility for foundation models, "
    "machine-learning research, and AI safety and evaluation.{apple}",
    "Other parts of Giannandrea’s organization moved to Sabih Khan and Eddy Cue, placing Apple’s core AI work under its software leadership."],
   [CP5], ['2025-W49-L5-3']),
  ('Runway introduces Gen-4.5 video generation', 'December 1',
   ["Runway introduced Gen-4.5, a video-generation model designed to follow detailed prompts and maintain motion and visual detail across a scene. Its "
    "demonstrations covered camera movement, complex compositions and interactions between objects.{gen45}",
    "Runway also listed the model’s known failures, among them events shown in the wrong causal order and objects that disappear."],
   [CP5], ['2025-W49-L5-2']),
  ('OpenAI declares a “code red” to improve ChatGPT', 'Reported December 1–2',
   ["Sam Altman told staff in a memo on December 1 that OpenAI was declaring a “code red” to improve ChatGPT, The *Wall Street Journal* and *The "
    "Information* reported. Priorities included speed, reliability, a wider range of answers and personalization; advertising, health and shopping "
    "agents and a personal assistant were delayed, and Altman encouraged temporary transfers to the ChatGPT effort.{codered}",
    "The memo followed reports that Google’s Gemini 3 had overtaken ChatGPT on industry benchmarks. OpenAI released GPT-5.2 10 days later."],
   [C, CP5, G3T], ['2025-W49-L3-2', '2025-W49-L5-1', '2025-W49-L6-2']),
  ('Gemini 3 Deep Think reaches Ultra subscribers', 'December 4',
   ["Google began rolling out Gemini 3 Deep Think to Google AI Ultra subscribers in the Gemini app. The mode explored multiple hypotheses in parallel for "
    "difficult mathematics, science and logic problems. Google reported 41.0 percent on Humanity’s Last Exam without tools and 45.1 percent on ARC-AGI-2 with code "
    "execution.{deepthink}",
    "The mode had been announced with Gemini 3 in November and held back for safety testing before this release."],
   [C, 'Copilot Smart (week 50)'], ['2025-W49-L3-1', '2025-W50-L1-3']),
  ('Meta acquires AI-wearables company Limitless', 'December 5',
   ["Meta acquired Limitless, the company behind a pendant that recorded and transcribed conversations. Financial terms were not disclosed. The "
    "transaction added a team working on wearable AI to Meta’s consumer-hardware efforts.{limitless}",
    "The purchase extended Meta’s bet on AI built into everyday devices beyond its smart glasses."],
   [C], ['2025-W49-L3-4']),
 ]),
 (50, 'December 8–14', 'Original post published December 14, 2025', [
  ('Accenture and Anthropic plan a larger enterprise practice', 'December 9',
   ["Accenture and Anthropic announced a multi-year expansion of their partnership and a dedicated business group built around Claude. About 30,000 "
    "Accenture professionals were to receive training. The companies also planned tools to help clients measure value from AI in software engineering "
    "and develop applications for regulated industries.{accenture}",
    "The agreement addressed the organizational work deployment requires: training, integration and measurement."],
   [GF], ['2025-W50-L3-3']),
  ('Adobe brings editing tools into ChatGPT', 'December 10',
   ["Adobe launched Photoshop, Express and Acrobat apps within ChatGPT. Users could request image changes, create designs and work with PDF documents "
    "through conversation, then use controls such as sliders to refine an edit.{adobe}",
    "The integration made chat an entry point to established creative tools, combining spoken instructions with direct controls."],
   [K], ['2025-W50-L5-5']),
  ('A 3D chip from a US foundry speeds AI workloads', 'December 10',
   ["Engineers from Stanford, Carnegie Mellon, the University of Pennsylvania and MIT, working with SkyWater Technology, reported a prototype monolithic "
    "3D chip that stacks memory and computing layers linked by dense vertical wiring. Built entirely at SkyWater’s Minnesota foundry, it outperformed "
    "comparable flat chips by about four times in hardware tests; simulations of taller designs showed up to 12 times. The work was presented at IEDM.{chip3d}",
    "The team described it as the first such chip with clear performance gains made in a commercial foundry, showing the design could leave the laboratory."],
   [CP], ['2025-W50-L1-5']),
  ('GPT-5.2 expands the model family for professional work', 'December 11',
   ["OpenAI released GPT-5.2, with Instant, Thinking and Pro variants. Rollout in ChatGPT began with paid plans, while API access opened to developers. "
    "The company presented improvements in handling long documents, using tools, coding and producing work such as spreadsheets and presentations.{gpt52}",
    "The release, less than a month after GPT-5.1, was OpenAI’s answer to the competition that had prompted its “code red.”"],
   [CP, GF, K], ['2025-W50-L1-2', '2025-W50-L3-2', '2025-W50-L5-1']),
  ('A federal order targets conflicting state AI rules', 'December 11',
   ["President Donald Trump signed Executive Order 14365, directing the Justice Department to establish a task force to challenge state AI laws "
    "considered inconsistent with federal policy. It also called for a legislative recommendation for a national AI framework.{eo}",
    "The order took up the dispute over state AI laws that had run since May, when a proposed 10-year moratorium drew opposition from 40 state "
    "attorneys general."],
   [CP, GF, 'Gemini 3 Fast (weeks 51, 52)'], ['2025-W50-L1-1', '2025-W50-L3-1', '2025-W51-L3-4', '2025-W52-L3-1']),
  ('Google opens Deep Research to developers', 'December 11',
   ["Google released a Gemini 3 Pro-based Deep Research agent through its new Interactions API. The agent planned searches, read results and searched "
    "again to fill gaps before producing a report, and developers could embed the process in their own applications. Google also released "
    "DeepSearchQA, a benchmark for multi-step web research.{deepres}",
    "Research became a component developers could build on, not only a feature of a consumer app."],
   [K], ['2025-W50-L5-3']),
  ('Runway announces interactive world models', 'December 11',
   ["Runway announced GWM-1, a family of models built on Gen-4.5 that generate video frame by frame in response to actions. Separate variants addressed "
    "explorable environments, conversational characters and robotic manipulation. Inputs could include camera movements, robot commands or audio.{gwm}",
    "The release took video generation toward interactive simulation, a direction Google DeepMind had shown with Genie 3 in August."],
   [K], ['2025-W50-L5-4']),
 ]),
 (51, 'December 15–21', 'Original post published December 21, 2025', [
  ('Disney and OpenAI agree to bring Disney characters to Sora', 'Background: December 11; selected December 21; restored by the editor, October 2026',
   ["Disney and OpenAI announced a three-year agreement letting Sora users generate short videos with more than 200 characters from Disney, Marvel, Pixar "
    "and Star Wars; ChatGPT users could also create images of them. The license excluded the likenesses and voices of human performers. Disney also "
    "agreed to make a $1 billion equity investment in OpenAI. The agreement remained subject to definitive agreements and closing conditions.{disney1}{disney2}",
    "It was the first major licensing partnership for Sora, from a studio that had joined Universal in suing the image generator Midjourney in June.",
    "Gemini 3 Fast recommended this agreement for December 15–21, describing implementation details on December 17, and repeated it on December 28. "
    "The agreement was announced on December 11, the week before; no later development was confirmed. The editor restored it as an important story of the month."],
   [G3F + ' (weeks 51, 52)'], ['2025-W51-L3-2', '2025-W52-L3-4']),
  ('Nvidia acquires Slurm developer SchedMD', 'December 15',
   ["Nvidia acquired SchedMD, the developer of the Slurm workload manager used to queue jobs and allocate computing resources on clusters. Nvidia said it "
    "would continue developing and distributing Slurm as open-source, vendor-neutral software.{schedmd}",
    "The deal put widely used open-source cluster-scheduling software under the leading AI chipmaker, with a pledge to keep it vendor-neutral."],
   [CHATGPT], ['2025-W51-L1-4']),
  ('Nvidia releases its Nemotron 3 open models', 'December 15',
   ["Nvidia introduced the Nemotron 3 family of open mixture-of-experts models in three sizes, from Nano, with about 30 billion parameters, to Ultra, with "
    "about 500 billion. Nano was available at once; Super and Ultra were expected in the first half of 2026. Nvidia also released three trillion tokens of "
    "training data and reinforcement-learning tools.{nemotron}",
    "Nvidia now supplied open models and training data for building agents as well as the chips that run them."],
   [G3F], ['2025-W51-L3-5']),
  ('ChatGPT Images adds a new editing model', 'December 16',
   ["OpenAI began rolling out a new ChatGPT Images model and made it available through the API as GPT Image 1.5. The release focused on following editing "
    "instructions while preserving details such as composition, lighting and appearance, and introduced a dedicated Images experience in ChatGPT.{images}",
    "Preserving what should stay unchanged reduces the need to regenerate a whole image for a small correction."],
   [CHATGPT], ['2025-W51-L1-1']),
  ('Gemini 3 Flash broadens access to the model family', 'December 17',
   ["Google released Gemini 3 Flash, a model designed to balance reasoning capability, response speed and cost. Rollout covered the Gemini app, AI Mode in "
    "Search and developer services, including the Gemini API and Vertex AI.{flash}",
    "The release brought a cheaper member of the Gemini 3 family into Google’s most widely used products."],
   [G3F, Q], ['2025-W51-L3-1', '2025-W51-L5-2']),
  ('Agent Skills becomes an open format', 'December 18',
   ["Anthropic published Agent Skills as an open standard for cross-platform portability. A skill packages instructions, scripts and resources that an agent "
    "can load when needed. The December update extended an approach Anthropic had introduced in October.{skills}",
    "A shared format let procedural knowledge travel between compatible agent tools."],
   [CHATGPT], ['2025-W51-L1-2']),
  ('GPT-5.2-Codex targets extended software work', 'December 18',
   ["OpenAI released GPT-5.2-Codex through Codex for paid ChatGPT users. The model was adapted for software engineering, with context compaction for "
    "longer work, improvements in Windows environments and stronger performance on large code changes. API access was planned for the following weeks.{codex}",
    "Its cybersecurity capabilities also made access controls and defensive-use safeguards part of the release."],
   [Q, G3F], ['2025-W51-L5-1', '2025-W51-L3-1']),
  ('Genesis Mission adds 24 research collaborators', 'December 18',
   ["The US Department of Energy announced memoranda of understanding with 24 organizations interested in advancing the Genesis Mission, including model "
    "developers, chipmakers and cloud providers. Some had existing projects with the department and its national laboratories; others had responded to a "
    "request for information.{genesis}",
    "The agreements gave the November order its first named industry partners."],
   [CHATGPT], ['2025-W51-L1-3']),
  ('Britain publishes its first Frontier AI Trends Report', 'December 18',
   ["The UK AI Security Institute published its first public overview of frontier-model trends, drawing on two years of testing. It covered cyber "
    "capabilities, assistance in biology and chemistry, autonomous behavior, safeguards and human influence.{aisi}",
    "The report brought government evaluation of successive models into the public record."],
   [G3F], ['2025-W51-L3-4']),
 ]),
 (52, 'December 22–28', 'Original post published December 28, 2025', [
  ('GLM-4.7 adds continuity to coding workflows', 'December 22',
   ["Z.ai released GLM-4.7 for coding, reasoning and tool use. The model could preserve its reasoning across turns in coding-agent workflows, with controls "
    "for enabling or disabling reasoning turn by turn. Model weights and deployment instructions were available through the company’s repository.{glm1}{glm2}",
    "Local deployment gave developers an open alternative to hosted coding models."],
   [CHATGPT], ['2025-W52-L1-2']),
  ('Groq licenses inference technology to Nvidia', 'December 24',
   ["Groq announced a non-exclusive licensing agreement with Nvidia for its inference technology. Founder Jonathan Ross, president Sunny Madra and other "
    "team members were to join Nvidia. Groq said Simon Edwards would become chief executive and GroqCloud would continue operating.{groq}",
    "The arrangement combined access to technology with the movement of staff, a structure Google had used with Windsurf in July."],
   [K41, C], ['2025-W52-L6-4', '2025-W52-L11-1']),
  ('China consults on human-like AI interaction services', 'December 27',
   ["China’s Cyberspace Administration published draft measures for AI services that simulate human personality and communication in emotional "
    "interactions. The proposal addressed emotional manipulation, excessive dependence and harm to users’ mental health, with additional protections "
    "for minors.{cac}",
    "The consultation treated relationships between users and human-like systems as a regulatory concern, as US regulators had begun to do with "
    "companion chatbots in September."],
   [CHATGPT, K41], ['2025-W52-L1-3', '2025-W52-L6-2']),
  ('NHS organizations use AI to forecast emergency demand', 'December 28',
   ["The UK government reported that 50 NHS organizations were using an AI tool to forecast demand in emergency departments. The system combined "
    "historical attendance with information such as weather and seasonal health data to support staffing and capacity planning, and was available to "
    "NHS trusts in England through the Federated Data Platform.{nhs}",
    "The deployment applied forecasting to one of the health service’s hardest winter problems."],
   [CHATGPT, K41], ['2025-W52-L1-1', '2025-W52-L6-1']),
  ('Hinton says AI has progressed faster than he expected', 'December 28',
   ["Geoffrey Hinton told CNN’s *State of the Union* that he was “probably more worried” about AI than when he left Google in 2023: “It’s progressed even "
    "faster than I thought.” He said AI had improved at reasoning and at deceiving people, and predicted it would gain the capability to replace many "
    "jobs in 2026.{hinton}",
    "Hinton estimated that the length of tasks AI could handle was doubling about every seven months, the rate METR had reported in March."],
   [C], ['2025-W52-L11-4']),
 ]),
 (53, 'December 29–31', 'Original post published January 4, 2026; 2025 excerpts only', [
  ('Manus announces that it is joining Meta', 'December 29',
   ["Manus announced that it was joining Meta. The company said its general-purpose agent service would continue operating through its app and website, "
    "with subscriptions maintained and operations remaining in Singapore.{manus}",
    "The agent that had drawn attention in March would now reach Meta’s users and businesses."],
   ['Grok 4.1 Thinking', 'Qwen3-Max'], ['2025-W53-L1-1', '2025-W53-L2-2']),
  ('xAI launches Grok Business and Enterprise', 'December 30',
   ["xAI introduced workplace versions of Grok with shared administration and connections to company information, starting with Google Drive. Grok "
    "Business was offered through self-service signup; Enterprise added custom single sign-on, directory synchronization and advanced audit controls. "
    "xAI said customer data would not be used for training.{grokbiz}",
    "The products moved Grok into organizational workflows, where administration and permissions matter alongside model performance."],
   ['Grok 4.1 Thinking'], ['2025-W53-L1-2']),
  ('SoftBank confirms completion of its OpenAI investment', 'December 31 announcement; final funding December 26',
   ["SoftBank announced that it had invested a final $22.5 billion in OpenAI on December 26. Added to $7.5 billion invested in April, this brought "
    "SoftBank’s contribution to $30 billion. Third-party co-investors supplied $11 billion, for a fully funded total of $41 billion.{softbank}",
    "The announcement closed the funding round SoftBank had agreed to lead in March."],
   ['Qwen3-Max'], ['2025-W53-L2-1']),
  ('OpenForecaster studies open-ended predictions', 'December 31 submission',
   ["Nikhil Chandak and colleagues trained language models on forecasting questions generated from news. Their OpenForesight dataset supported training "
    "of OpenForecaster 8B. The method used an offline news corpus to limit leakage of future information, followed by held-out testing on events from "
    "May to August 2025.{forecast}",
    "The study measured accuracy, calibration and consistency in open-ended predictions about real events."],
   ['Kimi K2'], ['2025-W53-L3-1']),
  ('AdaGReS selects context with less repetition', 'December 31 submission',
   ["Chao Peng and colleagues proposed AdaGReS, a method for selecting retrieved text within a fixed token budget. It balanced each passage’s relevance "
    "to a query against redundancy among the selected passages, using greedy selection and an adaptive calibration of that trade-off.{adagres}",
    "The approach targeted a common weakness of retrieval-augmented generation: top-ranked passages that repeat the same information."],
   ['Kimi K2'], ['2025-W53-L3-2']),
  ('RAIR tests relevance in product search', 'December 31 submission',
   ["Chenji Lu and colleagues introduced RAIR, a Chinese-language benchmark for relevance in e-commerce search. It combined general examples, difficult "
    "long-tail cases and a subset in which visual information mattered, and compared 14 open and closed models under a shared set of relevance rules.{rair}",
    "The benchmark tested whether a model could judge a product against a shopper’s request, including cases that depend on images."],
   ['Kimi K2'], ['2025-W53-L3-5']),
 ]),
]
