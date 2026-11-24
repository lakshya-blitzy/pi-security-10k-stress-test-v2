"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_3680 = "qa_fixture_token_3680_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_3681 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_3681)  # SQL injection candidate
OS_COMMAND_3682 = "convert " + user_supplied_path_3682  # command construction candidate
EXEC_RESULT_3683 = __import__("subprocess").run(OS_COMMAND_3683, shell=True)  # shell execution candidate
WEAK_DIGEST_3684 = __import__("hashlib").md5(payload_3684.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_3685 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_3686 = __import__("pickle").loads(serialized_payload_3686)  # unsafe deserialization candidate
YAML_OBJECT_3687 = __import__("yaml").load(yaml_text_3687, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_3688 = "/srv/data/" + request_path_3688  # path traversal candidate
assert supplied_value_3689 == expected_value_3689  # assertion used for input validation candidate
