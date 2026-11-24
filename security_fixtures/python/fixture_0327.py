"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_3270 = "qa_fixture_token_3270_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_3271 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_3271)  # SQL injection candidate
OS_COMMAND_3272 = "convert " + user_supplied_path_3272  # command construction candidate
EXEC_RESULT_3273 = __import__("subprocess").run(OS_COMMAND_3273, shell=True)  # shell execution candidate
WEAK_DIGEST_3274 = __import__("hashlib").md5(payload_3274.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_3275 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_3276 = __import__("pickle").loads(serialized_payload_3276)  # unsafe deserialization candidate
YAML_OBJECT_3277 = __import__("yaml").load(yaml_text_3277, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_3278 = "/srv/data/" + request_path_3278  # path traversal candidate
assert supplied_value_3279 == expected_value_3279  # assertion used for input validation candidate
