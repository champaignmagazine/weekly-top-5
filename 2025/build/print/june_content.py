# June 2025 print chapter, v0.2: content (American style).
COVERS = 'Edited from five posts published in June 2025, covering May 26–June 29.'

SOURCES = {
'senstrike': ('Office of Senator Edward J. Markey', 'After weeks of Markey raising the alarm, Senate strikes AI moratorium from budget reconciliation bill overnight in overwhelming 99-1 vote', 'July 1, 2025',
              'https://www.markey.senate.gov/news/press-releases/after-weeks-of-markey-raising-the-alarm-senate-strikes-ai-moratorium-from-budget-reconciliation-bill-overnight-in-overwhelming-99-1-vote'),
 'llama': ('TechRepublic, reporting Business Insider', "Will Meta's Retention Issues Put Its Llama AI in Jeopardy?", 'May 27, 2025',
           'https://www.techrepublic.com/article/news-meta-retention-challenges-llama-ai/'),
 'infa': ('Salesforce', 'Salesforce Signs Definitive Agreement to Acquire Informatica', 'May 27, 2025',
          'https://www.salesforce.com/in/news/press-releases/2025/05/27/salesforce-signs-definitive-agreement-to-acquire-informatica/'),
 'axios1': ('Axios', 'Axios AM: White-collar bloodbath', 'May 28, 2025', 'https://www.axios.com/newsletters/axios-am-e8b4908f-a6fa-40b1-8adc-7d9b60c94da2'),
 'axios2': ('Axios', 'Behind the Curtain: A white-collar bloodbath', 'May 28, 2025; original interview', 'https://www.axios.com/2025/05/28/ai-jobs-white-collar-unemployment-anthropic'),
 'nyt': ('The New York Times Company and Amazon', 'The New York Times Company and Amazon Announce Licensing Agreement', 'May 29, 2025',
         'https://s23.q4cdn.com/152113917/files/doc_news/2025/May/29/Blog-Post.pdf'),
 'mehta1': ('Yahoo News', 'AI dominates as judge weighs penalties in Google search case', 'May 30, 2025',
            'https://www.yahoo.com/news/ai-dominates-judge-weighs-penalties-210908647.html'),
 'mehta2': ('Tech Policy Press', "Reading the Tea Leaves: Closing Arguments in Google's Search Remedies Trial", 'June 5, 2025 (on the arguments of May 30)',
            'https://techpolicy.press/reading-the-tea-leaves-closing-arguments-in-googles-search-remedies-trial'),
 'bond': ('Mary Meeker, Jay Simons, Daegwon Chae and Alexander Krey; BOND', 'Trends – Artificial Intelligence', "May 30, 2025; report text via BOND's Relayto presentation",
          'https://bondcap.relayto.com/e/2025-trends-in-artificial-intelligence-tn9e6r7a9i24j'),
 'elsa': ('US Food and Drug Administration', 'FDA Launches Agency-Wide AI Tool to Optimize Performance for the American People', 'June 2, 2025',
          'https://www.fda.gov/news-events/press-announcements/fda-launches-agency-wide-ai-tool-optimize-performance-american-people'),
 'lawzero': ('LawZero', 'Yoshua Bengio Launches LawZero: A New Nonprofit Advancing Safe-by-Design AI', 'June 3, 2025',
             'https://lawzero.org/en/news/yoshua-bengio-launches-lawzero-new-nonprofit-advancing-safe-design-ai'),
 'mistral': ('Mistral AI', 'Introducing Mistral Code', 'June 4, 2025', 'https://mistral.ai/news/mistral-code/'),
 'markey': ('Office of Senator Edward J. Markey', "Senator Markey Hosts Roundtable on Republicans' Proposed State AI Regulation Moratorium", 'June 4, 2025',
            'https://www.markey.senate.gov/news/press-releases/senator-markey-hosts-roundtable-on-republicans-proposed-state-ai-regulation-moratorium'),
 'apple': ('Apple', 'Apple Intelligence gets even more powerful with new capabilities across Apple devices', 'June 9, 2025',
           'https://www.apple.com/newsroom/2025/06/apple-intelligence-gets-even-more-powerful-with-new-capabilities-across-apple-devices/'),
 'oairev': ('DIGITIMES', "OpenAI's annualized revenue reaches US$10 billion", 'June 10, 2025 (reports of June 9)', 'https://www.digitimes.com/news/a20250610PD229.html'),
 'datadog': ('Datadog', 'Datadog Unveils Latest AI Agents to Rapidly Resolve Application Issues', 'June 10, 2025',
             'https://investors.datadoghq.com/news-releases/news-release-details/datadog-unveils-latest-ai-agents-rapidly-resolve-application'),
 'koray': ('Semafor', 'Google names new chief AI architect to advance developments', 'June 11, 2025',
           'https://www.semafor.com/article/06/11/2025/google-names-new-chief-ai-architect-to-advance-developments'),
 'vjepa': ('Meta AI', 'Introducing the V-JEPA 2 world model and new benchmarks for physical reasoning', 'June 11, 2025', 'https://ai.meta.com/blog/v-jepa-2-world-model-benchmarks/'),
 'scale': ('Scale AI', "Scale AI Announces Next Phase of Company's Evolution", 'June 12, 2025', 'https://scale.com/blog/scale-ai-announces-next-phase-of-company-evolution'),
 'whatsapp': ('TechCabal', 'WhatsApp will start showing ads in the Updates tab', 'June 16, 2025', 'https://techcabal.com/2025/06/16/whatsapp-status-ads/'),
 'jassy1': ('Andy Jassy; Amazon', 'Message from CEO Andy Jassy: Some thoughts on Generative AI', 'June 17, 2025',
            'https://www.aboutamazon.com/news/company-news/amazon-ceo-andy-jassy-on-generative-ai'),
 'jassy2': ('Reuters (via Investing.com)', "Amazon's corporate workforce may shrink as AI takes over routine tasks", 'June 17, 2025',
            'https://www.investing.com/news/stock-market-news/amazons-corporate-workforce-may-shrink-as-ai-takes-over-routine-tasks-4099895'),
 'mj': ('Midjourney', 'Introducing Our V1 Video Model', 'June 18, 2025', 'https://updates.midjourney.com/introducing-our-v1-video-model/'),
 'agentforce': ('Salesforce', 'Salesforce Announces Agentforce 3', 'June 23, 2025', 'https://www.salesforce.com/news/press-releases/2025/06/23/agentforce-3-announcement/'),
 'fairuse': ('Manatt', 'Making Sense of the First Two—Often Contradictory, Sometimes Confounding—Gen AI Fair Use Rulings', 'June–July 2025 (on rulings of June 23 and 25)',
             'https://www.manatt.com/insights/newsletters/client-alert/making-sense-of-the-first-two-often-contradictory-sometimes-confounding-gen-ai-fair-use-rulings'),
 'nadv': ('US Senate', 'S. 2177: No Adversarial AI Act, as introduced', 'June 25, 2025', 'https://www.congress.gov/119/bills/s2177/BILLS-119s2177is.pdf'),
 'nvda': ('The Daily Star', "Nvidia reclaims 'world's most valuable company' title", 'June 26, 2025 (trading of June 25)',
          'https://www.thedailystar.net/tech-startup/news/nvidia-reclaims-worlds-most-valuable-company-title-3925991'),
 'vlo': ('Qwen Team', 'Qwen VLo: From “Understanding” the World to “Depicting” It', 'June 26, 2025', 'https://qwenlm.github.io/blog/qwen-vlo/'),
 'maia': ('The Decoder, reporting The Information', "Microsoft's AI chip Braga is delayed, gap to Nvidia is growing", 'June 27, 2025',
          'https://the-decoder.com/microsofts-ai-chip-braga-is-delayed-gap-to-nvidia-is-growing/'),
 'vend': ('Anthropic', 'Project Vend: Can Claude run a small shop? (And why does that matter?)', 'June 27, 2025', 'https://www.anthropic.com/research/project-vend-1'),
}

THEME = ('Employment, Scientific Tools', [
 ('Employment', " gave June's announcements urgency. Dario Amodei warned about entry-level jobs, and Andy Jassy told Amazon's staff to expect a smaller "
  "corporate workforce. Talent moved as well: Meta lost most of Llama's original authors and then invested in Scale AI and brought its founder into its AI work, "
  "while Google named a chief AI architect. Revenue, valuations and a record market value for Nvidia measured how much was riding on the outcome."),
 ('Scientific tools', ' widened the view. Meta released V-JEPA 2 for visual prediction and physical reasoning. LawZero proposed systems focused on '
  'understanding rather than autonomous action, and the FDA put an assistant into internal review work. Two federal judges ruled on '
  "whether training generative models on books is fair use, and an experiment with Claude running an office shop showed what a capable model could still get wrong over weeks of work. "
  'Data, supervision, judgment and permission mattered as much as capability.'),
])

WEEKS = [
 (22, 'May 26–June 1', 'Original post published June 1, 2025', [
  ("Meta loses most of Llama's original authors", 'Reported May 26',
   ["Business Insider reported that 11 of the 14 researchers credited on the 2023 paper introducing Meta's Llama models had left the company, several "
    "for rival laboratories; one became a founding member of Mistral.{llama}",
    "The departures were an early sign of the competition for researchers that Meta answered with large hiring offers later in the summer."],
   ['DeepSeek-R1'], ['2025-W22-L3-5']),
  ('Salesforce agrees to acquire Informatica', 'May 27',
   ["Salesforce announced an agreement to acquire Informatica for approximately $8 billion in equity value, net of its existing investment. The proposed "
    "combination would bring Informatica's data integration, cataloging and governance services into Salesforce's enterprise platform.{infa}",
    "The deal tied AI deployment to the quality and organization of business data; it still needed regulatory approval to close."],
   ['Grok-3'], ['2025-W22-L2-1']),
  ('Amodei warns about entry-level employment', 'May 28',
   ["Anthropic chief executive Dario Amodei told Axios that AI could eliminate half of entry-level white-collar jobs within one to five years.{axios1}{axios2}",
    "The forecast, from the head of a leading developer, became a reference point in the year's debate over AI and work."],
   ['DeepSeek-R1'], ['2025-W22-L3-1', '2025-W23-L2-2']),
  ('The *New York Times* licenses content to Amazon', 'May 29',
   ["The New York Times Company and Amazon announced a multiyear licensing agreement covering editorial material from the Times, NYT Cooking and "
    "The Athletic. The permitted uses included summaries and short excerpts in Amazon services, links to Times products, and training Amazon's foundation models.{nyt}",
    "The agreement set out a commercial route for using journalism in AI products while the paper's lawsuit "
    "against OpenAI and Microsoft continued."],
   ['DeepSeek-R1'], ['2025-W22-L3-3', '2025-W23-L2-4']),
  ("AI dominates closing arguments in Google's search case", 'May 30',
   ["In closing arguments on remedies in the government's search monopoly case against Google, Judge Amit Mehta spent much of an eight-hour session on "
    "AI's implications for search. The Justice Department sought a sale of Chrome, an end to paid default placements, and sharing of search data "
    "that AI rivals such as OpenAI and Perplexity could use. Mehta said he hoped to rule by August.{mehta1}{mehta2}",
    "Generative AI had become central to deciding how much of Google's search business the court should change."],
   ['GPT-4o-mini'], ['2025-W22-L1-3']),
 ]),
 (23, 'June 2–8', 'Original post published June 8, 2025', [
  ('Research focus: BOND surveys the AI economy', 'Background: May 30; selected June 8 at the editor’s request',
   ["Mary Meeker and colleagues at BOND published Trends – Artificial Intelligence, a chart-led survey of adoption, computing costs, investment "
    "and competition. It brought company disclosures and other datasets together to examine the pace and economics of AI development.{bond}",
    "The report offered a broad frame for reading individual announcements, assembled from many sources and measurement periods."],
   ['W.H.L.', 'DeepSeek-R1'], ['2025-W23-L3-1']),
  ('FDA launches Elsa for internal review work', 'June 2',
   ["The US Food and Drug Administration launched Elsa, an internal generative AI tool for reading, writing and summarizing. The agency described "
    "uses including adverse-event summaries, label comparisons and assistance with scientific review, within a government cloud environment.{elsa}",
    "The agency said the tool arrived ahead of schedule; it put an AI assistant inside the work of a regulator."],
   ['Gemini 2.5 Pro'], ['2025-W23-L1-3']),
  ('Bengio launches LawZero', 'June 3',
   ["Yoshua Bengio launched LawZero, a nonprofit devoted to AI safety research. Its proposed Scientist AI approach aimed to build systems that explain "
    "and predict rather than pursue goals through action. Possible applications included scientific discovery and oversight of AI agents.{lawzero}",
    "The initiative set out a research program for separating understanding from agency."],
   ['W.H.L.', 'DeepSeek-R1'], ['2025-W23-L4-1']),
  ('Mistral previews an enterprise coding assistant', 'June 4',
   ["Mistral introduced Mistral Code in private beta for JetBrains environments and Visual Studio Code. Built on the Continue project, the offering "
    "combined coding models, an editor assistant, deployment options and administrative controls for enterprise teams.{mistral}",
    "The product addressed the conditions for using AI with proprietary code: where it runs, what it can access and how an organization oversees it."],
   ['Gemini 2.5 Pro'], ['2025-W23-L1-2']),
  ('Markey challenges the proposed state AI-law moratorium', 'June 4',
   ["US Senator Edward Markey held a roundtable opposing a proposed 10-year moratorium on state AI regulation in the House-passed reconciliation bill. "
    "Participating advocates argued that it would weaken civil-rights and consumer protections without an adequate federal replacement.{markey}",
    "The debate concerned which level of government could respond to AI-related harm; the Senate struck the moratorium on July 1.{senstrike}"],
   ['Gemini 2.5 Pro'], ['2025-W23-L1-4']),
 ]),
 (24, 'June 9–15', 'Original post published June 15, 2025', [
  ('Apple opens its on-device model to developers', 'June 9',
   ["At WWDC, Apple introduced the Foundation Models framework, giving developers access to the on-device language model behind Apple Intelligence. "
    "It also previewed features including Live Translation and expanded visual intelligence. Developer testing began that day, with wider user "
    "availability planned for the fall.{apple}",
    "The framework brought generative functions into apps that could operate offline, on supported devices."],
   ['DeepSeek-R1'], ['2025-W24-L1-3']),
  ("OpenAI reports a $10 billion annualized revenue run rate", 'Reported June 9',
   ["OpenAI's annualized revenue run rate reached about $10 billion, nearly double the $5.5 billion run rate at the end of 2024. The figure covered ChatGPT "
    "subscriptions and API sales and excluded licensing and large one-off deals with Microsoft.{oairev}",
    "The growth showed how quickly paid use of chatbots and developer access had expanded."],
   ['GPT-4o'], ['2025-W24-L2-5']),
  ('Datadog introduces agents for software operations', 'June 10',
   ["At DASH, Datadog introduced Bits AI agents for incident response, development and security. Bits AI SRE entered limited availability; the Dev Agent "
    "and Security Analyst were in preview. Their intended work included investigating alerts, proposing code fixes and assessing security signals.{datadog}",
    "The tools connected models to operational data and established engineering workflows, starting with limited releases."],
   ['GPT-4o'], ['2025-W24-L2-3']),
  ('Google names a chief AI architect', 'June 11',
   ["Sundar Pichai named Koray Kavukcuoglu, chief technology officer of Google DeepMind, to the new post of chief AI architect, reporting directly to him. "
    "Pichai wrote that Kavukcuoglu would “accelerate how we bring our world-leading models into our products.”{koray}",
    "The appointment put a senior researcher in charge of turning Google's models into products faster."],
   ['GPT-4o'], ['2025-W24-L2-2']),
  ('V-JEPA 2 learns predictive representations from video', 'June 11',
   ["Meta released V-JEPA 2, a world model trained primarily through self-supervised learning from video. Its encoder and predictor worked with abstract "
    "representations of scenes. Meta also demonstrated an action-conditioned version for robot planning and released benchmarks for physical reasoning.{vjepa}",
    "The work connected visual prediction with planning, and supplied models and tests for further research."],
   ['W.H.L.', 'GPT-4o'], ['2025-W24-L2-HM1']),
  ('Meta invests in Scale AI as Wang joins its AI effort', 'June 12',
   ["Scale AI announced a Meta investment valuing the company at more than $29 billion. Founder Alexandr Wang was joining Meta's AI effort while remaining "
    "on Scale's board. Scale appointed Jason Droege interim chief executive and said Meta would hold a minority equity stake.{scale}",
    "The arrangement combined an investment, a commercial relationship and a leadership move; Wang went on to lead Meta Superintelligence Labs."],
   ['GPT-4o'], ['2025-W24-L2-1']),
 ]),
 (25, 'June 16–22', 'Original post published June 22, 2025', [
  ('WhatsApp introduces ads in its Updates tab', 'June 16',
   ["Meta announced that WhatsApp would show ads in its Updates tab, alongside Status and Channels, and add paid channel subscriptions and promoted "
    "channels. Personal chats would remain ad-free and end-to-end encrypted; ad targeting would use limited information such as location, language "
    "and channels followed.{whatsapp}",
    "The change ended WhatsApp's long-standing ad-free model and brought Meta's advertising business into its most private service."],
   ['DeepSeek-R1'], ['2025-W25-L2-4']),
  ("Jassy expects AI to reduce Amazon's corporate workforce", 'June 17',
   ["Amazon chief executive Andy Jassy told employees that generative AI and agents would change staffing needs. He expected fewer people in some "
    "roles and more in others, with a net reduction in the corporate workforce over the next few years.{jassy1}{jassy2}",
    "The message made workforce change an explicit management expectation at one of the largest US employers."],
   ['DeepSeek-R1'], ['2025-W25-L2-3']),
  ('Midjourney releases its first video model', 'June 18',
   ["Midjourney released V1 as an image-to-video model. Users could animate a generated or uploaded image, supply a motion prompt and extend a resulting "
    "clip. The release included automatic and manual animation controls, with options for higher or lower motion.{mj}",
    "The workflow extended still-image creation into moving scenes; Midjourney described real-time worlds and 3D interaction as its longer-term direction."],
   ['DeepSeek-R1'], ['2025-W25-L2-5']),
 ]),
 (26, 'June 23–29', 'Original post published June 29, 2025', [
  ('Salesforce announces monitoring and integration tools for agents', 'June 23',
   ["Salesforce announced Agentforce 3, including plans for a Command Center to monitor agent activity and support for Model Context Protocol "
    "connections. The release combined available features with previews and capabilities scheduled for later delivery.{agentforce}",
    "Monitoring and integration became product requirements alongside the models' ability to perform individual tasks."],
   ['Gemini 2.5 Flash'], ['2025-W26-L4-5']),
  ('Two courts rule on fair use in generative-AI training', 'June 23 and 25',
   ["In *Bartz v. Anthropic*, Judge William Alsup held that training Claude on books was fair use, calling it “exceedingly transformative,” but that "
    "keeping a library of pirated copies was not, leaving that claim for trial. Two days later, in *Kadrey v. Meta*, Judge Vince Chhabria granted Meta "
    "summary judgment on Llama's training, calling his ruling limited to the plaintiffs' arguments and record, and pointing to market dilution as "
    "a potentially stronger claim.{fairuse}",
    "Both rulings favored the developers on training, while differing on how much harm to authors' markets should count."],
   ['Gemini 2.5 Flash'], ['2025-W26-L4-1']),
  ('US senators propose restrictions on foreign-adversary AI', 'June 25',
   ["Senators Rick Scott and Gary Peters introduced the No Adversarial AI Act. The bill proposed a federal list of AI produced or developed by foreign "
    "adversaries, agency review for exclusion or removal, and a process for exceptions.{nadv}",
    "The proposal made the origin of AI systems a question of federal procurement and security."],
   ['GPT-4o'], ['2025-W26-L1-2']),
  ('Nvidia regains the title of most valuable company', 'June 25',
   ["Nvidia's shares rose more than 4 percent to a record $154.10, lifting its market value to about $3.76 trillion and past Microsoft's.{nvda}",
    "Investors priced continued demand for AI data-center chips into the company's value."],
   ['Gemini 2.5 Flash'], ['2025-W26-L4-3']),
  ('Qwen previews image generation and editing in VLo', 'June 26',
   ["The Qwen team introduced VLo, a preview combining multimodal understanding with image generation and editing. Through Qwen Chat, users could request "
    "an image or upload one and describe changes in natural language.{vlo}",
    "The preview connected image interpretation with revision in a conversational workflow."],
   ['GPT-4o'], ['2025-W26-L1-4']),
  ("Microsoft's next AI chip is reported delayed", 'Reported June 27',
   ["*The Information* reported that mass production of Microsoft's next in-house AI chip, code-named Braga, had slipped from 2025 into 2026, after "
    "design changes and staff turnover.{maia}",
    "The delay left Microsoft relying on Nvidia's hardware for longer."],
   ['GPT-4o'], ['2025-W26-L1-1']),
  ('Project Vend tests Claude as a shopkeeper', 'June 27',
   ["Anthropic and Andon Labs reported an experiment in which Claude Sonnet 3.7 managed a small office shop. The agent selected stock, set prices and "
    "interacted with customers, while people handled physical tasks. It made persistent pricing and discount errors, and the business failed to make money.{vend}",
    "The experiment tested sustained commercial judgment in a small, supported setting, where individually useful actions coexisted with poor overall management."],
   ['GPT-4o'], ['2025-W26-L1-5']),
 ]),
]
