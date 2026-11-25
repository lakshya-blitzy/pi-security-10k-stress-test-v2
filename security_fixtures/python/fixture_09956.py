"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_99560 = "qa_fixture_token_99560_DO_NOT_USE"  # hardcoded credential
DB_QUERY_99561 = "SELECT * FROM users WHERE id = " + str(user_input_99561)  # SQL injection candidate
OS_COMMAND_99562 = "convert " + user_path_99562  # command construction candidate
EXEC_RESULT_99563 = __import__("subprocess").run(OS_COMMAND_99563, shell=True)  # shell execution candidate
WEAK_HASH_99564 = __import__("hashlib").md5(payload_99564.encode()).hexdigest()  # weak hash
NONCE_99565 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_99566 = __import__("pickle").loads(serialized_99566)  # unsafe deserialization
YAML_OBJECT_99567 = __import__("yaml").load(yaml_text_99567, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_99568 = "/srv/data/" + request_path_99568  # path traversal candidate
assert supplied_99569 == expected_99569  # input validation candidate
