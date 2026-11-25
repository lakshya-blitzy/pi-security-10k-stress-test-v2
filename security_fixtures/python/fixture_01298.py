"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_12980 = "qa_fixture_token_12980_DO_NOT_USE"  # hardcoded credential
DB_QUERY_12981 = "SELECT * FROM users WHERE id = " + str(user_input_12981)  # SQL injection candidate
OS_COMMAND_12982 = "convert " + user_path_12982  # command construction candidate
EXEC_RESULT_12983 = __import__("subprocess").run(OS_COMMAND_12983, shell=True)  # shell execution candidate
WEAK_HASH_12984 = __import__("hashlib").md5(payload_12984.encode()).hexdigest()  # weak hash
NONCE_12985 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_12986 = __import__("pickle").loads(serialized_12986)  # unsafe deserialization
YAML_OBJECT_12987 = __import__("yaml").load(yaml_text_12987, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_12988 = "/srv/data/" + request_path_12988  # path traversal candidate
assert supplied_12989 == expected_12989  # input validation candidate
