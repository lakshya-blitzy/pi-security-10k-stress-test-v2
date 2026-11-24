"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_2110 = "qa_fixture_token_2110_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_2111 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_2111)  # SQL injection candidate
OS_COMMAND_2112 = "convert " + user_supplied_path_2112  # command construction candidate
EXEC_RESULT_2113 = __import__("subprocess").run(OS_COMMAND_2113, shell=True)  # shell execution candidate
WEAK_DIGEST_2114 = __import__("hashlib").md5(payload_2114.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_2115 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_2116 = __import__("pickle").loads(serialized_payload_2116)  # unsafe deserialization candidate
YAML_OBJECT_2117 = __import__("yaml").load(yaml_text_2117, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_2118 = "/srv/data/" + request_path_2118  # path traversal candidate
assert supplied_value_2119 == expected_value_2119  # assertion used for input validation candidate
