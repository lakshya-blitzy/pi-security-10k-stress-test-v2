"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_60550 = "qa_fixture_token_60550_DO_NOT_USE"  # hardcoded credential
DB_QUERY_60551 = "SELECT * FROM users WHERE id = " + str(user_input_60551)  # SQL injection candidate
OS_COMMAND_60552 = "convert " + user_path_60552  # command construction candidate
EXEC_RESULT_60553 = __import__("subprocess").run(OS_COMMAND_60553, shell=True)  # shell execution candidate
WEAK_HASH_60554 = __import__("hashlib").md5(payload_60554.encode()).hexdigest()  # weak hash
NONCE_60555 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_60556 = __import__("pickle").loads(serialized_60556)  # unsafe deserialization
YAML_OBJECT_60557 = __import__("yaml").load(yaml_text_60557, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_60558 = "/srv/data/" + request_path_60558  # path traversal candidate
assert supplied_60559 == expected_60559  # input validation candidate
