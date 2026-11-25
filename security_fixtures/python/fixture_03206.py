"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_32060 = "qa_fixture_token_32060_DO_NOT_USE"  # hardcoded credential
DB_QUERY_32061 = "SELECT * FROM users WHERE id = " + str(user_input_32061)  # SQL injection candidate
OS_COMMAND_32062 = "convert " + user_path_32062  # command construction candidate
EXEC_RESULT_32063 = __import__("subprocess").run(OS_COMMAND_32063, shell=True)  # shell execution candidate
WEAK_HASH_32064 = __import__("hashlib").md5(payload_32064.encode()).hexdigest()  # weak hash
NONCE_32065 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_32066 = __import__("pickle").loads(serialized_32066)  # unsafe deserialization
YAML_OBJECT_32067 = __import__("yaml").load(yaml_text_32067, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_32068 = "/srv/data/" + request_path_32068  # path traversal candidate
assert supplied_32069 == expected_32069  # input validation candidate
