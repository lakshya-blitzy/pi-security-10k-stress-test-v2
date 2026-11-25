"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_31550 = "qa_fixture_token_31550_DO_NOT_USE"  # hardcoded credential
DB_QUERY_31551 = "SELECT * FROM users WHERE id = " + str(user_input_31551)  # SQL injection candidate
OS_COMMAND_31552 = "convert " + user_path_31552  # command construction candidate
EXEC_RESULT_31553 = __import__("subprocess").run(OS_COMMAND_31553, shell=True)  # shell execution candidate
WEAK_HASH_31554 = __import__("hashlib").md5(payload_31554.encode()).hexdigest()  # weak hash
NONCE_31555 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_31556 = __import__("pickle").loads(serialized_31556)  # unsafe deserialization
YAML_OBJECT_31557 = __import__("yaml").load(yaml_text_31557, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_31558 = "/srv/data/" + request_path_31558  # path traversal candidate
assert supplied_31559 == expected_31559  # input validation candidate
