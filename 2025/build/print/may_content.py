# May 2025 print chapter, v0.2: content (American style).
COVERS = 'Edited from four posts published in May 2025, covering April 28–May 25.'

SOURCES = {
'senstrike': ('Office of Senator Edward J. Markey', 'After weeks of Markey raising the alarm, Senate strikes AI moratorium from budget reconciliation bill overnight in overwhelming 99-1 vote', 'July 1, 2025',
              'https://www.markey.senate.gov/news/press-releases/after-weeks-of-markey-raising-the-alarm-senate-strikes-ai-moratorium-from-budget-reconciliation-bill-overnight-in-overwhelming-99-1-vote'),
 'wsfall': ('TechCrunch', "Windsurf's CEO goes to Google; OpenAI's acquisition falls apart", 'July 11, 2025', 'https://techcrunch.com/2025/07/11/windsurfs-ceo-goes-to-google-openais-acquisition-falls-apart/'),
 'elsa': ('US Food and Drug Administration', 'FDA Launches Agency-Wide AI Tool to Optimize Performance for the American People', 'June 2, 2025',
          'https://www.fda.gov/news-events/press-announcements/fda-launches-agency-wide-ai-tool-optimize-performance-american-people'),
 'arena': ('Shivalika Singh and colleagues', 'The Leaderboard Illusion', 'April 29, 2025; version 1', 'https://arxiv.org/html/2504.20879v1'),
 'metaapp': ('Meta', 'Introducing the Meta AI App: A New Way to Access Your AI Assistant', 'April 29, 2025; launch section of subsequently updated page',
             'https://about.fb.com/news/2025/04/introducing-meta-ai-app-new-way-access-ai-assistant/'),
 'llama': ('TechCrunch', 'Meta says its Llama AI models have been downloaded 1.2B times', 'April 29, 2025',
           'https://techcrunch.com/2025/04/29/meta-says-its-llama-ai-models-have-been-downloaded-1-2b-times/'),
 'syc1': ('OpenAI', "Sycophancy in GPT-4o: what happened and what we're doing about it", 'April 29, 2025', 'https://openai.com/index/sycophancy-in-gpt-4o/'),
 'syc2': ('OpenAI', 'Expanding on what we missed with sycophancy', 'May 2, 2025', 'https://openai.com/index/expanding-on-sycophancy/'),
 'waymo': ('Waymo and Toyota', 'Waymo and Toyota Outline Strategic Partnership to Advance Autonomous Driving Deployment', 'April 29, 2025',
           'https://waymo.com/blog/2025/04/waymo-and-toyota-outline-strategic-partnership/'),
 'phi': ('Microsoft Azure', 'One year of Phi: Small language models making big leaps in AI', 'April 30, 2025; original announcement',
         'https://azure.microsoft.com/en-us/blog/one-year-of-phi-small-language-models-making-big-leaps-in-ai/'),
 'nova': ('Amazon Web Services', 'Amazon Nova Premier, our most capable model for complex tasks and teacher for model distillation', 'April 30, 2025',
          'https://aws.amazon.com/about-aws/whats-new/2025/04/amazon-nova-premier-complex-tasks-model-distillation/'),
 'pope': ('NPR (via OPB)', 'Catholic leaders criticize Trump for posting apparent AI photo of himself as the pope', 'May 4, 2025',
          'https://www.opb.org/article/2025/05/04/catholic-leaders-criticize-trump-for-posting-apparent-ai-photo-of-himself-as-the-pope/'),
 'oaistruct': ('OpenAI', "Evolving OpenAI's structure", 'May 5, 2025', 'https://openai.com/index/evolving-our-structure/'),
 'windsurf': ('Reuters (via The Kathmandu Post)', 'OpenAI agrees to buy Windsurf for about $3 billion, Bloomberg News reports', 'May 6, 2025',
              'https://kathmandupost.com/science-technology/2025/05/06/openai-agrees-to-buy-windsurf-for-about-3-billion-bloomberg-news-reports'),
 'ibm': ('IBM', 'IBM Accelerates Enterprise Gen AI Revolution with Hybrid Capabilities', 'May 6, 2025',
         'https://newsroom.ibm.com/2025-05-06-ibm-accelerates-enterprise-gen-ai-revolution-with-hybrid-capabilities'),
 'countries': ('OpenAI', 'Introducing OpenAI for Countries', 'May 7, 2025', 'https://openai.com/global-affairs/openai-for-countries/'),
 'bis': ('Bureau of Industry and Security', 'Department of Commerce Announces Rescission of Biden-Era Artificial Intelligence Diffusion Rule, Strengthens Chip-Related Export Controls', 'May 13, 2025',
         'https://www.bis.gov/press-release/department-commerce-announces-rescission-biden-era-artificial-intelligence-diffusion-rule-strengthens'),
 'msft': ('SiliconANGLE', 'OpenAI and Microsoft engage in tense negotiations over the future of their partnership', 'May 11, 2025',
          'https://siliconangle.com/?p=696024'),
 'diffusion': ('DatacenterDynamics, reporting Reuters and Bloomberg', "Trump administration to overhaul 'overly complex, overly bureaucratic' AI diffusion rule", 'May 9, 2025 (announcement of May 7)',
               'https://www.datacenterdynamics.com/en/news/trump-administration-to-overhaul-overly-complex-overly-bureaucratic-ai-diffusion-rule/'),
 'vulcan1': ('Amazon', "Introducing Vulcan: Amazon's first robot with a sense of touch", 'May 2025; launch reported May 7',
             'https://www.aboutamazon.com/news/operations/amazon-vulcan-robot-pick-stow-touch'),
 'vulcan2': ('WIRED', 'Amazon Has Made a Robot With a Sense of Touch', 'May 7, 2025', 'https://www.wired.com/story/ai-lab-amazon-launches-vulcan-a-robot-that-can-feel/'),
 'fda': ('US Food and Drug Administration', 'FDA Announces Completion of First AI-Assisted Scientific Review Pilot and Aggressive Agency-Wide AI Rollout Timeline', 'May 8, 2025',
         'https://www.fda.gov/news-events/press-announcements/fda-announces-completion-first-ai-assisted-scientific-review-pilot-and-aggressive-agency-wide-ai'),
 'leo': ('Vatican News', 'Pope Leo XIV addresses cardinals', 'May 10, 2025', 'https://www.vaticannews.va/en/pope/news/2025-05/pope-leo-xiv-addresses-cardinals-10-may-2025-vatican.html'),
 'humain': ('CNBC (via NBC San Diego)', 'Nvidia sending 18,000 of its top AI chips to Saudi Arabia', 'May 13, 2025',
            'https://www.nbcsandiego.com/news/business/money-report/nvidia-sending-18000-of-its-top-ai-chips-to-saudi-arabia/3824509/'),
 'uae': ('CNBC (via NBC Washington)', 'White House announces AI data campus partnership with the UAE', 'May 15, 2025',
         'https://www.nbcwashington.com/news/business/money-report/white-house-announces-ai-data-campus-partnership-with-the-uae/3914689/'),
 'alpha': ('Google DeepMind', 'AlphaEvolve: A Gemini-powered coding agent for designing advanced algorithms', 'May 14, 2025',
           'https://deepmind.google/blog/alphaevolve-a-gemini-powered-coding-agent-for-designing-advanced-algorithms/'),
 'grok': ('Reuters (via Investing.com)', "Musk's xAI updates Grok chatbot after “white genocide” comments", 'May 16, 2025; Reuters timestamp May 17 UTC',
          'https://www.investing.com/news/stock-market-news/musks-xai-updates-grok-chatbot-after-white-genocide-comments-4051501'),
 'ags': ('California Department of Justice', 'Attorney General Bonta to Congress: California Must Retain its Ability to Protect Californians, Respond to Emerging AI Technology', 'May 16, 2025',
         'https://oag.ca.gov/news/press-releases/attorney-general-bonta-congress-california-must-retain-its-ability-protect'),
 'aimode': ('Google', 'AI in Search: Going beyond information to intelligence', 'May 20, 2025',
            'https://blog.google/products-and-platforms/products/search/google-search-ai-mode-update/'),
 'veo': ('Google', 'Fuel your creativity with new generative media models and tools', 'May 20, 2025',
         'https://blog.google/innovation-and-ai/products/generative-media-models-io-2025/'),
 'flow': ('Google', 'Meet Flow: AI-powered filmmaking with Veo 3', 'May 20, 2025', 'https://blog.google/innovation-and-ai/products/google-flow-veo-ai-filmmaking-tool/'),
 'huang': ('Malay Mail, reporting Reuters', 'Nvidia CEO Jensen Huang calls US AI chip export controls a failure', 'May 21, 2025',
           'https://www.malaymail.com/news/money/2025/05/21/nvidia-ceo-jensen-huang-calls-us-ai-chip-export-controls-a-failure/177552'),
 'claude4': ('Anthropic', 'Introducing Claude 4', 'May 22, 2025', 'https://www.anthropic.com/news/claude-4'),
}

THEME = ('Evaluation, Self-Reporting', [
 ('Evaluation', " shaped May's advances and its disputes. A study questioned the practices behind a prominent model leaderboard, and AlphaEvolve "
  'paired generated programs with tests that could guide further search. New models, from compact reasoning systems to Claude 4, arrived with '
  "their developers' benchmarks. Each result raised the question of what it measured and how far it could be trusted."),
 ('Self-reporting', ' supplied much of the public evidence. OpenAI explained a rollback after GPT-4o became excessively agreeable; xAI attributed '
  'an episode of off-topic political claims to an unauthorized change. Around these accounts, AI became a matter of statecraft: Washington dropped a '
  'chip-export rule, sealed AI deals in the Gulf and heard Nvidia call export controls a failure, while a new pope took his name with AI in mind. '
  "A developer's explanation and an independently tested result remained different forms of evidence."),
])

WEEKS = [
 (18, 'April 28–May 4', 'Original post published May 5, 2025', [
  ("A study questions Chatbot Arena's ranking practices", 'April 29',
   ["The Leaderboard Illusion examined private model testing, selective publication of results and unequal access to evaluation data on Chatbot Arena. "
    "Its authors argued that these practices could advantage some providers and make scores less representative of general model quality.{arena}",
    "The study turned attention from the rankings themselves to the rules that produced them."],
   ['W.H.L.', 'GPT-4-turbo'], ['2025-W18-L2-6']),
  ('Meta launches a standalone AI app', 'April 29',
   ["Meta launched a standalone app for its AI assistant, built with Llama 4. The first version supported voice and text conversations and included "
    "a Discover feed where users could choose to share prompts and responses.{metaapp}",
    "The app gave the assistant a dedicated interface alongside its presence in Meta's social and messaging services, with personalization and "
    "optional sharing central to the design."],
   ['Grok-3'], ['2025-W18-L3-1']),
  ("Meta says Llama has been downloaded 1.2 billion times", 'April 29',
   ["At LlamaCon, Meta's first developer conference for its open-weight models, chief product officer Chris Cox said Llama models had been downloaded "
    "1.2 billion times, up from 1 billion in mid-March, and that the Meta AI assistant had about a billion users.{llama}",
    "The figures, reported by Meta, measured the spread of its open-weight models."],
   ['Grok-3'], ['2025-W18-L3-4']),
  ('OpenAI rolls back an overly agreeable GPT-4o update', 'April 29; explanation May 2',
   ["OpenAI withdrew a GPT-4o update after it produced excessively agreeable responses in ChatGPT. The company said it had placed too much weight on "
    "short-term user feedback. A May 2 account described shortcomings in its testing and plans to improve evaluation before deployment.{syc1}{syc2}",
    "The incident exposed a difference between pleasing a user and helping one: feedback that rewards an agreeable answer can miss whether that answer is sound."],
   ['Grok-3'], ['2025-W18-L3-2']),
  ('Waymo and Toyota explore autonomous-driving collaboration', 'April 29',
   ["Waymo and Toyota announced a preliminary agreement to explore collaboration on autonomous driving. Their proposed work included a new vehicle "
    "platform and possible uses of Waymo's technology in personally owned vehicles, with Woven by Toyota also involved.{waymo}",
    "The proposal connected an autonomous-driving developer with a large vehicle manufacturer; its scope remained under discussion."],
   ['Grok-3'], ['2025-W18-L3-3']),
  ('Microsoft expands the Phi family with reasoning models', 'April 30',
   ["Microsoft introduced Phi-4-reasoning, Phi-4-reasoning-plus and Phi-4-mini-reasoning. The models extended its work on compact language models "
    "to tasks requiring additional reasoning, including mathematics, science and coding.{phi}",
    "The releases pursued reasoning capability within smaller models suited to particular tasks and resource budgets."],
   ['Quark'], ['2025-W18-L5-2']),
  ('Amazon releases Nova Premier', 'April 30',
   ["Amazon announced general availability of Nova Premier through Bedrock. The multimodal model was designed for complex inputs and workflows, "
    "including long documents and video. It could also serve as a teacher model for producing smaller, task-specific models through distillation.{nova}",
    "The release linked a larger model to the development of smaller ones adapted to a narrower task and operating budget."],
   ['Grok-3'], ['2025-W18-L3-5']),
  ('An AI-generated image of Trump as pope draws criticism', 'May 2',
   ["President Trump posted an apparently AI-generated image of himself dressed as the pope on Truth Social, and the White House reposted it on X, "
    "days before the conclave to elect Pope Francis's successor. The New York State Catholic Conference and other Catholic leaders criticized the post.{pope}",
    "The episode showed generated images entering political communication at the highest level."],
   ['DeepSeek-R1'], ['2025-W18-L4-1']),
 ]),
 (19, 'May 5–11', 'Original post published May 11, 2025', [
  ('OpenAI keeps nonprofit control in its restructuring plan', 'May 5',
   ["OpenAI announced a revised plan under which its nonprofit would retain control. Its for-profit subsidiary would become a public benefit corporation, "
    "with the nonprofit also holding a substantial ownership stake.{oaistruct}",
    "The announcement set out the intended relationship between governance, investment and mission; the restructuring itself was still to be completed."],
   ['DeepSeek-R1'], ['2025-W19-L3-5']),
  ('OpenAI is reported to agree to buy Windsurf', 'Reported May 6',
   ["Bloomberg News reported that OpenAI had agreed to buy Windsurf, the AI coding tool formerly known as Codeium, for about $3 billion. The deal had not "
    "closed; OpenAI declined to comment.{windsurf}",
    "The deal never closed: in July, Google hired Windsurf's leaders and licensed its technology instead.{wsfall}"],
   ['Grok-3'], ['2025-W19-L2-3']),
  ('IBM announces tools for coordinating enterprise agents', 'May 6',
   ["At Think 2025, IBM announced additions to watsonx Orchestrate for building agents, connecting them to business applications and coordinating "
    "their work. The announcement included prebuilt agents and tools for monitoring and governing their operation.{ibm}",
    "The emphasis was on fitting agents into an organization's existing systems."],
   ['Grok-3'], ['2025-W19-L2-5']),
  ('OpenAI proposes national AI partnerships', 'May 7',
   ["OpenAI introduced OpenAI for Countries, an initiative offering partnerships on AI infrastructure, locally adapted services and startup ecosystems. "
    "The company connected the program to its Stargate infrastructure effort and described it as supporting democratic approaches to AI.{countries}",
    "The proposal extended the company's ambitions from individual products to national infrastructure, with each partnership to be negotiated separately."],
   ['GPT-4-turbo'], ['2025-W19-L1-1']),
  ('The administration moves to rescind the AI diffusion rule', 'Plan reported May 7; rescission and non-enforcement announced May 13',
   ["The Commerce Department said it would rescind the Biden-era AI diffusion rule, in effect since January 13, whose main compliance requirements were due to begin on May 15. The rule would have limited "
    "countries' access to advanced AI chips in tiers. A spokesperson called the rule “overly complex, overly bureaucratic” and promised “a much "
    "simpler rule.”{diffusion} On May 13 the department announced the rescission and told officials not to enforce the rule; a regulation formalizing "
    "the rescission and a replacement rule were still to come. It also warned companies against using Huawei's Ascend chips.{bis}",
    "Export policy shifted from a global framework toward bilateral deals; Reuters reported that country-by-country agreements could replace the tiers."],
   ['Grok-3'], ['2025-W19-L2-2']),
  ('Amazon introduces touch-sensitive warehouse robotics', 'May 7',
   ["Amazon introduced Vulcan, a robotic system that uses force and touch sensing to help pick and stow items in fulfillment centers. The company described "
    "how sensing contact allows the system to adjust its movements around objects.{vulcan1}{vulcan2}",
    "Vulcan showed how tactile sensing could support manipulation in a structured warehouse environment, where physical work depends on feedback from the world."],
   ['DeepSeek-R1'], ['2025-W19-L3-1']),
  ('FDA sets a timetable for internal AI deployment', 'May 8',
   ["The US Food and Drug Administration announced plans to expand generative AI across its centers by June 30, following an internal scientific-review "
    "pilot. The intended tools would assist staff with repetitive review tasks on a secure platform.{fda}",
    "The timetable put an AI rollout at the center of a regulator's internal work; the agency launched its tool, Elsa, on June 2.{elsa}"],
   ['GPT-4-turbo', 'Grok-3'], ['2025-W19-L1-2', '2025-W19-L2-1']),
  ('Pope Leo XIV links his name to the age of AI', 'May 10',
   ["In his first address to the College of Cardinals, Pope Leo XIV said he chose his name after Leo XIII, whose encyclical “addressed the social "
    "question in the context of the first great industrial revolution.” The Church, he said, now offers its social teaching “in response to another "
    "industrial revolution and the developments of artificial intelligence.”{leo}",
    "The new pope placed AI among the central questions of his pontificate."],
   ['GPT-4-turbo'], ['2025-W19-L1-3']),
  ('OpenAI and Microsoft are reported to renegotiate their partnership', 'Reported May 11',
   ["The *Financial Times* reported that OpenAI and Microsoft were renegotiating their partnership as OpenAI prepared to turn its for-profit arm into a "
    "public benefit corporation, a change Microsoft had to approve. The talks concerned the size of Microsoft's stake, after investments of more than "
    "$13 billion, and its access to OpenAI's technology after the current contract ends in 2030.{msft}",
    "The talks tied the governance plan announced earlier in the week to the commercial terms of OpenAI's most important partnership."],
   ['Grok-3'], ['2025-W19-L2-4']),
 ]),
 (20, 'May 12–18', 'Original post published May 18, 2025', [
  ('US AI deals are announced across the Gulf', 'May 13–15',
   ["During President Trump's Gulf visit, Nvidia said it would sell more than 18,000 of its latest AI chips to Humain, a company owned by Saudi Arabia's "
    "Public Investment Fund, and AMD announced its own supply deal with Humain.{humain} In Abu Dhabi, the White House announced a 5-gigawatt AI campus "
    "to be built by G42, which Commerce Secretary Howard Lutnick said came with security guarantees against diversion of US technology.{uae}",
    "The deals made the Gulf a major destination for American AI chips."],
   ['Grok-3', 'Grok-3 (week 21)'], ['2025-W20-L1-1', '2025-W21-L3-3', '2025-W21-L4-3']),
  ('AlphaEvolve searches for better algorithms', 'May 14',
   ["Google DeepMind introduced AlphaEvolve, a system combining Gemini models with automated evaluators and evolutionary search. It generated candidate "
    "programs, scored them and used promising results to guide further proposals. DeepMind reported applications in mathematics and its own computing infrastructure.{alpha}",
    "The approach suited problems where candidate solutions could be tested automatically."],
   ['DeepSeek-R1'], ['2025-W20-L2-1', '2025-W21-L1-4']),
  ('xAI responds to off-topic political claims from Grok', 'May 14–16',
   ["After Grok inserted claims about “white genocide” in South Africa into unrelated conversations, xAI attributed the behavior to an unauthorized "
    "change to its system prompt. Reuters reported that the company promised to publish its system prompts and add monitoring.{grok}",
    "The episode made control over a chatbot's instructions a public issue; the account of its cause came from xAI."],
   ['Grok-3', 'Grok-3 (week 21)'], ['2025-W20-L1-2', '2025-W21-L3-2', '2025-W21-L4-2']),
  ('State attorneys general oppose a proposed AI-law moratorium', 'May 16',
   ["A coalition of 40 state attorneys general wrote to congressional leaders opposing a proposed 10-year ban on state enforcement of laws addressing "
    "AI and automated decision-making. The proposal appeared in committee changes to a budget reconciliation bill.{ags}",
    "The dispute concerned who could act when AI caused harm; the Senate removed the moratorium on July 1.{senstrike}"],
   ['Grok-3'], ['2025-W20-L1-3']),
 ]),
 (21, 'May 19–25', 'Original post published May 25, 2025', [
  ('Google expands AI Mode in Search', 'May 20',
   ["Google began rolling out AI Mode in the United States without requiring Labs enrollment. The search interface supported follow-up questions and "
    "linked answers, using multiple searches across subtopics to assemble a response.{aimode}",
    "The rollout made conversational exploration a more prominent part of search."],
   ['DeepSeek-R1'], ['2025-W21-L1-1']),
  ('Veo 3 generates video with sound', 'May 20',
   ["Google introduced Veo 3, a video-generation model that could produce sound along with images, including ambient noise and dialogue. At launch, "
    "US Google AI Ultra subscribers could access it through Gemini and Flow.{veo}",
    "Generating sound and moving images together removed a separate step in producing a clip."],
   ['DeepSeek-R1', 'ChatGPT'], ['2025-W21-L1-1', '2025-W21-L2-1']),
  ('Flow brings generative models into a filmmaking workspace', 'May 20',
   ["Google introduced Flow, a filmmaking tool combining Veo, Imagen and Gemini. It was designed to help creators develop clips and scenes while managing "
    "visual elements within a shared workspace.{flow}",
    "Flow addressed developing a sequence rather than one isolated clip."],
   ['ChatGPT'], ['2025-W21-L2-4']),
  ('Huang calls US chip export controls a failure', 'May 21',
   ["Speaking at Computex in Taipei, Nvidia chief executive Jensen Huang said, “All in all, the export control was a failure,” adding that Nvidia's "
    "share of the Chinese market had fallen to 50 percent from 95 percent at the start of the Biden administration.{huang}",
    "The remarks put the industry's leading chipmaker openly at odds with the policy of restricting AI chips to China."],
   ['DeepSeek-R1'], ['2025-W21-L1-3']),
  ('Anthropic releases Claude Opus 4 and Sonnet 4', 'May 22',
   ["Anthropic released Claude Opus 4 and Claude Sonnet 4. Both offered rapid responses and an extended-thinking mode, with availability through Claude, "
    "Anthropic's API, Amazon Bedrock and Google Cloud's Vertex AI. Anthropic emphasized coding and agent workflows in its evaluations.{claude4}",
    "The release continued the integration of reasoning modes with software tools, measured on the developer's chosen benchmarks."],
   ['ChatGPT'], ['2025-W21-L2-3']),
 ]),
]
