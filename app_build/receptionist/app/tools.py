"""
🔧 AI RECEPTIONIST INTEGRATION TOOLS (PORTFOLIO SHOWCASE)
Declares the tools exposed to specialized agents for Sheets, Zendesk, and Exa operations.
"""

from typing import Dict, Any, Optional

def log_lead(
    name: str,
    phone_number: str,
    email: str,
    intent: str,
    urgency: str,
    sentiment: str,
    purchase_order: Optional[str] = "",
    summary: Optional[str] = ""
) -> Dict[str, Any]:
    """Logs the captured customer lead callback details to Google Sheets and Zendesk.

    Args:
        name: The customer's name.
        phone_number: The customer's phone number in E.164 format (e.g. +1XXXXXXXXXX).
        email: The customer's verified email address.
        intent: The reason for calling (e.g. "Lead Capture", "FAQ", "WISMO").
        urgency: The urgency level of the request ("high" or "low").
        sentiment: The customer's sentiment ("neutral" or "negative").
        purchase_order: The optional purchase order number.
        summary: The optional summary of the conversation to sync to CRM.

    Returns:
        A dictionary containing "success" status.
    """
    # Stub implementation. Production code executes sheets.py and zendesk.py clients.
    return {
        "success": True,
        "sync_status": "synced_all"
    }


def wismo_lookup(purchase_order: str) -> Dict[str, Any]:
    """Looks up order shipping status and details in Zendesk using the purchase order number.

    Args:
        purchase_order: The purchase order number to lookup (e.g. PO-XXXXXX).

    Returns:
        A dictionary containing order status, tracking, and details.
    """
    # Stub implementation. Production code queries Zendesk ticketing system.
    return {
        "success": True,
        "found": True,
        "status": "pending",
        "details": f"Found order associated with PO '{purchase_order}'."
    }
