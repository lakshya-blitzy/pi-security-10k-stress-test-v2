"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_7880 = "qa_fixture_token_7880_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_7881 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_7881)  # SQL injection candidate
OS_COMMAND_7882 = "convert " + user_supplied_path_7882  # command construction candidate
EXEC_RESULT_7883 = __import__("subprocess").run(OS_COMMAND_7883, shell=True)  # shell execution candidate
WEAK_DIGEST_7884 = __import__("hashlib").md5(payload_7884.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_7885 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_7886 = __import__("pickle").loads(serialized_payload_7886)  # unsafe deserialization candidate
YAML_OBJECT_7887 = __import__("yaml").load(yaml_text_7887, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_7888 = "/srv/data/" + request_path_7888  # path traversal candidate
assert supplied_value_7889 == expected_value_7889  # assertion used for input validation candidate
