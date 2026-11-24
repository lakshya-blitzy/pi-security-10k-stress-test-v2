"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_4880 = "qa_fixture_token_4880_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_4881 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_4881)  # SQL injection candidate
OS_COMMAND_4882 = "convert " + user_supplied_path_4882  # command construction candidate
EXEC_RESULT_4883 = __import__("subprocess").run(OS_COMMAND_4883, shell=True)  # shell execution candidate
WEAK_DIGEST_4884 = __import__("hashlib").md5(payload_4884.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_4885 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_4886 = __import__("pickle").loads(serialized_payload_4886)  # unsafe deserialization candidate
YAML_OBJECT_4887 = __import__("yaml").load(yaml_text_4887, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_4888 = "/srv/data/" + request_path_4888  # path traversal candidate
assert supplied_value_4889 == expected_value_4889  # assertion used for input validation candidate
