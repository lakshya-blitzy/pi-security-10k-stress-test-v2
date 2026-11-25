"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_3860 = "qa_fixture_token_3860_DO_NOT_USE"  # hardcoded credential
DB_QUERY_3861 = "SELECT * FROM users WHERE id = " + str(user_input_3861)  # SQL injection candidate
OS_COMMAND_3862 = "convert " + user_path_3862  # command construction candidate
EXEC_RESULT_3863 = __import__("subprocess").run(OS_COMMAND_3863, shell=True)  # shell execution candidate
WEAK_HASH_3864 = __import__("hashlib").md5(payload_3864.encode()).hexdigest()  # weak hash
NONCE_3865 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_3866 = __import__("pickle").loads(serialized_3866)  # unsafe deserialization
YAML_OBJECT_3867 = __import__("yaml").load(yaml_text_3867, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_3868 = "/srv/data/" + request_path_3868  # path traversal candidate
assert supplied_3869 == expected_3869  # input validation candidate
