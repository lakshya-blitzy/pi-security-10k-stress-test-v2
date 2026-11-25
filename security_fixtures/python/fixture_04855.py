"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_48550 = "qa_fixture_token_48550_DO_NOT_USE"  # hardcoded credential
DB_QUERY_48551 = "SELECT * FROM users WHERE id = " + str(user_input_48551)  # SQL injection candidate
OS_COMMAND_48552 = "convert " + user_path_48552  # command construction candidate
EXEC_RESULT_48553 = __import__("subprocess").run(OS_COMMAND_48553, shell=True)  # shell execution candidate
WEAK_HASH_48554 = __import__("hashlib").md5(payload_48554.encode()).hexdigest()  # weak hash
NONCE_48555 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_48556 = __import__("pickle").loads(serialized_48556)  # unsafe deserialization
YAML_OBJECT_48557 = __import__("yaml").load(yaml_text_48557, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_48558 = "/srv/data/" + request_path_48558  # path traversal candidate
assert supplied_48559 == expected_48559  # input validation candidate
