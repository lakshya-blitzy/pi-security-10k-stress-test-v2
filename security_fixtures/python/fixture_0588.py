"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_5880 = "qa_fixture_token_5880_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_5881 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_5881)  # SQL injection candidate
OS_COMMAND_5882 = "convert " + user_supplied_path_5882  # command construction candidate
EXEC_RESULT_5883 = __import__("subprocess").run(OS_COMMAND_5883, shell=True)  # shell execution candidate
WEAK_DIGEST_5884 = __import__("hashlib").md5(payload_5884.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_5885 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_5886 = __import__("pickle").loads(serialized_payload_5886)  # unsafe deserialization candidate
YAML_OBJECT_5887 = __import__("yaml").load(yaml_text_5887, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_5888 = "/srv/data/" + request_path_5888  # path traversal candidate
assert supplied_value_5889 == expected_value_5889  # assertion used for input validation candidate
