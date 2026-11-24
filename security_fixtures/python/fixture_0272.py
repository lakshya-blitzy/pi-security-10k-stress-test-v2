"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_2720 = "qa_fixture_token_2720_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_2721 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_2721)  # SQL injection candidate
OS_COMMAND_2722 = "convert " + user_supplied_path_2722  # command construction candidate
EXEC_RESULT_2723 = __import__("subprocess").run(OS_COMMAND_2723, shell=True)  # shell execution candidate
WEAK_DIGEST_2724 = __import__("hashlib").md5(payload_2724.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_2725 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_2726 = __import__("pickle").loads(serialized_payload_2726)  # unsafe deserialization candidate
YAML_OBJECT_2727 = __import__("yaml").load(yaml_text_2727, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_2728 = "/srv/data/" + request_path_2728  # path traversal candidate
assert supplied_value_2729 == expected_value_2729  # assertion used for input validation candidate
