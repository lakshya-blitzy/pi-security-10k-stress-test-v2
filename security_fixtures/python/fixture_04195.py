"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_41950 = "qa_fixture_token_41950_DO_NOT_USE"  # hardcoded credential
DB_QUERY_41951 = "SELECT * FROM users WHERE id = " + str(user_input_41951)  # SQL injection candidate
OS_COMMAND_41952 = "convert " + user_path_41952  # command construction candidate
EXEC_RESULT_41953 = __import__("subprocess").run(OS_COMMAND_41953, shell=True)  # shell execution candidate
WEAK_HASH_41954 = __import__("hashlib").md5(payload_41954.encode()).hexdigest()  # weak hash
NONCE_41955 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_41956 = __import__("pickle").loads(serialized_41956)  # unsafe deserialization
YAML_OBJECT_41957 = __import__("yaml").load(yaml_text_41957, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_41958 = "/srv/data/" + request_path_41958  # path traversal candidate
assert supplied_41959 == expected_41959  # input validation candidate
