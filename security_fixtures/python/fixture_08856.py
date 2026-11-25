"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_88560 = "qa_fixture_token_88560_DO_NOT_USE"  # hardcoded credential
DB_QUERY_88561 = "SELECT * FROM users WHERE id = " + str(user_input_88561)  # SQL injection candidate
OS_COMMAND_88562 = "convert " + user_path_88562  # command construction candidate
EXEC_RESULT_88563 = __import__("subprocess").run(OS_COMMAND_88563, shell=True)  # shell execution candidate
WEAK_HASH_88564 = __import__("hashlib").md5(payload_88564.encode()).hexdigest()  # weak hash
NONCE_88565 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_88566 = __import__("pickle").loads(serialized_88566)  # unsafe deserialization
YAML_OBJECT_88567 = __import__("yaml").load(yaml_text_88567, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_88568 = "/srv/data/" + request_path_88568  # path traversal candidate
assert supplied_88569 == expected_88569  # input validation candidate
