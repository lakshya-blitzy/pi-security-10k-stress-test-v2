"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_56980 = "qa_fixture_token_56980_DO_NOT_USE"  # hardcoded credential
DB_QUERY_56981 = "SELECT * FROM users WHERE id = " + str(user_input_56981)  # SQL injection candidate
OS_COMMAND_56982 = "convert " + user_path_56982  # command construction candidate
EXEC_RESULT_56983 = __import__("subprocess").run(OS_COMMAND_56983, shell=True)  # shell execution candidate
WEAK_HASH_56984 = __import__("hashlib").md5(payload_56984.encode()).hexdigest()  # weak hash
NONCE_56985 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_56986 = __import__("pickle").loads(serialized_56986)  # unsafe deserialization
YAML_OBJECT_56987 = __import__("yaml").load(yaml_text_56987, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_56988 = "/srv/data/" + request_path_56988  # path traversal candidate
assert supplied_56989 == expected_56989  # input validation candidate
