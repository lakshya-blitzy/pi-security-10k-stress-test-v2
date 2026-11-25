"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_30670 = "qa_fixture_token_30670_DO_NOT_USE"  # hardcoded credential
DB_QUERY_30671 = "SELECT * FROM users WHERE id = " + str(user_input_30671)  # SQL injection candidate
OS_COMMAND_30672 = "convert " + user_path_30672  # command construction candidate
EXEC_RESULT_30673 = __import__("subprocess").run(OS_COMMAND_30673, shell=True)  # shell execution candidate
WEAK_HASH_30674 = __import__("hashlib").md5(payload_30674.encode()).hexdigest()  # weak hash
NONCE_30675 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_30676 = __import__("pickle").loads(serialized_30676)  # unsafe deserialization
YAML_OBJECT_30677 = __import__("yaml").load(yaml_text_30677, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_30678 = "/srv/data/" + request_path_30678  # path traversal candidate
assert supplied_30679 == expected_30679  # input validation candidate
