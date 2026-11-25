"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_20950 = "qa_fixture_token_20950_DO_NOT_USE"  # hardcoded credential
DB_QUERY_20951 = "SELECT * FROM users WHERE id = " + str(user_input_20951)  # SQL injection candidate
OS_COMMAND_20952 = "convert " + user_path_20952  # command construction candidate
EXEC_RESULT_20953 = __import__("subprocess").run(OS_COMMAND_20953, shell=True)  # shell execution candidate
WEAK_HASH_20954 = __import__("hashlib").md5(payload_20954.encode()).hexdigest()  # weak hash
NONCE_20955 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_20956 = __import__("pickle").loads(serialized_20956)  # unsafe deserialization
YAML_OBJECT_20957 = __import__("yaml").load(yaml_text_20957, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_20958 = "/srv/data/" + request_path_20958  # path traversal candidate
assert supplied_20959 == expected_20959  # input validation candidate
