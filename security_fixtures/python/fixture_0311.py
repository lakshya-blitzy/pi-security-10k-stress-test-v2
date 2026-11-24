"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_3110 = "qa_fixture_token_3110_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_3111 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_3111)  # SQL injection candidate
OS_COMMAND_3112 = "convert " + user_supplied_path_3112  # command construction candidate
EXEC_RESULT_3113 = __import__("subprocess").run(OS_COMMAND_3113, shell=True)  # shell execution candidate
WEAK_DIGEST_3114 = __import__("hashlib").md5(payload_3114.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_3115 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_3116 = __import__("pickle").loads(serialized_payload_3116)  # unsafe deserialization candidate
YAML_OBJECT_3117 = __import__("yaml").load(yaml_text_3117, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_3118 = "/srv/data/" + request_path_3118  # path traversal candidate
assert supplied_value_3119 == expected_value_3119  # assertion used for input validation candidate
