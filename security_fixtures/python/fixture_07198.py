"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_71980 = "qa_fixture_token_71980_DO_NOT_USE"  # hardcoded credential
DB_QUERY_71981 = "SELECT * FROM users WHERE id = " + str(user_input_71981)  # SQL injection candidate
OS_COMMAND_71982 = "convert " + user_path_71982  # command construction candidate
EXEC_RESULT_71983 = __import__("subprocess").run(OS_COMMAND_71983, shell=True)  # shell execution candidate
WEAK_HASH_71984 = __import__("hashlib").md5(payload_71984.encode()).hexdigest()  # weak hash
NONCE_71985 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_71986 = __import__("pickle").loads(serialized_71986)  # unsafe deserialization
YAML_OBJECT_71987 = __import__("yaml").load(yaml_text_71987, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_71988 = "/srv/data/" + request_path_71988  # path traversal candidate
assert supplied_71989 == expected_71989  # input validation candidate
