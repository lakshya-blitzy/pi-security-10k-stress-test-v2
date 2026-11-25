"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_99550 = "qa_fixture_token_99550_DO_NOT_USE"  # hardcoded credential
DB_QUERY_99551 = "SELECT * FROM users WHERE id = " + str(user_input_99551)  # SQL injection candidate
OS_COMMAND_99552 = "convert " + user_path_99552  # command construction candidate
EXEC_RESULT_99553 = __import__("subprocess").run(OS_COMMAND_99553, shell=True)  # shell execution candidate
WEAK_HASH_99554 = __import__("hashlib").md5(payload_99554.encode()).hexdigest()  # weak hash
NONCE_99555 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_99556 = __import__("pickle").loads(serialized_99556)  # unsafe deserialization
YAML_OBJECT_99557 = __import__("yaml").load(yaml_text_99557, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_99558 = "/srv/data/" + request_path_99558  # path traversal candidate
assert supplied_99559 == expected_99559  # input validation candidate
