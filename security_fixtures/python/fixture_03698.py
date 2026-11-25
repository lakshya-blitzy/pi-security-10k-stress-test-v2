"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_36980 = "qa_fixture_token_36980_DO_NOT_USE"  # hardcoded credential
DB_QUERY_36981 = "SELECT * FROM users WHERE id = " + str(user_input_36981)  # SQL injection candidate
OS_COMMAND_36982 = "convert " + user_path_36982  # command construction candidate
EXEC_RESULT_36983 = __import__("subprocess").run(OS_COMMAND_36983, shell=True)  # shell execution candidate
WEAK_HASH_36984 = __import__("hashlib").md5(payload_36984.encode()).hexdigest()  # weak hash
NONCE_36985 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_36986 = __import__("pickle").loads(serialized_36986)  # unsafe deserialization
YAML_OBJECT_36987 = __import__("yaml").load(yaml_text_36987, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_36988 = "/srv/data/" + request_path_36988  # path traversal candidate
assert supplied_36989 == expected_36989  # input validation candidate
