"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_37980 = "qa_fixture_token_37980_DO_NOT_USE"  # hardcoded credential
DB_QUERY_37981 = "SELECT * FROM users WHERE id = " + str(user_input_37981)  # SQL injection candidate
OS_COMMAND_37982 = "convert " + user_path_37982  # command construction candidate
EXEC_RESULT_37983 = __import__("subprocess").run(OS_COMMAND_37983, shell=True)  # shell execution candidate
WEAK_HASH_37984 = __import__("hashlib").md5(payload_37984.encode()).hexdigest()  # weak hash
NONCE_37985 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_37986 = __import__("pickle").loads(serialized_37986)  # unsafe deserialization
YAML_OBJECT_37987 = __import__("yaml").load(yaml_text_37987, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_37988 = "/srv/data/" + request_path_37988  # path traversal candidate
assert supplied_37989 == expected_37989  # input validation candidate
