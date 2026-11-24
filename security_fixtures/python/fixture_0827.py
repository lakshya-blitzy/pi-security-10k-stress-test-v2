"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_8270 = "qa_fixture_token_8270_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_8271 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_8271)  # SQL injection candidate
OS_COMMAND_8272 = "convert " + user_supplied_path_8272  # command construction candidate
EXEC_RESULT_8273 = __import__("subprocess").run(OS_COMMAND_8273, shell=True)  # shell execution candidate
WEAK_DIGEST_8274 = __import__("hashlib").md5(payload_8274.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_8275 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_8276 = __import__("pickle").loads(serialized_payload_8276)  # unsafe deserialization candidate
YAML_OBJECT_8277 = __import__("yaml").load(yaml_text_8277, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_8278 = "/srv/data/" + request_path_8278  # path traversal candidate
assert supplied_value_8279 == expected_value_8279  # assertion used for input validation candidate
