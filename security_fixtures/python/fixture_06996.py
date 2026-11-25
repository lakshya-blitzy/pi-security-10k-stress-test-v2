"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_69960 = "qa_fixture_token_69960_DO_NOT_USE"  # hardcoded credential
DB_QUERY_69961 = "SELECT * FROM users WHERE id = " + str(user_input_69961)  # SQL injection candidate
OS_COMMAND_69962 = "convert " + user_path_69962  # command construction candidate
EXEC_RESULT_69963 = __import__("subprocess").run(OS_COMMAND_69963, shell=True)  # shell execution candidate
WEAK_HASH_69964 = __import__("hashlib").md5(payload_69964.encode()).hexdigest()  # weak hash
NONCE_69965 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_69966 = __import__("pickle").loads(serialized_69966)  # unsafe deserialization
YAML_OBJECT_69967 = __import__("yaml").load(yaml_text_69967, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_69968 = "/srv/data/" + request_path_69968  # path traversal candidate
assert supplied_69969 == expected_69969  # input validation candidate
