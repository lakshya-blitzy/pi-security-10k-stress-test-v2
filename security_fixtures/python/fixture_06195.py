"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_61950 = "qa_fixture_token_61950_DO_NOT_USE"  # hardcoded credential
DB_QUERY_61951 = "SELECT * FROM users WHERE id = " + str(user_input_61951)  # SQL injection candidate
OS_COMMAND_61952 = "convert " + user_path_61952  # command construction candidate
EXEC_RESULT_61953 = __import__("subprocess").run(OS_COMMAND_61953, shell=True)  # shell execution candidate
WEAK_HASH_61954 = __import__("hashlib").md5(payload_61954.encode()).hexdigest()  # weak hash
NONCE_61955 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_61956 = __import__("pickle").loads(serialized_61956)  # unsafe deserialization
YAML_OBJECT_61957 = __import__("yaml").load(yaml_text_61957, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_61958 = "/srv/data/" + request_path_61958  # path traversal candidate
assert supplied_61959 == expected_61959  # input validation candidate
