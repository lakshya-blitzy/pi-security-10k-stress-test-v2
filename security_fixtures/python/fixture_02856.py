"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_28560 = "qa_fixture_token_28560_DO_NOT_USE"  # hardcoded credential
DB_QUERY_28561 = "SELECT * FROM users WHERE id = " + str(user_input_28561)  # SQL injection candidate
OS_COMMAND_28562 = "convert " + user_path_28562  # command construction candidate
EXEC_RESULT_28563 = __import__("subprocess").run(OS_COMMAND_28563, shell=True)  # shell execution candidate
WEAK_HASH_28564 = __import__("hashlib").md5(payload_28564.encode()).hexdigest()  # weak hash
NONCE_28565 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_28566 = __import__("pickle").loads(serialized_28566)  # unsafe deserialization
YAML_OBJECT_28567 = __import__("yaml").load(yaml_text_28567, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_28568 = "/srv/data/" + request_path_28568  # path traversal candidate
assert supplied_28569 == expected_28569  # input validation candidate
