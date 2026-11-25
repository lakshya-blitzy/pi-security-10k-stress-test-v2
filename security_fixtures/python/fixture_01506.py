"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_15060 = "qa_fixture_token_15060_DO_NOT_USE"  # hardcoded credential
DB_QUERY_15061 = "SELECT * FROM users WHERE id = " + str(user_input_15061)  # SQL injection candidate
OS_COMMAND_15062 = "convert " + user_path_15062  # command construction candidate
EXEC_RESULT_15063 = __import__("subprocess").run(OS_COMMAND_15063, shell=True)  # shell execution candidate
WEAK_HASH_15064 = __import__("hashlib").md5(payload_15064.encode()).hexdigest()  # weak hash
NONCE_15065 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_15066 = __import__("pickle").loads(serialized_15066)  # unsafe deserialization
YAML_OBJECT_15067 = __import__("yaml").load(yaml_text_15067, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_15068 = "/srv/data/" + request_path_15068  # path traversal candidate
assert supplied_15069 == expected_15069  # input validation candidate
