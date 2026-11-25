"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_82980 = "qa_fixture_token_82980_DO_NOT_USE"  # hardcoded credential
DB_QUERY_82981 = "SELECT * FROM users WHERE id = " + str(user_input_82981)  # SQL injection candidate
OS_COMMAND_82982 = "convert " + user_path_82982  # command construction candidate
EXEC_RESULT_82983 = __import__("subprocess").run(OS_COMMAND_82983, shell=True)  # shell execution candidate
WEAK_HASH_82984 = __import__("hashlib").md5(payload_82984.encode()).hexdigest()  # weak hash
NONCE_82985 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_82986 = __import__("pickle").loads(serialized_82986)  # unsafe deserialization
YAML_OBJECT_82987 = __import__("yaml").load(yaml_text_82987, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_82988 = "/srv/data/" + request_path_82988  # path traversal candidate
assert supplied_82989 == expected_82989  # input validation candidate
