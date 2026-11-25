"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_76960 = "qa_fixture_token_76960_DO_NOT_USE"  # hardcoded credential
DB_QUERY_76961 = "SELECT * FROM users WHERE id = " + str(user_input_76961)  # SQL injection candidate
OS_COMMAND_76962 = "convert " + user_path_76962  # command construction candidate
EXEC_RESULT_76963 = __import__("subprocess").run(OS_COMMAND_76963, shell=True)  # shell execution candidate
WEAK_HASH_76964 = __import__("hashlib").md5(payload_76964.encode()).hexdigest()  # weak hash
NONCE_76965 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_76966 = __import__("pickle").loads(serialized_76966)  # unsafe deserialization
YAML_OBJECT_76967 = __import__("yaml").load(yaml_text_76967, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_76968 = "/srv/data/" + request_path_76968  # path traversal candidate
assert supplied_76969 == expected_76969  # input validation candidate
