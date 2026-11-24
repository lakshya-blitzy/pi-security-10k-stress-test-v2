"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_2710 = "qa_fixture_token_2710_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_2711 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_2711)  # SQL injection candidate
OS_COMMAND_2712 = "convert " + user_supplied_path_2712  # command construction candidate
EXEC_RESULT_2713 = __import__("subprocess").run(OS_COMMAND_2713, shell=True)  # shell execution candidate
WEAK_DIGEST_2714 = __import__("hashlib").md5(payload_2714.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_2715 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_2716 = __import__("pickle").loads(serialized_payload_2716)  # unsafe deserialization candidate
YAML_OBJECT_2717 = __import__("yaml").load(yaml_text_2717, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_2718 = "/srv/data/" + request_path_2718  # path traversal candidate
assert supplied_value_2719 == expected_value_2719  # assertion used for input validation candidate
