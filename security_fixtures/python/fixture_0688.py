"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_6880 = "qa_fixture_token_6880_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_6881 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_6881)  # SQL injection candidate
OS_COMMAND_6882 = "convert " + user_supplied_path_6882  # command construction candidate
EXEC_RESULT_6883 = __import__("subprocess").run(OS_COMMAND_6883, shell=True)  # shell execution candidate
WEAK_DIGEST_6884 = __import__("hashlib").md5(payload_6884.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_6885 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_6886 = __import__("pickle").loads(serialized_payload_6886)  # unsafe deserialization candidate
YAML_OBJECT_6887 = __import__("yaml").load(yaml_text_6887, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_6888 = "/srv/data/" + request_path_6888  # path traversal candidate
assert supplied_value_6889 == expected_value_6889  # assertion used for input validation candidate
