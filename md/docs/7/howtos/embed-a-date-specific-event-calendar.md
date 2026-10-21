---
title: "Embed a date-specific event calendar"
source_url: "https://www.drupal.org/docs/7/howtos/embed-a-date-specific-event-calendar"
page_type: page
last_updated: "Last updated on 25 January 2018"
published: "2012-11-12T06:56:13+00:00"
modified: "2018-01-25T23:52:42+00:00"
breadcrumb: ["Drupal 7", "Site building and development HowTos for Drupal 7"]
fetched: "2026-10-21T08:04:08Z"
raw: "raw/docs/7/howtos/embed-a-date-specific-event-calendar.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Embed a date-specific event calendar

It is fairly simple to display an event calendar for all event content on a site, but sometimes we need to display a date-specific calendar, e.g. for an event listing view. To do this, follow the instructions below.

*Modules needed:*

- [Views](https://www.drupal.org/project/views)
- [Calendar](https://www.drupal.org/project/calendar)
- [Date](https://www.drupal.org/project/date)
- [Views Field View](https://www.drupal.org/project/views_field_view)
- [Views PHP](https://www.drupal.org/project/views_php)

1\. Create a new content type for events (e.g. 'events') and add starting and ending date fields. You can create now create your desired event content.

2\. Add a new calendar view from the existing template in the calendar module(admin/structure/views add-template). From the list, you should select "A calendar view of the 'field_yourfieldname' field in the 'node' base table."(Display type of the view: Month)

3\. In the edit mode of your calendar view, under filter criteria, select the event content type that you created above. Also add a contextual filter - 'Content: Nid'. Save the view.

4\. Create a new view for your event listing. This view should have a page display. Under filter criteria, select the event content type that you created above. Add 'Content: Nid' as a new field and tick the option 'Exclude from display' in the configuration page. Add another field, 'Global: PHP', for grabbing the current date and passing it as an argument to the calendar view. You should write 'print date("Y-m")' in the Output Code field and tick the option 'Exclude from display' in the configuration page.

5\. Embed the calendar view in your event listing by adding a new field: 'Global: View'. (See the attached image for the configuration of this field.) Here you should specify the name of your calendar view in the View setting section and also specify the views display type. Then, you should add '\[%php\]/\[%nid\]' as a contextual filter for the calendar view. Save the view. Your customized event listing is now ready!
