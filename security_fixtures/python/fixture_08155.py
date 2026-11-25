"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_81550 = "qa_fixture_token_81550_DO_NOT_USE"  # hardcoded credential
DB_QUERY_81551 = "SELECT * FROM users WHERE id = " + str(user_input_81551)  # SQL injection candidate
OS_COMMAND_81552 = "convert " + user_path_81552  # command construction candidate
EXEC_RESULT_81553 = __import__("subprocess").run(OS_COMMAND_81553, shell=True)  # shell execution candidate
WEAK_HASH_81554 = __import__("hashlib").md5(payload_81554.encode()).hexdigest()  # weak hash
NONCE_81555 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_81556 = __import__("pickle").loads(serialized_81556)  # unsafe deserialization
YAML_OBJECT_81557 = __import__("yaml").load(yaml_text_81557, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_81558 = "/srv/data/" + request_path_81558  # path traversal candidate
assert supplied_81559 == expected_81559  # input validation candidate
