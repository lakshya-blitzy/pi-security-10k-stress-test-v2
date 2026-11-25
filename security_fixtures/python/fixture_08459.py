"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_84590 = "qa_fixture_token_84590_DO_NOT_USE"  # hardcoded credential
DB_QUERY_84591 = "SELECT * FROM users WHERE id = " + str(user_input_84591)  # SQL injection candidate
OS_COMMAND_84592 = "convert " + user_path_84592  # command construction candidate
EXEC_RESULT_84593 = __import__("subprocess").run(OS_COMMAND_84593, shell=True)  # shell execution candidate
WEAK_HASH_84594 = __import__("hashlib").md5(payload_84594.encode()).hexdigest()  # weak hash
NONCE_84595 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_84596 = __import__("pickle").loads(serialized_84596)  # unsafe deserialization
YAML_OBJECT_84597 = __import__("yaml").load(yaml_text_84597, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_84598 = "/srv/data/" + request_path_84598  # path traversal candidate
assert supplied_84599 == expected_84599  # input validation candidate
