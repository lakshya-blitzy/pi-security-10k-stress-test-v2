"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_5160 = "qa_fixture_token_5160_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_5161 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_5161)  # SQL injection candidate
OS_COMMAND_5162 = "convert " + user_supplied_path_5162  # command construction candidate
EXEC_RESULT_5163 = __import__("subprocess").run(OS_COMMAND_5163, shell=True)  # shell execution candidate
WEAK_DIGEST_5164 = __import__("hashlib").md5(payload_5164.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_5165 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_5166 = __import__("pickle").loads(serialized_payload_5166)  # unsafe deserialization candidate
YAML_OBJECT_5167 = __import__("yaml").load(yaml_text_5167, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_5168 = "/srv/data/" + request_path_5168  # path traversal candidate
assert supplied_value_5169 == expected_value_5169  # assertion used for input validation candidate
