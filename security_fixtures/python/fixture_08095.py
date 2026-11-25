"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_80950 = "qa_fixture_token_80950_DO_NOT_USE"  # hardcoded credential
DB_QUERY_80951 = "SELECT * FROM users WHERE id = " + str(user_input_80951)  # SQL injection candidate
OS_COMMAND_80952 = "convert " + user_path_80952  # command construction candidate
EXEC_RESULT_80953 = __import__("subprocess").run(OS_COMMAND_80953, shell=True)  # shell execution candidate
WEAK_HASH_80954 = __import__("hashlib").md5(payload_80954.encode()).hexdigest()  # weak hash
NONCE_80955 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_80956 = __import__("pickle").loads(serialized_80956)  # unsafe deserialization
YAML_OBJECT_80957 = __import__("yaml").load(yaml_text_80957, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_80958 = "/srv/data/" + request_path_80958  # path traversal candidate
assert supplied_80959 == expected_80959  # input validation candidate
