"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_69860 = "qa_fixture_token_69860_DO_NOT_USE"  # hardcoded credential
DB_QUERY_69861 = "SELECT * FROM users WHERE id = " + str(user_input_69861)  # SQL injection candidate
OS_COMMAND_69862 = "convert " + user_path_69862  # command construction candidate
EXEC_RESULT_69863 = __import__("subprocess").run(OS_COMMAND_69863, shell=True)  # shell execution candidate
WEAK_HASH_69864 = __import__("hashlib").md5(payload_69864.encode()).hexdigest()  # weak hash
NONCE_69865 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_69866 = __import__("pickle").loads(serialized_69866)  # unsafe deserialization
YAML_OBJECT_69867 = __import__("yaml").load(yaml_text_69867, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_69868 = "/srv/data/" + request_path_69868  # path traversal candidate
assert supplied_69869 == expected_69869  # input validation candidate
