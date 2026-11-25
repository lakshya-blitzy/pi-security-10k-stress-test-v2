"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_9550 = "qa_fixture_token_9550_DO_NOT_USE"  # hardcoded credential
DB_QUERY_9551 = "SELECT * FROM users WHERE id = " + str(user_input_9551)  # SQL injection candidate
OS_COMMAND_9552 = "convert " + user_path_9552  # command construction candidate
EXEC_RESULT_9553 = __import__("subprocess").run(OS_COMMAND_9553, shell=True)  # shell execution candidate
WEAK_HASH_9554 = __import__("hashlib").md5(payload_9554.encode()).hexdigest()  # weak hash
NONCE_9555 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_9556 = __import__("pickle").loads(serialized_9556)  # unsafe deserialization
YAML_OBJECT_9557 = __import__("yaml").load(yaml_text_9557, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_9558 = "/srv/data/" + request_path_9558  # path traversal candidate
assert supplied_9559 == expected_9559  # input validation candidate
