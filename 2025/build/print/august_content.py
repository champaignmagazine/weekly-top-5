# August 2025 print chapter, v0.2: content (American style).
COVERS = 'Edited from five posts published in August 2025, covering July 28–August 31.'

SOURCES = {
 'glm1': ('Z.ai', 'GLM-4.5: Reasoning, Coding, and Agentic Abilities', 'July 28, 2025', 'https://z.ai/blog/glm-4.5'),
 'glm2': ('Z.ai', 'GLM-4.5 repository and model documentation', 'July 2025 release; live repository', 'https://github.com/zai-org/GLM-4.5'),
 'study': ('OpenAI', 'ChatGPT study mode', 'July 29, 2025', 'https://openai.com/index/chatgpt-study-mode/'),
 'capex1': ('Finance Magnates (via TradingView)', 'Meta soars 12%, Microsoft tops $4 trillion as AI spending powers profits', 'coverage of July 30, 2025 results',
            'https://tr.tradingview.com/news/financemagnates%3A0f7a492ed094b%3A0-meta-soars-12-microsoft-tops-4-trillion-as-ai-spending-powers-profits'),
 'capex2': ('Sherwood News', 'Meta, Microsoft crush earnings', 'July 30–31, 2025', 'https://sherwood.news/snacks/newsletters/m-meta-microsoft-crush-earnings/'),
 'oairev': ('Reuters (via Yahoo Finance)', 'OpenAI hits $12 billion in annualized revenue, The Information reports', 'July 30, 2025',
            'https://finance.yahoo.com/news/openai-hits-12-billion-annualized-015009168.html'),
 'aiplus': ('SESEC', 'China Approves "AI +" Action Plan to Drive Industrial Integration', 'August 22, 2025 (on the July 31 State Council meeting)', 'https://sesec.eu/?p=2117'),
 'cset': ('Center for Security and Emerging Technology', 'Opinions of the State Council on Deepening the Implementation of the "Artificial Intelligence+" Initiative (translation)',
          'originally published August 26, 2025; translation September 24, 2025', 'https://cset.georgetown.edu/publication/china-ai-plus-opinions-2025/'),
 'norway': ('OpenAI', 'Introducing Stargate Norway', 'July 31, 2025', 'https://openai.com/index/introducing-stargate-norway/'),
 'anthoai': ('Notebookcheck, reporting Wired', "Anthropic cuts OpenAI's Claude API access over alleged terms-of-service breach", 'August 4, 2025',
             'https://www.notebookcheck.net/Anthropic-cuts-OpenAI-s-Claude-API-access-over-alleged-terms-of-service-breach.1078560.0.html'),
 'gpai': ('European Commission', 'Guidelines for providers of general-purpose AI models', 'page updated April 28, 2026; confirms the 2025 timetable',
          'https://digital-strategy.ec.europa.eu/en/policies/guidelines-gpai-providers'),
 'grokimg': ('Decrypt', "Elon Musk's xAI Tool Made Nude Deepfakes of Taylor Swift, Bypassing Its Own Rules", 'August 6, 2025',
             'https://decrypt.co/333796/elon-musk-xai-nude-deepfakes-taylor-swift'),
 'gptoss': ('OpenAI', 'Introducing gpt-oss', 'August 5, 2025', 'https://openai.com/index/introducing-gpt-oss/'),
 'opus41': ('Anthropic', 'Claude Opus 4.1', 'August 5, 2025', 'https://www.anthropic.com/news/claude-opus-4-1'),
 'genie': ('Google DeepMind', 'Genie 3: A new frontier for world models', 'August 5, 2025', 'https://deepmind.google/blog/genie-3-a-new-frontier-for-world-models/'),
 'jules': ('Google', 'Jules, our asynchronous coding agent, is now available for everyone', 'August 6, 2025',
           'https://blog.google/innovation-and-ai/models-and-research/google-labs/jules-now-available/'),
 'gsa': ('US General Services Administration', 'GSA Announces New Partnership with OpenAI, Delivering Deep Discount to ChatGPT Gov-Wide Through MAS', 'August 6, 2025',
         'https://www.gsa.gov/about-gsa/newsroom/news-releases/gsa-announces-new-partnership-with-openai-delivering-deep-discount-to-chatgpt-08062025'),
 'gpt5': ('OpenAI', 'Introducing GPT-5', 'August 7, 2025', 'https://openai.com/index/introducing-gpt-5/'),
 'miro': ('MiroMind', 'MiroMind Research Agent v0.1', 'August 7, 2025; comparison table dated August 8', 'https://www.miromind.ai/blog/miromind-research-agent'),
 'nvamd': ('Associated Press (via PBS NewsHour)', 'Under new, unusual agreement, U.S. will get a 15% cut of Nvidia and AMD chip sales to China', 'August 11, 2025',
           'https://www.pbs.org/newshour/politics/under-new-unusual-agreement-u-s-will-get-a-15-cut-of-nvidia-and-amd-chip-sales-to-china'),
 'cosmos': ('Nvidia', 'NVIDIA Research Shapes Physical AI', 'August 11, 2025', 'https://blogs.nvidia.com/blog/physical-ai-research-siggraph-2025/'),
 'anth1': ('Anthropic', 'Offering expanded Claude access across all three branches of the U.S. government', 'August 12, 2025',
           'https://www.anthropic.com/news/offering-expanded-claude-access-across-all-three-branches-of-government'),
 'ctx1m': ('Anthropic', 'Claude Sonnet 4 now supports 1M tokens of context', 'August 12, 2025; page later updated', 'https://claude.com/resources/articles/1m-context'),
 'metarules': ('TechCrunch, reporting Reuters', 'Leaked Meta AI rules show chatbots were allowed to have romantic chats with kids', 'August 14, 2025',
               'https://techcrunch.com/2025/08/14/leaked-meta-ai-rules-show-chatbots-were-allowed-to-have-romantic-chats-with-kids/'),
 'cohere': ('Cohere', 'Cohere raises $500M at $6.8B valuation to accelerate enterprise efficiency with agentic AI', 'August 14, 2025',
            'https://cohere.com/blog/august-2025-funding-round'),
 'dino': ('Meta', 'DINOv3: Self-supervised learning for vision at unprecedented scale', 'August 14, 2025', 'https://ai.meta.com/blog/dinov3-self-supervised-vision-model/'),
 'nsf': ('US National Science Foundation', 'NSF and NVIDIA partnership enables Ai2 to develop fully open AI models to fuel U.S. scientific innovation', 'August 14, 2025',
         'https://www.nsf.gov/news/nsf-nvidia-partnership-enables-ai2-develop-fully-open-ai'),
 'texas': ('Digital Policy Alert', 'Attorney General Ken Paxton announced investigation into Meta and Character.AI over deceptive marketing of mental health services provided by artificial intelligence', 'August 18, 2025',
           'https://digitalpolicyalert.org/event/32803-attorney-general-ken-paxton-announced-investigation-into-meta-and-characterai-over-deceptive-marketing-of-mental-health-services-provided-by-artificial-intelligence'),
 'gao': ('Huan-ang Gao and colleagues', 'A Survey of Self-Evolving Agents: On Path to Artificial Super Intelligence', 'July 28, 2025; arXiv version 1', 'https://arxiv.org/abs/2507.21046v1'),
 'fang': ('Jinyuan Fang and colleagues', 'A Comprehensive Survey of Self-Evolving AI Agents: A New Paradigm Bridging Foundation Models and Lifelong Agentic Systems', 'August 10, 2025; arXiv version 1',
          'https://arxiv.org/abs/2508.07407v1'),
 'acrobat': ('Adobe', 'Acrobat Studio Delivers New AI-Powered Home for Productivity and Creativity with PDF Spaces, Express Creation Tools, AI Agents', 'August 19, 2025',
             'https://news.adobe.com/news/2025/08/acrobat-studio-delivers-new-ai-powered-home-for-productivity-creativity'),
 'hiring': ('Channels Television, reporting the Wall Street Journal', 'Meta Freezes AI Hiring', 'August 21, 2025', 'https://www.channelstv.com/2025/08/21/meta-freezes-ai-hiring/amp/'),
 'dsv31': ('DeepSeek', 'DeepSeek-V3.1 Release', 'August 21, 2025', 'https://api-docs.deepseek.com/news/news250821/'),
 'aimode': ('Google', 'AI Mode in Search gets new agentic features and expands globally', 'August 21, 2025',
            'https://blog.google/products-and-platforms/products/search/ai-mode-agentic-personalized/'),
 'metagoog': ('Reuters (via Al Arabiya)', 'Meta signs over $10 bln deal with Google: Source', 'August 22, 2025',
              'https://english.alarabiya.net/business/technology/2025/08/22/meta-signs-over-10-bln-deal-with-google-source-'),
 'retro': ('OpenAI', 'Accelerating life sciences research', 'August 22, 2025', 'https://openai.com/index/accelerating-life-sciences-research-with-retro-biosciences/'),
 'midj': ('Engadget', "Meta is licensing Midjourney's AI image and video tech", 'August 23, 2025 (announcement of August 22)',
          'https://www.engadget.com/ai/meta-is-licensing-midjourneys-ai-image-and-video-tech-120012178.html'),
 'naag': ('National Association of Attorneys General', 'Bipartisan Coalition of State Attorneys General Issues Letter to AI Industry Leaders on Child Safety', 'August 25, 2025',
          'https://www.naag.org/press-releases/bipartisan-coalition-of-state-attorneys-general-issues-letter-to-ai-industry-leaders-on-child-safety/'),
 'xai': ('The Register', "xAI fires legal rocket at Apple and OpenAI claiming they're locking out Grok", 'August 25, 2025',
         'https://www.theregister.com/2025/08/25/xai_apple_openai_lawsuit/'),
 'nano': ('Google', 'Introducing Gemini 2.5 Flash Image, our state-of-the-art image model', 'August 26, 2025', 'https://developers.googleblog.com/introducing-gemini-2-5-flash-image/'),
 'council': ('Anthropic', 'Introducing the Anthropic National Security and Public Sector Advisory Council', 'August 27, 2025',
             'https://www.anthropic.com/news/introducing-the-anthropic-national-security-and-public-sector-advisory-council'),
 'nvq2': ('Nasdaq (Zacks)', 'NVIDIA Q2 Earnings Beat, Stock Falls on Data Center Sales Miss', 'August 28, 2025',
          'https://www.nasdaq.com/articles/nvidia-q2-earnings-beat-stock-falls-data-center-sales-miss'),
 'nvq2b': ('Nasdaq', 'Nvidia Posts 56% Revenue Jump in Q2', 'August 2025', 'https://www.nasdaq.com/articles/nvidia-posts-56-revenue-jump-q2'),
 'mai': ('Microsoft AI', 'Two in-house models in support of our mission', 'August 28, 2025', 'https://microsoft.ai/news/two-new-in-house-models/'),
}

THEME = ('New Models, Evidence', [
 ('New models', ' arrived in several forms: routed reasoning systems, downloadable weights, visual representations and interactive worlds. '
  'GPT-5 drew broad attention, while releases from Anthropic, DeepSeek, Google, Meta and Microsoft served different tasks. Spending rose with them: '
  'technology companies raised their capital budgets, and cloud and licensing deals tied rivals together. Government pricing and developer tools widened access.'),
 ('Evidence', ' determined what could be said about these developments. Protein designs reached laboratory tests, and surveys of evolving agents examined '
  'learning through interaction. New obligations took effect in Europe, and attorneys general and a state investigation pressed companies on children\'s use of chatbots '
  'after reporting on Meta\'s internal rules. A chip-export deal and an antitrust suit showed how far AI had moved into trade and competition law. '
  'Each entry is dated and described as what it was at the time.'),
])

WEEKS = [
 (31, 'July 28–August 3', 'Original post published August 3, 2025', [
  ('GLM-4.5 joins the open-weight model field', 'July 28',
   ["Z.ai released GLM-4.5 and the smaller GLM-4.5-Air, with downloadable weights. The models combined reasoning, coding and tool use, with thinking "
    "and non-thinking modes. GLM-4.5 used a mixture-of-experts architecture with 355 billion total parameters and 32 billion active per token.{glm1}{glm2}",
    "The release gave developers another open-weight option for agent tasks; its design keeps the parameters active for each token far below the headline count."],
   ['Copilot', 'Kimi K2'], ['2025-W31-L2-5', '2025-W32-L4-5']),
  ('ChatGPT adds a guided study mode', 'July 29',
   ["OpenAI introduced study mode in ChatGPT. It used questions, hints and checks of understanding to guide students through a problem rather than "
    "simply supplying an answer. The first release relied on system instructions and was available to logged-in users across several subscription tiers.{study}",
    "The feature reorganized a tutoring exchange around the student's own reasoning."],
   ['Copilot'], ['2025-W31-L2-2']),
  ('Meta and Microsoft raise their AI spending', 'July 30',
   ["Reporting quarterly results, Meta set its 2025 capital-spending forecast at $66 billion to $72 billion and said 2026 would bring similarly large growth.{capex2} "
    "Microsoft projected more than $30 billion in capital expenditures and finance leases for its current quarter. The next day Meta's shares rose about 12 percent, "
    "and Microsoft's market value passed $4 trillion.{capex1}",
    "Spending on data centers had become the measure investors used to judge companies' AI ambitions."],
   ['Claude Sonnet 4', 'Perplexity', 'Llama 4'], ['2025-W31-L1-2', '2025-W31-L5-1', '2025-W31-L4-4']),
  ("OpenAI's annualized revenue reportedly reaches $12 billion", 'Reported July 30',
   ["*The Information* reported that OpenAI's annualized revenue run rate had roughly doubled since the start of 2025, to about $12 billion, or about "
    "$1 billion a month, with some 700 million weekly users of ChatGPT. Reuters could not confirm the report, and OpenAI declined to comment.{oairev}",
    "The figures, though unconfirmed, gave an outside measure of how fast paid use of AI was growing."],
   ['Claude Sonnet 4', 'Perplexity'], ['2025-W31-L1-4', '2025-W31-L5-2']),
  ("China approves its 'AI Plus' guidelines", 'July 31; published August 26',
   ["China's State Council approved guidelines to deepen its “AI Plus” initiative, calling for large-scale commercial use of AI across the "
    "economy.{aiplus} When published on August 26, the guidelines set targets for smart devices and AI agents to exceed 70 percent adoption by 2027 "
    "and 90 percent by 2030.{cset}",
    "The plan made adoption across the economy, rather than frontier capability alone, the measure of China's AI policy."],
   ['Claude Sonnet 4', 'GPT-5'], ['2025-W31-L1-3', '2025-W35-L1-5']),
  ('Stargate Norway sets out European computing plans', 'July 31',
   ["OpenAI announced Stargate Norway with Nscale and Aker. A joint venture of those two companies was expected to own and operate the facility, with "
    "OpenAI as an initial customer. Plans called for 100,000 Nvidia GPUs by the end of 2026.{norway}",
    "The project tied European demand for AI computing to the region's power and construction capacity; its scale was a target for 2026."],
   ['Claude Sonnet 4', 'Perplexity'], ['2025-W31-L1-1', '2025-W31-L5-5']),
  ("Anthropic cuts off OpenAI's access to Claude", 'Reported August 1',
   ["Anthropic withdrew OpenAI's access to its Claude models through the API. Anthropic said OpenAI's engineers had been using its coding tools ahead "
    "of the launch of GPT-5, in breach of terms that bar using Claude to build competing products, and that access for benchmarking and safety "
    "evaluations would continue. OpenAI called such testing standard industry practice.{anthoai}",
    "The dispute showed how closely the leading labs test their models against one another's."],
   ['Kimi K2'], ['2025-W31-L3-5']),
  ('EU general-purpose AI obligations begin to apply', 'August 2',
   ["The AI Act's obligations for providers of general-purpose AI models began to apply on August 2. Models already on the market before that date had "
    "a longer transition period. The Commission's guidance distinguished the start of these duties from its later enforcement powers.{gpai}",
    "This was one stage in a phased timetable; the voluntary Code of Practice offered one route to show compliance."],
   ['Copilot', 'Kimi K2', 'GPT-5', 'Gemini 2.5 Flash'], ['2025-W31-L2-1', '2025-W31-L3-3', '2025-W32-L1-2', '2025-W32-L2-2']),
 ]),
 (32, 'August 4–10', 'Original post published August 10, 2025', [
  ('Grok Imagine renews the argument over guardrails', 'August 5',
   ["xAI launched Grok Imagine, which turns generated images into short videos, for Premium subscribers in the Grok app. One of its presets, "
    "“spicy,” could produce sexually suggestive clips. After The Verge reported that the tool had generated such a video of a Taylor Swift "
    "lookalike without being asked, xAI restricted that content.{grokimg}",
    "The episode reopened the question of how much a generator should refuse, and who decides."],
   ['Gemini 2.5 Flash'], ['2025-W32-L2-5']),
  ('OpenAI releases gpt-oss model weights', 'August 5',
   ["OpenAI released gpt-oss-120b and gpt-oss-20b under the Apache 2.0 license. These text models supported reasoning and tool use, with weights "
    "available for developers to run and adapt outside OpenAI's hosted service.{gptoss}",
    "The release gave developers OpenAI models they could deploy and customize on their own hardware."],
   ['Grok 4'], ['2025-W32-L3-4']),
  ('Anthropic releases Claude Opus 4.1', 'August 5',
   ["Anthropic introduced Claude Opus 4.1 as an update focused on coding, reasoning and agentic tasks. It became available through paid Claude plans, "
    "Claude Code, Anthropic's API, Amazon Bedrock and Google Cloud's Vertex AI.{opus41}",
    "The update continued the labs' competition over models for long, multistep work such as software development."],
   ['Grok 4'], ['2025-W32-L3-2']),
  ('Genie 3 turns prompts into interactive environments', 'August 5',
   ["Google DeepMind introduced Genie 3 in a limited research preview. The world model generated environments that responded to users' actions and "
    "could sustain several minutes of interaction. Early access was restricted to a small group of academics and creators.{genie}",
    "DeepMind listed its limits, including restricted actions, imperfect geographic accuracy and difficulty simulating interactions among several agents."],
   ['Grok 4'], ['2025-W32-L3-3', '2025-W34-L3-2']),
  ('Jules leaves public beta', 'August 6',
   ["Google brought Jules, its asynchronous coding agent, out of public beta. The service used Gemini 2.5 Pro to develop coding plans and added "
    "improvements including GitHub issues integration and reuse of previous task setups. Higher usage limits came with paid Google AI plans.{jules}",
    "Coding agents that work in the background moved from preview to a general product."],
   ['Kimi K2'], ['2025-W32-L4-2']),
  ('Federal agencies gain $1 ChatGPT access', 'August 6',
   ["The US General Services Administration announced an agreement making ChatGPT Enterprise available to participating federal agencies for a nominal "
    "$1 per agency for one year. The arrangement also included introductory training and a temporary period of expanded model access.{gsa}",
    "The price removed a procurement barrier for agencies trying the tool."],
   ['GPT-5'], ['2025-W32-L1-4']),
  ('GPT-5 combines fast responses with deeper reasoning', 'August 7',
   ["OpenAI launched GPT-5. In ChatGPT, it described a system combining a fast model, a deeper reasoning model and a router that selected between them. "
    "The release began rolling out across ChatGPT tiers, with access limits varying by plan.{gpt5}",
    "The design built a choice about how much reasoning to spend on a question into the product itself."],
   ['GPT-5', 'Gemini 2.5 Flash', 'Grok 4', 'Kimi K2'], ['2025-W32-L1-1', '2025-W32-L2-1', '2025-W32-L3-1', '2025-W32-L4-1']),
  ('Research focus: MiroMind opens a research-agent stack', 'August 7',
   ["MiroMind introduced a research-agent stack comprising the MiroFlow orchestration framework, MiroThinker models and MiroVerse data and training "
    "tools. The release aimed to make the components of a deep-research workflow available for inspection and further development.{miro}",
    "Its system and model evaluations measured different configurations, which matters when comparing scores or reproducing results."],
   ['W.H.L.', 'Kimi K2'], ['2025-W32-L5-1']),
 ]),
 (33, 'August 11–17', 'Original post published August 17, 2025', [
  ('Nvidia and AMD agree to share China chip revenue with the US', 'August 11',
   ["President Donald Trump confirmed an agreement under which Nvidia and AMD would pay the US government 15 percent of their revenue from sales of "
    "certain AI chips to China, in return for export licenses for Nvidia's H20 and AMD's MI308, which had been blocked earlier in the year.{nvamd}",
    "The arrangement turned an export restriction into a revenue share, an unusual approach to trade control."],
   ['Gemini 2.5 Flash'], ['2025-W33-L1-2']),
  ('Cosmos Reason connects vision with physical reasoning', 'August 11',
   ["Nvidia introduced Cosmos Reason at SIGGRAPH as a vision-language model for physical AI. It was designed to reason about visual scenes using "
    "knowledge of physical relationships, alongside the company's simulation and synthetic-data tools.{cosmos}",
    "The model addressed one step in a robotics toolchain: interpreting the physical world before acting in it."],
   ['Copilot'], ['2025-W33-L4-2']),
  ('Anthropic offers Claude to all three branches of government for $1', 'August 12',
   ["Anthropic offered Claude for Enterprise and Claude for Government to civilian agencies of the executive branch, and to the legislative and "
    "judicial branches, for $1 for one year, with technical support for adoption.{anth1}",
    "Coming a week after OpenAI's similar offer, it showed the leading labs competing on price for government customers."],
   ['Grok 4'], ['2025-W33-L2-5']),
  ('Claude Sonnet 4 offers a million-token context window', 'August 12',
   ["Anthropic opened a one-million-token context window for Claude Sonnet 4 in public beta through its API. The expanded window allowed developers "
    "to submit substantially more material in a single request, including large codebases or document collections.{ctx1m}",
    "The change made long-context work a practical option on Anthropic's mid-sized model."],
   ['Grok 4'], ['2025-W33-L2-5', '2025-W34-L3-3']),
  ("Reporting exposes Meta's chatbot rules for children", 'August 14',
   ["Reuters reported on an internal Meta document, “GenAI: Content Risk Standards,” which had permitted its chatbots to engage children in "
    "conversations that were “romantic or sensual.” Meta confirmed the document was authentic, said those passages had been removed, and said "
    "its policies did not allow provocative behavior with children.{metarules}",
    "Child-safety advocates called on Meta to publish its revised rules so that parents could see how its chatbots treat children."],
   ['Gemini 2.5 Flash'], ['2025-W33-L1-3']),
  ('Cohere raises $500 million for enterprise AI', 'August 14',
   ["Cohere announced a $500 million funding round at a $6.8 billion valuation. The company said the capital would support expansion of its enterprise "
    "and sovereign AI business.{cohere}",
    "The round backed a strategy built on business and government customers rather than consumer chat."],
   ['Grok 4'], ['2025-W33-L2-1']),
  ('DINOv3 learns reusable features from images', 'August 14',
   ["Meta released DINOv3, a family of self-supervised vision models. Its image representations could support tasks such as classification, segmentation "
    "and tracking through lightweight adapters. The release included pretrained models and code under Meta's license.{dino}",
    "Self-supervised training reduced the need for labeled images, and the same features could serve many specialized applications."],
   ['Grok 4'], ['2025-W33-L2-2']),
  ('NSF and Nvidia back open models for science', 'August 14',
   ["The US National Science Foundation announced $75 million for the Open Multimodal AI Infrastructure to Accelerate Science project, with Nvidia "
    "providing an additional $77 million. Led by the Allen Institute for AI, the project would develop open models trained on scientific data and literature.{nsf}",
    "The funding committed support for open models built for researchers; the models themselves were still to be developed."],
   ['Gemini 2.5 Flash'], ['2025-W33-L1-4']),
 ]),
 (34, 'August 18–24', 'Original post published August 24, 2025', [
  ('Texas investigates Meta and Character.AI over mental-health claims', 'August 18',
   ["Texas Attorney General Ken Paxton opened an investigation into Meta's AI Studio and Character.AI over concerns that chatbots on the platforms were "
    "presented as mental-health professionals in ways that could mislead users, including children.{texas}",
    "State regulators began applying consumer-protection law to companion chatbots."],
   ['Kimi K2'], ['2025-W34-L4-5']),
  ('Research focus: what can an agent change?', 'Background: July 28; selected August 24 at the editor’s request',
   ["A survey by Huan-ang Gao and colleagues organized work on self-evolving agents around what changes, when changes occur and how they are guided. "
    "The components included models, context, tools and agent architectures.{gao}",
    "The framework separated changes to an agent's working context from changes to its model or design, and mapped open research directions."],
   ['W.H.L.', 'Claude Sonnet 4'], ['2025-W34-L1-HM1']),
  ('Research focus: learning from agent interactions', 'Background: August 10; selected August 24 at the editor’s request',
   ["Jinyuan Fang and colleagues surveyed methods for improving agents through interaction data and environmental feedback. Their framework connected "
    "the inputs, agent system and environment with the mechanisms used to optimize behavior.{fang}",
    "The review placed adaptation within a continuing cycle of action and feedback, and made evaluation a central question."],
   ['W.H.L.', 'Claude Sonnet 4'], ['2025-W34-L1-HM2']),
  ('Acrobat Studio combines documents, AI and design', 'August 19',
   ["Adobe launched Acrobat Studio, bringing Acrobat's document tools together with Adobe Express and AI assistants. PDF Spaces let users collect "
    "documents and web pages, ask questions across them and share the resulting workspace.{acrobat}",
    "The product combined reading, synthesis and content creation in one workspace."],
   ['Kimi K2'], ['2025-W34-L4-2']),
  ('Meta pauses hiring for its AI division', 'Reported August 20',
   ["The *Wall Street Journal* reported that Meta had frozen hiring in its AI division after adding more than 50 researchers and engineers. A Meta "
    "spokesperson described the pause as routine organizational planning for its superintelligence effort.{hiring}",
    "The pause followed months of unusually expensive recruiting for frontier AI talent."],
   ['Claude Sonnet 4'], ['2025-W34-L1-1']),
  ('DeepSeek-V3.1 combines thinking and non-thinking modes', 'August 21',
   ["DeepSeek released V3.1 with downloadable weights and a hybrid design supporting thinking and non-thinking responses. Both API modes offered a "
    "128,000-token context window, and the company reported improvements in tool use and multistep tasks.{dsv31}",
    "The release brought a reasoning mode and ordinary responses into one model."],
   ['Grok 4', 'GPT-5 (via Copilot)'], ['2025-W34-L3-1', '2025-W34-L5-5']),
  ('Google expands AI Mode to more countries', 'August 21',
   ["Google announced that AI Mode in Search was expanding in English to more than 180 additional countries and territories. The conversational "
    "search interface supported longer questions and follow-up exchanges.{aimode}",
    "Experimental agentic features announced at the same time remained more narrowly available."],
   ['Kimi K2'], ['2025-W34-L4-3']),
  ('Meta signs a cloud deal with Google', 'Reported August 22',
   ["Reuters, following *The Information*, reported that Meta had signed a six-year cloud-computing deal with Google worth more than $10 billion, "
    "covering servers, storage, networking and other services. Neither company commented.{metagoog}",
    "Meta, which builds much of its own infrastructure, turned to a competitor's cloud for additional capacity."],
   ['Gemini 2.5 Flash'], ['2025-W34-L2-2']),
  ('A specialized GPT model proposes reprogramming proteins', 'August 22',
   ["OpenAI and Retro Biosciences described GPT-4b micro, an experimental model adapted for protein engineering. They reported that redesigned "
    "proteins increased expression of stem-cell reprogramming markers in laboratory cell experiments compared with unmodified controls.{retro}",
    "The work linked generated protein sequences with laboratory testing at an early, cell-based stage."],
   ['Kimi K2'], ['2025-W34-L4-1']),
  ("Meta licenses Midjourney's image technology", 'August 22',
   ["Alexandr Wang, Meta's chief AI officer, announced that Meta would license Midjourney's “aesthetic technology” for its future models and "
    "products. Terms were not disclosed.{midj}",
    "Meta supplemented its own models with technology from an independent image lab."],
   ['Kimi K2'], ['2025-W34-L4-4']),
 ]),
 (35, 'August 25–31', 'Original post published August 31, 2025', [
  ('Attorneys general press AI companies on child safety', 'August 25',
   ["A coalition of 44 state attorneys general sent AI companies a letter raising concerns about children's interactions with chatbots. It called for "
    "stronger safeguards against inappropriate and harmful content and warned that existing legal powers could be used to protect young users.{naag}",
    "The letter signaled coordinated attention from state law enforcement to children's use of chatbots."],
   ['GPT-5'], ['2025-W35-L1-4', '2025-W35-L5-1']),
  ('xAI sues Apple and OpenAI', 'August 25',
   ["xAI and X sued Apple and OpenAI in federal court in Texas, alleging that Apple's agreement to integrate ChatGPT and its App Store practices "
    "unlawfully favored OpenAI and held back rivals such as Grok. OpenAI said the filing was consistent with what it called Musk's pattern of harassment.{xai}",
    "The suit carried the competition among AI assistants into antitrust law."],
   ['DeepSeek-V3.1'], ['2025-W35-L7-2']),
  ('Nano Banana adds targeted image editing', 'August 26',
   ["Google introduced Gemini 2.5 Flash Image, also known as Nano Banana. The model could combine images and make edits from natural-language "
    "instructions, with an emphasis on preserving a subject's appearance. It was available in preview through Google's developer tools.{nano}",
    "The release made iterative editing a central use of image generation; Google noted remaining limits in text rendering, fine detail and consistency."],
   ['Gemini 2.5 Flash'], ['2025-W35-L9-3']),
  ('Anthropic forms a public-sector advisory council', 'August 27',
   ["Anthropic announced a National Security and Public Sector Advisory Council. Its members included former senators and officials from defense, "
    "intelligence, energy and justice institutions. The group would advise on applications and public-private partnerships.{council}",
    "The council gave Anthropic a standing source of advice from former officials as it sought government work."],
   ['GPT-5'], ['2025-W35-L1-2', '2025-W35-L3-1']),
  ("Nvidia's results meet a market braced for more", 'August 27',
   ["Nvidia reported quarterly revenue of $46.7 billion, up 56 percent from a year earlier, including $41.1 billion from data centers, and forecast "
    "about $54 billion for the next quarter. It recorded no H20 sales to China and assumed none in its outlook.{nvq2b} Its shares fell about 3 percent "
    "in after-hours trading as data-center revenue came in slightly below analysts' estimates.{nvq2}",
    "Even record results were judged against very high expectations for AI spending."],
   ['DeepSeek-V3.1'], ['2025-W35-L7-1']),
  ('Microsoft previews two in-house models', 'August 28',
   ["Microsoft AI introduced MAI-Voice-1 for speech generation and began public testing of MAI-1-preview on LMArena. MAI-Voice-1 was already used "
    "in Copilot Daily and Podcasts, while the text model was being evaluated ahead of product integration.{mai}",
    "The releases showed Microsoft building more of the models behind its products alongside its partnership with OpenAI."],
   ['GPT-5', 'Gemini 2.5 Flash'], ['2025-W35-L1-1', '2025-W35-L2-1', '2025-W35-L9-2']),
 ]),
]
