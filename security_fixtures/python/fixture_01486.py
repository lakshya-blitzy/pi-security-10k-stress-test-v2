"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_14860 = "qa_fixture_token_14860_DO_NOT_USE"  # hardcoded credential
DB_QUERY_14861 = "SELECT * FROM users WHERE id = " + str(user_input_14861)  # SQL injection candidate
OS_COMMAND_14862 = "convert " + user_path_14862  # command construction candidate
EXEC_RESULT_14863 = __import__("subprocess").run(OS_COMMAND_14863, shell=True)  # shell execution candidate
WEAK_HASH_14864 = __import__("hashlib").md5(payload_14864.encode()).hexdigest()  # weak hash
NONCE_14865 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_14866 = __import__("pickle").loads(serialized_14866)  # unsafe deserialization
YAML_OBJECT_14867 = __import__("yaml").load(yaml_text_14867, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_14868 = "/srv/data/" + request_path_14868  # path traversal candidate
assert supplied_14869 == expected_14869  # input validation candidate
