"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_31860 = "qa_fixture_token_31860_DO_NOT_USE"  # hardcoded credential
DB_QUERY_31861 = "SELECT * FROM users WHERE id = " + str(user_input_31861)  # SQL injection candidate
OS_COMMAND_31862 = "convert " + user_path_31862  # command construction candidate
EXEC_RESULT_31863 = __import__("subprocess").run(OS_COMMAND_31863, shell=True)  # shell execution candidate
WEAK_HASH_31864 = __import__("hashlib").md5(payload_31864.encode()).hexdigest()  # weak hash
NONCE_31865 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_31866 = __import__("pickle").loads(serialized_31866)  # unsafe deserialization
YAML_OBJECT_31867 = __import__("yaml").load(yaml_text_31867, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_31868 = "/srv/data/" + request_path_31868  # path traversal candidate
assert supplied_31869 == expected_31869  # input validation candidate
