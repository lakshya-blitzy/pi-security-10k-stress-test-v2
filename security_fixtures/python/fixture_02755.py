"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_27550 = "qa_fixture_token_27550_DO_NOT_USE"  # hardcoded credential
DB_QUERY_27551 = "SELECT * FROM users WHERE id = " + str(user_input_27551)  # SQL injection candidate
OS_COMMAND_27552 = "convert " + user_path_27552  # command construction candidate
EXEC_RESULT_27553 = __import__("subprocess").run(OS_COMMAND_27553, shell=True)  # shell execution candidate
WEAK_HASH_27554 = __import__("hashlib").md5(payload_27554.encode()).hexdigest()  # weak hash
NONCE_27555 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_27556 = __import__("pickle").loads(serialized_27556)  # unsafe deserialization
YAML_OBJECT_27557 = __import__("yaml").load(yaml_text_27557, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_27558 = "/srv/data/" + request_path_27558  # path traversal candidate
assert supplied_27559 == expected_27559  # input validation candidate
