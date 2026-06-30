# Encryption

Source: https://www.unifyapps.com/docs/unify-data/encryption
Section: data

---

AES (**Advanced Encryption Standard**) is a symmetric encryption algorithm widely used to **secure data**. It encrypts data using the same key for both encrypting and decrypting, making it essential to keep the key secret.

This guide will walk you through using AES encryption and decryption transformations to protect sensitive data, such as PII (Personally Identifiable Information).

## AES Encryption

AES encryption allows you to secure any field with a 256-bit encryption key.

"AES Encryption method is crucial for protecting sensitive information from unauthorized access."

![Frame 427319219 (1).png](_img/75f8b1475b199387.webp)

### Steps to Apply Encryption

1. **AES Encryption Key**:
  - This is the 256-bit encryption key required to encrypt the data.
  - **Example**: 6b71RouelDY2xLFfy1x0oYXq3oUDkfuc. **Note:** Generate a strong key using a reliable cryptographic tool and store it securely. Do **not** hard-code the key in your application code.
2. **Initialization Vector (IV)**:
  - An IV is a 128-bit value used with the encryption key to enhance security.
  - **Example**: d4QaIQMb8RbOG5ai.

![Group 65.png](_img/e5bdbf5cd939d5a7.webp)

### Testing Encryption

After applying the encryption transformation, test it to ensure it is working correctly.

You should compare the encrypted output with expected values to verify the encryption process.

**Example:** Encrypting a customer's social security number before storing it in a database:

- **Input**: Sample String
- **Encrypted Output**: enhTmMxQS+2o1Oi1nvnpxA==

  ![Frame 427319214 (5).png](_img/8cba56a8706636c3.webp)

## AES Decryption

AES decryption uses the same symmetric algorithm to convert encrypted data back to its original form.

"Decryption is essential for retrieving and using the original data."

![Frame 427319215 (5).png](_img/79df0132ac20abe1.webp)

### Steps to Apply Decryption

1. **AES Decryption Key**:
  - Enter the 256-bit encryption key used for encryption.
  - **Example**: 6b71RouelDY2xLFfy1x0oYXq3oUDkfuc. **Note:** The key must match the one used during encryption for successful decryption.
2. **Initialization Vector (IV)**:
  - Provide the same 128-bit IV used during encryption.
  - **Example**: d4QaIQMb8RbOG5ai.

![Frame 427319215 (6).png](_img/37e8a6a76da741b0.webp)

### Testing Decryption

After applying the decryption transformation, test it to ensure it is working correctly.

You should compare the decrypted output with the original data to verify the decryption process.

**Example:** Decrypting a customer's social security number to verify identity:

- **Encrypted Input**: enhTmMxQS+2o1Oi1nvnpxA==
- **Decrypted Output**: 123-45-6789

![Frame 427319216 (4).png](_img/1424e86aa24cfb62.webp)

## Best Practices

- **Key Management**: Implement a secure key management system to handle encryption keys. This may involve using key management services (KMS) provided by cloud providers.
- **Regular Audits**: Regularly audit your encryption and decryption processes to ensure they comply with security standards and best practices.
