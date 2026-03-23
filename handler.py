import runpod
import audalign
import os

def handler(job):
    # 1. Get the URLs from Lovable's request
    job_input = job['input']
    yt_url = job_input.get('youtube_url')
    rss_url = job_input.get('rss_url')

    if not yt_url or not rss_url:
        return {"error": "Missing YouTube or RSS URL"}

    # 2. Initialize Audalign
    ada = audalign.Audalign()
    
    # 3. Find the offset (Shazam-style match)
    # We look at the first 5 minutes (300 seconds) to find the intro match
    results = ada.align_files(yt_url, rss_url, start_end=(0, 300))
    
    # 4. Return the exact seconds to offset
    return {"offset_seconds": results.get('offset_seconds', 0)}

runpod.serverless.start({"handler": handler})
