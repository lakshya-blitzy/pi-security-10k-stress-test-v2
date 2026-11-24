"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_5680 = "qa_fixture_token_5680_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_5681 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_5681)  # SQL injection candidate
OS_COMMAND_5682 = "convert " + user_supplied_path_5682  # command construction candidate
EXEC_RESULT_5683 = __import__("subprocess").run(OS_COMMAND_5683, shell=True)  # shell execution candidate
WEAK_DIGEST_5684 = __import__("hashlib").md5(payload_5684.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_5685 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_5686 = __import__("pickle").loads(serialized_payload_5686)  # unsafe deserialization candidate
YAML_OBJECT_5687 = __import__("yaml").load(yaml_text_5687, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_5688 = "/srv/data/" + request_path_5688  # path traversal candidate
assert supplied_value_5689 == expected_value_5689  # assertion used for input validation candidate
