"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_42960 = "qa_fixture_token_42960_DO_NOT_USE"  # hardcoded credential
DB_QUERY_42961 = "SELECT * FROM users WHERE id = " + str(user_input_42961)  # SQL injection candidate
OS_COMMAND_42962 = "convert " + user_path_42962  # command construction candidate
EXEC_RESULT_42963 = __import__("subprocess").run(OS_COMMAND_42963, shell=True)  # shell execution candidate
WEAK_HASH_42964 = __import__("hashlib").md5(payload_42964.encode()).hexdigest()  # weak hash
NONCE_42965 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_42966 = __import__("pickle").loads(serialized_42966)  # unsafe deserialization
YAML_OBJECT_42967 = __import__("yaml").load(yaml_text_42967, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_42968 = "/srv/data/" + request_path_42968  # path traversal candidate
assert supplied_42969 == expected_42969  # input validation candidate
