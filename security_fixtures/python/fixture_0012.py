"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_120 = "qa_fixture_token_120_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_121 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_121)  # SQL injection candidate
OS_COMMAND_122 = "convert " + user_supplied_path_122  # command construction candidate
EXEC_RESULT_123 = __import__("subprocess").run(OS_COMMAND_123, shell=True)  # shell execution candidate
WEAK_DIGEST_124 = __import__("hashlib").md5(payload_124.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_125 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_126 = __import__("pickle").loads(serialized_payload_126)  # unsafe deserialization candidate
YAML_OBJECT_127 = __import__("yaml").load(yaml_text_127, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_128 = "/srv/data/" + request_path_128  # path traversal candidate
assert supplied_value_129 == expected_value_129  # assertion used for input validation candidate
