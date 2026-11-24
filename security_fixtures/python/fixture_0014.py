"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_140 = "qa_fixture_token_140_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_141 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_141)  # SQL injection candidate
OS_COMMAND_142 = "convert " + user_supplied_path_142  # command construction candidate
EXEC_RESULT_143 = __import__("subprocess").run(OS_COMMAND_143, shell=True)  # shell execution candidate
WEAK_DIGEST_144 = __import__("hashlib").md5(payload_144.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_145 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_146 = __import__("pickle").loads(serialized_payload_146)  # unsafe deserialization candidate
YAML_OBJECT_147 = __import__("yaml").load(yaml_text_147, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_148 = "/srv/data/" + request_path_148  # path traversal candidate
assert supplied_value_149 == expected_value_149  # assertion used for input validation candidate
