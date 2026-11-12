---
description: Rewrite one document in plain, natural language for ordinary Yerevan residents, keeping its meaning, language, structure, and length.
agent: build
model: openrouter/google/gemini-3.8-flash
subagent: true
---

Rewrite the single document at the path given after the command:

`$ARGUMENTS`

You are running as a subagent in a fresh session. The conversation that invoked you is not visible, and no one can answer questions while you work, so treat the path above and these instructions as the complete brief. Return your report as your final message, and do not delegate to further subagents. The rewrite is the whole job: your report closes it, and nobody is waiting to continue the work from it.

## One file, nothing else

- The argument is one file path, relative to the repository root. If it is empty, points to a directory, or the file cannot be read, report the problem in one sentence and stop. Do not search for a similar file, guess a path, or ask for a replacement.
- Read that exact file with the `read` tool. Do not read any other file in this repository or elsewhere: no sibling translations, no other articles, no `AGENTS.md`, no style guides, no skills, no configuration. These instructions are the whole brief.
- The only file you may change is the one that was specified. Use the `edit` or `write` tools and leave everything else untouched.
- Never use code or shell commands to inspect, transform, or save the document. No `sed`, `awk`, `python`, `perl`, `node`, `prettier`, `make format`, no formatters, and no one-off scripts. Edit the prose directly.

## Keep the document whole

- Detect the document's main language and keep it. English stays English, Russian stays Russian, Armenian stays Armenian. Do not translate, and do not add another language version.
- Leave the frontmatter alone, including its format and keys. Same for heading levels and their order, links and their URLs, image names, tables, lists, blockquotes, and emphasis that carries meaning.
- Keep every fact, figure, date, name, source, and caveat. This is an editing pass, not a fact-check, a summary, or a new argument. If a sentence is confusing, say the same thing more simply instead of dropping it.
- Keep direct quotations and official titles verbatim, even when they are stiff.
- Keep the document's own terminology for a thing. Do not introduce synonyms that make the text wobble between two names for one object.
- Preserve meaning over elegance: never soften a verdict, a criticism, or a number to make the prose flow better.
- Keep the length. The result should be about the same size as the original, paragraph by paragraph. Noticeably longer means you started explaining; noticeably shorter means you dropped something.
- Keep the order. Sentences stay where they are and in the same sequence, paragraphs are not merged or moved, and no heading, list item, table row, or image changes place.

## Write for the reader

The audience is an ordinary Yerevan resident: someone who lives in the city, cares about trees and courtyards, and has no professional training in planning, law, or ecology. They are fluent in Armenian and Russian, and read English as a second or third language. Write so that this person understands the point on the first pass.

Prefer:

- Plain, spoken language and the words people actually use at home and in the courtyard.
- Short sentences, one idea each, one rewritten sentence for each original sentence.
- Active voice with a concrete subject: who does what, to whom, and where.
- Direct address to the reader, where the original already uses it.
- Concrete nouns instead of abstract bundles: "the park is fenced off" rather than "access restrictions are in place".

Avoid:

- Calques. Write the thought as a native speaker of that language would, not by carrying over English word order or English metaphors.
- Bureaucratese and officialese: "осуществляется", "является", "в рамках", "данный", "принимая во внимание", "was implemented", "in order to ensure", "with regard to".
- Technical jargon and slang alike. If a term is unavoidable, keep the document's own word for it instead of inventing a gloss.
- Idioms, literary flourishes, and rhetorical padding that assume a native English reader. No "Shakespearean" phrasing, no "it is worth noting that", no metaphors doing the work of a plain statement.
- Long chains of nouns, stacked participles, and sentences that only make sense when read twice.

## No AI fingerprints

The document should read like a person who knows the subject wrote it. Strip the marks of machine prose where they are already there, and never add new ones.

Cut or rewrite these on sight:

- Throat-clearing openers: "In today's world", "When it comes to", "At the end of the day", "It's worth noting", "It's important to note", "Here's the thing", "Let's dive in".
- The "not just X, but Y" frame: "This isn't just about trees, it's about community", "not only … but also", "more than just a park".
- Hollow abstractions and intensifiers: "crucial", "vital", "pivotal", "robust", "seamless", "vibrant", "holistic", "multifaceted", "leverage", "foster", "navigate", "landscape" as a metaphor, "testament to", "underscores", "showcases".
- Scaffolding where plain sequencing would do: "Moreover", "Furthermore", "Additionally", "Notably", "Ultimately", "In essence".
- Rhetorical questions the writer then answers, and dramatic one-line fragments: "The result?", "The catch?", "And that matters."
- Rule-of-three lists kept for rhythm rather than content, and "from … to …" ranges that name nothing in particular.
- A closing sentence in each paragraph that restates the paragraph.
- Perfectly even sentence lengths and a tidy metaphor in every paragraph. Written prose is uneven; leave the unevenness alone.

The same applies in the other languages: Russian "в современном мире", "важно отметить", "стоит подчеркнуть", "играет важную роль", "является неотъемлемой частью", "не только …, но и", "это не просто X, это Y"; Armenian "ժամանակակից աշխարհում", "կարևոր է նշել", "հարկ է ընդգծել", "կարևոր դեր է խաղում", "ոչ միայն …, այլև".

Two cautions. The author's deliberate style is not an AI tell: a blunt verdict line, an em dash, an unusually short sentence are all fine, so do not sand them down. And do not trade one cliché for another — if a sentence exists only to sound good, say the plain thing in its place, at the same length.

## Language notes

English: short sentences, common words, plain word order. The reader handles English fine but reads it as a foreign language, so cut idioms, cultural references, and rare vocabulary. Prefer "the city says" to "the city contends", and "about" to "approximately" when the number is rough.

Russian: write living Russian, not a translation. Watch for calques such as "делает смысл", "имеет место быть", "в конечном итоге" used as filler, and for chains of genitives. Prefer verbs to verbal nouns.

Armenian: use natural Eastern Armenian syntax and punctuation (։, ՝, «»), and keep the standard spellings of place names. Avoid calques from Russian or English, overlong noun phrases, and bookish connectors that no one says aloud.

## How to work

1. Read the specified file once, from start to finish.
2. Note its language, its audience, and the argument it makes, section by section.
3. Rewrite sentence by sentence, in place. Keep every sentence in its position and order, with paragraph breaks, headings, and list items exactly where they are. Do not merge, move, add, or delete sentences, and do not reorder anything. Most of the job is de-translation: where a sentence reads like the English was carried over word by word, say it the way a native speaker of that language would. In an English document, apply the same test to press-release phrasing and borrowed metaphors. If a sentence is truly unreadable, split it inside its own paragraph — but do not restructure the text around it.
4. Leave alone any sentence that already reads naturally, even if you would have worded it differently. This is a repair pass, not a restyling.
5. Before finishing, read the same file again and check that the frontmatter is intact, the links and numbers are unchanged, no section or image went missing, the language is still the same one you started with, and the word count is close to the original.
6. Report in this exact shape, and nothing else:

   File: <path, exactly as given>
   Language: <language detected>
   Changed: <up to three short lines, what kind of repair was made>
   Left alone: <sentences kept as-is that looked like candidates; omit if none>
   Status: done — the file on disk is the deliverable. Nothing is pending and nothing is needed from the caller.

   Do not paste the document back. Do not suggest next steps, do not propose follow-up work, and do not mention other files or translations. Reporting is a receipt, not a handoff.
