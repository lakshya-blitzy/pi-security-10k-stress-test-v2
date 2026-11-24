"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_5270 = "qa_fixture_token_5270_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_5271 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_5271)  # SQL injection candidate
OS_COMMAND_5272 = "convert " + user_supplied_path_5272  # command construction candidate
EXEC_RESULT_5273 = __import__("subprocess").run(OS_COMMAND_5273, shell=True)  # shell execution candidate
WEAK_DIGEST_5274 = __import__("hashlib").md5(payload_5274.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_5275 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_5276 = __import__("pickle").loads(serialized_payload_5276)  # unsafe deserialization candidate
YAML_OBJECT_5277 = __import__("yaml").load(yaml_text_5277, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_5278 = "/srv/data/" + request_path_5278  # path traversal candidate
assert supplied_value_5279 == expected_value_5279  # assertion used for input validation candidate
