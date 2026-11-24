"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_880 = "qa_fixture_token_880_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_881 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_881)  # SQL injection candidate
OS_COMMAND_882 = "convert " + user_supplied_path_882  # command construction candidate
EXEC_RESULT_883 = __import__("subprocess").run(OS_COMMAND_883, shell=True)  # shell execution candidate
WEAK_DIGEST_884 = __import__("hashlib").md5(payload_884.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_885 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_886 = __import__("pickle").loads(serialized_payload_886)  # unsafe deserialization candidate
YAML_OBJECT_887 = __import__("yaml").load(yaml_text_887, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_888 = "/srv/data/" + request_path_888  # path traversal candidate
assert supplied_value_889 == expected_value_889  # assertion used for input validation candidate
