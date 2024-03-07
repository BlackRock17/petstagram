from django import template

register = template.Library()


@register.inclusion_tag("common/tags/prev_button.html", takes_context=True)
def prev_button(context):

    page_obj = context["page_obj"]
    pet_name_pattern = context["pet_name_pattern"]

    search_query = ""
    if pet_name_pattern:
        search_query = f"&pet_name_pattern={pet_name_pattern}"


    page_query = "#"

    if page_obj.has_previous():
         page_query = f"?page={page_obj.previous_page_number()}"

    class_name = "" if page_obj.has_previous() else "disabled"

    return {
        "page_query": page_query,
        "search_query": search_query,
        "class_name": class_name,
        "arrow_class_name": "fa-solid fa-arrow-left",
    }


@register.inclusion_tag("common/tags/prev_button.html", takes_context=True)
def next_button(context):

    page_obj = context["page_obj"]
    pet_name_pattern = context["pet_name_pattern"]

    search_query = ""
    if pet_name_pattern:
        search_query = f"&pet_name_pattern={pet_name_pattern}"


    page_query = "#"

    if page_obj.has_next():
         page_query = f"?page={page_obj.next_page_number()}"

    class_name = "" if page_obj.has_next() else "disabled"

    return {
        "page_query": page_query,
        "search_query": search_query,
        "class_name": class_name,
        "arrow_class_name": "fa-solid fa-arrow-right",
    }
