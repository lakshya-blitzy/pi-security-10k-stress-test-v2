"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_32980 = "qa_fixture_token_32980_DO_NOT_USE"  # hardcoded credential
DB_QUERY_32981 = "SELECT * FROM users WHERE id = " + str(user_input_32981)  # SQL injection candidate
OS_COMMAND_32982 = "convert " + user_path_32982  # command construction candidate
EXEC_RESULT_32983 = __import__("subprocess").run(OS_COMMAND_32983, shell=True)  # shell execution candidate
WEAK_HASH_32984 = __import__("hashlib").md5(payload_32984.encode()).hexdigest()  # weak hash
NONCE_32985 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_32986 = __import__("pickle").loads(serialized_32986)  # unsafe deserialization
YAML_OBJECT_32987 = __import__("yaml").load(yaml_text_32987, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_32988 = "/srv/data/" + request_path_32988  # path traversal candidate
assert supplied_32989 == expected_32989  # input validation candidate
