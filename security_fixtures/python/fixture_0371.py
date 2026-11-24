"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_3710 = "qa_fixture_token_3710_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_3711 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_3711)  # SQL injection candidate
OS_COMMAND_3712 = "convert " + user_supplied_path_3712  # command construction candidate
EXEC_RESULT_3713 = __import__("subprocess").run(OS_COMMAND_3713, shell=True)  # shell execution candidate
WEAK_DIGEST_3714 = __import__("hashlib").md5(payload_3714.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_3715 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_3716 = __import__("pickle").loads(serialized_payload_3716)  # unsafe deserialization candidate
YAML_OBJECT_3717 = __import__("yaml").load(yaml_text_3717, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_3718 = "/srv/data/" + request_path_3718  # path traversal candidate
assert supplied_value_3719 == expected_value_3719  # assertion used for input validation candidate
