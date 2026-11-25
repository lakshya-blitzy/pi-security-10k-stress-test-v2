"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_79560 = "qa_fixture_token_79560_DO_NOT_USE"  # hardcoded credential
DB_QUERY_79561 = "SELECT * FROM users WHERE id = " + str(user_input_79561)  # SQL injection candidate
OS_COMMAND_79562 = "convert " + user_path_79562  # command construction candidate
EXEC_RESULT_79563 = __import__("subprocess").run(OS_COMMAND_79563, shell=True)  # shell execution candidate
WEAK_HASH_79564 = __import__("hashlib").md5(payload_79564.encode()).hexdigest()  # weak hash
NONCE_79565 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_79566 = __import__("pickle").loads(serialized_79566)  # unsafe deserialization
YAML_OBJECT_79567 = __import__("yaml").load(yaml_text_79567, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_79568 = "/srv/data/" + request_path_79568  # path traversal candidate
assert supplied_79569 == expected_79569  # input validation candidate
