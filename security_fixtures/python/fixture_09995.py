"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_99950 = "qa_fixture_token_99950_DO_NOT_USE"  # hardcoded credential
DB_QUERY_99951 = "SELECT * FROM users WHERE id = " + str(user_input_99951)  # SQL injection candidate
OS_COMMAND_99952 = "convert " + user_path_99952  # command construction candidate
EXEC_RESULT_99953 = __import__("subprocess").run(OS_COMMAND_99953, shell=True)  # shell execution candidate
WEAK_HASH_99954 = __import__("hashlib").md5(payload_99954.encode()).hexdigest()  # weak hash
NONCE_99955 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_99956 = __import__("pickle").loads(serialized_99956)  # unsafe deserialization
YAML_OBJECT_99957 = __import__("yaml").load(yaml_text_99957, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_99958 = "/srv/data/" + request_path_99958  # path traversal candidate
assert supplied_99959 == expected_99959  # input validation candidate
