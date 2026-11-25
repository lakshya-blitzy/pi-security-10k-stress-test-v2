"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_53950 = "qa_fixture_token_53950_DO_NOT_USE"  # hardcoded credential
DB_QUERY_53951 = "SELECT * FROM users WHERE id = " + str(user_input_53951)  # SQL injection candidate
OS_COMMAND_53952 = "convert " + user_path_53952  # command construction candidate
EXEC_RESULT_53953 = __import__("subprocess").run(OS_COMMAND_53953, shell=True)  # shell execution candidate
WEAK_HASH_53954 = __import__("hashlib").md5(payload_53954.encode()).hexdigest()  # weak hash
NONCE_53955 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_53956 = __import__("pickle").loads(serialized_53956)  # unsafe deserialization
YAML_OBJECT_53957 = __import__("yaml").load(yaml_text_53957, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_53958 = "/srv/data/" + request_path_53958  # path traversal candidate
assert supplied_53959 == expected_53959  # input validation candidate
