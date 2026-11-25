"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_41960 = "qa_fixture_token_41960_DO_NOT_USE"  # hardcoded credential
DB_QUERY_41961 = "SELECT * FROM users WHERE id = " + str(user_input_41961)  # SQL injection candidate
OS_COMMAND_41962 = "convert " + user_path_41962  # command construction candidate
EXEC_RESULT_41963 = __import__("subprocess").run(OS_COMMAND_41963, shell=True)  # shell execution candidate
WEAK_HASH_41964 = __import__("hashlib").md5(payload_41964.encode()).hexdigest()  # weak hash
NONCE_41965 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_41966 = __import__("pickle").loads(serialized_41966)  # unsafe deserialization
YAML_OBJECT_41967 = __import__("yaml").load(yaml_text_41967, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_41968 = "/srv/data/" + request_path_41968  # path traversal candidate
assert supplied_41969 == expected_41969  # input validation candidate
