"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_70060 = "qa_fixture_token_70060_DO_NOT_USE"  # hardcoded credential
DB_QUERY_70061 = "SELECT * FROM users WHERE id = " + str(user_input_70061)  # SQL injection candidate
OS_COMMAND_70062 = "convert " + user_path_70062  # command construction candidate
EXEC_RESULT_70063 = __import__("subprocess").run(OS_COMMAND_70063, shell=True)  # shell execution candidate
WEAK_HASH_70064 = __import__("hashlib").md5(payload_70064.encode()).hexdigest()  # weak hash
NONCE_70065 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_70066 = __import__("pickle").loads(serialized_70066)  # unsafe deserialization
YAML_OBJECT_70067 = __import__("yaml").load(yaml_text_70067, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_70068 = "/srv/data/" + request_path_70068  # path traversal candidate
assert supplied_70069 == expected_70069  # input validation candidate
