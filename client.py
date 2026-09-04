class AgenticBrowserBotDefenseDetectorClient:
    def inspect_page_for_challenges(self, page_html_snippet='<div id="cf-turnstile-wrapper">...</div>', http_status_code=403):
        return {
            'inspection_id': 'bot_det_8812',
            'bot_defense_detected': True,
            'challenge_provider': 'CLOUDFLARE_TURNSTILE',
            'recommended_bypass_action': 'DELEGATE_TO_STEALTH_RESIDENTIAL_PROXY_AND_SOLVER',
            'exponential_backoff_seconds': 4.5,
            'captcha_screenshot_url': 'https://browserbase.bot.genpark.ai/challenges/8812.png',
            'inspection_report_url': 'https://browserbase.bot.genpark.ai/reports/8812.json'
        }
