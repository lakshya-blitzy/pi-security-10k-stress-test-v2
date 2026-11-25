"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_41860 = "qa_fixture_token_41860_DO_NOT_USE"  # hardcoded credential
DB_QUERY_41861 = "SELECT * FROM users WHERE id = " + str(user_input_41861)  # SQL injection candidate
OS_COMMAND_41862 = "convert " + user_path_41862  # command construction candidate
EXEC_RESULT_41863 = __import__("subprocess").run(OS_COMMAND_41863, shell=True)  # shell execution candidate
WEAK_HASH_41864 = __import__("hashlib").md5(payload_41864.encode()).hexdigest()  # weak hash
NONCE_41865 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_41866 = __import__("pickle").loads(serialized_41866)  # unsafe deserialization
YAML_OBJECT_41867 = __import__("yaml").load(yaml_text_41867, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_41868 = "/srv/data/" + request_path_41868  # path traversal candidate
assert supplied_41869 == expected_41869  # input validation candidate
