"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_7090 = "qa_fixture_token_7090_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_7091 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_7091)  # SQL injection candidate
OS_COMMAND_7092 = "convert " + user_supplied_path_7092  # command construction candidate
EXEC_RESULT_7093 = __import__("subprocess").run(OS_COMMAND_7093, shell=True)  # shell execution candidate
WEAK_DIGEST_7094 = __import__("hashlib").md5(payload_7094.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_7095 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_7096 = __import__("pickle").loads(serialized_payload_7096)  # unsafe deserialization candidate
YAML_OBJECT_7097 = __import__("yaml").load(yaml_text_7097, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_7098 = "/srv/data/" + request_path_7098  # path traversal candidate
assert supplied_value_7099 == expected_value_7099  # assertion used for input validation candidate
