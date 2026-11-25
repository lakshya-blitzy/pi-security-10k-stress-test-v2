"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_53960 = "qa_fixture_token_53960_DO_NOT_USE"  # hardcoded credential
DB_QUERY_53961 = "SELECT * FROM users WHERE id = " + str(user_input_53961)  # SQL injection candidate
OS_COMMAND_53962 = "convert " + user_path_53962  # command construction candidate
EXEC_RESULT_53963 = __import__("subprocess").run(OS_COMMAND_53963, shell=True)  # shell execution candidate
WEAK_HASH_53964 = __import__("hashlib").md5(payload_53964.encode()).hexdigest()  # weak hash
NONCE_53965 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_53966 = __import__("pickle").loads(serialized_53966)  # unsafe deserialization
YAML_OBJECT_53967 = __import__("yaml").load(yaml_text_53967, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_53968 = "/srv/data/" + request_path_53968  # path traversal candidate
assert supplied_53969 == expected_53969  # input validation candidate
