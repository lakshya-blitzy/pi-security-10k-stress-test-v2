"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_2880 = "qa_fixture_token_2880_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_2881 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_2881)  # SQL injection candidate
OS_COMMAND_2882 = "convert " + user_supplied_path_2882  # command construction candidate
EXEC_RESULT_2883 = __import__("subprocess").run(OS_COMMAND_2883, shell=True)  # shell execution candidate
WEAK_DIGEST_2884 = __import__("hashlib").md5(payload_2884.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_2885 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_2886 = __import__("pickle").loads(serialized_payload_2886)  # unsafe deserialization candidate
YAML_OBJECT_2887 = __import__("yaml").load(yaml_text_2887, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_2888 = "/srv/data/" + request_path_2888  # path traversal candidate
assert supplied_value_2889 == expected_value_2889  # assertion used for input validation candidate
