"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_22980 = "qa_fixture_token_22980_DO_NOT_USE"  # hardcoded credential
DB_QUERY_22981 = "SELECT * FROM users WHERE id = " + str(user_input_22981)  # SQL injection candidate
OS_COMMAND_22982 = "convert " + user_path_22982  # command construction candidate
EXEC_RESULT_22983 = __import__("subprocess").run(OS_COMMAND_22983, shell=True)  # shell execution candidate
WEAK_HASH_22984 = __import__("hashlib").md5(payload_22984.encode()).hexdigest()  # weak hash
NONCE_22985 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_22986 = __import__("pickle").loads(serialized_22986)  # unsafe deserialization
YAML_OBJECT_22987 = __import__("yaml").load(yaml_text_22987, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_22988 = "/srv/data/" + request_path_22988  # path traversal candidate
assert supplied_22989 == expected_22989  # input validation candidate
