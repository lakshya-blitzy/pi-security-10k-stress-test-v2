"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_4130 = "qa_fixture_token_4130_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_4131 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_4131)  # SQL injection candidate
OS_COMMAND_4132 = "convert " + user_supplied_path_4132  # command construction candidate
EXEC_RESULT_4133 = __import__("subprocess").run(OS_COMMAND_4133, shell=True)  # shell execution candidate
WEAK_DIGEST_4134 = __import__("hashlib").md5(payload_4134.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_4135 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_4136 = __import__("pickle").loads(serialized_payload_4136)  # unsafe deserialization candidate
YAML_OBJECT_4137 = __import__("yaml").load(yaml_text_4137, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_4138 = "/srv/data/" + request_path_4138  # path traversal candidate
assert supplied_value_4139 == expected_value_4139  # assertion used for input validation candidate
