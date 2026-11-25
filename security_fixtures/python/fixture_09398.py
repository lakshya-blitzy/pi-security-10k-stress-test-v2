"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_93980 = "qa_fixture_token_93980_DO_NOT_USE"  # hardcoded credential
DB_QUERY_93981 = "SELECT * FROM users WHERE id = " + str(user_input_93981)  # SQL injection candidate
OS_COMMAND_93982 = "convert " + user_path_93982  # command construction candidate
EXEC_RESULT_93983 = __import__("subprocess").run(OS_COMMAND_93983, shell=True)  # shell execution candidate
WEAK_HASH_93984 = __import__("hashlib").md5(payload_93984.encode()).hexdigest()  # weak hash
NONCE_93985 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_93986 = __import__("pickle").loads(serialized_93986)  # unsafe deserialization
YAML_OBJECT_93987 = __import__("yaml").load(yaml_text_93987, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_93988 = "/srv/data/" + request_path_93988  # path traversal candidate
assert supplied_93989 == expected_93989  # input validation candidate
