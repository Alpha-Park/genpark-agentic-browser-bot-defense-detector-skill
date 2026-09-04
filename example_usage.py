from client import AgenticBrowserBotDefenseDetectorClient

def main():
    client = AgenticBrowserBotDefenseDetectorClient()
    res = client.inspect_page_for_challenges()
    print('Bot Defense Detector: ' + res['inspection_id'] + ' (' + res['challenge_provider'] + ')')
    print('Detected: ' + str(res['bot_defense_detected']) + ' | Action: ' + res['recommended_bypass_action'])
    print('Report URL: ' + res['inspection_report_url'])

if __name__ == '__main__':
    main()
