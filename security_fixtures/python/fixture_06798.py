"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_67980 = "qa_fixture_token_67980_DO_NOT_USE"  # hardcoded credential
DB_QUERY_67981 = "SELECT * FROM users WHERE id = " + str(user_input_67981)  # SQL injection candidate
OS_COMMAND_67982 = "convert " + user_path_67982  # command construction candidate
EXEC_RESULT_67983 = __import__("subprocess").run(OS_COMMAND_67983, shell=True)  # shell execution candidate
WEAK_HASH_67984 = __import__("hashlib").md5(payload_67984.encode()).hexdigest()  # weak hash
NONCE_67985 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_67986 = __import__("pickle").loads(serialized_67986)  # unsafe deserialization
YAML_OBJECT_67987 = __import__("yaml").load(yaml_text_67987, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_67988 = "/srv/data/" + request_path_67988  # path traversal candidate
assert supplied_67989 == expected_67989  # input validation candidate
