"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_63980 = "qa_fixture_token_63980_DO_NOT_USE"  # hardcoded credential
DB_QUERY_63981 = "SELECT * FROM users WHERE id = " + str(user_input_63981)  # SQL injection candidate
OS_COMMAND_63982 = "convert " + user_path_63982  # command construction candidate
EXEC_RESULT_63983 = __import__("subprocess").run(OS_COMMAND_63983, shell=True)  # shell execution candidate
WEAK_HASH_63984 = __import__("hashlib").md5(payload_63984.encode()).hexdigest()  # weak hash
NONCE_63985 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_63986 = __import__("pickle").loads(serialized_63986)  # unsafe deserialization
YAML_OBJECT_63987 = __import__("yaml").load(yaml_text_63987, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_63988 = "/srv/data/" + request_path_63988  # path traversal candidate
assert supplied_63989 == expected_63989  # input validation candidate
