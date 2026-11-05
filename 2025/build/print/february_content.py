# February 2025 print chapter, v0.2: content (American style).
COVERS = ('Edited from the reconstructed week of February 3–9 and the original posts published February 17 and 24, 2025.')

SOURCES = {
 'cc': ('Anthropic', 'Constitutional Classifiers: Defending against universal jailbreaks', 'February 3, 2025; results update February 13',
        'https://www.anthropic.com/research/constitutional-classifiers'),
 's1': ('Niklas Muennighoff and colleagues', 's1: Simple test-time scaling', 'January 31, 2025; version 2, February 3', 'https://arxiv.org/abs/2501.19393v2'),
 'resp': ('Google', 'Responsible AI: Our 2024 report and ongoing work', 'February 4, 2025',
          'https://blog.google/innovation-and-ai/products/responsible-ai-2024-report-ongoing-work/'),
 'prin2018': ('Google', 'AI at Google: our principles', 'June 7, 2018', 'https://blog.google/innovation-and-ai/products/ai-principles/'),
 'wired': ('WIRED', 'Google Lifts a Ban on Using Its AI for Weapons and Surveillance', 'February 4, 2025', 'https://www.wired.com/story/google-responsible-ai-principles/'),
 'kakao': ('Kakao', 'Kakao and OpenAI announce Strategic Collaboration, a first in Korea', 'February 4, 2025', 'https://www.kakaocorp.com/page/detail/11451'),
 'figure': ('TechCrunch', 'Figure drops OpenAI in favor of in-house models', 'February 4, 2025', 'https://techcrunch.com/2025/02/04/figure-drops-openai-in-favor-of-in-house-models/'),
 'gemini': ('Google Developers Blog', 'Gemini 2.0: Flash, Flash-Lite and Pro', 'February 5, 2025', 'https://developers.googleblog.com/en/gemini-2-family-expands/'),
 'lechat': ('Mistral AI', 'The all new le Chat: Your AI assistant for life and work', 'February 6, 2025', 'https://mistral.ai/news/all-new-le-chat/'),
 'science': ('Élysée', 'Science Days', 'updated January 17, 2025; program for February 6–7', 'https://www.elysee.fr/en/sommet-pour-l-action-sur-l-ia/science-days'),
 'macron109': ('Reuters, via Investing.com', 'Macron signals investments of 109 billion euros in French AI by private sector', 'February 9, 2025',
               'https://www.investing.com/news/economy-news/macron-signals-investments-of-109-billion-euros-in-french-ai-by-private-sector-3857923'),
 'champions': ('General Catalyst', 'Launching the “EU AI Champions Initiative” to Unlock Europe’s Full Potential in AI', 'February 10, 2025', 'https://www.generalcatalyst.com/stories/euaici'),
 'elysee': ('Élysée', 'Clôture de la première journée du Sommet pour l’action sur l’IA', 'February 10, 2025',
            'https://www.elysee.fr/emmanuel-macron/2025/02/10/cloture-de-la-premiere-journee-du-sommet-pour-laction-sur-lia'),
 'chip': ('Reuters (via The Edge Malaysia)', 'OpenAI set to finalise first custom chip design this year', 'February 10, 2025', 'https://theedgemalaysia.com/node/743937'),
 'investai': ('European Commission', 'EU launches InvestAI initiative to mobilise €200 billion of investment in artificial intelligence', 'February 11, 2025; release IP/25/467, updated April 10',
              'https://ec.europa.eu/commission/presscorner/api/files/document/print/en/ip_25_467/IP_25_467_EN.pdf'),
 'vance': ('Office of the Vice President, preserved by the American Presidency Project', 'Remarks by Vice President Vance at the Artificial Intelligence Action Summit', 'February 11, 2025',
           'https://www.presidency.ucsb.edu/sites/default/files/documents_with_attached_files/376290/2025-02-11remarksbyvicepresidentvanceattheartificialintelligenceactionsummittrimmed.pdf'),
 'firefly': ('Adobe', 'Adobe Expands Generative AI Offerings Delivering New Firefly App with Industry’s First Commercially Safe Video Model', 'February 12, 2025',
             'https://news.adobe.com/news/2025/02/firefly-web-app-commercially-safe'),
 'veo': ('YouTube', 'Imagine it, create it: Veo 2 is coming to YouTube Shorts', 'February 13, 2025', 'https://blog.youtube/news-and-events/veo-2-shorts/'),
 'cohere': ('News/Media Alliance', 'News/Media Alliance Announces Industry Lawsuit Against AI Content Theft', 'February 13, 2025',
            'https://www.newsmediaalliance.org/news-media-alliance-announces-industry-lawsuit/'),
 'musk': ('Reuters', "OpenAI board rejects Musk's $97.4 billion offer", 'February 14, 2025; updated February 15 UTC',
          'https://www.reuters.com/technology/openai-board-rejects-musks-974-billion-offer-2025-02-14/'),
 'grok1': ('xAI', 'Grok 3 Beta - The Age of Reasoning Agents', 'February 19, 2025', 'https://x.ai/news/grok-3'),
 'grok2': ('Reuters', "Musk's xAI unveils Grok-3 AI chatbot to rival ChatGPT, China's DeepSeek", 'February 18, 2025',
           'https://www.reuters.com/technology/artificial-intelligence/musks-xai-unveils-grok-3-ai-chatbot-rival-chatgpt-chinas-deepseek-2025-02-18/'),
 'pipc': ('Personal Information Protection Commission, Republic of Korea', 'DeepSeek Temporarily Suspends Its Application Service in Korea', 'release February 17, 2025; English page February 18',
          'https://pipc.go.kr/eng/user/ltn/new/noticeDetail.do?bbsId=BBSMSTR_000000000001&nttId=2784'),
 'novelty': ('Arash Lagzian, Srinivas Anumasa and Dianbo Liu', 'Multi-Novelty: Improve the Diversity and Novelty of Contents Generated by Large Language Models via inference-time Multi-Views Brainstorming',
             'February 18, 2025; version 1', 'https://arxiv.org/html/2502.12700v1'),
}

THEME = ('Policy, Infrastructure', [
 ('Policy', ' shaped the conditions under which AI could be developed and used. In Paris, governments and businesses set out competing priorities '
  "for investment and regulation. Google revised its principles, while South Korea's privacy regulator addressed the distribution of DeepSeek's app."),
 ('Infrastructure', ' gave these debates a physical scale. France promoted its electricity supply and investment plans; the European Commission '
  'proposed financing for large computing facilities; OpenAI was reported to be finishing its first chip design. Alongside them came new model releases, '
  'mobile assistants and video tools, while research on reasoning and safeguards asked how existing systems could become more useful and dependable.'),
])

RETRO = ('Reconstructed in October 2026. Selections by Claude, ChatGPT, DeepSeek and Grok were compiled in 2026 and were not all independent: '
         "ChatGPT had read Claude's draft; Grok received suggested stories; DeepSeek used sources supplied by the collection.")

C = 'Claude (Opus 5.5)'; G = 'ChatGPT (GPT-6)'; D = 'DeepSeek V4.1-Flash-1017'; K = 'Grok 4 (prompted)'
P7 = ['DeepSeek-R1', 'Perplexity Pro Search', 'Copilot']

WEEKS = [
 (6, 'February 3–9', RETRO, [
  ('Constitutional Classifiers face adversarial testing', 'February 3',
   ["Anthropic introduced input and output classifiers trained with synthetic examples derived from written rules. The company reported stronger "
    "resistance to jailbreaks in its evaluations and opened a public challenge. Its earlier prototype had also imposed substantial computing overhead "
    "and rejected too many harmless requests.{cc}",
    "The work treated safety as a system-level engineering problem, with robustness, cost and ordinary usability measured together."],
   [C, G], ['2025-W06-L1-4', '2025-W06-L2-3']),
  ('s1 explores reasoning with a small training set', 'February 3 revision; first posted January 31',
   ["The s1 researchers fine-tuned Qwen2.5-32B-Instruct on 1,000 questions paired with reasoning traces. Their “budget forcing” method controlled how "
    "long the model continued reasoning. The paper reported improvements on specified mathematics benchmarks and released the model, data and code.{s1}",
    "The experiment separated two ways to improve answers: fine-tuning an existing model and allocating more computation when it answers."],
   [C, G], ['2025-W06-L1-5', '2025-W06-L2-4']),
  ('Google revises its AI principles', 'February 4',
   ["Google replaced its earlier framework with principles centered on innovation, responsible development and collaboration. The revised principles "
    "omitted the 2018 exclusions concerning weapons and surveillance that violated internationally accepted norms. Google linked the revision to "
    "global competition and the national-security interests of democracies.{resp}{prin2018}{wired}",
    "The change altered the company's stated boundaries for acceptable applications of AI."],
   [C, G, K], ['2025-W06-L1-2', '2025-W06-L2-2', '2025-W06-L4-1']),
  ('Kakao and OpenAI announce a partnership', 'February 4',
   ["Kakao announced plans to incorporate OpenAI technology into its Korean services, including Kanana and its wider digital ecosystem. The companies "
    "also planned joint product development, while Kakao intended to deploy ChatGPT Enterprise internally.{kakao}",
    "The partnership connected model development to an established distribution network, with the integrations still to be built."],
   [D], ['2025-W06-L3-1']),
  ('Figure ends its collaboration with OpenAI', 'February 4',
   ["Humanoid-robot maker Figure AI said it was leaving its agreement with OpenAI after a “major breakthrough” in robot AI built in-house. Chief "
    "executive Brett Adcock said that “to solve embodied AI at scale in the real world, you have to vertically integrate robot AI,” and promised to "
    "show something new within 30 days.{figure}",
    "The split showed robotics companies seeking to own the models that drive their machines, a year after the two companies' partnership was announced."],
   [D], ['2025-W06-L3-2']),
  ('Gemini 2.0 expands for developers', 'February 5',
   ["Google made Gemini 2.0 Flash generally available through the Gemini API, Google AI Studio and Vertex AI. Flash-Lite entered public preview, while "
    "Gemini 2.0 Pro remained experimental. Flash supported multimodal input and text output; other output modes were still planned.{gemini}",
    "The release offered developers a choice of cost and capability, with different readiness levels across the family."],
   [C, G, K], ['2025-W06-L1-1', '2025-W06-L2-1', '2025-W06-L4-2']),
  ('Le Chat reaches mobile users', 'February 6',
   ["Mistral released Le Chat on iOS and Android alongside a broader update to its assistant. The announcement offered free access and a paid Pro tier, "
    "extending the product beyond its browser interface.{lechat}",
    "Mobile distribution made the assistant easier to reach in daily use, making access part of the competition alongside model performance."],
   [D], ['2025-W06-L3-3']),
  ('Science opens the Paris summit program', 'February 6–7',
   ["The Paris AI Action Week program placed an international conference on AI, Science and Society at the Institut Polytechnique de Paris before the "
    "leaders' summit. Its agenda addressed AI's effects on scientific research and society, bringing an academic strand into the wider policy gathering.{science}",
    "The program connected research questions with the decisions facing governments and industry."],
   [D], ['2025-W06-L3-4']),
  ('France announces €109 billion in prospective investment', 'February 9',
   ["President Emmanuel Macron announced €109 billion in prospective private investment in French AI over the coming years, ahead of the Paris summit. "
    "The figure described investment commitments and plans.{macron109}",
    "The announcement made financing and computing capacity central to France's case for a larger role in AI."],
   [C, G], ['2025-W06-L1-3', '2025-W06-L2-5']),
 ]),
 (7, 'February 10–16', 'Original post published February 17, 2025', [
  ('France links AI investment to electricity supply', 'February 10',
   ["At the Paris summit, Macron presented France's nuclear-based electricity supply, available sites and engineering talent as advantages for AI "
    "investment. He urged companies to build computing facilities in France and called for faster development.{elysee}",
    "His pitch brought the physical requirements of AI into view: power, land and construction capacity, alongside software and research."],
   P7, ['2025-W07-L1-2']),
  ('European companies launch AI Champions', 'February 10',
   ["General Catalyst launched the EU AI Champions Initiative with more than 60 European companies. The initiative aimed to connect technology providers, "
    "investors and established businesses to accelerate AI adoption across industry.{champions}",
    "Its emphasis was practical deployment: linking model capabilities to manufacturing, energy and other sectors with existing customers and operations."],
   P7, ['2025-W07-L2-2']),
  ('OpenAI is reported to be finishing its first chip design', 'Reported February 10',
   ["Reuters reported that OpenAI was finalizing the design of its first in-house AI chip, to be made by TSMC on its 3-nanometer process and developed "
    "with Broadcom. The design was expected to go to fabrication within months, with mass production targeted for 2026. OpenAI and TSMC declined to comment.{chip}",
    "The effort aimed to reduce OpenAI's dependence on Nvidia for the hardware its models run on."],
   P7, ['2025-W07-L2-1']),
  ('InvestAI targets €200 billion in investment', 'February 11',
   ["The European Commission launched InvestAI to mobilize €200 billion for AI, including a proposed €20 billion European fund for AI gigafactories: "
    "planned large computing facilities for training advanced models. The initiative combined public and private financing; €200 billion was a "
    "mobilization target, not EU budget spending.{investai}",
    "The proposal sought to widen access to the computing capacity needed for large-scale model development."],
   P7, ['2025-W07-L1-3']),
  ('Vance argues for lighter AI regulation', 'February 11',
   ["US Vice President JD Vance used his Paris summit speech to advocate policies favoring AI investment and development. He warned that excessive "
    "regulation could inhibit the industry and stressed the importance of electricity, semiconductors and American technological leadership.{vance}",
    "The speech made a clear policy case for prioritizing expansion and infrastructure in international AI discussions."],
   P7, ['2025-W07-L1-4']),
  ('Firefly expands video generation', 'February 12',
   ["Adobe released its updated Firefly application with the Firefly Video Model in public beta. Generate Video accepted text prompts or images, with "
    "controls for camera movement and an initial output resolution of 1080p.{firefly}",
    "Adobe presented the model as commercially safe, bringing generated footage into a creative workflow linked to its editing applications."],
   P7, ['2025-W07-L1-5']),
  ('Veo 2 adds generated clips to YouTube Shorts', 'February 13',
   ["YouTube announced Veo 2 integration for Dream Screen and the ability to generate standalone clips for Shorts. Creators could use text prompts to "
    "produce footage, extending the earlier feature for generated backgrounds.{veo}",
    "Video generation was becoming an editing tool inside a distribution platform, reducing the steps between creating a clip and publishing it."],
   P7, ['2025-W07-L1-5']),
  ('Publishers bring a case against Cohere', 'February 13',
   ["News and magazine publishers filed a copyright and trademark infringement case against Cohere in the Southern District of New York. The News/Media "
    "Alliance announced the filing on behalf of its participating members.{cohere}",
    "The case placed the use of publishers' material in AI services before a court."],
   P7, ['2025-W07-L2-3']),
  ('OpenAI rejects the Musk-led offer', 'February 14',
   ["OpenAI's board rejected the $97.4 billion offer from an Elon Musk-led consortium. The board said OpenAI was not for sale and that any "
    "reorganization would strengthen its nonprofit mission.{musk}",
    "The dispute put institutional control and the nonprofit's role at the center of the company's financing debate."],
   P7, ['2025-W07-L1-1']),
 ]),
 (8, 'February 17–23', 'Original post published February 24, 2025', [
  ('xAI introduces Grok 3', 'February 17, Pacific time',
   ["xAI unveiled Grok 3 on the evening of February 17 in the United States. Its subsequent technical announcement described Grok 3 and Grok 3 mini "
    "reasoning models, using additional computation to work through problems before answering.{grok1}{grok2}",
    "The release extended competition in reasoning systems; the benchmark results published with it were xAI's own evaluations."],
   ['Gemini 2.0 Flash'], ['2025-W08-L4-1']),
  ('DeepSeek pauses new downloads in South Korea', 'Announced February 17; effective February 15',
   ["South Korea's privacy regulator announced that DeepSeek had removed its app from local app stores while addressing compliance with personal-data "
    "law. New downloads stopped on February 15. Existing app users and web users could still access the service; the English notice appeared on February 18.{pipc}",
    "The episode showed how data-handling requirements could affect the distribution of an AI service after launch."],
   ['Gemini 2.0 Flash'], ['2025-W08-L4-3']),
  ('Multi-Novelty tests more varied model outputs', 'February 18',
   ["The Multi-Novelty preprint proposed supplying multiple textual and visual perspectives to models during inference. Experiments included GPT-4o "
    "and other language models, with responses assessed for diversity, novelty and correctness. The authors reported improvements under their chosen evaluation methods.{novelty}",
    "The work explored variation in outputs without changing model architecture."],
   ['Gemini 2.0 Flash'], ['2025-W08-L4-4']),
 ]),
]
