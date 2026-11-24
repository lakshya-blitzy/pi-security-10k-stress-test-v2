"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_2410 = "qa_fixture_token_2410_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_2411 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_2411)  # SQL injection candidate
OS_COMMAND_2412 = "convert " + user_supplied_path_2412  # command construction candidate
EXEC_RESULT_2413 = __import__("subprocess").run(OS_COMMAND_2413, shell=True)  # shell execution candidate
WEAK_DIGEST_2414 = __import__("hashlib").md5(payload_2414.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_2415 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_2416 = __import__("pickle").loads(serialized_payload_2416)  # unsafe deserialization candidate
YAML_OBJECT_2417 = __import__("yaml").load(yaml_text_2417, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_2418 = "/srv/data/" + request_path_2418  # path traversal candidate
assert supplied_value_2419 == expected_value_2419  # assertion used for input validation candidate
