# March 2025 print chapter, v0.2: content (American style).
COVERS = 'Edited from five posts published in March 2025, covering February 24–March 30.'

SOURCES = {
 'claude37': ('Anthropic', 'Claude 3.7 Sonnet and Claude Code', 'February 24, 2025', 'https://www.anthropic.com/news/claude-3-7-sonnet'),
 'wan': ('Wan Team', 'Wan2.1 model repository', 'February 25, 2025 release entry', 'https://github.com/Wan-Video/Wan2.1'),
 'alexa': ('Amazon', 'Introducing Alexa+, the next generation of Alexa', 'originally February 26, 2025; live page updated July 21, 2026',
           'https://www.aboutamazon.com/news/devices/new-alexa-generative-artificial-intelligence'),
 'gpt45': ('OpenAI', 'Introducing GPT-4.5', 'February 27, 2025', 'https://openai.com/index/introducing-gpt-4-5/'),
 'pplx': ('TechRadar', "Perplexity's voice mode gets a futuristic makeover on your iPhone", 'February 27, 2025',
          'https://www.techradar.com/computing/artificial-intelligence/perplexitys-voice-mode-gets-a-futuristic-makeover-on-your-iphone'),
 'osw': ('DeepSeek', 'Open Infra Index: February 2025 Open-Source Week', 'February 24–28, 2025', 'https://github.com/deepseek-ai/open-infra-index'),
 'moddy': ('Moderne', 'Moderne Unveils Moddy: The First Multi-Repository AI Code Agent', 'March 4, 2025',
           'https://moderne.ai/press/moderne-unveils-moddy-the-first-multi-repository-ai-code-agent'),
 'agentforce': ('Salesforce', 'Agentforce 2dx News Announcement', 'March 5, 2025', 'https://www.salesforce.com/in/news/press-releases/2025/03/05/agentforce-2dx-news/'),
 'manus': ('South China Morning Post', 'Another DeepSeek moment? General AI agent Manus shows ability to handle complex tasks', 'March 6, 2025',
           'https://www.scmp.com/tech/policy/article/3301283/another-deepseek-moment-general-ai-agent-manus-shows-ability-handle-complex-tasks'),
 'diloco': ('Zachary Charles and colleagues', 'Communication-Efficient Language Model Training Scales Reliably and Robustly: Scaling Laws for DiLoCo',
            'March 12, 2025; arXiv version 1', 'https://arxiv.org/abs/2503.09799v1'),
 'oaipolicy': ('OpenAI', "OpenAI's proposals for the U.S. AI Action Plan", 'March 13, 2025', 'https://openai.com/global-affairs/openai-proposals-for-the-us-ai-action-plan/'),
 'ernie': ('Baidu, via PR Newswire', 'Baidu Unveils ERNIE 4.5 and Reasoning Model ERNIE X1, Makes ERNIE Bot Free Ahead of Schedule', 'March 16, 2025',
           'https://www.prnewswire.com/news-releases/baidu-unveils-ernie-4-5-and-reasoning-model-ernie-x1--makes-ernie-bot-free-ahead-of-schedule-302402490.html'),
 'judges': ('University of Chicago Law School', 'AI Research From Eric Posner, Shivam Saran Featured in Washington Post', 'March 17, 2025',
            'https://www.law.uchicago.edu/news/ai-research-eric-posner-shivam-saran-featured-washington-post'),
 'cosmos': ('Nvidia', 'NVIDIA Announces Major Release of Cosmos World Foundation Models and Physical AI Data Tools', 'March 18, 2025',
            'https://nvidianews.nvidia.com/news/nvidia-announces-major-release-of-cosmos-world-foundation-models-and-physical-ai-data-tools'),
 'skywork': ('Skywork AI', 'Skywork-R1V repository: original release announcement', 'March 18, 2025 entry', 'https://github.com/SkyworkAI/Skywork-R1V'),
 'ampere': ('SoftBank Group', 'Acquisition of Ampere Computing Holdings LLC', 'March 20, 2025; agreement dated March 19 US time', 'https://group.softbank/en/news/press/20250320_0'),
 'metr': ('METR', 'Measuring AI Ability to Complete Long Software Tasks', 'March 19, 2025; live page also contains later chart updates',
          'https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/'),
 'alexnet': ('Computer History Museum', 'CHM Releases AlexNet Source Code', 'March 20, 2025', 'https://computerhistory.org/blog/chm-releases-alexnet-source-code/'),
 'audio': ('OpenAI', 'Introducing next-generation audio models in the API', 'March 20, 2025', 'https://openai.com/index/introducing-our-next-generation-audio-models/'),
 'v3a': ('DeepSeek, via Hugging Face', 'DeepSeek-V3-0324 model card', 'March 2025 release', 'https://huggingface.co/deepseek-ai/DeepSeek-V3-0324'),
 'v3b': ('DeepSeek, via Hugging Face', 'DeepSeek-V3-0324 repository commit history', 'March 24–25, 2025 upload and release history',
         'https://huggingface.co/deepseek-ai/DeepSeek-V3-0324/commits/main'),
 'arc2': ('ARC Prize', 'ARC-AGI-2 + ARC Prize 2025 is Live!', 'March 24, 2025', 'https://arcprize.org/blog/announcing-arc-agi-2-and-arc-prize-2025'),
 'gemini25': ('Google DeepMind', 'Gemini 2.5: Our most intelligent AI model', 'March 25, 2025; updated March 26',
              'https://blog.google/innovation-and-ai/models-and-research/google-deepmind/gemini-model-thinking-updates-march-2025/'),
 'image': ('OpenAI', 'Introducing 4o Image Generation', 'March 25, 2025', 'https://openai.com/index/introducing-4o-image-generation/'),
 'xai1': ('Reuters, via Investing.com', "Musk's social media firm X bought by his AI company, valued at $33 billion", 'March 28, 2025; updated March 29',
          'https://www.investing.com/news/stock-market-news/musks-xai-buys-social-media-platform-x-for-45-billion-3955500'),
 'xai2': ('Associated Press', 'Elon Musk sells X to his own xAI for $33 billion in all-stock deal', 'March 28, 2025', 'https://apnews.com/article/b245f463076ac9b72c41f92160dc77eb'),
}

THEME = ('Agents, Reasoning', [
 ('Agents', " brought the month's developments into practical settings: maintaining software, navigating websites, searching by voice and working within "
  'business systems. These products proposed a shift from answering a request to carrying it out, and their value depended on completing the task.'),
 ('Reasoning', ' also became a more explicit design choice. Developers offered extended-thinking modes and new models, while researchers examined '
  'alternative approaches and harder tests. METR measured the difficulty of tasks agents could complete; ARC-AGI-2 exposed gaps in abstract problem '
  'solving. Around them, OpenAI set out its policy proposals, SoftBank bought a chip designer and xAI absorbed X, sharpening the question of how '
  'reported capability translated into dependable work.'),
])

WEEKS = [
 (9, 'February 24–March 2', 'Original post published March 3, 2025', [
  ('Claude 3.7 Sonnet offers two modes of response', 'February 24',
   ["Anthropic released Claude 3.7 Sonnet with standard responses and an extended-thinking mode. API users could set a budget for the model's thinking "
    "tokens. The release was available through Claude, Anthropic's API, Amazon Bedrock and Google Cloud's Vertex AI; extended thinking was excluded "
    "from the free Claude tier.{claude37}",
    "The design made additional reasoning a choice within one model, with consequences for response time and cost."],
   ['Grok-3'], ['2025-W09-L2-2']),
  ('DeepSeek shares its infrastructure tools', 'February 24–28',
   ["DeepSeek's Open-Source Week published FlashMLA, DeepEP, DeepGEMM, parallelism tools including DualPipe and EPLB, and the 3FS file system. "
    "The releases addressed model decoding, communication, matrix operations, workload distribution and storage.{osw}",
    "Sharing these components exposed the engineering behind model training and inference that benchmarks alone do not describe."],
   ['W.H.L.', 'Copilot'], ['2025-W09-L1-1', '2025-W09-L1-2', '2025-W09-L1-3', '2025-W09-L1-4', '2025-W09-L1-5']),
  ('Wan2.1 opens video-generation code and weights', 'February 25',
   ["Alibaba's Wan team released inference code and model weights for Wan2.1, including text-to-video and image-to-video generation. The repository "
    "recorded the release on February 25.{wan}",
    "The release gave developers access to the models themselves, widening the options for experimentation beyond a hosted video-generation service."],
   ['Grok-3'], ['2025-W09-L2-3']),
  ('Amazon announces Alexa+', 'February 26',
   ["Amazon announced Alexa+, a generative-AI version of its assistant designed for more conversational interactions and help with everyday tasks. "
    "The company said it would be included with Prime.{alexa}",
    "The announcement brought generative AI into an established consumer assistant, with the rollout still to come."],
   ['Grok-3'], ['2025-W09-L2-4']),
  ('GPT-4.5 enters research preview', 'February 27',
   ["OpenAI released GPT-4.5 as a research preview for ChatGPT Pro users and developers. The company emphasized improvements from scaling pre-training "
    "and distinguished the model from systems that spend additional time reasoning before answering.{gpt45}",
    "The release showed that model development followed more than one approach: larger pre-training runs continued alongside explicit reasoning methods."],
   ['Grok-3'], ['2025-W09-L2-1']),
  ('Perplexity refreshes voice search on iPhone', 'Reported February 27',
   ["Perplexity's iOS app received a redesigned voice mode with six voices and search results linked to spoken answers, TechRadar reported. "
    "The update connected voice interaction to the service's source-linked search interface.{pplx}",
    "The change concerned how users reached answers and checked their sources by voice."],
   ['Grok-3'], ['2025-W09-L2-5']),
 ]),
 (10, 'March 3–9', 'Original post published March 10, 2025', [
  ('Moddy applies AI to changes across code repositories', 'March 4',
   ["Moderne announced Moddy, an agent for analyzing and changing code across multiple repositories. It combined a natural-language interface with the "
    "company's code-analysis and transformation platform.{moddy}",
    "The target was maintenance across an existing codebase, where the scope and consistency of changes matter more than generating new code."],
   ['Gemini 2.0'], ['2025-W10-L2-2', '2025-W10-L3-4']),
  ('Agentforce 2dx extends agents into workflows', 'March 5',
   ["Salesforce announced Agentforce 2dx, with tools for connecting agents to business systems and workflows beyond a chat interface. The announcement "
    "included development, testing and monitoring tools. Full general availability was scheduled for April, with some features arriving earlier.{agentforce}",
    "The product placed agents inside existing business processes, with integration and oversight built in."],
   ['Gemini 2.0'], ['2025-W10-L2-2', '2025-W10-L3-2']),
  ('Manus previews an agent for multi-step tasks', 'Reported March 6',
   ["Manus appeared as an invitation-only web preview. Its demonstrations showed tasks such as building a website and preparing a travel itinerary, "
    "according to contemporaneous reporting by the South China Morning Post.{manus}",
    "The demonstrations, compared by some to a “DeepSeek moment,” presented an assistant that could work through a goal across several steps."],
   ['Grok-3'], ['2025-W10-L1-1']),
 ]),
 (11, 'March 10–16', 'Original post published March 16, 2025', [
  ('Research shows DiLoCo training scaling predictably', 'March 12',
   ["Zachary Charles and colleagues reported scaling laws for DiLoCo, a training method that reduces how often data-parallel training must synchronize. "
    "When well tuned, it scaled predictably with model size and could outperform standard data-parallel training, with larger optimal batch sizes.{diloco}",
    "The work supported training large models across less tightly connected hardware."],
   ['Grok-3'], ['2025-W11-L1-2']),
  ('OpenAI submits proposals for US AI policy', 'March 13',
   ["OpenAI submitted recommendations for the US AI Action Plan, addressing regulation, export policy, infrastructure, energy, copyright and government "
    "adoption. The company presented the proposals as measures to support US leadership in AI.{oaipolicy}",
    "The submission showed how an AI developer sought to shape the conditions under which its industry would operate; the plan itself followed in July."],
   ['Grok-3'], ['2025-W11-L1-1']),
  ('Baidu releases ERNIE 4.5 and ERNIE X1', 'March 16',
   ["Baidu introduced ERNIE 4.5, a multimodal foundation model, and ERNIE X1, a reasoning model. Individual users could access both through ERNIE Bot "
    "without charge. Baidu published its own comparisons with competing models.{ernie}",
    "The release combined a new model offering with free access for individual users."],
   ['Grok-3', 'GPT-4.5'], ['2025-W11-L1-3', '2025-W11-L2-2']),
 ]),
 (12, 'March 17–23', 'Original post published March 23, 2025', [
  ('An experiment pits ChatGPT against federal judges', 'March 17',
   ["A *Washington Post* column by Jason Willick described a working paper by Eric Posner and Shivam Saran comparing federal judges with ChatGPT on the same "
    "case materials. The judges appeared more easily swayed by legally irrelevant factors than the AI.{judges}",
    "The experiment brought the question of AI in judicial decisions into a mainstream newspaper."],
   ['Grok-3'], ['2025-W12-L1-2']),
  ('Cosmos expands its physical-AI tools', 'March 18',
   ["Nvidia announced additions to Cosmos for generating and interpreting data used in physical AI. Cosmos Predict and Cosmos Transfer were openly "
    "available, while the reasoning component was offered through early access.{cosmos}",
    "The tools addressed different parts of building robotics and autonomous systems: generating training material, adapting it and reasoning about physical scenes."],
   ['W.H.L.', 'Grok-3'], ['2025-W12-L1-HM2']),
  ('Skywork R1V extends reasoning to visual inputs', 'March 18',
   ["Skywork introduced R1V, a multimodal reasoning model with downloadable weights. The release combined visual inputs with step-by-step reasoning "
    "and was recorded in the project's repository on March 18.{skywork}",
    "The release extended the reasoning-model approach beyond text, with published evaluations on visual and mathematical tests."],
   ['W.H.L.', 'Grok-3'], ['2025-W12-L1-HM4']),
  ('METR measures the length of tasks agents can complete', 'March 19',
   ["METR measured agent performance against the time human experts needed for software and reasoning tasks. At a 50 percent success threshold, the "
    "estimated task horizon had doubled roughly every seven months across the historical models studied.{metr}",
    "The measure expressed task difficulty in human working time, giving agent progress a unit that could be tracked across models."],
   ['W.H.L.', 'Grok-3'], ['2025-W12-L1-HM3']),
  ('SoftBank agrees to acquire Ampere', 'March 19',
   ["SoftBank agreed to acquire Ampere Computing for $6.5 billion. The company described Ampere as a designer of energy-efficient computing chips based "
    "on the Arm platform. The transaction remained subject to closing conditions.{ampere}",
    "The agreement expanded SoftBank's planned investment in the hardware supporting AI."],
   ['Grok-3'], ['2025-W12-L1-1']),
  ("AlexNet's original source code becomes available", 'March 20',
   ["The Computer History Museum released AlexNet's source code in partnership with Google. AlexNet was the image-recognition neural network developed "
    "in 2012 by Alex Krizhevsky, Ilya Sutskever and Geoffrey Hinton.{alexnet}",
    "The release preserved for study how a landmark neural network was built."],
   ['W.H.L.', 'Grok-3'], ['2025-W12-L1-HM1']),
  ('OpenAI adds transcription and speech-generation models', 'March 20',
   ["OpenAI released gpt-4o-transcribe and gpt-4o-mini-transcribe for speech recognition, together with gpt-4o-mini-tts for speech generation. "
    "The models were available through its API.{audio}",
    "The release supplied components for voice applications, converting speech into text and generating spoken responses."],
   ['Grok-3'], ['2025-W12-L1-6']),
 ]),
 (13, 'March 24–30', 'Original post published March 30, 2025', [
  ('DeepSeek updates V3', 'March 24–25',
   ["DeepSeek released V3-0324, an updated version of its V3 model, with downloadable weights under the MIT license. Its model card reported improvements "
    "across several evaluated capabilities, including reasoning and coding.{v3a}{v3b}",
    "The release continued development of a general-purpose model alongside the company's R1 reasoning family."],
   ['Grok-3'], ['2025-W13-L1-5']),
  ('ARC-AGI-2 raises the reasoning challenge', 'March 24',
   ["The ARC Prize team introduced ARC-AGI-2, a new collection of abstract reasoning tasks, alongside its 2025 competition. The launch report showed low "
    "scores for the evaluated AI systems and added explicit attention to the cost of solving tasks.{arc2}",
    "The benchmark sought to expose gaps that earlier tests no longer captured as clearly."],
   ['Grok-3'], ['2025-W13-L1-4']),
  ('Google introduces Gemini 2.5 Pro Experimental', 'March 25',
   ["Google introduced Gemini 2.5 Pro Experimental, a model designed to reason before responding. The company reported stronger results on coding and "
    "reasoning evaluations and made the experimental model available for use.{gemini25}",
    "The release brought a new generation of reasoning models into competition, under an experimental label."],
   ['Grok-3'], ['2025-W13-L1-2']),
  ('GPT-4o adds native image generation', 'March 25',
   ["OpenAI introduced native image generation in GPT-4o, allowing images to be created and refined within a conversation. The announcement emphasized "
    "instruction following, text rendering and the use of uploaded images as context.{image}",
    "The capability connected visual production to an ongoing dialogue, in which an image could be refined step by step."],
   ['Grok-3'], ['2025-W13-L1-3']),
  ("Musk announces xAI's acquisition of X", 'March 28',
   ["Elon Musk announced that xAI had acquired X in an all-stock transaction. He put X's equity value at $33 billion, or $45 billion including $12 billion "
    "of debt; the figures were valuations stated for the deal, not a cash price.{xai1}{xai2}",
    "The combination brought an AI developer and a major distribution platform under one corporate arrangement."],
   ['Grok-3'], ['2025-W13-L1-1']),
 ]),
]
