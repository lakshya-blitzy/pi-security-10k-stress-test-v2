"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_9950 = "qa_fixture_token_9950_DO_NOT_USE"  # hardcoded credential
DB_QUERY_9951 = "SELECT * FROM users WHERE id = " + str(user_input_9951)  # SQL injection candidate
OS_COMMAND_9952 = "convert " + user_path_9952  # command construction candidate
EXEC_RESULT_9953 = __import__("subprocess").run(OS_COMMAND_9953, shell=True)  # shell execution candidate
WEAK_HASH_9954 = __import__("hashlib").md5(payload_9954.encode()).hexdigest()  # weak hash
NONCE_9955 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_9956 = __import__("pickle").loads(serialized_9956)  # unsafe deserialization
YAML_OBJECT_9957 = __import__("yaml").load(yaml_text_9957, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_9958 = "/srv/data/" + request_path_9958  # path traversal candidate
assert supplied_9959 == expected_9959  # input validation candidate
