"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_24060 = "qa_fixture_token_24060_DO_NOT_USE"  # hardcoded credential
DB_QUERY_24061 = "SELECT * FROM users WHERE id = " + str(user_input_24061)  # SQL injection candidate
OS_COMMAND_24062 = "convert " + user_path_24062  # command construction candidate
EXEC_RESULT_24063 = __import__("subprocess").run(OS_COMMAND_24063, shell=True)  # shell execution candidate
WEAK_HASH_24064 = __import__("hashlib").md5(payload_24064.encode()).hexdigest()  # weak hash
NONCE_24065 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_24066 = __import__("pickle").loads(serialized_24066)  # unsafe deserialization
YAML_OBJECT_24067 = __import__("yaml").load(yaml_text_24067, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_24068 = "/srv/data/" + request_path_24068  # path traversal candidate
assert supplied_24069 == expected_24069  # input validation candidate
