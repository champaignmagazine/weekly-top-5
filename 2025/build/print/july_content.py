# July 2025 print chapter, v0.2: content (American style).
COVERS = 'Edited from four posts published in July 2025, covering June 30–July 27.'

SOURCES = {
 'msl': ('Mark Zuckerberg, memo reproduced by Business Insider', "Read Mark Zuckerberg's memo explaining what Alexandr Wang will be running at Meta", 'June 30, 2025',
         'https://www.businessinsider.com/meta-ceo-mark-zuckerberg-announces-superintelligence-ai-division-internal-memo-2025-6'),
 'mai': ('Microsoft AI', 'The Path to Medical Superintelligence', 'June 30, 2025', 'https://microsoft.ai/news/the-path-to-medical-superintelligence/'),
 'cf': ('Cloudflare', 'Introducing pay per crawl: Enabling content owners to charge AI crawlers for access', 'July 1, 2025', 'https://blog.cloudflare.com/introducing-pay-per-crawl/'),
 'sakana': ('Sakana AI', 'Inference-Time Scaling and Collective Intelligence for Frontier AI', 'July 1, 2025', 'https://sakana.ai/ab-mcts/'),
 'ssi': ('Safe Superintelligence', 'Updates: message to team and investors', 'July 3, 2025', 'https://ssi.inc/updates'),
 'iso': ('Fortune', "DeepMind's Isomorphic Labs nears first human trials of AI-designed drugs", 'July 6, 2025',
         'https://fortune.com/2025/07/06/deepmind-isomorphic-labs-cure-all-diseases-ai-now-first-human-trials/'),
 'pang': ('9to5Mac, reporting Bloomberg', "Meta just hired Apple's head of foundation models", 'July 7, 2025',
          'https://9to5mac.com/2025/07/07/meta-just-hired-apples-head-of-foundation-models/'),
 'rubio': ('NPR (via WHQR)', 'An AI imposter is pretending to be Marco Rubio', 'July 8, 2025',
           'https://www.whqr.org/2025-07-08/an-ai-imposter-is-pretending-to-be-marco-rubio'),
 'grok': ('xAI', 'Grok 4', 'July 9, 2025', 'https://x.ai/news/grok-4'),
 'eucode': ('European Commission', 'General-Purpose AI Code of Practice now available', 'July 10, 2025',
            'https://ec.europa.eu/commission/presscorner/api/files/document/print/en/ip_25_1787/IP_25_1787_EN.pdf'),
 'windsurf': ('Reuters (via Investing.com)', 'Google hires Windsurf execs in $2.4 billion deal to advance AI coding ambitions', 'July 11, 2025',
              'https://www.investing.com/news/stock-market-news/google-hires-windsurf-ceo-and-researchers-to-advance-ai-ambitions-4132685'),
 'kimi1': ('Moonshot AI', 'Kimi K2: repository and model documentation', 'July 2025; launch July 11', 'https://github.com/MoonshotAI/Kimi-K2'),
 'kimi2': ('Moonshot AI, Hugging Face', 'Kimi-K2-Instruct: commit history', 'July 11, 2025 initial release records', 'https://huggingface.co/moonshotai/Kimi-K2-Instruct/commits/main'),
 'owdelay': ('TechCrunch', 'OpenAI delays the release of its open model, again', 'July 11, 2025',
             'https://techcrunch.com/2025/07/11/openai-delays-the-release-of-its-open-model-again/'),
 'meta': ('Reuters (via Investing.com)', "Meta's Zuckerberg pledges hundreds of billions for AI data centers in superintelligence push", 'July 14, 2025; updated July 15',
          'https://www.investing.com/news/stock-market-news/zuckerberg-says-meta-will-invest-hundreds-of-billions-in-superintelligence-4134149'),
 'tml': ('Wilson Sonsini', 'Wilson Sonsini Advises Thinking Machines on $2 Billion Round Led by a16z', 'July 15, 2025',
         'https://www.wsgr.com/en/insights/wilson-sonsini-advises-thinking-machines-on-dollar2-billion-round-led-by-a16z.html'),
 'pa': ('Office of Senator Dave McCormick', "Fact sheet: More than $90 billion in investments announced at Senator McCormick's Pennsylvania Energy and Innovation Summit", 'July 15, 2025',
        'https://www.mccormick.senate.gov/news/press-releases/fact-sheet-more-than-90-billion-in-investments-announced-at-senator-mccormicks-pennsylvania-energy-and-innovation-summit/'),
 'aimode': ('Google', 'More advanced AI capabilities are coming to Search', 'July 16, 2025',
            'https://blog.google/products/search/deep-search-business-calling-google-search/'),
 'agent': ('OpenAI', 'Introducing ChatGPT agent: bridging research and action', 'July 17, 2025', 'https://openai.com/index/introducing-chatgpt-agent/'),
 'pplx': ('Bloomberg (via Business Standard)', 'AI startup Perplexity secures $100 mn funding, hits $18 billion valuation', 'July 18, 2025 (Bloomberg report of July 17)',
          'https://www.business-standard.com/amp/technology/tech-news/ai-startup-perplexity-secures-100-mn-funding-hits-18-billion-valuation-125071800104_1.html'),
 'imo1': ('Alexander Wei; announcement reproduced by Simon Willison', "OpenAI's gold medal performance on the International Math Olympiad", 'July 19, 2025',
          'https://simonwillison.net/2025/Jul/19/openai-gold-medal-math-olympiad/'),
 'imo2': ('Alexander Wei', 'OpenAI IMO 2025 Proofs', 'July 2025', 'https://github.com/aw31/openai-imo-2025-proofs/'),
 'gemimo': ('Google DeepMind', 'Advanced version of Gemini with Deep Think officially achieves gold-medal standard at the International Mathematical Olympiad', 'July 21, 2025',
            'https://deepmind.google/blog/advanced-version-of-gemini-with-deep-think-officially-achieves-gold-medal-standard-at-the-international-mathematical-olympiad/'),
 'plan': ('The White House', "White House Unveils America's AI Action Plan", 'July 23, 2025', 'https://www.whitehouse.gov/releases/2025/07/white-house-unveils-americas-ai-action-plan/'),
 'eos': ('CNBC (via NBC Washington)', "'No woke AI' in Washington, Trump says as he launches American AI Action Plan", 'July 24, 2025 (event of July 23)',
         'https://www.nbcwashington.com/news/business/money-report/no-woke-ai-in-washington-trump-says-as-he-launches-american-ai-action-plan/'),
 'india': ('Google India Team', "Google I/O Connect India 2025: Empowering developers with AI to lead India's ambitions", 'July 23, 2025',
           'https://blog.google/intl/en-in/company-news/google-io-connect-india-2025-empowering-developers-with-ai-to-lead-indias-ambitions/'),
 'msft': ('Fortune', "Satya Nadella's memo on Microsoft layoffs and the 'enigma of success'", 'July 24, 2025',
          'https://fortune.com/2025/07/24/satya-nadella-memo-microsoft-layoffs-enigma-of-success-artificial-intelligence/'),
 'asiarch': ('Yixiu Liu and colleagues', 'AlphaGo Moment for Model Architecture Discovery', 'July 24, 2025; arXiv version 1', 'https://arxiv.org/abs/2507.18074v1'),
 'asean': ('ASEAN', 'Secretary-General of ASEAN Delivers Remarks at the Opening Ceremony of the 2025 World Artificial Intelligence Conference in Shanghai, China', 'July 26, 2025',
           'https://asean.org/secretary-general-of-asean-delivers-remarks-at-the-opening-ceremony-of-the-2025-world-artificial-intelligence-conference-in-shanghai-china/'),
 'liqiang': ('Shanghai Municipal Government', 'China proposes global cooperation body on AI', 'July 26, 2025',
             'https://english.shanghai.gov.cn/en-WAICLatest/20250726/54fe55779ead485a8d71fafc68ff6c42.html'),
 'hinton': ('Yicai Global', "'AI Godfather' Geoffrey Hinton Warns About AI Takeover Risks at WAIC in Shanghai", 'July 28, 2025 (speech of July 26)',
            'https://www.yicaiglobal.com/news/ai-godfather-geoffrey-hinton-warns-about-ai-takeover-risks-at-waic-in-shanghai'),
}

THEME = ('Claims, Verification', [
 ('Claims', ' of greater capability met concrete tests in this month\'s selections. Microsoft evaluated difficult diagnoses, Sakana AI combined models '
  'in a search process, and two laboratories reported gold-level results on Olympiad mathematics. New agents joined research to action, and a '
  'trillion-parameter model was released as open weights while OpenAI held back its own. Each result depended on a particular model, task and method of assessment.'),
 ('Verification', ' gave these announcements their meaning. A published proof could be inspected; a diagnostic benchmark could be examined for its limits. '
  'Outside the laboratory, funding rounds, hiring and computing plans measured ambition in money, while Washington, Brussels and Shanghai set out competing '
  'agendas for governing AI. A cloned voice impersonating the US secretary of state showed what the same technology could do in the wrong hands. '
  'The clearest evidence lay in specific results, stated conditions and commitments whose completion could later be checked.'),
])

WEEKS = [
 (27, 'June 30–July 6', 'Original post published July 6, 2025', [
  ('Meta brings its AI teams into Superintelligence Labs', 'June 30',
   ["Mark Zuckerberg reorganized Meta's AI work under Meta Superintelligence Labs. His staff memo named Alexandr Wang chief AI officer and placed "
    "Nat Friedman alongside him, leading AI products and applied research.{msl}",
    "The reorganization brought research and product development under new leadership, with superintelligence named as the goal."],
   ['GPT-4o', 'Llama 4'], ['2025-W27-L1-2', '2025-W27-L4-5']),
  ('Microsoft tests an orchestrator for difficult diagnoses', 'June 30',
   ["Microsoft reported that its MAI-DxO orchestrator, paired with OpenAI's o3, correctly diagnosed 85.5 percent of cases in a benchmark built from "
    "304 complex New England Journal of Medicine case records. A comparison group of physicians, working without colleagues, reference materials "
    "or AI assistance, averaged 20 percent on the cases they completed.{mai}",
    "The results came from a research benchmark of published cases; testing in clinical care was a later step."],
   ['Llama 4'], ['2025-W27-L4-2']),
  ('Cloudflare tests paid access for AI crawlers', 'July 1',
   ["Cloudflare introduced pay per crawl in private beta. Website owners could allow a crawler free access, block it, or set a price per request. "
    "The system used HTTP's Payment Required response to communicate pricing and supported payment through Cloudflare.{cf}",
    "The experiment gave publishers a way to manage automated access to their pages and to charge for it."],
   ['Llama 4'], ['2025-W27-L4-3']),
  ('TreeQuest coordinates search across several models', 'July 1',
   ["Sakana AI described AB-MCTS, a search method implemented in its TreeQuest library. It can generate new candidate answers, refine promising "
    "ones and choose among models. Initial experiments combined o4-mini, Gemini 2.5 Pro and DeepSeek-R1-0528 on ARC-AGI-2 tasks.{sakana}",
    "The reported result measured whether a correct answer appeared among many attempts within a substantial computation budget, showing what "
    "collaboration among models could add at inference time."],
   ['Llama 4'], ['2025-W27-L4-4']),
  ("Ilya Sutskever becomes SSI's chief executive", 'July 3',
   ["Safe Superintelligence announced that Ilya Sutskever had formally become chief executive and Daniel Levy president. Daniel Gross had left the "
    "company on June 29. Sutskever said the technical team would continue to report to him.{ssi}",
    "The announcement settled the leadership of a laboratory that had released no products and described its work only in general terms."],
   ['GPT-4o'], ['2025-W27-L1-1']),
  ('Isomorphic Labs prepares for human trials', 'Reported July 6',
   ["Colin Murdoch, president of Isomorphic Labs, the Alphabet company spun out of DeepMind in 2021, told Fortune that “the next big milestone is "
    "actually going out to clinical trials” and that the company was staffing up for them. Isomorphic was designing its own drug candidates in "
    "oncology and immunology and had announced $600 million in its first outside funding round on March 31.{iso}",
    "Clinical trials would test the company's candidates in people."],
   ['GPT-4o'], ['2025-W27-L1-3']),
 ]),
 (28, 'July 7–13', 'Original post published July 14, 2025', [
  ("Meta hires Apple's head of foundation models", 'Reported July 7',
   ["Bloomberg reported that Ruoming Pang, who led Apple's foundation-models team of about 100 people, was leaving for Meta Superintelligence Labs "
    "on a package reportedly worth millions of dollars a year.{pang}",
    "The move was among the most prominent in Meta's recruiting of senior AI researchers from its rivals that summer."],
   ['ChatGPT-4o'], ['2025-W28-L1-3']),
  ('An AI-cloned voice impersonates the US secretary of state', 'Reported July 8',
   ["An internal State Department cable, reported by the *Washington Post*, said that someone using AI software to mimic Marco Rubio's voice and "
    "writing style had contacted a US governor, a member of Congress and three foreign ministers. The impostor used a Signal account opened in mid-June "
    "and left voice and text messages.{rubio}",
    "The case showed how voice cloning could be used to impersonate officials who rely on messaging apps."],
   ['DeepSeek-R1'], ['2025-W28-L3-4']),
  ('xAI releases Grok 4 with built-in tool use', 'July 9',
   ["xAI released Grok 4 with native tool use and live search. The model could use a code interpreter and web browsing during reasoning. "
    "The company also introduced Grok 4 Heavy through a new subscription tier.{grok}",
    "Tool access broadened what the system could attempt beyond answering from stored knowledge; its usefulness depended on choosing suitable tools "
    "and checking what they returned."],
   ['ChatGPT-4o', 'DeepSeek-R1'], ['2025-W28-L1-2', '2025-W28-L2-3']),
  ('EU publishes the general-purpose AI Code of Practice', 'July 10',
   ["The European Commission published the final General-Purpose AI Code of Practice. This voluntary tool addressed transparency, copyright, and "
    "safety and security, with the last chapter aimed at providers of models posing systemic risk.{eucode}",
    "Signing the code offered one route toward compliance with the AI Act's binding rules for general-purpose models, which were due to apply from August 2."],
   ['ChatGPT-4o'], ['2025-W28-L1-4']),
  ('Google hires Windsurf leaders in a licensing deal', 'July 11',
   ["Google and Windsurf announced that chief executive Varun Mohan, co-founder Douglas Chen and selected researchers would join Google DeepMind. "
    "Reuters reported a $2.4 billion arrangement that included a non-exclusive technology license, without Google taking a stake in Windsurf.{windsurf}",
    "The arrangement combined recruitment with access to technology while Windsurf continued as a separate business."],
   ['ChatGPT-4o'], ['2025-W28-L1-1']),
  ("Moonshot releases Kimi K2's model weights", 'July 11',
   ["Moonshot AI released Kimi K2 in base and instruction-tuned variants. Its mixture-of-experts architecture contained one trillion parameters, "
    "with 32 billion activated for each token. The release included downloadable weights and support for tool use.{kimi1}{kimi2}",
    "Access to the weights let developers deploy and adapt the model under its license, and put a Chinese model near the front of the open-weight field."],
   ['DeepSeek-R1', 'Gemini 2.5 Flash (week 29)'], ['2025-W28-L2-2', '2025-W29-L3-3']),
  ('OpenAI postpones its open-weight model', 'July 11',
   ["Sam Altman said OpenAI would delay its planned open-weight model, due the following week, to run additional safety tests and review "
    "high-risk areas, adding that “once weights are out, they can’t be pulled back.” He gave no new date; it was the second delay.{owdelay}",
    "The same day Moonshot released its weights, the decision showed the two companies weighing openness and risk differently."],
   ['DeepSeek-R1'], ['2025-W28-L2-1']),
 ]),
 (29, 'July 14–20', 'Original post published July 20, 2025', [
  ('Meta outlines large computing-cluster plans', 'July 14',
   ["Mark Zuckerberg outlined plans for large AI computing clusters. Prometheus was expected to come online in 2026; Hyperion was designed to expand "
    "toward five gigawatts over several years. Reuters reported his statement that Meta would invest hundreds of billions of dollars.{meta}",
    "The plans tied model development to electricity, construction and long-term capital commitments, measured in capacity still to be built."],
   ['GPT-4o', 'Gemini 2.5 Flash'], ['2025-W29-L1-3', '2025-W29-L3-2']),
  ('Thinking Machines raises $2 billion', 'July 15',
   ["Thinking Machines Lab, founded by former OpenAI executive Mira Murati, announced a $2 billion financing round led by Andreessen Horowitz. "
    "Participants included Nvidia, Accel, ServiceNow, Cisco, AMD and Jane Street, according to the company's legal adviser.{tml}",
    "The round showed how much investors would commit to a new laboratory before it had released a product."],
   ['GPT-4o'], ['2025-W29-L1-5']),
  ('Pennsylvania summit brings together AI and energy investment', 'July 15',
   ["At the Pennsylvania Energy and Innovation Summit, Senator Dave McCormick's office announced more than $90 billion in investment commitments "
    "spanning data centers, energy infrastructure and training. Its fact sheet listed projects from companies including Blackstone, CoreWeave and Brookfield.{pa}",
    "The commitments, from many companies over different time horizons, linked AI's growth to power generation in one state."],
   ['Kimi K2'], ['2025-W29-L4-3']),
  ("Google adds Gemini 2.5 Pro and Deep Search to AI Mode", 'July 16',
   ["Google made Gemini 2.5 Pro and Deep Search, which runs many searches and compiles a cited report, available in AI Mode to US subscribers "
    "of its AI Pro and Ultra plans. It also began rolling out a feature that lets Search call local businesses to check prices and availability.{aimode}",
    "Search was taking on research and errands on the user's behalf, with the most capable model reserved for paying subscribers."],
   ['Kimi K2'], ['2025-W29-L4-4']),
  ('ChatGPT agent combines research with computer actions', 'July 17',
   ["OpenAI introduced ChatGPT agent, combining capabilities from Operator and deep research. The system used a virtual computer with browsers, "
    "a terminal and other tools to carry out multi-step tasks. Users could interrupt its work, and sensitive actions required confirmation.{agent}",
    "The release brought information gathering and action into one workflow, with the user kept in the loop for consequential steps."],
   ['GPT-4o', 'Gemini 2.5 Flash'], ['2025-W29-L1-1', '2025-W29-L3-1']),
  ('Perplexity is valued at $18 billion', 'Reported July 17',
   ["Bloomberg reported that Perplexity had raised $100 million at an $18 billion valuation, extending a round that had valued the company at "
    "$14 billion a few months earlier. The report cited a person familiar with the matter; Perplexity declined to comment.{pplx}",
    "The valuation reflected investors' bet on AI-driven search as an alternative to Google's."],
   ['GPT-4o'], ['2025-W29-L1-4']),
  ('OpenAI reports gold-level performance on IMO problems', 'July 19',
   ["OpenAI researcher Alexander Wei reported that an experimental model solved five of six International Mathematical Olympiad problems, scoring "
    "35 out of 42. He said three former IMO medalists independently graded each proof and reached agreement on the scores.{imo1}{imo2}",
    "The model was unreleased and the grading was arranged by OpenAI rather than the competition; the team published its proofs for others to inspect."],
   ['Kimi K2'], ['2025-W29-L4-1']),
 ]),
 (30, 'July 21–27', 'Original post published July 27, 2025', [
  ("Gemini's IMO solutions receive official assessment", 'July 21',
   ["Google DeepMind announced that an advanced version of Gemini Deep Think solved five of six IMO problems and scored 35 out of 42. IMO coordinators "
    "graded and certified the solutions; the announcement included confirmation from IMO president Gregor Dolinar.{gemimo}",
    "The model wrote its proofs in natural language within the competition's time limits, and official grading made the score directly comparable "
    "with those of human contestants."],
   ['Qwen3-235B-A22B-2507'], ['2025-W30-L2-1']),
  ('White House releases its AI Action Plan', 'July 23',
   ["The White House released America's AI Action Plan, setting out more than 90 proposed federal policy actions under three pillars: innovation, "
    "infrastructure, and international diplomacy and security. Priorities included data-center permitting and exports of US AI technology.{plan} "
    "President Trump signed three executive orders the same day, among them “Preventing Woke AI in the Federal Government,” which bars "
    "federal agencies from buying AI models that compromise accuracy for ideological goals.{eos}",
    "The plan joined technology policy to industrial capacity and foreign policy; most of its measures awaited action by agencies."],
   ['Gemini 2.5 Flash', 'GPT-4o (week 29)'], ['2025-W30-L1-1', '2025-W29-L1-2']),
  ('Google brings local AI processing and developer tools to India', 'July 23',
   ["At I/O Connect India in Bengaluru, Google announced onshore processing for Gemini 2.5 Flash, new agentic tools in Firebase Studio, and a "
    "Google Play–Unity training program. It also highlighted Indian startups building models with Gemma.{india}",
    "The announcements addressed the practical conditions for adoption: where data is processed, how applications are built and who has the skills to develop them."],
   ['Gemini 2.5 Flash'], ['2025-W30-L1-3']),
  ('Nadella addresses layoffs amid record AI spending', 'July 24',
   ["In a memo to employees, Microsoft chief executive Satya Nadella addressed job cuts of more than 15,000 positions since January, about 9,000 of "
    "them in July, while the company was spending about $80 billion on AI infrastructure in its fiscal year. He called it “the enigma of success in an "
    "industry that has no franchise value.”{msft}",
    "The memo set out openly the trade-off between investment in AI infrastructure and the size of the workforce."],
   ['Qwen3-235B-A22B-2507'], ['2025-W30-L2-4']),
  ('ASI-Arch explores automated neural-architecture research', 'July 24',
   ["Researchers introduced ASI-Arch, a system that proposed neural-network architectures, implemented them and evaluated them through experiments. "
    "The original paper reported 1,773 experiments focused on linear-attention architectures.{asiarch}",
    "The work extended automation into the design of models themselves, within one family of architectures."],
   ['Qwen3-235B-A22B-2507'], ['2025-W30-L2-HM1']),
  ('World AI Conference opens in Shanghai', 'July 26',
   ["The World Artificial Intelligence Conference opened in Shanghai for three days. At the opening ceremony Premier Li Qiang proposed a world AI "
    "cooperation organization, observing that global AI governance remained fragmented.{liqiang} ASEAN secretary-general Kao Kim Hourn also spoke.{asean} "
    "Geoffrey Hinton warned that AI agents might seek more control to reach their goals, comparing humanity's position to keeping a tiger cub as a pet.{hinton}",
    "Three days after Washington's plan, the conference put China's case for multilateral governance alongside technical demonstrations."],
   ['Gemini 2.5 Flash', 'Qwen3-235B-A22B-2507'], ['2025-W30-L1-2', '2025-W30-L2-2', '2025-W30-L2-3']),
 ]),
]
