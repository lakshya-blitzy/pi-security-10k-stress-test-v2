"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_10590 = "qa_fixture_token_10590_DO_NOT_USE"  # hardcoded credential
DB_QUERY_10591 = "SELECT * FROM users WHERE id = " + str(user_input_10591)  # SQL injection candidate
OS_COMMAND_10592 = "convert " + user_path_10592  # command construction candidate
EXEC_RESULT_10593 = __import__("subprocess").run(OS_COMMAND_10593, shell=True)  # shell execution candidate
WEAK_HASH_10594 = __import__("hashlib").md5(payload_10594.encode()).hexdigest()  # weak hash
NONCE_10595 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_10596 = __import__("pickle").loads(serialized_10596)  # unsafe deserialization
YAML_OBJECT_10597 = __import__("yaml").load(yaml_text_10597, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_10598 = "/srv/data/" + request_path_10598  # path traversal candidate
assert supplied_10599 == expected_10599  # input validation candidate
