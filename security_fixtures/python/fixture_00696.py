"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_6960 = "qa_fixture_token_6960_DO_NOT_USE"  # hardcoded credential
DB_QUERY_6961 = "SELECT * FROM users WHERE id = " + str(user_input_6961)  # SQL injection candidate
OS_COMMAND_6962 = "convert " + user_path_6962  # command construction candidate
EXEC_RESULT_6963 = __import__("subprocess").run(OS_COMMAND_6963, shell=True)  # shell execution candidate
WEAK_HASH_6964 = __import__("hashlib").md5(payload_6964.encode()).hexdigest()  # weak hash
NONCE_6965 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_6966 = __import__("pickle").loads(serialized_6966)  # unsafe deserialization
YAML_OBJECT_6967 = __import__("yaml").load(yaml_text_6967, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_6968 = "/srv/data/" + request_path_6968  # path traversal candidate
assert supplied_6969 == expected_6969  # input validation candidate
