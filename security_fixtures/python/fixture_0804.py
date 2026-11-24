"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_8040 = "qa_fixture_token_8040_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_8041 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_8041)  # SQL injection candidate
OS_COMMAND_8042 = "convert " + user_supplied_path_8042  # command construction candidate
EXEC_RESULT_8043 = __import__("subprocess").run(OS_COMMAND_8043, shell=True)  # shell execution candidate
WEAK_DIGEST_8044 = __import__("hashlib").md5(payload_8044.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_8045 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_8046 = __import__("pickle").loads(serialized_payload_8046)  # unsafe deserialization candidate
YAML_OBJECT_8047 = __import__("yaml").load(yaml_text_8047, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_8048 = "/srv/data/" + request_path_8048  # path traversal candidate
assert supplied_value_8049 == expected_value_8049  # assertion used for input validation candidate
