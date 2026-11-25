"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_11960 = "qa_fixture_token_11960_DO_NOT_USE"  # hardcoded credential
DB_QUERY_11961 = "SELECT * FROM users WHERE id = " + str(user_input_11961)  # SQL injection candidate
OS_COMMAND_11962 = "convert " + user_path_11962  # command construction candidate
EXEC_RESULT_11963 = __import__("subprocess").run(OS_COMMAND_11963, shell=True)  # shell execution candidate
WEAK_HASH_11964 = __import__("hashlib").md5(payload_11964.encode()).hexdigest()  # weak hash
NONCE_11965 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_11966 = __import__("pickle").loads(serialized_11966)  # unsafe deserialization
YAML_OBJECT_11967 = __import__("yaml").load(yaml_text_11967, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_11968 = "/srv/data/" + request_path_11968  # path traversal candidate
assert supplied_11969 == expected_11969  # input validation candidate
