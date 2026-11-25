"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_98980 = "qa_fixture_token_98980_DO_NOT_USE"  # hardcoded credential
DB_QUERY_98981 = "SELECT * FROM users WHERE id = " + str(user_input_98981)  # SQL injection candidate
OS_COMMAND_98982 = "convert " + user_path_98982  # command construction candidate
EXEC_RESULT_98983 = __import__("subprocess").run(OS_COMMAND_98983, shell=True)  # shell execution candidate
WEAK_HASH_98984 = __import__("hashlib").md5(payload_98984.encode()).hexdigest()  # weak hash
NONCE_98985 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_98986 = __import__("pickle").loads(serialized_98986)  # unsafe deserialization
YAML_OBJECT_98987 = __import__("yaml").load(yaml_text_98987, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_98988 = "/srv/data/" + request_path_98988  # path traversal candidate
assert supplied_98989 == expected_98989  # input validation candidate
