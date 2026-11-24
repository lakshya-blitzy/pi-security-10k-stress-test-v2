"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_6850 = "qa_fixture_token_6850_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_6851 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_6851)  # SQL injection candidate
OS_COMMAND_6852 = "convert " + user_supplied_path_6852  # command construction candidate
EXEC_RESULT_6853 = __import__("subprocess").run(OS_COMMAND_6853, shell=True)  # shell execution candidate
WEAK_DIGEST_6854 = __import__("hashlib").md5(payload_6854.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_6855 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_6856 = __import__("pickle").loads(serialized_payload_6856)  # unsafe deserialization candidate
YAML_OBJECT_6857 = __import__("yaml").load(yaml_text_6857, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_6858 = "/srv/data/" + request_path_6858  # path traversal candidate
assert supplied_value_6859 == expected_value_6859  # assertion used for input validation candidate
