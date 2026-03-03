"""
Firebase Service for state management and real-time data streaming.
CRITICAL: Uses firebase-admin as required by ecosystem constraints.
Handles all database, state management, and real-time streaming needs.
"""

import logging
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional, Union
import json

try:
    import firebase_admin
    from firebase_admin import credentials, firestore, db
    from google.cloud.firestore_v1 import DocumentSnapshot
    FIREBASE_AVAILABLE = True
except ImportError:
    logging.warning("firebase-admin not available. Install with: pip install firebase-admin")
    FIREBASE_AVAILABLE = False

class FirebaseService:
    """Firebase service for state management and real-time data streaming."""
    
    def __init__(self, service_account_path: str, database_url: str):
        """
        Initialize Firebase service.
        
        Args:
            service_account_path: Path to Firebase service account key JSON
            database_url: Firebase Realtime Database URL
            
        Raises:
            FileNotFoundError: If service account file doesn't exist
            ValueError: If Firebase initialization fails
        """
        if not FIREBASE_AVAILABLE:
            raise ImportError("firebase-admin package not installed")
        
        # Verify file exists before attempting to read