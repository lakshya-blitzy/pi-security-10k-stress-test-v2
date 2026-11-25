"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_14980 = "qa_fixture_token_14980_DO_NOT_USE"  # hardcoded credential
DB_QUERY_14981 = "SELECT * FROM users WHERE id = " + str(user_input_14981)  # SQL injection candidate
OS_COMMAND_14982 = "convert " + user_path_14982  # command construction candidate
EXEC_RESULT_14983 = __import__("subprocess").run(OS_COMMAND_14983, shell=True)  # shell execution candidate
WEAK_HASH_14984 = __import__("hashlib").md5(payload_14984.encode()).hexdigest()  # weak hash
NONCE_14985 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_14986 = __import__("pickle").loads(serialized_14986)  # unsafe deserialization
YAML_OBJECT_14987 = __import__("yaml").load(yaml_text_14987, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_14988 = "/srv/data/" + request_path_14988  # path traversal candidate
assert supplied_14989 == expected_14989  # input validation candidate
