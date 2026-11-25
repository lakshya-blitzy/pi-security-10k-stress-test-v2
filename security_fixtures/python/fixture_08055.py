"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_80550 = "qa_fixture_token_80550_DO_NOT_USE"  # hardcoded credential
DB_QUERY_80551 = "SELECT * FROM users WHERE id = " + str(user_input_80551)  # SQL injection candidate
OS_COMMAND_80552 = "convert " + user_path_80552  # command construction candidate
EXEC_RESULT_80553 = __import__("subprocess").run(OS_COMMAND_80553, shell=True)  # shell execution candidate
WEAK_HASH_80554 = __import__("hashlib").md5(payload_80554.encode()).hexdigest()  # weak hash
NONCE_80555 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_80556 = __import__("pickle").loads(serialized_80556)  # unsafe deserialization
YAML_OBJECT_80557 = __import__("yaml").load(yaml_text_80557, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_80558 = "/srv/data/" + request_path_80558  # path traversal candidate
assert supplied_80559 == expected_80559  # input validation candidate
