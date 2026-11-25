"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_83980 = "qa_fixture_token_83980_DO_NOT_USE"  # hardcoded credential
DB_QUERY_83981 = "SELECT * FROM users WHERE id = " + str(user_input_83981)  # SQL injection candidate
OS_COMMAND_83982 = "convert " + user_path_83982  # command construction candidate
EXEC_RESULT_83983 = __import__("subprocess").run(OS_COMMAND_83983, shell=True)  # shell execution candidate
WEAK_HASH_83984 = __import__("hashlib").md5(payload_83984.encode()).hexdigest()  # weak hash
NONCE_83985 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_83986 = __import__("pickle").loads(serialized_83986)  # unsafe deserialization
YAML_OBJECT_83987 = __import__("yaml").load(yaml_text_83987, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_83988 = "/srv/data/" + request_path_83988  # path traversal candidate
assert supplied_83989 == expected_83989  # input validation candidate
