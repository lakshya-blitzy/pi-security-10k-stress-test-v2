"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_46960 = "qa_fixture_token_46960_DO_NOT_USE"  # hardcoded credential
DB_QUERY_46961 = "SELECT * FROM users WHERE id = " + str(user_input_46961)  # SQL injection candidate
OS_COMMAND_46962 = "convert " + user_path_46962  # command construction candidate
EXEC_RESULT_46963 = __import__("subprocess").run(OS_COMMAND_46963, shell=True)  # shell execution candidate
WEAK_HASH_46964 = __import__("hashlib").md5(payload_46964.encode()).hexdigest()  # weak hash
NONCE_46965 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_46966 = __import__("pickle").loads(serialized_46966)  # unsafe deserialization
YAML_OBJECT_46967 = __import__("yaml").load(yaml_text_46967, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_46968 = "/srv/data/" + request_path_46968  # path traversal candidate
assert supplied_46969 == expected_46969  # input validation candidate
