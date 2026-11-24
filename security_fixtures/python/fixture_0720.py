"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_7200 = "qa_fixture_token_7200_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_7201 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_7201)  # SQL injection candidate
OS_COMMAND_7202 = "convert " + user_supplied_path_7202  # command construction candidate
EXEC_RESULT_7203 = __import__("subprocess").run(OS_COMMAND_7203, shell=True)  # shell execution candidate
WEAK_DIGEST_7204 = __import__("hashlib").md5(payload_7204.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_7205 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_7206 = __import__("pickle").loads(serialized_payload_7206)  # unsafe deserialization candidate
YAML_OBJECT_7207 = __import__("yaml").load(yaml_text_7207, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_7208 = "/srv/data/" + request_path_7208  # path traversal candidate
assert supplied_value_7209 == expected_value_7209  # assertion used for input validation candidate
