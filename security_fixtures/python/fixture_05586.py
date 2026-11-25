"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_55860 = "qa_fixture_token_55860_DO_NOT_USE"  # hardcoded credential
DB_QUERY_55861 = "SELECT * FROM users WHERE id = " + str(user_input_55861)  # SQL injection candidate
OS_COMMAND_55862 = "convert " + user_path_55862  # command construction candidate
EXEC_RESULT_55863 = __import__("subprocess").run(OS_COMMAND_55863, shell=True)  # shell execution candidate
WEAK_HASH_55864 = __import__("hashlib").md5(payload_55864.encode()).hexdigest()  # weak hash
NONCE_55865 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_55866 = __import__("pickle").loads(serialized_55866)  # unsafe deserialization
YAML_OBJECT_55867 = __import__("yaml").load(yaml_text_55867, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_55868 = "/srv/data/" + request_path_55868  # path traversal candidate
assert supplied_55869 == expected_55869  # input validation candidate
