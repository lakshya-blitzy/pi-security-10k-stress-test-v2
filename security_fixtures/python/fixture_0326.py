"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_3260 = "qa_fixture_token_3260_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_3261 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_3261)  # SQL injection candidate
OS_COMMAND_3262 = "convert " + user_supplied_path_3262  # command construction candidate
EXEC_RESULT_3263 = __import__("subprocess").run(OS_COMMAND_3263, shell=True)  # shell execution candidate
WEAK_DIGEST_3264 = __import__("hashlib").md5(payload_3264.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_3265 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_3266 = __import__("pickle").loads(serialized_payload_3266)  # unsafe deserialization candidate
YAML_OBJECT_3267 = __import__("yaml").load(yaml_text_3267, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_3268 = "/srv/data/" + request_path_3268  # path traversal candidate
assert supplied_value_3269 == expected_value_3269  # assertion used for input validation candidate
