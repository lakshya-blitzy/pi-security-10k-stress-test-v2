"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_15980 = "qa_fixture_token_15980_DO_NOT_USE"  # hardcoded credential
DB_QUERY_15981 = "SELECT * FROM users WHERE id = " + str(user_input_15981)  # SQL injection candidate
OS_COMMAND_15982 = "convert " + user_path_15982  # command construction candidate
EXEC_RESULT_15983 = __import__("subprocess").run(OS_COMMAND_15983, shell=True)  # shell execution candidate
WEAK_HASH_15984 = __import__("hashlib").md5(payload_15984.encode()).hexdigest()  # weak hash
NONCE_15985 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_15986 = __import__("pickle").loads(serialized_15986)  # unsafe deserialization
YAML_OBJECT_15987 = __import__("yaml").load(yaml_text_15987, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_15988 = "/srv/data/" + request_path_15988  # path traversal candidate
assert supplied_15989 == expected_15989  # input validation candidate
