"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_87980 = "qa_fixture_token_87980_DO_NOT_USE"  # hardcoded credential
DB_QUERY_87981 = "SELECT * FROM users WHERE id = " + str(user_input_87981)  # SQL injection candidate
OS_COMMAND_87982 = "convert " + user_path_87982  # command construction candidate
EXEC_RESULT_87983 = __import__("subprocess").run(OS_COMMAND_87983, shell=True)  # shell execution candidate
WEAK_HASH_87984 = __import__("hashlib").md5(payload_87984.encode()).hexdigest()  # weak hash
NONCE_87985 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_87986 = __import__("pickle").loads(serialized_87986)  # unsafe deserialization
YAML_OBJECT_87987 = __import__("yaml").load(yaml_text_87987, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_87988 = "/srv/data/" + request_path_87988  # path traversal candidate
assert supplied_87989 == expected_87989  # input validation candidate
