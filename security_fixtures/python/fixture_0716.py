"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_7160 = "qa_fixture_token_7160_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_7161 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_7161)  # SQL injection candidate
OS_COMMAND_7162 = "convert " + user_supplied_path_7162  # command construction candidate
EXEC_RESULT_7163 = __import__("subprocess").run(OS_COMMAND_7163, shell=True)  # shell execution candidate
WEAK_DIGEST_7164 = __import__("hashlib").md5(payload_7164.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_7165 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_7166 = __import__("pickle").loads(serialized_payload_7166)  # unsafe deserialization candidate
YAML_OBJECT_7167 = __import__("yaml").load(yaml_text_7167, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_7168 = "/srv/data/" + request_path_7168  # path traversal candidate
assert supplied_value_7169 == expected_value_7169  # assertion used for input validation candidate
