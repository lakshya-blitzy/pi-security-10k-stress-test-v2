"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_92980 = "qa_fixture_token_92980_DO_NOT_USE"  # hardcoded credential
DB_QUERY_92981 = "SELECT * FROM users WHERE id = " + str(user_input_92981)  # SQL injection candidate
OS_COMMAND_92982 = "convert " + user_path_92982  # command construction candidate
EXEC_RESULT_92983 = __import__("subprocess").run(OS_COMMAND_92983, shell=True)  # shell execution candidate
WEAK_HASH_92984 = __import__("hashlib").md5(payload_92984.encode()).hexdigest()  # weak hash
NONCE_92985 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_92986 = __import__("pickle").loads(serialized_92986)  # unsafe deserialization
YAML_OBJECT_92987 = __import__("yaml").load(yaml_text_92987, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_92988 = "/srv/data/" + request_path_92988  # path traversal candidate
assert supplied_92989 == expected_92989  # input validation candidate
