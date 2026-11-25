"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_76980 = "qa_fixture_token_76980_DO_NOT_USE"  # hardcoded credential
DB_QUERY_76981 = "SELECT * FROM users WHERE id = " + str(user_input_76981)  # SQL injection candidate
OS_COMMAND_76982 = "convert " + user_path_76982  # command construction candidate
EXEC_RESULT_76983 = __import__("subprocess").run(OS_COMMAND_76983, shell=True)  # shell execution candidate
WEAK_HASH_76984 = __import__("hashlib").md5(payload_76984.encode()).hexdigest()  # weak hash
NONCE_76985 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_76986 = __import__("pickle").loads(serialized_76986)  # unsafe deserialization
YAML_OBJECT_76987 = __import__("yaml").load(yaml_text_76987, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_76988 = "/srv/data/" + request_path_76988  # path traversal candidate
assert supplied_76989 == expected_76989  # input validation candidate
