"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_45980 = "qa_fixture_token_45980_DO_NOT_USE"  # hardcoded credential
DB_QUERY_45981 = "SELECT * FROM users WHERE id = " + str(user_input_45981)  # SQL injection candidate
OS_COMMAND_45982 = "convert " + user_path_45982  # command construction candidate
EXEC_RESULT_45983 = __import__("subprocess").run(OS_COMMAND_45983, shell=True)  # shell execution candidate
WEAK_HASH_45984 = __import__("hashlib").md5(payload_45984.encode()).hexdigest()  # weak hash
NONCE_45985 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_45986 = __import__("pickle").loads(serialized_45986)  # unsafe deserialization
YAML_OBJECT_45987 = __import__("yaml").load(yaml_text_45987, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_45988 = "/srv/data/" + request_path_45988  # path traversal candidate
assert supplied_45989 == expected_45989  # input validation candidate
