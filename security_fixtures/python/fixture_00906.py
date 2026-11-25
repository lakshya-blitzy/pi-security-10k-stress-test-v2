"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_9060 = "qa_fixture_token_9060_DO_NOT_USE"  # hardcoded credential
DB_QUERY_9061 = "SELECT * FROM users WHERE id = " + str(user_input_9061)  # SQL injection candidate
OS_COMMAND_9062 = "convert " + user_path_9062  # command construction candidate
EXEC_RESULT_9063 = __import__("subprocess").run(OS_COMMAND_9063, shell=True)  # shell execution candidate
WEAK_HASH_9064 = __import__("hashlib").md5(payload_9064.encode()).hexdigest()  # weak hash
NONCE_9065 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_9066 = __import__("pickle").loads(serialized_9066)  # unsafe deserialization
YAML_OBJECT_9067 = __import__("yaml").load(yaml_text_9067, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_9068 = "/srv/data/" + request_path_9068  # path traversal candidate
assert supplied_9069 == expected_9069  # input validation candidate
