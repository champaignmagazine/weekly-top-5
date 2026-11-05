# November 2025 print chapter, v0.2: content (American style).
COVERS = 'Edited from five posts published in November 2025, covering October 27–November 30.'

SOURCES = {
 'qcom1': ('Qualcomm', 'Qualcomm Unveils AI200 and AI250—Redefining Rack-Scale Data Center Inference Performance for the AI Era', 'Company page dated October 28, 2025',
           'https://www.qualcomm.com/news/releases/2025/10/qualcomm-unveils-ai200-and-ai250-redefining-rack-scale-data-cent'),
 'qcom2': ('Qualcomm', 'HUMAIN and QUALCOMM to deploy AI Infrastructure in Saudi Arabia For Global Inferencing', 'October 27, 2025',
           'https://www.qualcomm.com/news/releases/2025/10/humain-and-qualcomm-to-deploy-ai-infrastructure-in-saudi-arabia-'),
 'doe': ('US Department of Energy', 'Energy Department Announces New Partnership with NVIDIA and Oracle to Build Largest DOE AI Supercomputer', 'October 28, 2025',
         'https://www.energy.gov/articles/energy-department-announces-new-partnership-nvidia-and-oracle-build-largest-doe-ai'),
 'nvqlink': ('Nvidia', 'NVIDIA Introduces NVQLink — Connecting Quantum and GPU Computing for 17 Quantum Builders and Nine Scientific Labs', 'October 28, 2025',
             'https://www.globenewswire.com/news-release/2025/10/28/3175764/0/en/nvidia-introduces-nvqlink-connecting-quantum-and-gpu-computing-for-17-quantum-builders-and-nine-scientific-labs.html'),
 'intro': ('Anthropic', 'Signs of introspection in large language models', 'October 29, 2025', 'https://www.anthropic.com/research/introspection'),
 'five': ('Bloomberg News, via Advisor Perspectives', 'Nvidia Becomes First $5 Trillion Firm as AI Rally Picks Up Steam', 'October 29, 2025',
          'https://www.advisorperspectives.com/articles/2025/10/29/nvidia-first-5-trillion-firm-ai-rally-picks-up'),
 'umg': ('Universal Music Group', 'Universal Music Group and Stability AI Announce Strategic Alliance to Co-Develop Professional AI Music Creation Tools', 'October 30, 2025',
         'https://www.universalmusic.com/universal-music-group-and-stability-ai-announce-strategic-alliance-to-co-develop-professional-ai-music-creation-tools/'),
 'aardvark': ('OpenAI', "Introducing Aardvark: OpenAI's agentic security researcher", 'October 30, 2025; live page includes a March 2026 update',
              'https://openai.com/index/introducing-aardvark/'),
 'aws': ('Amazon', 'AWS and OpenAI announce multi-year strategic partnership', 'November 3, 2025',
         'https://www.aboutamazon.com/news/aws/aws-open-ai-workloads-compute-infrastructure'),
 'uae': ('Reuters, via Business Standard', 'Microsoft plans $15 bn UAE investment, secures US Nvidia chip licence', 'November 3, 2025',
         'https://www.business-standard.com/world-news/microsoft-plans-15-bn-uae-investment-secures-us-nvidia-chip-licence-125110301402_1.html'),
 'apple': ('AppleInsider', 'Apple considers paying $1B per year to use Google Gemini in Siri', 'November 5, 2025',
           'https://appleinsider.com/articles/25/11/05/apple-considers-paying-1b-per-year-to-use-google-gemini-in-siri'),
 'china': ('eWeek, citing Reuters', 'China Blocks Foreign AI Chips in State Data Centers', 'November 6, 2025 (Reuters report of November 5)',
           'https://www.eweek.com/news/china-blocks-foreign-ai-chips/'),
 'snap': ('TechRepublic', 'Snap Strikes $400M Deal with Perplexity', 'November 6, 2025', 'https://www.techrepublic.com/article/news-snap-perplexity-400m-deal/'),
 'kimi1': ('Moonshot AI', 'Kimi-K2-Thinking model card', 'November 2025 release', 'https://huggingface.co/moonshotai/Kimi-K2-Thinking'),
 'kimi2': ('Moonshot AI', 'Kimi CLI changelog: version 0.48 adds Kimi K2 thinking mode', 'November 6, 2025 entry',
           'https://github.com/MoonshotAI/kimi-cli/blob/main/CHANGELOG.md'),
 'ironwood': ('Google Cloud', 'Announcing Ironwood TPUs General Availability and new Axion VMs to power the age of inference', 'November 6, 2025',
              'https://cloud.google.com/blog/products/compute/ironwood-tpus-and-new-axion-based-vms-for-your-ai-workloads/'),
 'teen': ('OpenAI', 'Introducing the Teen Safety Blueprint', 'November 6, 2025', 'https://openai.com/index/introducing-the-teen-safety-blueprint/'),
 'meta600': ('SiliconANGLE', 'Meta announces plans to spend $600B in the US over three years', 'November 7, 2025',
             'https://siliconangle.com/2025/11/07/meta-announces-plans-spend-600b-us-three-years/'),
 'asr': ('Meta', 'Omnilingual ASR: Advancing Automatic Speech Recognition for 1,600+ Languages', 'November 10, 2025',
         'https://ai.meta.com/blog/omnilingual-asr-advancing-automatic-speech-recognition/'),
 'jhu': ('Johns Hopkins Medicine', 'Johns Hopkins Researchers Launch Projects Under the Cancer AI Alliance', 'November 10, 2025',
         'https://www.hopkinsmedicine.org/news/newsroom/news-releases/2025/11/johns-hopkins-researchers-launch-projects-under-the-cancer-ai-alliance'),
 'lecun': ('Fortune', "Who is Yann LeCun, Meta's chief AI scientist", 'November 11, 2025 (citing the Financial Times)',
           'https://fortune.com/2025/11/11/who-is-yann-lecun-career-meta-ai-chief-scientist-nyu-turing/'),
 'gpt51': ('OpenAI', 'GPT-5.1: A smarter, more conversational ChatGPT', 'November 12, 2025', 'https://openai.com/index/gpt-5-1/'),
 'ant50': ('Anthropic', 'Anthropic invests $50 billion in American AI infrastructure', 'November 12, 2025',
           'https://www.anthropic.com/news/anthropic-invests-50-billion-in-american-ai-infrastructure'),
 'mlperf': ('Nvidia', 'NVIDIA Wins Every MLPerf Training v5.1 Benchmark', 'November 12, 2025', 'https://blogs.nvidia.com/blog/mlperf-training-benchmark-blackwell-ultra/'),
 'sparse': ('OpenAI', 'Understanding neural networks through sparse circuits', 'November 13, 2025',
            'https://openai.com/index/understanding-neural-networks-through-sparse-circuits/'),
 'spy': ('Anthropic', 'Disrupting the first reported AI-orchestrated cyber espionage campaign', 'November 13, 2025; edited November 14',
         'https://www.anthropic.com/news/disrupting-AI-espionage'),
 'galaxy': ('ScienceDaily, from RIKEN', 'AI creates the first 100-billion-star Milky Way simulation', 'November 16, 2025',
            'https://sciencedaily.com/releases/2025/11/251116105515.htm'),
 'grok41': ('xAI', 'Grok 4.1', 'November 17, 2025', 'https://x.ai/news/grok-4-1'),
 'gemini3': ('Google', 'A new era of intelligence with Gemini 3', 'November 18, 2025', 'https://blog.google/products-and-platforms/products/gemini/gemini-3/'),
 'antigrav': ('Google Antigravity Team', 'Introducing Google Antigravity, a new era in AI-assisted software development', 'November 18, 2025',
              'https://antigravity.google/blog/introducing-google-antigravity/'),
 'msant': ('Microsoft', 'Microsoft, NVIDIA and Anthropic announce strategic partnerships', 'November 18, 2025',
           'https://blogs.microsoft.com/blog/2025/11/18/microsoft-nvidia-and-anthropic-announce-strategic-partnerships/'),
 'codex': ('OpenAI', 'Building more with GPT-5.1-Codex-Max', 'November 19, 2025', 'https://openai.com/index/gpt-5-1-codex-max/'),
 'teachers': ('OpenAI', 'ChatGPT for Teachers', 'November 19, 2025', 'https://openai.com/index/chatgpt-for-teachers/'),
 'nvq3': ('Nvidia', 'NVIDIA Announces Financial Results for Third Quarter Fiscal 2026', 'November 19, 2025',
          'https://www.sec.gov/Archives/edgar/data/1045810/000104581025000228/q3fy26pr.htm'),
 'olmo': ('Ai2', 'Olmo 3: Charting a path through the model flow to lead open-source AI', 'November 20, 2025; original post below a December update',
          'https://allenai.org/blog/olmo3'),
 'foxconn': ('OpenAI', 'OpenAI and Foxconn collaborate to strengthen U.S. manufacturing across the AI supply chain', 'November 20, 2025',
             'https://openai.com/index/openai-and-foxconn-collaborate/'),
 'opus': ('Anthropic', 'Introducing Claude Opus 4.5', 'November 24, 2025', 'https://www.anthropic.com/news/claude-opus-4-5'),
 'genesis': ('The White House', 'Launching the Genesis Mission, Executive Order 14363', 'November 24, 2025',
             'https://www.whitehouse.gov/presidential-actions/2025/11/launching-the-genesis-mission/'),
 'aws50': ('Amazon', 'Amazon to invest up to $50 billion to expand AI and supercomputing infrastructure for US government agencies', 'November 24, 2025',
           'https://www.aboutamazon.com/news/company-news/amazon-ai-investment-us-federal-agencies'),
 'fraud': ('Office of Rep. Ted W. Lieu', 'Reps. Lieu and Dunn Introduce Bill to Enhance Penalties for Using AI to Commit Fraud', 'November 25, 2025',
           'https://lieu.house.gov/media-center/press-releases/reps-lieu-and-dunn-introduce-bill-enhance-penalties-using-ai-commit'),
 'uspto1': ('USPTO', 'Revised inventorship guidance for AI-assisted inventions', 'November 26, 2025 announcement',
            'https://www.uspto.gov/subscription-center/2025/revised-inventorship-guidance-ai-assisted-inventions'),
 'uspto2': ('Federal Register', 'Revised Inventorship Guidance for AI-Assisted Inventions, 90 FR 54636–54637', 'November 28, 2025',
            'https://www.govinfo.gov/content/pkg/FR-2025-11-28/html/2025-21457.htm'),
 'poem1': ('The Guardian, via inkl', "AI's safety features can be circumvented with poetry, research finds", 'November 30, 2025',
           'https://www.inkl.com/news/ai-s-safety-features-can-be-circumvented-with-poetry-research-finds'),
 'poem2': ('Piercosma Bisconti and colleagues', 'Adversarial Poetry as a Universal Single-Turn Jailbreak Mechanism in Large Language Models',
           'November 19, 2025; arXiv version 1', 'https://arxiv.org/abs/2511.15304v1'),
}

THEME = ('Capability, Infrastructure', [
 ('Capability', ' advanced on several fronts at once. Google, OpenAI, Anthropic and xAI released new frontier models within two weeks; coding agents '
  'learned to sustain longer tasks; open models from Moonshot and Ai2 exposed more of how such systems are built; and speech recognition reached more '
  'than 1,600 languages. Research asked how much of a model can be inspected, from injected concepts to sparse circuits, while security reports and a '
  'study of poetic prompts showed how capable systems could be misused or misled.'),
 ('Infrastructure', ' set the scale of the month. Agreements for chips, cloud capacity and data centers ran into the tens of billions of dollars, '
  'Nvidia became the first company valued at $5 trillion and reported record data center revenue, and governments shaped where the hardware could go, '
  'from US export licenses for the Gulf to reported Chinese rules for state-funded facilities. Washington also set out a national program for '
  'AI-assisted science and revised how patent law treats AI-assisted invention.'),
])

K = 'Grok (Expert mode)'; KE = 'Grok Expert'; K41 = 'Grok 4.1'; C = 'Claude Sonnet 4.5'; GP = 'Gemini 2.5 Pro'; GC = 'Gemini 2.5 Pro and Copilot Smart'
G3 = 'Gemini 3 Pro'; G3T = 'Gemini 3 Thinking'; G51 = 'GPT-5.1'; DS = 'DeepSeek-V3.2'

WEEKS = [
 (44, 'October 27–November 2', 'Original post published November 2, 2025', [
  ('Qualcomm announces accelerators for data center inference', 'October 27–28',
   ["Qualcomm announced AI200 and AI250 accelerator cards and racks for running AI models in data centers, with commercial availability planned for 2026 "
    "and 2027 respectively. A related agreement with HUMAIN targeted 200 megawatts of Qualcomm-based infrastructure in Saudi Arabia, starting in 2026.{qcom1}{qcom2}",
    "The roadmap took the company best known for smartphone chips into rack-scale inference, the part of the market where models are run rather than trained."],
   [K], ['2025-W44-L6-2']),
  ('Argonne plans two new AI supercomputers', 'October 28',
   ["The US Department of Energy, Argonne National Laboratory, Nvidia and Oracle announced plans for two systems at Argonne. Solstice would use 100,000 "
    "Nvidia Blackwell GPUs; Equinox would use 10,000 and was expected in 2026. Oracle would also provide immediate access to existing AI computing resources.{doe}",
    "The agreement paired near-term cloud access for researchers with the construction of dedicated scientific machines."],
   [C], ['2025-W44-L4-1']),
  ('NVQLink connects quantum processors to GPU supercomputers', 'October 28',
   ["At its GTC conference in Washington, D.C., Nvidia introduced NVQLink, an open system architecture for coupling GPU computing with quantum processors. "
    "It supported 17 quantum-processor builders, five controller builders and nine US national laboratories, and was programmed through Nvidia’s CUDA-Q "
    "platform.{nvqlink}",
    "The link targeted quantum error correction, which needs fast classical computation alongside error-prone qubits; Jensen Huang called it “the Rosetta "
    "Stone connecting quantum and classical supercomputers.”"],
   [K], ['2025-W44-L6-1']),
  ('Experiments test whether models can detect internal changes', 'October 29',
   ["Anthropic tested whether Claude models could identify concepts injected into their internal activations. Under its best injection protocol, Claude "
    "Opus 4.1 recognized such changes about 20 percent of the time. Detection depended on injection strength, and failures included confusion and incorrect reports.{intro}",
    "The experiments gave limited, unreliable evidence that the reports of the most advanced Claude models about themselves can sometimes "
    "reflect their internal states."],
   [K], ['2025-W44-L6-3']),
  ('Nvidia becomes the first $5 trillion company', 'October 29',
   ["Nvidia’s market value passed $5 trillion in morning trading, about four months after it first crossed $4 trillion. The rise followed new chip-supply "
    "partnerships announced by Jensen Huang, his statement that the company’s latest chips were on track for half a trillion dollars in revenue, and hopes "
    "for US–China talks on chip exports.{five}",
    "The valuation put a single supplier of AI hardware at the center of the market’s expectations for the technology."],
   [GP], ['2025-W44-L1-1']),
  ('Universal Music and Stability AI plan music-creation tools', 'October 30',
   ["Universal Music Group and Stability AI announced a collaboration to develop professional music-creation tools. The companies planned to involve artists, "
    "producers and songwriters in design and testing, with the stated aim of producing tools based on licensed training data.{umg}",
    "The agreement brought one of the largest rights holders into the development of AI tools for musicians."],
   [GP], ['2025-W44-L1-3']),
  ('Aardvark enters private testing for software security', 'October 30',
   ["OpenAI introduced Aardvark, a GPT-5-based security agent, in private beta. It examined code repositories and changes, tested suspected vulnerabilities "
    "in an isolated environment, and proposed patches through Codex for human review.{aardvark}",
    "The workflow connected finding a possible defect with testing whether it could be exploited and preparing a repair, with an engineer reviewing each "
    "proposed change."],
   [GP], ['2025-W44-L1-5']),
 ]),
 (45, 'November 3–9', 'Original post published November 9, 2025', [
  ('OpenAI signs a $38 billion AWS computing agreement', 'November 3',
   ["Amazon Web Services and OpenAI announced a $38 billion agreement extending over seven years. OpenAI would begin using AWS computing resources "
    "immediately, with the planned capacity targeted for deployment by the end of 2026. The infrastructure would support both model training and inference.{aws}",
    "The agreement added another major supplier to OpenAI’s computing arrangements, which had previously centered on Microsoft."],
   [GC, C, KE], ['2025-W45-L1-1', '2025-W45-L2-4', '2025-W45-L4-3']),
  ('Microsoft gains licenses to ship advanced Nvidia chips to the UAE', 'November 3',
   ["Microsoft said it had secured US export licenses in September to ship the equivalent of 60,400 A100 chips, in the form of Nvidia’s more advanced GB300 "
    "GPUs, to its data centers in the United Arab Emirates; shipments were expected within months. Brad Smith also set out $15.2 billion in Microsoft "
    "investment in the UAE from 2023 through 2029, most of it for AI data centers.{uae}",
    "The licenses showed how far access to frontier chips now ran through government approval."],
   [GC], ['2025-W45-L1-5']),
  ('Apple is reported to near a deal to use Gemini for Siri', 'Reported November 5',
   ["Bloomberg reported that Apple was finalizing an arrangement to pay Google about $1 billion a year for a custom 1.2-trillion-parameter Gemini model. "
    "The model would handle Siri’s summarization and planning functions and run on Apple’s own Private Cloud Compute servers, in a revamp planned for 2026.{apple}",
    "The report described Apple turning to a competitor’s model to rebuild its assistant."],
   [GC], ['2025-W45-L1-2']),
  ('China is reported to bar foreign AI chips from state-funded data centers', 'Reported November 5',
   ["Reuters reported, citing two sources, that Chinese regulators had told new data center projects receiving state funds to use only domestically made "
    "AI chips. Projects less than 30 percent complete were reportedly told to remove foreign chips or cancel planned purchases; those near completion would be "
    "reviewed case by case. The guidance had not been publicly announced.{china}",
    "As reported, the rule would close much of China’s data center market to Nvidia, AMD and Intel and steer demand to Chinese chipmakers."],
   [KE], ['2025-W45-L4-4']),
  ('Kimi K2 Thinking combines reasoning with tool use', 'November 6',
   ["Moonshot AI released Kimi K2 Thinking with downloadable weights and a modified MIT license. The mixture-of-experts model used one trillion total "
    "parameters, activating 32 billion per token. It combined extended reasoning with tool calls and supported a 256,000-token context window.{kimi1}{kimi2}",
    "The release gave developers a large reasoning model they could host and adapt themselves, with Moonshot’s published results "
    "emphasizing agentic search and coding tasks."],
   [C], ['2025-W45-L2-1']),
  ('Google prepares Ironwood TPUs for general availability', 'November 6',
   ["Google said Ironwood, its seventh-generation Tensor Processing Unit, would be generally available in the coming weeks. It reported more than four times "
    "the per-chip performance of its predecessor, Trillium, for both training and inference, and superpods of up to 9,216 chips sharing 1.77 petabytes of "
    "high-bandwidth memory. New Arm-based Axion virtual machines entered preview.{ironwood}",
    "Anthropic, which planned to use up to one million TPUs, was named among the customers, giving Google’s in-house chips a prominent outside buyer."],
   [GC], ['2025-W45-L1-3']),
  ('Perplexity agrees to pay Snap $400 million for search in Snapchat', 'Reported November 6',
   ["Announced just after Snap’s third-quarter results, the agreement had Perplexity paying Snap $400 million in cash and equity to provide AI search inside "
    "Snapchat’s chat interface, beginning in early 2026.{snap}",
    "The deal reversed the usual direction of payment: an AI company paid a social platform for access to its users."],
   [C], ['2025-W45-L2-HM2']),
  ('OpenAI publishes a framework for teen safety', 'November 6',
   ["OpenAI published its Teen Safety Blueprint, proposing age-appropriate design, product safeguards, and continuing research and evaluation. The "
    "announcement referred to parental controls already introduced and an age-prediction system still under development.{teen}",
    "The document set out a provider’s proposed principles for protecting younger users, as companion chatbots and teenage use drew scrutiny from "
    "regulators."],
   [C], ['2025-W45-L2-2']),
  ('Meta pledges $600 billion for US infrastructure', 'November 7',
   ["Meta said it would invest $600 billion in the United States over three years as part of its AI push, including new AI data centers, supporting "
    "infrastructure such as transmission lines, and workforce expansion. The pledge followed recent financing for its Hyperion campus in Louisiana.{meta600}",
    "The figure placed Meta among the largest planned spenders on AI computing in the country."],
   [KE], ['2025-W45-L4-5']),
 ]),
 (46, 'November 10–16', 'Original post published November 16, 2025', [
  ('Meta expands speech recognition to more than 1,600 languages', 'November 10',
   ["Meta released Omnilingual ASR, a family of open speech-recognition models covering more than 1,600 languages. It also released a corpus of transcribed "
    "speech in 350 underserved languages and tools intended to help communities extend coverage using their own recordings.{asr}",
    "The release widened the range of languages available for transcription research and applications, including hundreds never before supported."],
   [G51, GP, KE, DS], ['2025-W46-L1-6', '2025-W46-L3-3', '2025-W46-L4-3', '2025-W46-L5-6']),
  ('Johns Hopkins announces two cancer AI research projects', 'November 10',
   ["Johns Hopkins researchers announced two projects within the Cancer AI Alliance. One adapted a language model to structured health records to study "
    "patient trajectories. The other used data from multiple centers to investigate rare brain cancers. The alliance’s federated approach allowed "
    "participating institutions to keep their data locally.{jhu}",
    "The projects addressed both research questions and the practical difficulty of working across hospitals that cannot pool patient data."],
   [G51], ['2025-W46-L1-2']),
  ('Yann LeCun is reported to plan a departure from Meta', 'Reported November 11',
   ["The *Financial Times* reported that Yann LeCun, Meta’s chief AI scientist and founder of its FAIR research lab, had told colleagues he planned to leave "
    "within months to start a company building “world models” that learn from video and spatial data.{lecun}",
    "The report came months after Meta reorganized its AI work under Superintelligence Labs and shifted its emphasis toward rapid product development."],
   [G51], ['2025-W46-L1-5']),
  ('GPT-5.1 updates reasoning and conversational controls', 'November 12',
   ["OpenAI began rolling out GPT-5.1 Instant and Thinking in ChatGPT, starting with paid users. Instant gained adaptive reasoning, while Thinking varied "
    "its reasoning time more closely with task difficulty. The release also expanded controls over response tone and style.{gpt51}",
    "The update treated communication and response timing as parts of model usability, reserving more reasoning for difficult tasks."],
   [G51, GP, KE], ['2025-W46-L1-1', '2025-W46-L3-5', '2025-W46-L4-2']),
  ('Anthropic plans $50 billion in US computing infrastructure', 'November 12',
   ["Anthropic announced a $50 billion investment program for American computing infrastructure, including data centers built with Fluidstack in Texas "
    "and New York. The company said sites would begin coming online during 2026, with further locations planned.{ant50}",
    "The program tied Anthropic’s future model development to construction and power supply in the United States."],
   [KE], ['2025-W46-L4-5']),
  ('Nvidia sweeps MLPerf Training v5.1', 'November 12',
   ["Nvidia reported the fastest time to train on all seven tests in the MLPerf Training v5.1 benchmarks, and was the only company to submit results on every "
    "test. Its GB300 NVL72 system, based on Blackwell Ultra, made its debut, and Nvidia reported a 10-minute time to the training target "
    "on the Llama 3.1 405B benchmark, using more than 5,000 Blackwell GPUs and FP4 precision for the first time in the benchmark’s history.{mlperf}",
    "The results gave an industry-standard measure of how quickly the newest systems could train large models."],
   [KE], ['2025-W46-L4-4']),
  ('Sparse networks make some model computations easier to inspect', 'November 13',
   ["OpenAI reported experiments with language models trained so that most connections had zero weight. For simple tasks, researchers could isolate small "
    "circuits that still performed the required computation, such as matching opening and closing quotation marks in code.{sparse}",
    "The work explored designing small experimental models for interpretability from the start, as a possible route toward understanding larger ones."],
   [G51], ['2025-W46-L1-7']),
  ('Anthropic reports misuse of Claude Code in an espionage campaign', 'November 13',
   ["Anthropic reported detecting an espionage campaign in September that used Claude Code to attempt intrusions into roughly 30 organizations. The "
    "company said a small number succeeded, and that it banned accounts and notified affected parties. It attributed the campaign to a Chinese "
    "state-sponsored group.{spy}",
    "According to Anthropic’s investigation, the attackers used an AI agent to carry out most of the operation’s steps, with people intervening at a "
    "few decision points."],
   [DS], ['2025-W46-L5-1']),
  ('AI helps simulate the Milky Way star by star', 'November 16',
   ["Researchers led by Keiya Hirashima at RIKEN, with the University of Tokyo and Universitat de Barcelona, simulated a model of the Milky Way with more "
    "than 100 billion individual stars. A deep-learning model trained on high-resolution supernova simulations predicted how gas spreads after each "
    "explosion; simulating one million years took 2.78 hours, against an estimated 315 hours by conventional methods. The work was to be presented at the SC ’25 supercomputing conference, held November 16–21.{galaxy}",
    "The surrogate let a physics simulation skip its most expensive small-scale calculations."],
   [GP], ['2025-W46-L3-1']),
 ]),
 (47, 'November 17–23', 'Original post published November 23, 2025', [
  ('Grok 4.1 emphasizes conversational behavior', 'November 17',
   ["xAI released Grok 4.1 across its web and mobile services after a limited rollout earlier in November. The company emphasized conversational style, "
    "creative writing and responses to emotional context, alongside work to reduce factual errors.{grok41}",
    "The release made interaction quality a prominent part of model competition, measured through preference and role-play evaluations."],
   [K41], ['2025-W47-L3-1']),
  ('Gemini 3 Pro enters preview across Google products', 'November 18',
   ["Google introduced Gemini 3 Pro in preview, bringing it to the Gemini app, developer platforms and selected Search experiences on the day of release. "
    "The model combined reasoning, multimodal input and coding capabilities. An enhanced Deep Think mode was being evaluated by safety testers before "
    "release to Ultra subscribers.{gemini3}",
    "The launch connected a new model generation to several of Google’s established products at once."],
   [G3], ['2025-W47-L1-1']),
  ('Antigravity brings coding agents into a shared workspace', 'November 18',
   ["Google introduced Antigravity in public preview for macOS, Windows and Linux. The development environment combined a code editor with a separate view "
    "for managing agents. Agents could work through the editor, terminal and browser, producing plans, screenshots and walkthroughs for users to inspect.{antigrav}",
    "The design shifted attention from individual code suggestions to supervising tasks, giving developers work products to check and comment on."],
   [G51, K41], ['2025-W47-L2-4', '2025-W47-L4-1']),
  ('Anthropic expands its Microsoft and Nvidia partnerships', 'November 18',
   ["Anthropic committed to purchase $30 billion of Azure computing capacity, with additional capacity arrangements planned. Nvidia and Microsoft committed "
    "to invest up to $10 billion and $5 billion respectively in Anthropic. Claude models became available in Microsoft Foundry, "
    "and Microsoft committed to continuing access across its Copilot family.{msant}",
    "The agreements linked investment, computing supply and model distribution, and made Claude available on all three major US cloud platforms."],
   [G3, G51, K41], ['2025-W47-L1-2', '2025-W47-L2-2', '2025-W47-L6-1']),
  ('Codex-Max is designed for longer software tasks', 'November 19',
   ["OpenAI released GPT-5.1-Codex-Max in Codex. The coding model was trained to continue work across multiple context windows using compaction, which "
    "retained relevant information as a task progressed. It was available through Codex’s command-line, editor, cloud and code-review interfaces; API access "
    "was planned.{codex}",
    "The release addressed continuity during extended software work, letting a single task outlast one context window."],
   [G3, G51, K41], ['2025-W47-L1-5', '2025-W47-L2-1', '2025-W47-L5-1']),
  ('OpenAI offers a free ChatGPT for US teachers', 'November 19',
   ["OpenAI introduced ChatGPT for Teachers, free for verified US K–12 educators through June 2027. The workspace offered GPT-5.1, search, file uploads and "
    "connections to Canva, Google Drive and Microsoft 365, with administrator controls for schools and districts. Content shared in it was not used to train "
    "models by default.{teachers}",
    "The offer targeted classroom preparation and school administration, with privacy terms intended to support compliance with student-records law."],
   [G3], ['2025-W47-L1-3']),
  ('Nvidia reports $57 billion in quarterly revenue', 'November 19',
   ["Nvidia reported record revenue of $57.0 billion for its third fiscal quarter, up 62 percent from a year earlier, including $51.2 billion from its data center "
    "business. It forecast about $65 billion for the next quarter. “Blackwell sales are off the charts, and cloud GPUs are sold out,” Jensen Huang said.{nvq3}",
    "The results arrived amid debate over whether spending on AI infrastructure could be sustained."],
   [K41], ['2025-W47-L7-1']),
  ('Olmo 3 opens more of the model-development process', 'November 20',
   ["Ai2 released Olmo 3, a family of models with seven-billion and 32-billion-parameter versions. Alongside weights, the project published training data, "
    "code, intermediate checkpoints and evaluation resources, allowing researchers to inspect stages of model development.{olmo}",
    "The release treated openness as access to a process as well as a finished model, making it easier to study how training choices shape behavior."],
   [G3], ['2025-W47-L1-4']),
  ('OpenAI and Foxconn plan US AI hardware manufacturing', 'November 20',
   ["OpenAI and Foxconn announced work on AI data center hardware design and US manufacturing readiness. Plans covered racks and components for cabling, "
    "networking, cooling and power. The initial agreement carried no purchase commitments or financial obligations; OpenAI would have early evaluation "
    "access and an option to buy.{foxconn}",
    "The collaboration addressed the equipment needed to turn computing plans into operating facilities."],
   [G3, G51], ['2025-W47-L1-3', '2025-W47-L2-3']),
 ]),
 (48, 'November 24–30', 'Original post published November 30, 2025', [
  ('Claude Opus 4.5 targets coding and sustained agent work', 'November 24',
   ["Anthropic released Claude Opus 4.5 through its applications, API and major cloud platforms. The company emphasized coding, computer use and "
    "longer-running agent tasks. Standard API pricing was $5 per million input tokens and $25 per million output tokens.{opus}",
    "The release combined a new model with a lower price for Opus-level access, about a third of the previous Opus rate."],
   [C, K41, G3T], ['2025-W48-L1-1', '2025-W48-L3-3', '2025-W48-L4-2']),
  ('Genesis Mission sets a national program for AI-assisted science', 'November 24',
   ["President Donald Trump signed an executive order establishing the Genesis Mission. It directed the Department of Energy to develop an integrated "
    "platform connecting scientific computing, appropriate datasets, AI models and experimental tools. The program aimed to support hypothesis testing "
    "and automate parts of research workflows.{genesis}",
    "The order framed AI for science as an institutional program involving national laboratories, infrastructure, data access and coordination."],
   [C, K41, G3T], ['2025-W48-L1-2', '2025-W48-L3-1', '2025-W48-L4-3']),
  ('AWS plans up to $50 billion for government computing', 'November 24',
   ["Amazon announced plans to invest up to $50 billion in AI and high-performance computing infrastructure for US government customers. Construction was "
    "due to begin in 2026. The program aimed to add nearly 1.3 gigawatts of capacity across AWS government regions with different security classifications.{aws50}",
    "The plan expanded the infrastructure available for public-sector computing, including work at the Top Secret and Secret levels."],
   [C, K41], ['2025-W48-L1-4', '2025-W48-L3-4']),
  ('A bill would raise penalties for AI-assisted fraud', 'November 25',
   ["Representatives Ted Lieu and Neal Dunn introduced the bipartisan AI Fraud Deterrence Act, which would increase the maximum penalties for various kinds "
    "of fraud committed with the help of AI, including impersonation of federal officials. Their announcement cited reported AI impersonations of "
    "Secretary of State Marco Rubio and White House Chief of Staff Susie Wiles.{fraud}",
    "The proposal addressed AI by raising the stakes for existing fraud offenses."],
   [C], ['2025-W48-L1-5']),
  ('USPTO revises guidance on AI-assisted inventions', 'November 26 announcement; November 28 publication',
   ["The US Patent and Trademark Office announced revised inventorship guidance, replacing its February 2024 guidance. It reaffirmed that only natural persons "
    "can be inventors and that the same inventorship standard applies whether or not AI is used. AI systems were treated as tools assisting human inventors.{uspto1}{uspto2}",
    "The revision applied the ordinary inventorship test to AI-assisted work, withdrawing the separate framework issued in 2024."],
   [C], ['2025-W48-L1-3']),
  ('Poetic prompts expose a weakness in safety testing', 'Reported November 30',
   ["The Guardian reported research from Icaro Lab, part of the Italian company DexAI, with Sapienza University of Rome and Sant’Anna School of Advanced "
    "Studies. Harmful requests written as verse bypassed safeguards in tests across 25 models from nine providers: 20 handcrafted poems averaged a 62 percent "
    "success rate, and 1,200 prose prompts converted to verse raised the average from 8 percent to 43 percent. Outputs were judged by three models, with human review.{poem1}{poem2}",
    "The study asked whether safeguards survive a change in literary form, and found that style alone could shift a model’s response."],
   [G3T], ['2025-W48-L4-5']),
 ]),
]
