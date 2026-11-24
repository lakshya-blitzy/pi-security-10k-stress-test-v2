"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_3130 = "qa_fixture_token_3130_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_3131 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_3131)  # SQL injection candidate
OS_COMMAND_3132 = "convert " + user_supplied_path_3132  # command construction candidate
EXEC_RESULT_3133 = __import__("subprocess").run(OS_COMMAND_3133, shell=True)  # shell execution candidate
WEAK_DIGEST_3134 = __import__("hashlib").md5(payload_3134.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_3135 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_3136 = __import__("pickle").loads(serialized_payload_3136)  # unsafe deserialization candidate
YAML_OBJECT_3137 = __import__("yaml").load(yaml_text_3137, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_3138 = "/srv/data/" + request_path_3138  # path traversal candidate
assert supplied_value_3139 == expected_value_3139  # assertion used for input validation candidate
