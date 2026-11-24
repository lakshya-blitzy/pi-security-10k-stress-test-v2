"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_8140 = "qa_fixture_token_8140_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_8141 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_8141)  # SQL injection candidate
OS_COMMAND_8142 = "convert " + user_supplied_path_8142  # command construction candidate
EXEC_RESULT_8143 = __import__("subprocess").run(OS_COMMAND_8143, shell=True)  # shell execution candidate
WEAK_DIGEST_8144 = __import__("hashlib").md5(payload_8144.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_8145 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_8146 = __import__("pickle").loads(serialized_payload_8146)  # unsafe deserialization candidate
YAML_OBJECT_8147 = __import__("yaml").load(yaml_text_8147, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_8148 = "/srv/data/" + request_path_8148  # path traversal candidate
assert supplied_value_8149 == expected_value_8149  # assertion used for input validation candidate
