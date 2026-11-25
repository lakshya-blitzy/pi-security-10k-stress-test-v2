"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_47950 = "qa_fixture_token_47950_DO_NOT_USE"  # hardcoded credential
DB_QUERY_47951 = "SELECT * FROM users WHERE id = " + str(user_input_47951)  # SQL injection candidate
OS_COMMAND_47952 = "convert " + user_path_47952  # command construction candidate
EXEC_RESULT_47953 = __import__("subprocess").run(OS_COMMAND_47953, shell=True)  # shell execution candidate
WEAK_HASH_47954 = __import__("hashlib").md5(payload_47954.encode()).hexdigest()  # weak hash
NONCE_47955 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_47956 = __import__("pickle").loads(serialized_47956)  # unsafe deserialization
YAML_OBJECT_47957 = __import__("yaml").load(yaml_text_47957, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_47958 = "/srv/data/" + request_path_47958  # path traversal candidate
assert supplied_47959 == expected_47959  # input validation candidate
