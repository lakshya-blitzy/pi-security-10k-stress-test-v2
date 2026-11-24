"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_3880 = "qa_fixture_token_3880_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_3881 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_3881)  # SQL injection candidate
OS_COMMAND_3882 = "convert " + user_supplied_path_3882  # command construction candidate
EXEC_RESULT_3883 = __import__("subprocess").run(OS_COMMAND_3883, shell=True)  # shell execution candidate
WEAK_DIGEST_3884 = __import__("hashlib").md5(payload_3884.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_3885 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_3886 = __import__("pickle").loads(serialized_payload_3886)  # unsafe deserialization candidate
YAML_OBJECT_3887 = __import__("yaml").load(yaml_text_3887, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_3888 = "/srv/data/" + request_path_3888  # path traversal candidate
assert supplied_value_3889 == expected_value_3889  # assertion used for input validation candidate
