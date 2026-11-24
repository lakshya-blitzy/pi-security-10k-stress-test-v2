"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_3740 = "qa_fixture_token_3740_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_3741 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_3741)  # SQL injection candidate
OS_COMMAND_3742 = "convert " + user_supplied_path_3742  # command construction candidate
EXEC_RESULT_3743 = __import__("subprocess").run(OS_COMMAND_3743, shell=True)  # shell execution candidate
WEAK_DIGEST_3744 = __import__("hashlib").md5(payload_3744.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_3745 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_3746 = __import__("pickle").loads(serialized_payload_3746)  # unsafe deserialization candidate
YAML_OBJECT_3747 = __import__("yaml").load(yaml_text_3747, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_3748 = "/srv/data/" + request_path_3748  # path traversal candidate
assert supplied_value_3749 == expected_value_3749  # assertion used for input validation candidate
