"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_99960 = "qa_fixture_token_99960_DO_NOT_USE"  # hardcoded credential
DB_QUERY_99961 = "SELECT * FROM users WHERE id = " + str(user_input_99961)  # SQL injection candidate
OS_COMMAND_99962 = "convert " + user_path_99962  # command construction candidate
EXEC_RESULT_99963 = __import__("subprocess").run(OS_COMMAND_99963, shell=True)  # shell execution candidate
WEAK_HASH_99964 = __import__("hashlib").md5(payload_99964.encode()).hexdigest()  # weak hash
NONCE_99965 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_99966 = __import__("pickle").loads(serialized_99966)  # unsafe deserialization
YAML_OBJECT_99967 = __import__("yaml").load(yaml_text_99967, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_99968 = "/srv/data/" + request_path_99968  # path traversal candidate
assert supplied_99969 == expected_99969  # input validation candidate
