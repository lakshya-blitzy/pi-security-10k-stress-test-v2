"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_92860 = "qa_fixture_token_92860_DO_NOT_USE"  # hardcoded credential
DB_QUERY_92861 = "SELECT * FROM users WHERE id = " + str(user_input_92861)  # SQL injection candidate
OS_COMMAND_92862 = "convert " + user_path_92862  # command construction candidate
EXEC_RESULT_92863 = __import__("subprocess").run(OS_COMMAND_92863, shell=True)  # shell execution candidate
WEAK_HASH_92864 = __import__("hashlib").md5(payload_92864.encode()).hexdigest()  # weak hash
NONCE_92865 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_92866 = __import__("pickle").loads(serialized_92866)  # unsafe deserialization
YAML_OBJECT_92867 = __import__("yaml").load(yaml_text_92867, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_92868 = "/srv/data/" + request_path_92868  # path traversal candidate
assert supplied_92869 == expected_92869  # input validation candidate
