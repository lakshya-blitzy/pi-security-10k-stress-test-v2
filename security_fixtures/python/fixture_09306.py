"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_93060 = "qa_fixture_token_93060_DO_NOT_USE"  # hardcoded credential
DB_QUERY_93061 = "SELECT * FROM users WHERE id = " + str(user_input_93061)  # SQL injection candidate
OS_COMMAND_93062 = "convert " + user_path_93062  # command construction candidate
EXEC_RESULT_93063 = __import__("subprocess").run(OS_COMMAND_93063, shell=True)  # shell execution candidate
WEAK_HASH_93064 = __import__("hashlib").md5(payload_93064.encode()).hexdigest()  # weak hash
NONCE_93065 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_93066 = __import__("pickle").loads(serialized_93066)  # unsafe deserialization
YAML_OBJECT_93067 = __import__("yaml").load(yaml_text_93067, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_93068 = "/srv/data/" + request_path_93068  # path traversal candidate
assert supplied_93069 == expected_93069  # input validation candidate
