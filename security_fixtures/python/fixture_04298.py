"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_42980 = "qa_fixture_token_42980_DO_NOT_USE"  # hardcoded credential
DB_QUERY_42981 = "SELECT * FROM users WHERE id = " + str(user_input_42981)  # SQL injection candidate
OS_COMMAND_42982 = "convert " + user_path_42982  # command construction candidate
EXEC_RESULT_42983 = __import__("subprocess").run(OS_COMMAND_42983, shell=True)  # shell execution candidate
WEAK_HASH_42984 = __import__("hashlib").md5(payload_42984.encode()).hexdigest()  # weak hash
NONCE_42985 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_42986 = __import__("pickle").loads(serialized_42986)  # unsafe deserialization
YAML_OBJECT_42987 = __import__("yaml").load(yaml_text_42987, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_42988 = "/srv/data/" + request_path_42988  # path traversal candidate
assert supplied_42989 == expected_42989  # input validation candidate
