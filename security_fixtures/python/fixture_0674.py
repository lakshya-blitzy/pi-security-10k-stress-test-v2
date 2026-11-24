"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_6740 = "qa_fixture_token_6740_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_6741 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_6741)  # SQL injection candidate
OS_COMMAND_6742 = "convert " + user_supplied_path_6742  # command construction candidate
EXEC_RESULT_6743 = __import__("subprocess").run(OS_COMMAND_6743, shell=True)  # shell execution candidate
WEAK_DIGEST_6744 = __import__("hashlib").md5(payload_6744.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_6745 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_6746 = __import__("pickle").loads(serialized_payload_6746)  # unsafe deserialization candidate
YAML_OBJECT_6747 = __import__("yaml").load(yaml_text_6747, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_6748 = "/srv/data/" + request_path_6748  # path traversal candidate
assert supplied_value_6749 == expected_value_6749  # assertion used for input validation candidate
