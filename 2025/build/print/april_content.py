# April 2025 print chapter, v0.2: content (American style).
COVERS = 'Edited from four posts published in April 2025, covering March 31–April 27.'

SOURCES = {
 'tfmeet': ('SHRM', 'SHRM CEO participates in White House Task Force on AI Education', 'September 2025 (meeting of September 4)', 'https://www.shrm.org/mena/advocacy/shrm-ceo-participates-in-white-house-task-force-on-ai-education'),
 'iso': ('Isomorphic Labs', 'Isomorphic Labs announces $600m external investment round', 'March 31, 2025',
         'https://www.isomorphiclabs.com/articles/isomorphic-labs-announces-600m-external-investment-round'),
 'nova': ('Amazon Science', 'Introducing Amazon Nova Act', 'March 31, 2025', 'https://www.amazon.science/blog/nova-act'),
 'sb': ('SoftBank Group', 'Announcement Regarding Follow-on Investments in OpenAI', 'April 1, 2025; agreement March 31 US time', 'https://group.softbank/en/news/press/20250401'),
 'pineau': ('Bloomberg (via Advisor Perspectives)', "Meta's head of AI research to leave amid investment push", 'April 3, 2025 (announcement of April 1)',
            'https://www.advisorperspectives.com/articles/2025/04/03/metas-head-ai-research-leave-investment-push'),
 'agi': ('Google DeepMind', 'Taking a responsible path to AGI', 'April 2, 2025', 'https://deepmind.google/blog/taking-a-responsible-path-to-agi/'),
 'ai2027': ('Daniel Kokotajlo and colleagues', 'AI 2027', 'April 3, 2025; live page contains later dated additions', 'https://ai-2027.com/'),
 'index1': ('Stanford HAI', 'The 2025 AI Index Report', 'April 2025', 'https://hai.stanford.edu/ai-index/2025-ai-index-report'),
 'index2': ('Stanford HAI', 'AI Index 2025: State of AI in 10 Charts', 'April 7, 2025', 'https://hai.stanford.edu/news/ai-index-2025-state-of-ai-in-10-charts'),
 'megamath': ('Fan Zhou and colleagues', 'MegaMath: Pushing the Limits of Open Math Corpora', 'April 3, 2025; arXiv version 1', 'https://arxiv.org/abs/2504.02807v1'),
 'eu': ('European Commission', 'AI Continent Action Plan, COM(2025) 165 final', 'April 9, 2025; Council copy received April 10',
        'https://data.consilium.europa.eu/doc/document/ST-7955-2025-INIT/en/pdf'),
 'ironwood': ('Google Cloud', 'Introducing Ironwood TPUs and new innovations in AI Hypercomputer', 'April 9, 2025',
              'https://cloud.google.com/blog/products/compute/whats-new-with-ai-hypercomputer'),
 'a2a': ('Google Developers Blog', 'Announcing the Agent2Agent Protocol (A2A)', 'April 9, 2025', 'https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability/'),
 'counter': ('TechRepublic', "OpenAI's Countersuit of Elon Musk Alleges Harassment & 'Sham' Takeover Bid", 'April 10, 2025 (filing of April 9)',
             'https://www.techrepublic.com/article/news-openai-countersues-elon-musk/'),
 'grokapi': ('TechCrunch', "Elon Musk's AI company, xAI, launches an API for Grok 3", 'April 9, 2025',
             'https://techcrunch.com/2025/04/09/elon-musks-ai-company-xai-launches-an-api-for-grok-3/'),
 'gpt4': ('OpenAI Help Center', 'ChatGPT release notes: Sunsetting GPT-4 in ChatGPT', 'April 10, 2025 entry', 'https://help.openai.com/en/articles/6825453-chatgpt-release-notes'),
 'dpc': ('Data Protection Commission (Ireland)', 'Data Protection Commission announces commencement of inquiry into X Internet Unlimited Company (XIUC)', 'April 11, 2025',
         'https://www.dataprotection.ie/en/news-media/latest-news/data-protection-commission-announces-commencement-inquiry-x-internet-unlimited-company-xiuc'),
 'gpt41': ('OpenAI', 'Introducing GPT-4.1 in the API', 'April 14, 2025', 'https://openai.com/index/gpt-4-1/'),
 'veo': ('Google', 'Generate videos in Gemini and Whisk with Veo 2', 'April 15, 2025', 'https://blog.google/products-and-platforms/products/gemini/video-generation/'),
 'prep': ('OpenAI', 'Our updated Preparedness Framework', 'April 15, 2025', 'https://openai.com/index/updating-our-preparedness-framework/'),
 'o3': ('OpenAI', 'Introducing OpenAI o3 and o4-mini', 'April 16, 2025; original launch section', 'https://openai.com/index/introducing-o3-and-o4-mini/'),
 'wiki': ('Wikimedia Enterprise', 'Wikipedia Kaggle Dataset using Structured Contents Snapshot', 'April 16, 2025; describes April 15 upload', 'https://enterprise.wikimedia.com/blog/kaggle-dataset/'),
 'flash': ('Google Developers Blog', 'Start building with Gemini 2.5 Flash', 'April 17, 2025', 'https://developers.googleblog.com/en/start-building-with-gemini-25-flash/'),
 'hassabis': ('VentureBeat', 'Watch: Google DeepMind CEO and AI Nobel winner Demis Hassabis on CBS’ 60 Minutes', 'April 21, 2025 (broadcast of April 20)',
              'https://venturebeat.com/ai/watch-google-deepmind-ceo-and-ai-nobel-winner-demis-hassabis-on-cbs-60-minutes'),
 'genie': ('Databricks', "What's New in AI/BI - April 2025 Roundup", 'April 21, 2025', 'https://www.databricks.com/blog/whats-new-aibi-april-2025-roundup'),
 'image': ('OpenAI', 'Introducing our latest image generation model in the API', 'April 23, 2025', 'https://openai.com/index/image-generation-api/'),
 'eo': ('The White House', 'Advancing Artificial Intelligence Education for American Youth', 'April 23, 2025',
        'https://www.whitehouse.gov/presidential-actions/2025/04/advancing-artificial-intelligence-education-for-american-youth/'),
}

THEME = ('Reasoning, Collaboration', [
 ('Reasoning', " became part of the workflow. OpenAI's o3 and o4-mini combined deliberation with tools; Gemini 2.5 Flash let developers adjust how "
  'much computation a response used. Alongside them came longer context windows, open mathematics data, a model API from xAI and new ways to generate '
  'images and video. The practical question was how to fit these capabilities to a task.'),
 ('Collaboration', ' required connections: between agents, between applications and data, and between institutions. Google proposed a protocol for '
  'agents to coordinate work, Databricks expanded conversational access to business data, and Wikimedia supplied structured material for developers. '
  'Funding, safety frameworks, a European action plan, a privacy inquiry and a federal education order set the conditions around those tools, '
  'while DeepMind and the authors of AI 2027 set out how far they expected the technology to go.'),
])

WEEKS = [
 (14, 'March 31–April 6', 'Original post published April 6, 2025', [
  ('Isomorphic Labs raises $600 million', 'March 31',
   ["Isomorphic Labs announced $600 million in its first external funding round, led by Thrive Capital, with participation from GV and Alphabet. "
    "The company said the funding would support its AI drug-design engine and therapeutic programs.{iso}",
    "The investment backed an effort to turn computational drug design into treatments; clinical trials were the next milestone."],
   ['Gemini 2.5 Pro'], ['2025-W14-L1-2']),
  ('Amazon previews browser actions with Nova Act', 'March 31',
   ["Amazon introduced Nova Act, a model trained to perform actions in a web browser, and released a research preview of its software development "
    "kit. Developers could use the kit to build and test agents for browser-based tasks.{nova}",
    "The browser offered access to workflows that lack a dedicated software interface, provided an agent could complete them reliably."],
   ['Gemini 2.5 Pro'], ['2025-W14-L1-3']),
  ('SoftBank agrees to lead new OpenAI funding', 'March 31',
   ["SoftBank agreed to invest up to $40 billion in OpenAI, with plans to syndicate $10 billion to other investors. Its expected own contribution "
    "was up to $30 billion. The agreement provided for staged funding, with the size of the second closing dependent on conditions tied to OpenAI's restructuring.{sb}",
    "The agreement, paid in stages, signaled the scale of capital now sought for AI development."],
   ['Grok-3', 'ChatGPT (GPT-4) (week 15)'], ['2025-W14-L3-1', '2025-W15-L7-3']),
  ("Meta's head of AI research announces her departure", 'April 1',
   ["Joelle Pineau, the vice president who had led Meta's Fundamental AI Research group since early 2023, said she would leave the company in May, "
    "writing that “it is time to create space for others to pursue the work.” Meta said its AI research plans had not changed.{pineau}",
    "Her departure opened a leadership gap in Meta's research arm as the company increased its AI spending."],
   ['Gemini 2.5 Pro'], ['2025-W14-L1-1']),
  ('DeepMind sets out its approach to AGI safety', 'April 2',
   ["Google DeepMind published its approach to technical AGI safety and security. The paper considered misuse, misalignment, accidents and structural "
    "risks, with particular attention to misuse and misalignment. It discussed evaluating dangerous capabilities and developing safeguards.{agi}",
    "The paper made the laboratory's assumptions and proposed protections available for outside scrutiny."],
   ['GPT-4.5', 'DeepSeek-R1-Lite-Preview (week 15)'], ['2025-W14-L2-2', '2025-W15-L1-5']),
  ('AI 2027 publishes a detailed future scenario', 'April 3',
   ["The AI Futures Project published AI 2027, a scenario by Daniel Kokotajlo and colleagues about rapid AI development and its consequences. The authors "
    "combined forecasts with a narrative and supplied two alternative endings, describing their work as one possible future.{ai2027}",
    "Its detail gave readers concrete assumptions to examine and contest."],
   ['Grok-3', 'Grok-3 (week 17)'], ['2025-W14-L3-2', '2025-W17-L2-5']),
 ]),
 (15, 'April 7–13', 'Original post published April 13, 2025', [
  ("Research focus: MegaMath opens a mathematics corpus", 'Background: April 3; selected April 13 at the editor’s request',
   ["The MegaMath paper described an open mathematics pre-training dataset containing 371 billion tokens. Its authors combined mathematical web documents, "
    "mathematics-related code and synthetic material.{megamath}",
    "The release addressed the data used to develop mathematical reasoning, as a resource others could test through training experiments."],
   ['W.H.L.', 'DeepSeek-R1-Lite-Preview'], ['2025-W15-L5-1', '2025-W15-L5-2', '2025-W15-L5-3', '2025-W15-L5-4', '2025-W15-L5-5']),
  ("Stanford's AI Index takes stock of the field", 'April 7',
   ["Stanford HAI released the 2025 AI Index, bringing together evidence on technical performance, investment, research, governance, education and "
    "public opinion. Much of its annual comparison described developments in 2024.{index1}{index2}",
    "The report supplied a broader frame for weekly announcements, measured mostly on the previous year."],
   ['W.H.L.', 'DeepSeek-R1-Lite-Preview', 'Gemini 2.5 Pro'],
   ['2025-W15-L3-1', '2025-W15-L3-2', '2025-W15-L3-3', '2025-W15-L3-4', '2025-W15-L3-5', '2025-W15-L4-1', '2025-W15-L4-2', '2025-W15-L4-3', '2025-W15-L6-2']),
  ('Europe publishes its AI Continent Action Plan', 'April 9',
   ["The European Commission published the AI Continent Action Plan. Its program addressed computing infrastructure, access to data, adoption across "
    "sectors, skills and implementation of the AI Act.{eu}",
    "The plan treated AI development as an institutional task as well as a technical one, dependent on later investment."],
   ['Gemini 2.5 Pro'], ['2025-W15-L6-1']),
  ('Cloud Next links computing capacity and agent tools', 'April 9',
   ["At Cloud Next, Google announced Ironwood, its seventh-generation tensor processing unit, designed for inference. It also introduced Agent2Agent, "
    "an open protocol intended to let agents from different providers exchange information and coordinate tasks.{ironwood}{a2a}",
    "The announcements addressed two requirements for wider deployment: capacity to run models and a common way for agents to work together."],
   ['ChatGPT (GPT-4)'], ['2025-W15-L7-2']),
  ('OpenAI countersues Elon Musk', 'April 9',
   ["OpenAI filed counterclaims against Elon Musk, accusing him of a campaign of harassment that included press attacks, legal claims and a “sham bid” "
    "for its assets, a reference to the $97.4 billion offer its board had rejected in February. The case was set for trial in spring 2026.{counter}",
    "The dispute over OpenAI's structure moved from Musk's original claims to accusations in both directions."],
   ['DeepSeek-R1-Lite-Preview'], ['2025-W15-L1-4']),
  ('xAI opens Grok 3 to developers', 'April 9',
   ["xAI made Grok 3 and Grok 3 Mini available through an API, charging $3 per million input tokens and $15 per million output tokens for Grok 3. "
    "The API supported a context window of 131,072 tokens, less than the one million xAI had claimed for the model in February.{grokapi}",
    "The release put xAI's flagship model in direct price competition with other developers' APIs."],
   ['Grok-3'], ['2025-W15-L8-4']),
  ("OpenAI announces GPT-4's retirement from ChatGPT", 'April 10',
   ["OpenAI announced that GPT-4 would leave ChatGPT on April 30 and be replaced there by GPT-4o. The notice stated that GPT-4 would remain available through the API.{gpt4}",
    "GPT-4, introduced in March 2023, left the consumer product while remaining available to developers."],
   ['Grok-3'], ['2025-W15-L8-1']),
  ("Ireland's privacy regulator opens an inquiry into Grok's training data", 'April 11',
   ["Ireland's Data Protection Commission opened an inquiry into whether X lawfully used personal data in public posts by users in the European Union "
    "and European Economic Area to train xAI's Grok models, examining the lawfulness and transparency of that processing under the GDPR.{dpc}",
    "European privacy law became a constraint on what public posts could be used for in training."],
   ['DeepSeek-R1-Lite-Preview'], ['2025-W15-L1-3']),
 ]),
 (16, 'April 14–20', 'Original post published April 20, 2025', [
  ('GPT-4.1 brings longer context to the API', 'April 14',
   ["OpenAI released GPT-4.1, GPT-4.1 mini and GPT-4.1 nano through its API. The models supported context windows of up to one million tokens. "
    "OpenAI reported improvements in coding, instruction following and the use of long inputs.{gpt41}",
    "The range offered developers different choices of capacity, speed and price, with the larger window expanding what a single request could include."],
   ['Grok-3', 'GPT-4-turbo'], ['2025-W16-L1-1', '2025-W16-L4-1']),
  ('Veo 2 reaches Gemini Advanced and Whisk', 'April 15',
   ["Google began rolling out Veo 2 video generation in Gemini Advanced for Google One AI Premium subscribers. The feature produced eight-second clips "
    "from text prompts. Whisk Animate also used Veo 2 to turn images into short videos for subscribers.{veo}",
    "The rollout placed video generation inside consumer creative tools, with subscription access and usage limits."],
   ['Grok-3'], ['2025-W16-L1-2']),
  ('OpenAI revises its Preparedness Framework', 'April 15',
   ["OpenAI updated its framework for assessing severe risks from advanced models. Its tracked categories covered biological and chemical capabilities, "
    "cybersecurity and AI self-improvement. The update defined High and Critical capability thresholds with corresponding safeguard requirements.{prep}",
    "The framework set out how the company intended to connect capability assessments to deployment decisions."],
   ['GPT-4-turbo'], ['2025-W16-L4-3']),
  ('o3 and o4-mini combine reasoning with tools', 'April 16',
   ["OpenAI released o3 and o4-mini, reasoning models able to select and combine tools in ChatGPT, including web search, Python and image generation. "
    "The release also introduced Codex CLI, an open-source experiment for working with code from a terminal.{o3}",
    "Reasoning could now guide a sequence of actions as well as an answer, making the choice of tools part of the task."],
   ['Gemini 2.5 Pro'], ['2025-W16-L6-1']),
  ('Wikimedia shares structured Wikipedia data on Kaggle', 'April 16',
   ["Wikimedia Enterprise announced a beta dataset on Kaggle containing structured Wikipedia content in English and French. The April 15 upload "
    "included article sections and other fields in a machine-readable format, excluding references and some non-prose material.{wiki}",
    "The dataset gave developers an organized route to Wikipedia content, with its scope defined by what was included and left out."],
   ['Gemini 2.5 Pro'], ['2025-W16-L6-4']),
  ('Gemini 2.5 Flash makes thinking adjustable', 'April 17',
   ["Google released a preview of Gemini 2.5 Flash through the Gemini API in AI Studio and Vertex AI. Developers could switch its thinking mode on or off "
    "and set a thinking budget to control the balance between response quality, cost and latency.{flash}",
    "Reasoning became a setting developers could adjust for each application."],
   ['Gemini 2.5 Pro'], ['2025-W16-L6-2']),
  ('Hassabis sets out DeepMind’s ambitions on 60 Minutes', 'April 20',
   ["In a 60 Minutes interview, Demis Hassabis said artificial general intelligence could arrive as soon as 2030 and demonstrated Project Astra, an assistant "
    "that interprets the visual world in real time. He warned that “the race for AI dominance could become a race to the bottom for safety” and called "
    "for international cooperation on oversight.{hassabis}",
    "A Nobel laureate's timeline for AGI reached a mass television audience."],
   ['Gemini 2.5 Pro', 'GPT-4-turbo'], ['2025-W16-L6-3', '2025-W16-L4-4']),
 ]),
 (17, 'April 21–27', 'Original post published April 28, 2025', [
  ('Databricks expands conversational data analysis', 'April 21',
   ["Databricks described updates to AI/BI Genie, including suggested follow-up questions and file uploads. The upload feature, in gated public "
    "preview, let users combine Excel or CSV files with data in Unity Catalog. The roundup also covered conversation APIs in public preview.{genie}",
    "The updates brought external files into a conversational analysis workflow, initially for preview users."],
   ['DeepSeek-R1'], ['2025-W17-L5-2']),
  ('OpenAI opens its image model to developers', 'April 23',
   ["OpenAI made gpt-image-1 available through its API. The model brought the image-generation capability introduced in ChatGPT the previous month "
    "into developers' own applications.{image}",
    "The API extended image creation beyond the chat interface into other companies' products."],
   ['Gemini 2.5 Pro', 'DeepSeek-R1'], ['2025-W17-L3-2', '2025-W17-L4-2', '2025-W17-L5-3']),
  ('US executive order establishes an AI education program', 'April 23',
   ["A US executive order established a White House AI Education Task Force and directed work on student resources, educator training and a "
    "Presidential AI Challenge. It called for partnerships involving government, educational institutions and industry.{eo}",
    "The order set a federal program in motion; the task force met to advance the Presidential AI Challenge in September.{tfmeet}"],
   ['Gemini 2.5 Pro'], ['2025-W17-L3-3', '2025-W17-L4-3']),
 ]),
]
