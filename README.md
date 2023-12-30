#  RSA Decoder in Python

Welcome to the RSA Decoder project! This is a Python implementation of an RSA (Rivest–Shamir–Adleman) decoder. RSA is a widely used cryptography system that ensures security and privacy across various applications, including securing emails, passwords, private browsing, and online payments 

## Security Considerations

While RSA is a robust cryptographic system, it is essential to acknowledge that no system is entirely secure. The advent of quantum computation poses a potential threat to RSA. Quantum computers could theoretically crack an RSA key in polynomial time, making it vulnerable to attacks. However, practical quantum computation capable of affecting data security is not expected in the near future.

In the meantime, there are classical methods to exploit vulnerabilities in RSA keys. This project focuses on exploring these methods by attempting to crack 21 RSA keys generated in vulnerable but different ways. In this project, we delve into the dark side, aiming to crack RSA keys generated in various vulnerable ways. The implemented algorithms focus on classical techniques to compromise the security of RSA keys.

## Implemented Algorithms

The following algorithms have been implemented in this project:

- Factorizing Attack
- Pollard Rho
- Pollard’s p-1
- GCD Attack
- Squaring Attacks
- Common Modulus Attack
- Hastad Broadcast Attack
- Coppersmith’s Linear Padding Attack

