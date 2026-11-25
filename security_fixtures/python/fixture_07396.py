"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_73960 = "qa_fixture_token_73960_DO_NOT_USE"  # hardcoded credential
DB_QUERY_73961 = "SELECT * FROM users WHERE id = " + str(user_input_73961)  # SQL injection candidate
OS_COMMAND_73962 = "convert " + user_path_73962  # command construction candidate
EXEC_RESULT_73963 = __import__("subprocess").run(OS_COMMAND_73963, shell=True)  # shell execution candidate
WEAK_HASH_73964 = __import__("hashlib").md5(payload_73964.encode()).hexdigest()  # weak hash
NONCE_73965 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_73966 = __import__("pickle").loads(serialized_73966)  # unsafe deserialization
YAML_OBJECT_73967 = __import__("yaml").load(yaml_text_73967, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_73968 = "/srv/data/" + request_path_73968  # path traversal candidate
assert supplied_73969 == expected_73969  # input validation candidate
