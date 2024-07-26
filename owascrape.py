def interact_with_calendar(driver):
    try:
        # Scroll the calendar to ensure all events are loaded
        calendar_body = driver.find_element(By.CSS_SELECTOR, "[role='grid']")
        driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", calendar_body)
        time.sleep(2)  # Wait for potential dynamic content to load
        
        print("Scrolled calendar to load all events.")
    except Exception as e:
        print(f"Error interacting with calendar: {str(e)}")

def scrape_events(driver):
    events = []
    try:
        # Wait for events to be present
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[role='button'][aria-label]"))
        )
        
        # Find all event elements with a more general selector
        event_elements = driver.find_elements(By.CSS_SELECTOR, "[role='button'][aria-label]")
        
        for event in event_elements:
            aria_label = event.get_attribute("aria-label")
            if aria_label:
                # Print each aria-label for debugging
                print(f"Found event with aria-label: {aria_label}")
                
                # Adjust parsing logic based on the actual format of aria-labels
                # This is an example and may need further adjustment
                parts = aria_label.split(", ")
                if len(parts) >= 2:
                    events.append({
                        "title": parts[0],
                        "details": ", ".join(parts[1:])
                    })
        
        print(f"Found {len(events)} events.")
    except Exception as e:
        print(f"Error scraping events: {str(e)}")
    
    return events
