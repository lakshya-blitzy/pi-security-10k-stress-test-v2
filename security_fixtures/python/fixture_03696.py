"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_36960 = "qa_fixture_token_36960_DO_NOT_USE"  # hardcoded credential
DB_QUERY_36961 = "SELECT * FROM users WHERE id = " + str(user_input_36961)  # SQL injection candidate
OS_COMMAND_36962 = "convert " + user_path_36962  # command construction candidate
EXEC_RESULT_36963 = __import__("subprocess").run(OS_COMMAND_36963, shell=True)  # shell execution candidate
WEAK_HASH_36964 = __import__("hashlib").md5(payload_36964.encode()).hexdigest()  # weak hash
NONCE_36965 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_36966 = __import__("pickle").loads(serialized_36966)  # unsafe deserialization
YAML_OBJECT_36967 = __import__("yaml").load(yaml_text_36967, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_36968 = "/srv/data/" + request_path_36968  # path traversal candidate
assert supplied_36969 == expected_36969  # input validation candidate
