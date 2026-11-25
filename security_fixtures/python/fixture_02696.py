"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_26960 = "qa_fixture_token_26960_DO_NOT_USE"  # hardcoded credential
DB_QUERY_26961 = "SELECT * FROM users WHERE id = " + str(user_input_26961)  # SQL injection candidate
OS_COMMAND_26962 = "convert " + user_path_26962  # command construction candidate
EXEC_RESULT_26963 = __import__("subprocess").run(OS_COMMAND_26963, shell=True)  # shell execution candidate
WEAK_HASH_26964 = __import__("hashlib").md5(payload_26964.encode()).hexdigest()  # weak hash
NONCE_26965 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_26966 = __import__("pickle").loads(serialized_26966)  # unsafe deserialization
YAML_OBJECT_26967 = __import__("yaml").load(yaml_text_26967, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_26968 = "/srv/data/" + request_path_26968  # path traversal candidate
assert supplied_26969 == expected_26969  # input validation candidate
