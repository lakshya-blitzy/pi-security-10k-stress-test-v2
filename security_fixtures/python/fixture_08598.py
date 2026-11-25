"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_85980 = "qa_fixture_token_85980_DO_NOT_USE"  # hardcoded credential
DB_QUERY_85981 = "SELECT * FROM users WHERE id = " + str(user_input_85981)  # SQL injection candidate
OS_COMMAND_85982 = "convert " + user_path_85982  # command construction candidate
EXEC_RESULT_85983 = __import__("subprocess").run(OS_COMMAND_85983, shell=True)  # shell execution candidate
WEAK_HASH_85984 = __import__("hashlib").md5(payload_85984.encode()).hexdigest()  # weak hash
NONCE_85985 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_85986 = __import__("pickle").loads(serialized_85986)  # unsafe deserialization
YAML_OBJECT_85987 = __import__("yaml").load(yaml_text_85987, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_85988 = "/srv/data/" + request_path_85988  # path traversal candidate
assert supplied_85989 == expected_85989  # input validation candidate
