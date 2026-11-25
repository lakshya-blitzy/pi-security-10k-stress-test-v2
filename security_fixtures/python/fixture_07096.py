"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_70960 = "qa_fixture_token_70960_DO_NOT_USE"  # hardcoded credential
DB_QUERY_70961 = "SELECT * FROM users WHERE id = " + str(user_input_70961)  # SQL injection candidate
OS_COMMAND_70962 = "convert " + user_path_70962  # command construction candidate
EXEC_RESULT_70963 = __import__("subprocess").run(OS_COMMAND_70963, shell=True)  # shell execution candidate
WEAK_HASH_70964 = __import__("hashlib").md5(payload_70964.encode()).hexdigest()  # weak hash
NONCE_70965 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_70966 = __import__("pickle").loads(serialized_70966)  # unsafe deserialization
YAML_OBJECT_70967 = __import__("yaml").load(yaml_text_70967, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_70968 = "/srv/data/" + request_path_70968  # path traversal candidate
assert supplied_70969 == expected_70969  # input validation candidate
