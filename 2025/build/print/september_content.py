# September 2025 print chapter, v0.2: content (American style).
# Each entry: code suffix, title, dateline, body paragraphs (with {src} markers), selectors, master IDs.

COVERS = 'Edited from four posts published in September 2025, covering September 1–28.'

SOURCES = {
 'apertus': ('ETH Zurich', 'Apertus: a fully open, transparent, multilingual language model', 'September 2, 2025',
             'https://ethz.ch/en/news-and-events/eth-news/news/2025/09/press-release-apertus-a-fully-open-transparent-multilingual-language-model.html'),
 'promptlock': ('ESET / WeLiveSecurity', 'First known AI-powered ransomware uncovered by ESET Research', 'August 26, 2025; updated September 3',
             'https://www.welivesecurity.com/en/ransomware/first-known-ai-powered-ransomware-uncovered-eset-research/'),
 'hunger': ('TechSpot', 'Activists launch hunger strikes outside DeepMind and Anthropic offices over race to build advanced AI', 'September 8, 2025',
             'https://www.techspot.com/news/109368-activists-launch-hunger-strikes-outside-anthropic-deepmind-offices.html'),
 'jobs': ('OpenAI', 'Expanding economic opportunity with AI', 'September 4, 2025',
             'https://openai.com/index/expanding-economic-opportunity-with-ai/'),
 'wh': ('Government Executive', 'Agencies and industry announce efforts to further Presidential AI Challenge', 'September 5, 2025',
             'https://www.govexec.com/technology/2025/09/agencies-and-industry-announce-efforts-further-presidential-ai-challenge/407929/'),
 'wbd': ('Los Angeles Magazine', 'Warner Bros. Discovery Sues Midjourney for Copyright Infringement Over AI Use of Iconic Characters', 'September 5, 2025',
             'https://lamag.com/news/warner-bros-discovery-sues-midjourney-for-copyright-infringement-over-ai-use-of-iconic-characters/'),
 'ftchip': ('Outlook Business, reporting the Financial Times', 'OpenAI to Build its Own AI Chip with Broadcom, Aims to Ship in 2026', 'September 5, 2025',
             'https://www.outlookbusiness.com/artificial-intelligence/openai-to-build-its-own-ai-chip-with-broadcom-aims-to-ship-in-2026'),
 'halluc': ('OpenAI', 'Why language models hallucinate', 'September 5, 2025',
             'https://openai.com/index/why-language-models-hallucinate/'),
 'aap': ('Association of American Publishers', 'Frequently Asked Questions re Proposed Settlement in Bartz v. Anthropic', 'September 5, 2025',
             'https://publishers.org/wp-content/uploads/2025/09/FAQS-Anthropic-September-5-2025-1.pdf'),
 'ag': ('Authors Guild', 'Anthropic Settlement: Key Updates', 'updates of September 8–25, 2025',
             'https://authorsguild.org/news/anthropic-settlement-key-updates/'),
 'critterz': ('Entrepreneur', 'An AI-Made Animated Feature Film Backed By OpenAI Is Premiering Next Year', 'September 8, 2025',
             'https://www.entrepreneur.com/business-news/an-openai-backed-ai-made-animated-movie-is-coming-out-next/496853'),
 'critterz2': ('PetaPixel', 'OpenAI is Developing a Feature-Length Animated Movie Using AI Technology', 'September 10, 2025',
             'https://petapixel.com/2025/09/10/openai-plans-to-make-a-full-hollywood-movie-animated-critterz-using-ai'),
 'aimode': ('TechCrunch', "Google's AI Mode adds 5 new languages including Hindi, Japanese, and Korean", 'September 8, 2025',
             'https://techcrunch.com/2025/09/08/googles-ai-mode-adds-5-new-languages-including-hindi-japanese-and-korean'),
 'wiener': ('California State Senator Scott Wiener', "Senator Wiener's Landmark Responsible AI Innovation Bill Advances to Final Vote", 'September 8, 2025',
             'https://sd11.senate.ca.gov/news/senator-wieners-landmark-responsible-ai-innovation-bill-advances-final-vote'),
 'dpa': ('Digital Policy Alert', 'California Legislature adopts the Transparency in Frontier Artificial Intelligence Act (SB 53)', 'event of September 13, 2025',
             'https://digitalpolicyalert.org/event/33866-act-on-frontier-artificial-intelligence-models-and-whistleblower-protections-including-artificial-intelligence-authority-governance-sb-53-was-adopted-by-california-legislature'),
 'gov': ('Office of Governor Gavin Newsom', "Governor Newsom signs SB 53, advancing California's world-leading artificial intelligence industry", 'September 29, 2025',
             'https://www.gov.ca.gov/2025/09/29/governor-newsom-signs-sb-53-advancing-californias-world-leading-artificial-intelligence-industry/'),
 'ftc': ('US Federal Trade Commission', 'FTC Launches Inquiry into AI Chatbots Acting as Companions', 'September 11, 2025',
             'https://www.ftc.gov/news-events/news/press-releases/2025/09/ftc-launches-inquiry-ai-chatbots-acting-companions'),
 'hassabis': ('Associated Press (via WJXT)', "Google's top AI scientist says 'learning how to learn' will be next generation's most needed skill", 'September 12, 2025',
             'https://www.news4jax.com/tech/2025/09/12/googles-top-ai-scientist-says-learning-how-to-learn-will-be-next-generations-most-needed-skill/'),
 'youtube': ('YouTube', 'The next 20: Powering the future of entertainment together at Made on YouTube', 'September 16, 2025',
             'https://blog.youtube/news-and-events/made-on-youtube-2025/'),
 'nature': ('Daya Guo and colleagues / Nature', 'DeepSeek-R1 incentivizes reasoning in LLMs through reinforcement learning', 'September 17, 2025',
             'https://www.nature.com/articles/s41586-025-09422-z'),
 'icpc': ('Google DeepMind', 'Gemini achieves gold-medal level at the International Collegiate Programming Contest World Finals', 'September 17, 2025',
             'https://deepmind.google/blog/gemini-achieves-gold-medal-level-at-the-international-collegiate-programming-contest-world-finals/'),
 'meta': ('Meta', 'Introducing Meta Ray-Ban Display: AI Glasses With an EMG Wristband', 'September 17, 2025; page updated September 30',
             'https://about.fb.com/news/2025/09/meta-ray-ban-display-ai-glasses-emg-wristband/'),
 'embl': ('European Molecular Biology Laboratory', 'AI model forecasts disease risk decades in advance', 'September 17, 2025',
             'https://www.embl.org/news/science-technology/ai-model-forecasts-disease-risk-decades-in-advance/'),
 'icmp': ('AFP (via The Jakarta Post)', "Music industry group says AI firms guilty of 'wilful' copyright theft", 'September 18, 2025',
             'https://www.thejakartapost.com/culture/2025/09/18/music-industry-group-says-ai-firms-guilty-of-wilful-copyright-theft.html'),
 'chrome': ('Google', 'Chrome, reimagined with AI', 'September 18, 2025',
             'https://blog.google/products-and-platforms/products/chrome/chrome-reimagined-with-ai/'),
 'nvintel': ('Nvidia', 'NVIDIA and Intel to Develop AI Infrastructure and Personal Computing Products', 'September 18, 2025',
             'https://nvidianews.nvidia.com/news/nvidia-and-intel-to-develop-ai-infrastructure-and-personal-computing-products'),
 'oainv': ('OpenAI', 'OpenAI and NVIDIA announce strategic partnership to deploy 10 gigawatts of NVIDIA systems', 'September 22, 2025',
             'https://openai.com/index/openai-nvidia-systems-partnership/'),
 'tii': ('Technology Innovation Institute', "Abu Dhabi's TII and NVIDIA Launch Middle East's First Joint AI & Robotics NVAITC Research Lab", 'September 22, 2025',
             'https://www.tii.ae/news/abu-dhabis-tii-and-nvidia-launch-middle-easts-first-joint-ai-robotics-nvaitc-research-lab'),
 'gsa': ('US General Services Administration', 'GSA, Meta Collaborate on AI Adoption', 'September 22, 2025',
             'https://www.gsa.gov/about-gsa/newsroom/news-releases/gsa-meta-collaborate-on-ai-adoption-09222025'),
 'riverwood': ('Riverwood Capital', 'AppZen Raises $180 Million Growth Round Led by Riverwood Capital to Take the Next Step in Autonomous Finance', 'September 22, 2025',
             'https://www.riverwoodcapital.com/rwcm_news/appzen-raises-180-million-growth-round-led-by-riverwood-capital-to-take-the-next-step-in-autonomous-finance/'),
 'appzen': ('AppZen', "AppZen's AI Agents are redefining finance operations (again)", 'funding announcement; date corroborated by Riverwood, September 22',
             'https://www.appzen.com/blog/appzen-ai-agent-studio-redefining-finance-operations-again'),
 'deepseek': ('DeepSeek', 'DeepSeek-V3.1-Terminus Release', 'September 22, 2025',
             'https://api-docs.deepseek.com/news/news250922/'),
 'stargate': ('OpenAI', 'Five new Stargate sites', 'September 23, 2025; page later updated',
             'https://openai.com/index/five-new-stargate-sites/'),
 'altman': ('TechSpot', 'Sam Altman predicts Artificial General Intelligence by 2030, says AI will take over 40% of tasks', 'September 26, 2025',
             'https://www.techspot.com/news/109644-sam-altman-predicts-artificial-general-intelligence-2030-ai.html'),
}

THEME = ('Adoption, Accountability', [
 ('Adoption', ' brought AI into browsers, search, video tools, finance departments and government procurement. '
  'New releases made models easier to inspect and use, and research reached programming contests, disease risk and the '
  'peer-reviewed literature. Behind these applications, proposed partnerships set out plans for a far larger computing infrastructure.'),
 ('Accountability', ' concerned what happened as these systems reached people. Regulators examined companion chatbots, '
  'California passed a disclosure law for frontier AI, and authors, studios and music publishers pressed claims over the material '
  'used to build AI systems. Protesters took their concerns to company doors. The entries mix finished products, announced plans '
  'and research results; each is dated and described as what it was at the time.'),
])

WEEKS = [
 (36, 'September 1–7', 'Original post published September 7, 2025', [
  ('Hunger strikes target Anthropic and Google DeepMind', 'From early September; reported September 8',
   ["Activists began hunger strikes outside two AI developers. By September 8, Guido Reichstadter had gone just over a week without food "
    "outside Anthropic's San Francisco office, and Michael Trazzi more than three days outside Google DeepMind's London headquarters.{hunger}",
    "Reichstadter asked Anthropic to stop frontier AI development. Trazzi asked DeepMind's chief executive to commit to releasing no further "
    "frontier models if the other leading labs also stopped. The protests took public concern about advanced AI from open letters to the companies' doors."],
   ['GPT-5'], ['2025-W36-L4-1']),
  ('Apertus opens a multilingual model for inspection', 'September 2',
   ["ETH Zurich, EPFL and the Swiss National Supercomputing Centre released Apertus in 8-billion- and 70-billion-parameter versions. "
    "The project published the model weights with documentation of its architecture, training data and methods. Its training material "
    "covered more than 1,000 languages.{apertus}",
    "Apertus treated openness as more than released weights: researchers and developers could examine how the system was built and adapt it under a permissive license."],
   ['Copilot'], ['2025-W36-L1-1']),
  ('PromptLock shows how language models could enter malware', 'Updated September 3; first reported August 26',
   ["ESET first described PromptLock on August 26 as AI-powered ransomware. On September 3 it updated its account: the code was a proof of concept "
    "from an academic study, whose authors had contacted ESET's researchers. The software used a language model to generate scripts within a ransomware prototype.{promptlock}",
    "The case showed how a language model could write malicious code on demand, and why a sample's origin matters when judging a new threat."],
   ['Copilot'], ['2025-W36-L1-5']),
  ('OpenAI plans a jobs platform and AI certifications', 'September 4',
   ["OpenAI announced plans for a jobs platform to connect employers with people who have AI skills, and for a certification program in AI skills. "
    "Both formed part of its stated work on economic opportunity and workforce preparation.{jobs}",
    "The plans tied AI adoption to hiring and training, a field long served by established recruitment platforms."],
   ['Grok 4'], ['2025-W36-L3-4']),
  ('A White House task force advances an AI education challenge', 'September 4',
   ["At the second meeting of the White House Task Force on Artificial Intelligence Education, hosted by First Lady Melania Trump, cabinet officials "
    "set out next steps for the Presidential AI Challenge, including toolkits, classroom guides and training materials. Alphabet's chief executive, "
    "Sundar Pichai, described a billion-dollar commitment to AI education and workforce training.{wh}",
    "The meeting joined federal agencies and technology companies in a push for AI literacy in schools and the workforce."],
   ['Grok 4'], ['2025-W36-L3-2']),
  ('Warner Bros. Discovery sues Midjourney', 'September 4',
   ["Warner Bros. Discovery filed a copyright lawsuit against the image generator Midjourney in federal court in California. The complaint alleged "
    "that Midjourney let users generate images of the studio's characters, including Batman and Scooby-Doo, without permission, and chose not to use "
    "measures that could have prevented it.{wbd}",
    "The suit followed similar cases brought by Disney and Universal earlier in the summer, making Warner Bros. Discovery the third major studio to sue."],
   ['Grok 4'], ['2025-W36-L3-3']),
  ('OpenAI is reported to be building a chip with Broadcom', 'Reported September 5',
   ["The *Financial Times* reported that OpenAI was working with Broadcom on a custom AI chip, with the first chips expected to ship in 2026 for "
    "OpenAI's own data centers rather than for sale. Neither company confirmed the arrangement. On an earnings call, Broadcom's chief executive "
    "said an unnamed customer had placed substantial production orders.{ftchip}",
    "The reported aim was to reduce OpenAI's reliance on Nvidia's processors for part of its computing needs."],
   ['GPT-5'], ['2025-W36-L4-5']),
  ('Research examines why models guess instead of abstaining', 'September 5',
   ["OpenAI published research on why language models produce plausible but false answers. It argued that training and evaluation practices can "
    "reward guessing over acknowledging uncertainty: accuracy scores that give no credit for abstaining hide the difference between an honest "
    "“I don't know” and a confident error.{halluc}",
    "The analysis made the handling of uncertainty part of how a model is judged. Improving a benchmark score and reducing the harm of a wrong answer can call for different incentives."],
   ['DeepSeek-V3.1'], ['2025-W36-L2-1']),
  ('Anthropic agrees to settle authors’ piracy claims', 'September 5; hearing September 8',
   ["A proposed settlement in *Bartz v. Anthropic* provided at least $1.5 billion to resolve claims over books Anthropic had obtained from pirated "
    "collections. The Association of American Publishers set out the agreement and its claims process on September 5.{aap} At a September 8 hearing, "
    "Judge William Alsup asked the parties for more detail before ruling. He granted preliminary approval on September 25.{ag}",
    "The claims concerned how the books were obtained, not whether training AI models on them was lawful."],
   ['Grok 4', 'Gemini 2.5 Flash'], ['2025-W36-L3-1', '2025-W37-L2-2']),
  ('OpenAI backs an animated feature made with its tools', 'Reported September 7',
   ["The *Wall Street Journal* reported that OpenAI was supporting Critterz, an animated feature conceived by Chad Nelson, a creative specialist at "
    "OpenAI, and produced with Vertigo Films and Native Foreign. The film was to be made with OpenAI's image and language models in about nine months, "
    "on a budget under $30 million, with a premiere planned for the Cannes Film Festival in May 2026.{critterz}{critterz2}",
    "The project was conceived as a public demonstration of generative tools in feature animation."],
   ['GPT-5'], ['2025-W36-L4-4']),
 ]),
 (37, 'September 8–14', 'Original post published September 14, 2025', [
  ("Google's AI Mode adds five languages", 'September 8',
   ["Google extended AI Mode, its conversational search feature built on a customized version of Gemini 2.5, to Hindi, Indonesian, Japanese, "
    "Korean and Brazilian Portuguese.{aimode}",
    "The expansion brought AI-generated search answers to speakers of five more languages."],
   ['DeepSeek-V3.1'], ['2025-W37-L3-5']),
  ("California passes SB 53, a frontier-AI disclosure law", 'September 8 amendments; passed September 13',
   ["Senator Scott Wiener announced final amendments to SB 53, the Transparency in Frontier Artificial Intelligence Act, on September 8.{wiener} "
    "The Legislature passed the bill on September 13,{dpa} and Governor Gavin Newsom signed it on September 29. The law requires large frontier "
    "developers to publish safety frameworks and report critical safety incidents, protects whistleblowers, and creates a consortium to plan a "
    "public computing cluster.{gov}",
    "The law made disclosure, incident reporting and whistleblower protection the core of California's approach to frontier AI."],
   ['Gemini 2.5 Flash'], ['2025-W37-L2-1', '2025-W38-L3-2']),
  ('FTC opens an inquiry into companion chatbots', 'September 11',
   ["The US Federal Trade Commission issued orders to seven companies operating AI chatbots, seeking information on how companion-like services "
    "were developed, tested and monitored, including their effects on children and teenagers and their handling of personal information.{ftc}",
    "The orders gathered information under the FTC's study authority, separate from any enforcement action."],
   ['GPT-5'], ['2025-W37-L1-1']),
  ('Hassabis calls learning how to learn the key skill', 'September 12',
   ["Speaking in Athens, Google DeepMind's chief executive, Demis Hassabis, said the pace of AI would require people to keep learning throughout "
    "their careers, and that learning how to learn would be among the most important skills for the next generation.{hassabis}",
    "The remarks placed adaptability, rather than any single technical skill, at the center of education for an AI economy."],
   ['Gemini 2.5 Flash'], ['2025-W37-L2-3']),
 ]),
 (38, 'September 15–21', 'Original post published September 22, 2025', [
  ('YouTube brings generated video and sound to Shorts', 'September 16',
   ["At Made on YouTube, the company announced the rollout of Veo 3 Fast for Shorts, which generates clips with sound. It also previewed editing tools "
    "intended to turn raw footage into a first draft and help creators develop videos.{youtube}",
    "The announcements placed generation tools inside a major platform's publishing workflow, some available at launch and others to follow."],
   ['ChatGPT'], ['2025-W38-L1-5']),
  ('DeepSeek-R1 research appears in *Nature*', 'September 17',
   ["*Nature* published DeepSeek's research on reinforcement learning for language-model reasoning. The paper described methods and evaluations "
    "involving mathematical, coding and other reasoning tasks, as well as transferring capabilities to smaller models through distillation.{nature}",
    "The peer-reviewed paper gave a fuller account of how a model released in January had been trained."],
   ['ChatGPT'], ['2025-W38-L1-1']),
  ('Gemini reaches gold-medal level in programming', 'Reported September 17; contest held September 4',
   ["Google DeepMind reported that an advanced version of Gemini 2.5 Deep Think solved 10 of 12 problems from the ICPC World Finals. The system worked "
    "remotely within the five-hour contest window under arrangements with the organizers, and its score reached the gold-medal level.{icpc}",
    "The result measured performance on demanding programming problems under contest conditions. It came from a research version of the model, not the one offered to users."],
   ['ChatGPT', 'Gemini 2.5 Flash'], ['2025-W38-L1-4', '2025-W38-L3-1']),
  ('Meta announces display glasses with wristband control', 'September 17',
   ["Meta introduced Ray-Ban Display glasses and a wristband that interprets muscle signals to control them. The glasses can show information such "
    "as messages and translations. Meta said sales would begin at selected US retailers on September 30.{meta}",
    "The design paired a small in-lens display with an input method that leaves the hands largely free."],
   ['ChatGPT'], ['2025-W38-L1-3']),
  ('Delphi models long-term disease risk', 'September 17',
   ["Researchers introduced Delphi-2M, a model that estimates the risk of more than 1,000 diseases from health histories. It was trained using "
    "about 400,000 UK Biobank participants and tested on records from 1.9 million people in Denmark.{embl}",
    "Its developers described it as a proof of concept, not yet ready for clinical use; its estimates describe risk across populations, not individual diagnoses."],
   ['Gemini 2.5 Flash'], ['2025-W38-L3-5']),
  ('Music publishers accuse AI companies of copyright theft', 'Reported September 18; findings first published September 9',
   ["The International Confederation of Music Publishers accused generative AI companies, including OpenAI, Suno, Udio and Mistral, of “wilful, "
    "commercial-scale copyright infringement,” citing an investigation into the scraping of music and lyrics. Its director general, John Phelan, "
    "said the companies were “engaged in the largest copyright infringement exercise that has been seen.”{icmp}",
    "The publishers used the findings to press for stronger transparency rules, including under the EU's AI Act."],
   ['Gemini 2.5 Flash'], ['2025-W38-L3-4']),
  ('Gemini expands its role inside Chrome', 'September 18',
   ["Google announced a wider rollout of Gemini in Chrome for English-language users on Mac and Windows in the United States. The assistant could "
    "help interpret pages and work across multiple tabs. More autonomous actions, such as completing purchases, were announced for later.{chrome}",
    "The browser became a place to read, compare and act across the web with an assistant built in."],
   ['ChatGPT'], ['2025-W38-L1-2']),
  ('Nvidia and Intel plan joint computing products', 'September 18',
   ["Nvidia and Intel announced plans to develop data-center and personal-computing products together, connecting Intel's x86 processors with "
    "Nvidia technology. Nvidia also agreed to invest $5 billion in Intel common stock, with closing subject to customary conditions, including "
    "regulatory approval.{nvintel}",
    "The partnership joined two long-standing competitors' technologies in planned products for data centers and PCs."],
   ['Gemini 2.5 Flash'], ['2025-W38-L3-3']),
 ]),
 (39, 'September 22–28', 'Original post published September 28, 2025', [
  ('Nvidia and OpenAI outline a large infrastructure partnership', 'September 22',
   ["OpenAI and Nvidia signed a letter of intent for systems providing at least 10 gigawatts of AI computing infrastructure. Nvidia intended to invest "
    "up to $100 billion progressively as that capacity was deployed. Details of the partnership were still to be finalized.{oainv}",
    "The announcement tied staged investment to the construction of computing capacity."],
   ['Qwen3-Max'], ['2025-W39-L5-1']),
  ('TII and Nvidia establish an AI robotics research lab', 'September 22',
   ["Abu Dhabi's Technology Innovation Institute and Nvidia announced a joint research laboratory within Nvidia's AI Technology Center program. "
    "Its work would address AI and robotics, including robot learning, control and the integration of TII's Falcon models.{tii}",
    "The lab extended the institute's language-model research into robotics."],
   ['GPT-5'], ['2025-W39-L1-2']),
  ('GSA and Meta arrange federal access to Llama', 'September 22',
   ["The US General Services Administration announced a collaboration with Meta to make Llama models available to federal agencies through its "
    "OneGov initiative, on agreed terms for government use.{gsa}",
    "The arrangement gave agencies a common route to an open-weight model family; each agency still decides which tasks it suits."],
   ['GPT-5'], ['2025-W39-L1-3']),
  ('AppZen raises $180 million for finance automation', 'September 22',
   ["AppZen announced $180 million in growth funding led by Riverwood Capital. The company develops AI tools for finance operations, including "
    "expense auditing and accounts payable, and said the funding would support its next stage of expansion.{riverwood}{appzen}",
    "The round reflected investor interest in AI agents built for a single business function."],
   ['Gemini 2.5 Flash'], ['2025-W39-L7-2']),
  ('DeepSeek updates V3.1 with Terminus', 'September 22',
   ["DeepSeek released V3.1-Terminus through its app, website and API, with model weights also available. The company described improvements to "
    "language consistency and fewer unexpected characters, alongside updates to coding and search-agent behavior.{deepseek}",
    "The release concentrated on reliability within an existing model family, refinements that matter in daily use."],
   ['W.H.L.', 'Kimi K2'], ['2025-W39-L8-1']),
  ('Stargate announces five additional US sites', 'September 23',
   ["OpenAI, Oracle and SoftBank announced five additional US data-center sites for Stargate. With previously announced projects, OpenAI said the "
    "plans brought the program to nearly seven gigawatts of planned capacity and more than $400 billion of investment over three years.{stargate}",
    "The figures described an infrastructure program under development, dependent on construction, power supply and equipment arriving over time."],
   ['GPT-5'], ['2025-W39-L1-1']),
  ('Altman puts a figure on AI’s share of economic tasks', 'Reported September 26',
   ["In an interview in Berlin for the Axel Springer Global Reporters Network, OpenAI's chief executive, Sam Altman, was reported as expecting AI to "
    "perform 30 to 40 percent of the tasks in the economy before long. He said he would be “very surprised” if models were not "
    "“extraordinarily capable” by 2030.{altman}",
    "The estimate was a forecast, not a measurement, and it gave a public marker against which later progress can be compared."],
   ['Gemini 2.5 Flash'], ['2025-W39-L7-1']),
 ]),
]
