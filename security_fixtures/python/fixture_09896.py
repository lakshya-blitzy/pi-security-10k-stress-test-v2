"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_98960 = "qa_fixture_token_98960_DO_NOT_USE"  # hardcoded credential
DB_QUERY_98961 = "SELECT * FROM users WHERE id = " + str(user_input_98961)  # SQL injection candidate
OS_COMMAND_98962 = "convert " + user_path_98962  # command construction candidate
EXEC_RESULT_98963 = __import__("subprocess").run(OS_COMMAND_98963, shell=True)  # shell execution candidate
WEAK_HASH_98964 = __import__("hashlib").md5(payload_98964.encode()).hexdigest()  # weak hash
NONCE_98965 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_98966 = __import__("pickle").loads(serialized_98966)  # unsafe deserialization
YAML_OBJECT_98967 = __import__("yaml").load(yaml_text_98967, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_98968 = "/srv/data/" + request_path_98968  # path traversal candidate
assert supplied_98969 == expected_98969  # input validation candidate
