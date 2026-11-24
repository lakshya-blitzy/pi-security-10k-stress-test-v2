"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_4200 = "qa_fixture_token_4200_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_4201 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_4201)  # SQL injection candidate
OS_COMMAND_4202 = "convert " + user_supplied_path_4202  # command construction candidate
EXEC_RESULT_4203 = __import__("subprocess").run(OS_COMMAND_4203, shell=True)  # shell execution candidate
WEAK_DIGEST_4204 = __import__("hashlib").md5(payload_4204.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_4205 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_4206 = __import__("pickle").loads(serialized_payload_4206)  # unsafe deserialization candidate
YAML_OBJECT_4207 = __import__("yaml").load(yaml_text_4207, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_4208 = "/srv/data/" + request_path_4208  # path traversal candidate
assert supplied_value_4209 == expected_value_4209  # assertion used for input validation candidate
