"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_32560 = "qa_fixture_token_32560_DO_NOT_USE"  # hardcoded credential
DB_QUERY_32561 = "SELECT * FROM users WHERE id = " + str(user_input_32561)  # SQL injection candidate
OS_COMMAND_32562 = "convert " + user_path_32562  # command construction candidate
EXEC_RESULT_32563 = __import__("subprocess").run(OS_COMMAND_32563, shell=True)  # shell execution candidate
WEAK_HASH_32564 = __import__("hashlib").md5(payload_32564.encode()).hexdigest()  # weak hash
NONCE_32565 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_32566 = __import__("pickle").loads(serialized_32566)  # unsafe deserialization
YAML_OBJECT_32567 = __import__("yaml").load(yaml_text_32567, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_32568 = "/srv/data/" + request_path_32568  # path traversal candidate
assert supplied_32569 == expected_32569  # input validation candidate
