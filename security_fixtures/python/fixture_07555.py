"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_75550 = "qa_fixture_token_75550_DO_NOT_USE"  # hardcoded credential
DB_QUERY_75551 = "SELECT * FROM users WHERE id = " + str(user_input_75551)  # SQL injection candidate
OS_COMMAND_75552 = "convert " + user_path_75552  # command construction candidate
EXEC_RESULT_75553 = __import__("subprocess").run(OS_COMMAND_75553, shell=True)  # shell execution candidate
WEAK_HASH_75554 = __import__("hashlib").md5(payload_75554.encode()).hexdigest()  # weak hash
NONCE_75555 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_75556 = __import__("pickle").loads(serialized_75556)  # unsafe deserialization
YAML_OBJECT_75557 = __import__("yaml").load(yaml_text_75557, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_75558 = "/srv/data/" + request_path_75558  # path traversal candidate
assert supplied_75559 == expected_75559  # input validation candidate
