"""
ADVANCED CORE SECURITY
Integrates all advanced security features
"""

from core_security import ProtectSelfCore
from advanced_biometrics import AdvancedBiometricAuth
from quantum_encryption import QuantumResistantEncryption
from multi_factor_auth import MultiFactorNeuralAuth

class AdvancedProtectSelfCore(ProtectSelfCore):
    """
    Enhanced security core with advanced features
    """
    
    def __init__(self):
        super().__init__()
        self.advanced_biometrics = AdvancedBiometricAuth()
        self.quantum_crypto = QuantumResistantEncryption()
        self.multi_factor = MultiFactorNeuralAuth()
        self.encrypted_data_store = {}
        
    def advanced_biometric_enroll(self, eeg_samples):
        """Advanced biometric enrollment with anti-spoofing"""
        return self.advanced_biometrics.enroll_user(eeg_samples)
    
    def multi_factor_enroll(self, user_biometrics):
        """Enroll multiple biometric factors"""
        self.multi_factor.register_factors(user_biometrics)
        
    def quantum_encrypt_sensitive_data(self, neural_data):
        """Encrypt sensitive neural data with quantum-resistant crypto"""
        encrypted, nonce = self.quantum_crypto.encrypt_neural_data(neural_data)
        data_id = len(self.encrypted_data_store)
        self.encrypted_data_store[data_id] = (encrypted, nonce)
        return data_id
    
    def get_security_status_advanced(self):
        """Enhanced security status with advanced features"""
        base_status = super().get_security_status()
        
        advanced_status = {
            **base_status,
            'quantum_encryption_active': self.quantum_crypto.master_key is not None,
            'multi_factor_registered': bool(self.multi_factor.factors),
            'advanced_biometrics_enrolled': self.advanced_biometrics.user_eeg_template is not None,
            'encrypted_data_items': len(self.encrypted_data_store)
        }
        
        return advanced_status
