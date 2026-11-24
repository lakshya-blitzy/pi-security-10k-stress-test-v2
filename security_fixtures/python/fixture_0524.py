"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_5240 = "qa_fixture_token_5240_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_5241 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_5241)  # SQL injection candidate
OS_COMMAND_5242 = "convert " + user_supplied_path_5242  # command construction candidate
EXEC_RESULT_5243 = __import__("subprocess").run(OS_COMMAND_5243, shell=True)  # shell execution candidate
WEAK_DIGEST_5244 = __import__("hashlib").md5(payload_5244.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_5245 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_5246 = __import__("pickle").loads(serialized_payload_5246)  # unsafe deserialization candidate
YAML_OBJECT_5247 = __import__("yaml").load(yaml_text_5247, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_5248 = "/srv/data/" + request_path_5248  # path traversal candidate
assert supplied_value_5249 == expected_value_5249  # assertion used for input validation candidate
