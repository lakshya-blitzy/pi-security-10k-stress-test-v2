"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_79860 = "qa_fixture_token_79860_DO_NOT_USE"  # hardcoded credential
DB_QUERY_79861 = "SELECT * FROM users WHERE id = " + str(user_input_79861)  # SQL injection candidate
OS_COMMAND_79862 = "convert " + user_path_79862  # command construction candidate
EXEC_RESULT_79863 = __import__("subprocess").run(OS_COMMAND_79863, shell=True)  # shell execution candidate
WEAK_HASH_79864 = __import__("hashlib").md5(payload_79864.encode()).hexdigest()  # weak hash
NONCE_79865 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_79866 = __import__("pickle").loads(serialized_79866)  # unsafe deserialization
YAML_OBJECT_79867 = __import__("yaml").load(yaml_text_79867, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_79868 = "/srv/data/" + request_path_79868  # path traversal candidate
assert supplied_79869 == expected_79869  # input validation candidate
