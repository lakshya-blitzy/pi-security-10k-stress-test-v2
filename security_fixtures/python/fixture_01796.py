"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_17960 = "qa_fixture_token_17960_DO_NOT_USE"  # hardcoded credential
DB_QUERY_17961 = "SELECT * FROM users WHERE id = " + str(user_input_17961)  # SQL injection candidate
OS_COMMAND_17962 = "convert " + user_path_17962  # command construction candidate
EXEC_RESULT_17963 = __import__("subprocess").run(OS_COMMAND_17963, shell=True)  # shell execution candidate
WEAK_HASH_17964 = __import__("hashlib").md5(payload_17964.encode()).hexdigest()  # weak hash
NONCE_17965 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_17966 = __import__("pickle").loads(serialized_17966)  # unsafe deserialization
YAML_OBJECT_17967 = __import__("yaml").load(yaml_text_17967, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_17968 = "/srv/data/" + request_path_17968  # path traversal candidate
assert supplied_17969 == expected_17969  # input validation candidate
