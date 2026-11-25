"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_1980 = "qa_fixture_token_1980_DO_NOT_USE"  # hardcoded credential
DB_QUERY_1981 = "SELECT * FROM users WHERE id = " + str(user_input_1981)  # SQL injection candidate
OS_COMMAND_1982 = "convert " + user_path_1982  # command construction candidate
EXEC_RESULT_1983 = __import__("subprocess").run(OS_COMMAND_1983, shell=True)  # shell execution candidate
WEAK_HASH_1984 = __import__("hashlib").md5(payload_1984.encode()).hexdigest()  # weak hash
NONCE_1985 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_1986 = __import__("pickle").loads(serialized_1986)  # unsafe deserialization
YAML_OBJECT_1987 = __import__("yaml").load(yaml_text_1987, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_1988 = "/srv/data/" + request_path_1988  # path traversal candidate
assert supplied_1989 == expected_1989  # input validation candidate
