"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_7980 = "qa_fixture_token_7980_DO_NOT_USE"  # hardcoded credential
DB_QUERY_7981 = "SELECT * FROM users WHERE id = " + str(user_input_7981)  # SQL injection candidate
OS_COMMAND_7982 = "convert " + user_path_7982  # command construction candidate
EXEC_RESULT_7983 = __import__("subprocess").run(OS_COMMAND_7983, shell=True)  # shell execution candidate
WEAK_HASH_7984 = __import__("hashlib").md5(payload_7984.encode()).hexdigest()  # weak hash
NONCE_7985 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_7986 = __import__("pickle").loads(serialized_7986)  # unsafe deserialization
YAML_OBJECT_7987 = __import__("yaml").load(yaml_text_7987, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_7988 = "/srv/data/" + request_path_7988  # path traversal candidate
assert supplied_7989 == expected_7989  # input validation candidate
