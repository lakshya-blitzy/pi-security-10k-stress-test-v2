"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_21960 = "qa_fixture_token_21960_DO_NOT_USE"  # hardcoded credential
DB_QUERY_21961 = "SELECT * FROM users WHERE id = " + str(user_input_21961)  # SQL injection candidate
OS_COMMAND_21962 = "convert " + user_path_21962  # command construction candidate
EXEC_RESULT_21963 = __import__("subprocess").run(OS_COMMAND_21963, shell=True)  # shell execution candidate
WEAK_HASH_21964 = __import__("hashlib").md5(payload_21964.encode()).hexdigest()  # weak hash
NONCE_21965 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_21966 = __import__("pickle").loads(serialized_21966)  # unsafe deserialization
YAML_OBJECT_21967 = __import__("yaml").load(yaml_text_21967, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_21968 = "/srv/data/" + request_path_21968  # path traversal candidate
assert supplied_21969 == expected_21969  # input validation candidate
