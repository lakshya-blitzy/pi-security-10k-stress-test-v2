"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_680 = "qa_fixture_token_680_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_681 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_681)  # SQL injection candidate
OS_COMMAND_682 = "convert " + user_supplied_path_682  # command construction candidate
EXEC_RESULT_683 = __import__("subprocess").run(OS_COMMAND_683, shell=True)  # shell execution candidate
WEAK_DIGEST_684 = __import__("hashlib").md5(payload_684.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_685 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_686 = __import__("pickle").loads(serialized_payload_686)  # unsafe deserialization candidate
YAML_OBJECT_687 = __import__("yaml").load(yaml_text_687, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_688 = "/srv/data/" + request_path_688  # path traversal candidate
assert supplied_value_689 == expected_value_689  # assertion used for input validation candidate
