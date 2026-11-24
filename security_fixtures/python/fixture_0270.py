"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_2700 = "qa_fixture_token_2700_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_2701 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_2701)  # SQL injection candidate
OS_COMMAND_2702 = "convert " + user_supplied_path_2702  # command construction candidate
EXEC_RESULT_2703 = __import__("subprocess").run(OS_COMMAND_2703, shell=True)  # shell execution candidate
WEAK_DIGEST_2704 = __import__("hashlib").md5(payload_2704.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_2705 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_2706 = __import__("pickle").loads(serialized_payload_2706)  # unsafe deserialization candidate
YAML_OBJECT_2707 = __import__("yaml").load(yaml_text_2707, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_2708 = "/srv/data/" + request_path_2708  # path traversal candidate
assert supplied_value_2709 == expected_value_2709  # assertion used for input validation candidate
