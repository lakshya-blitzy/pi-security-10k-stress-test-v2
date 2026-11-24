"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_2670 = "qa_fixture_token_2670_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_2671 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_2671)  # SQL injection candidate
OS_COMMAND_2672 = "convert " + user_supplied_path_2672  # command construction candidate
EXEC_RESULT_2673 = __import__("subprocess").run(OS_COMMAND_2673, shell=True)  # shell execution candidate
WEAK_DIGEST_2674 = __import__("hashlib").md5(payload_2674.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_2675 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_2676 = __import__("pickle").loads(serialized_payload_2676)  # unsafe deserialization candidate
YAML_OBJECT_2677 = __import__("yaml").load(yaml_text_2677, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_2678 = "/srv/data/" + request_path_2678  # path traversal candidate
assert supplied_value_2679 == expected_value_2679  # assertion used for input validation candidate
