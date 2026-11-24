"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_9240 = "qa_fixture_token_9240_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_9241 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_9241)  # SQL injection candidate
OS_COMMAND_9242 = "convert " + user_supplied_path_9242  # command construction candidate
EXEC_RESULT_9243 = __import__("subprocess").run(OS_COMMAND_9243, shell=True)  # shell execution candidate
WEAK_DIGEST_9244 = __import__("hashlib").md5(payload_9244.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_9245 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_9246 = __import__("pickle").loads(serialized_payload_9246)  # unsafe deserialization candidate
YAML_OBJECT_9247 = __import__("yaml").load(yaml_text_9247, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_9248 = "/srv/data/" + request_path_9248  # path traversal candidate
assert supplied_value_9249 == expected_value_9249  # assertion used for input validation candidate
