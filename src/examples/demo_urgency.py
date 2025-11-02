"""
PROTECTSELFNOWASAP DEMONSTRATION
IMMEDIATE SECURITY PROTOCOLS ACTIVATION
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core_security import ProtectSelfCore, SecurityState

def main():
    print("🚨 PROTECTSELFNOWASAP ACTIVATION 🚨")
    print("=====================================")
    
    # Initialize security core
    security = ProtectSelfCore()
    
    print("1. BOOTING IN AIR-GAP MODE...")
    status = security.get_security_status()
    print(f"   • Wireless Physical Status: {'❌ TERMINATED' if not status['wireless_physical_status'] else '⚠️  ACTIVE'}")
    print(f"   • Security State: {status['security_state']}")
    
    print("\n2. BIOMETRIC REGISTRATION...")
    # User registers their neural signature
    my_neural_signature = "user_unique_brain_pattern_alpha_theta_123"
    security.biometric_authenticate(my_neural_signature)
    
    status = security.get_security_status()
    print(f"   • Biometric Registered: {'✅ YES' if status['biometric_registered'] else '❌ NO'}")
    print(f"   • Panic Signal Ready: {'✅ ARMED' if status['panic_signal_registered'] else '❌ DISABLED'}")
    
    print("\n3. ATTEMPT UNAUTHORIZED ACCESS...")
    print("   • Intruder neural pattern detected...")
    intruder_signature = "malicious_hack_pattern"
    security.biometric_authenticate(intruder_signature)
    
    status = security.get_security_status()
    print(f"   • Security State: {status['security_state']}")
    print(f"   • Auto-response: {'🚨 AIRGAP RE-ENGAGED' if status['security_state'] == 'AIRGAP_ACTIVE' else '⚠️  SYSTEM VULNERABLE'}")
    
    print("\n4. PANIC SIGNAL ACTIVATION...")
    print("   • User thinking emergency kill pattern...")
    security.panic_signal_detected("user_unique_brain_pattern_alpha_theta_123PANIC")
    
    status = security.get_security_status()
    print(f"   • Security State: {status['security_state']}")
    print(f"   • Wireless Status: {'❌ HARDWARE DISCONNECTED' if not status['wireless_physical_status'] else '⚠️  STILL ACTIVE'}")
    
    print("\n5. SECURITY LEDGER AUDIT...")
    print(f"   • Events Logged: {status['events_logged']}")
    for i, event in enumerate(security.security_ledger[-3:]):  # Show last 3 events
        print(f"     {i+1}. {event.event_type} - {event.data_hash[:16]}...")
    
    print("\n" + "="*50)
    print("🔒 PROTECTSELFNOWASAP: INFINITE DEFENSE ACTIVE")
    print("🔒 NEURAL SOVEREIGNTY: VERIFIED")
    print("🔒 ZERO-TRUST: ENFORCED")

if __name__ == "__main__":
    main()
