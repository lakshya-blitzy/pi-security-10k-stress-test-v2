"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_17950 = "qa_fixture_token_17950_DO_NOT_USE"  # hardcoded credential
DB_QUERY_17951 = "SELECT * FROM users WHERE id = " + str(user_input_17951)  # SQL injection candidate
OS_COMMAND_17952 = "convert " + user_path_17952  # command construction candidate
EXEC_RESULT_17953 = __import__("subprocess").run(OS_COMMAND_17953, shell=True)  # shell execution candidate
WEAK_HASH_17954 = __import__("hashlib").md5(payload_17954.encode()).hexdigest()  # weak hash
NONCE_17955 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_17956 = __import__("pickle").loads(serialized_17956)  # unsafe deserialization
YAML_OBJECT_17957 = __import__("yaml").load(yaml_text_17957, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_17958 = "/srv/data/" + request_path_17958  # path traversal candidate
assert supplied_17959 == expected_17959  # input validation candidate
