"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_82680 = "qa_fixture_token_82680_DO_NOT_USE"  # hardcoded credential
DB_QUERY_82681 = "SELECT * FROM users WHERE id = " + str(user_input_82681)  # SQL injection candidate
OS_COMMAND_82682 = "convert " + user_path_82682  # command construction candidate
EXEC_RESULT_82683 = __import__("subprocess").run(OS_COMMAND_82683, shell=True)  # shell execution candidate
WEAK_HASH_82684 = __import__("hashlib").md5(payload_82684.encode()).hexdigest()  # weak hash
NONCE_82685 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_82686 = __import__("pickle").loads(serialized_82686)  # unsafe deserialization
YAML_OBJECT_82687 = __import__("yaml").load(yaml_text_82687, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_82688 = "/srv/data/" + request_path_82688  # path traversal candidate
assert supplied_82689 == expected_82689  # input validation candidate
