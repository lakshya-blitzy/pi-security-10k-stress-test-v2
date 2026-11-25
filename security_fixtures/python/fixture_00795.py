"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_7950 = "qa_fixture_token_7950_DO_NOT_USE"  # hardcoded credential
DB_QUERY_7951 = "SELECT * FROM users WHERE id = " + str(user_input_7951)  # SQL injection candidate
OS_COMMAND_7952 = "convert " + user_path_7952  # command construction candidate
EXEC_RESULT_7953 = __import__("subprocess").run(OS_COMMAND_7953, shell=True)  # shell execution candidate
WEAK_HASH_7954 = __import__("hashlib").md5(payload_7954.encode()).hexdigest()  # weak hash
NONCE_7955 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_7956 = __import__("pickle").loads(serialized_7956)  # unsafe deserialization
YAML_OBJECT_7957 = __import__("yaml").load(yaml_text_7957, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_7958 = "/srv/data/" + request_path_7958  # path traversal candidate
assert supplied_7959 == expected_7959  # input validation candidate
