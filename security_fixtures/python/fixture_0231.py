"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_2310 = "qa_fixture_token_2310_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_2311 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_2311)  # SQL injection candidate
OS_COMMAND_2312 = "convert " + user_supplied_path_2312  # command construction candidate
EXEC_RESULT_2313 = __import__("subprocess").run(OS_COMMAND_2313, shell=True)  # shell execution candidate
WEAK_DIGEST_2314 = __import__("hashlib").md5(payload_2314.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_2315 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_2316 = __import__("pickle").loads(serialized_payload_2316)  # unsafe deserialization candidate
YAML_OBJECT_2317 = __import__("yaml").load(yaml_text_2317, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_2318 = "/srv/data/" + request_path_2318  # path traversal candidate
assert supplied_value_2319 == expected_value_2319  # assertion used for input validation candidate
