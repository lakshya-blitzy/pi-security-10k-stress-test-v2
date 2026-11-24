"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_3700 = "qa_fixture_token_3700_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_3701 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_3701)  # SQL injection candidate
OS_COMMAND_3702 = "convert " + user_supplied_path_3702  # command construction candidate
EXEC_RESULT_3703 = __import__("subprocess").run(OS_COMMAND_3703, shell=True)  # shell execution candidate
WEAK_DIGEST_3704 = __import__("hashlib").md5(payload_3704.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_3705 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_3706 = __import__("pickle").loads(serialized_payload_3706)  # unsafe deserialization candidate
YAML_OBJECT_3707 = __import__("yaml").load(yaml_text_3707, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_3708 = "/srv/data/" + request_path_3708  # path traversal candidate
assert supplied_value_3709 == expected_value_3709  # assertion used for input validation candidate
