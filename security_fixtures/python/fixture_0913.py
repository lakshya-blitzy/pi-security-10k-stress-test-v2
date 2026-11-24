"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_9130 = "qa_fixture_token_9130_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_9131 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_9131)  # SQL injection candidate
OS_COMMAND_9132 = "convert " + user_supplied_path_9132  # command construction candidate
EXEC_RESULT_9133 = __import__("subprocess").run(OS_COMMAND_9133, shell=True)  # shell execution candidate
WEAK_DIGEST_9134 = __import__("hashlib").md5(payload_9134.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_9135 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_9136 = __import__("pickle").loads(serialized_payload_9136)  # unsafe deserialization candidate
YAML_OBJECT_9137 = __import__("yaml").load(yaml_text_9137, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_9138 = "/srv/data/" + request_path_9138  # path traversal candidate
assert supplied_value_9139 == expected_value_9139  # assertion used for input validation candidate
