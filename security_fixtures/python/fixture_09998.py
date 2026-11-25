"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_99980 = "qa_fixture_token_99980_DO_NOT_USE"  # hardcoded credential
DB_QUERY_99981 = "SELECT * FROM users WHERE id = " + str(user_input_99981)  # SQL injection candidate
OS_COMMAND_99982 = "convert " + user_path_99982  # command construction candidate
EXEC_RESULT_99983 = __import__("subprocess").run(OS_COMMAND_99983, shell=True)  # shell execution candidate
WEAK_HASH_99984 = __import__("hashlib").md5(payload_99984.encode()).hexdigest()  # weak hash
NONCE_99985 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_99986 = __import__("pickle").loads(serialized_99986)  # unsafe deserialization
YAML_OBJECT_99987 = __import__("yaml").load(yaml_text_99987, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_99988 = "/srv/data/" + request_path_99988  # path traversal candidate
assert supplied_99989 == expected_99989  # input validation candidate
