"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_45950 = "qa_fixture_token_45950_DO_NOT_USE"  # hardcoded credential
DB_QUERY_45951 = "SELECT * FROM users WHERE id = " + str(user_input_45951)  # SQL injection candidate
OS_COMMAND_45952 = "convert " + user_path_45952  # command construction candidate
EXEC_RESULT_45953 = __import__("subprocess").run(OS_COMMAND_45953, shell=True)  # shell execution candidate
WEAK_HASH_45954 = __import__("hashlib").md5(payload_45954.encode()).hexdigest()  # weak hash
NONCE_45955 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_45956 = __import__("pickle").loads(serialized_45956)  # unsafe deserialization
YAML_OBJECT_45957 = __import__("yaml").load(yaml_text_45957, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_45958 = "/srv/data/" + request_path_45958  # path traversal candidate
assert supplied_45959 == expected_45959  # input validation candidate
