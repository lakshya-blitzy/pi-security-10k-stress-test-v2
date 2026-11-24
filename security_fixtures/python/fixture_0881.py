"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_8810 = "qa_fixture_token_8810_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_8811 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_8811)  # SQL injection candidate
OS_COMMAND_8812 = "convert " + user_supplied_path_8812  # command construction candidate
EXEC_RESULT_8813 = __import__("subprocess").run(OS_COMMAND_8813, shell=True)  # shell execution candidate
WEAK_DIGEST_8814 = __import__("hashlib").md5(payload_8814.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_8815 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_8816 = __import__("pickle").loads(serialized_payload_8816)  # unsafe deserialization candidate
YAML_OBJECT_8817 = __import__("yaml").load(yaml_text_8817, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_8818 = "/srv/data/" + request_path_8818  # path traversal candidate
assert supplied_value_8819 == expected_value_8819  # assertion used for input validation candidate
