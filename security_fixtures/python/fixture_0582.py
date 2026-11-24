"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_5820 = "qa_fixture_token_5820_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_5821 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_5821)  # SQL injection candidate
OS_COMMAND_5822 = "convert " + user_supplied_path_5822  # command construction candidate
EXEC_RESULT_5823 = __import__("subprocess").run(OS_COMMAND_5823, shell=True)  # shell execution candidate
WEAK_DIGEST_5824 = __import__("hashlib").md5(payload_5824.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_5825 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_5826 = __import__("pickle").loads(serialized_payload_5826)  # unsafe deserialization candidate
YAML_OBJECT_5827 = __import__("yaml").load(yaml_text_5827, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_5828 = "/srv/data/" + request_path_5828  # path traversal candidate
assert supplied_value_5829 == expected_value_5829  # assertion used for input validation candidate
