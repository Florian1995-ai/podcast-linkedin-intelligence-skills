from scripts.apify_serp import normalize_serp_items
from scripts.discover_podcast_interviews_serp import niche_queries, serp_rows_to_episode_rows


def test_normalize_serp_items_handles_organic_results():
    rows = normalize_serp_items(
        [
            {
                "searchQuery": "pool construction podcast interview",
                "organicResults": [
                    {"title": "Pool Chasers Podcast with Jane Builder", "url": "https://example.com/ep", "description": "Interview with Jane Builder"}
                ],
            }
        ]
    )
    assert rows[0]["query"] == "pool construction podcast interview"
    assert rows[0]["url"] == "https://example.com/ep"


def test_niche_queries_include_major_episode_platforms():
    queries = niche_queries("pool construction", "pool builders", "design build")
    assert any("youtube.com/watch" in q for q in queries)
    assert any("podcasts.apple.com" in q for q in queries)
    assert any("spotify.com/episode" in q for q in queries)


def test_serp_rows_to_episode_rows_extracts_guest_name():
    rows = serp_rows_to_episode_rows(
        [
            {
                "query": "pool construction podcast interview",
                "rank": 1,
                "title": "Pool Builders Podcast with Jane Builder",
                "url": "https://example.com/episode",
                "snippet": "A pool construction interview.",
            }
        ],
        "pool construction",
    )
    assert rows[0]["guest_or_speaker"] == "Jane Builder"
