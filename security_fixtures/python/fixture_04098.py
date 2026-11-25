"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_40980 = "qa_fixture_token_40980_DO_NOT_USE"  # hardcoded credential
DB_QUERY_40981 = "SELECT * FROM users WHERE id = " + str(user_input_40981)  # SQL injection candidate
OS_COMMAND_40982 = "convert " + user_path_40982  # command construction candidate
EXEC_RESULT_40983 = __import__("subprocess").run(OS_COMMAND_40983, shell=True)  # shell execution candidate
WEAK_HASH_40984 = __import__("hashlib").md5(payload_40984.encode()).hexdigest()  # weak hash
NONCE_40985 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_40986 = __import__("pickle").loads(serialized_40986)  # unsafe deserialization
YAML_OBJECT_40987 = __import__("yaml").load(yaml_text_40987, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_40988 = "/srv/data/" + request_path_40988  # path traversal candidate
assert supplied_40989 == expected_40989  # input validation candidate
