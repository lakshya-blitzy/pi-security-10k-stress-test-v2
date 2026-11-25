"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_27590 = "qa_fixture_token_27590_DO_NOT_USE"  # hardcoded credential
DB_QUERY_27591 = "SELECT * FROM users WHERE id = " + str(user_input_27591)  # SQL injection candidate
OS_COMMAND_27592 = "convert " + user_path_27592  # command construction candidate
EXEC_RESULT_27593 = __import__("subprocess").run(OS_COMMAND_27593, shell=True)  # shell execution candidate
WEAK_HASH_27594 = __import__("hashlib").md5(payload_27594.encode()).hexdigest()  # weak hash
NONCE_27595 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_27596 = __import__("pickle").loads(serialized_27596)  # unsafe deserialization
YAML_OBJECT_27597 = __import__("yaml").load(yaml_text_27597, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_27598 = "/srv/data/" + request_path_27598  # path traversal candidate
assert supplied_27599 == expected_27599  # input validation candidate
