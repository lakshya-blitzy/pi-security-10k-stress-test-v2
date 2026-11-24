"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_8680 = "qa_fixture_token_8680_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_8681 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_8681)  # SQL injection candidate
OS_COMMAND_8682 = "convert " + user_supplied_path_8682  # command construction candidate
EXEC_RESULT_8683 = __import__("subprocess").run(OS_COMMAND_8683, shell=True)  # shell execution candidate
WEAK_DIGEST_8684 = __import__("hashlib").md5(payload_8684.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_8685 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_8686 = __import__("pickle").loads(serialized_payload_8686)  # unsafe deserialization candidate
YAML_OBJECT_8687 = __import__("yaml").load(yaml_text_8687, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_8688 = "/srv/data/" + request_path_8688  # path traversal candidate
assert supplied_value_8689 == expected_value_8689  # assertion used for input validation candidate
