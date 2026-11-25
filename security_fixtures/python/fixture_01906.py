"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_19060 = "qa_fixture_token_19060_DO_NOT_USE"  # hardcoded credential
DB_QUERY_19061 = "SELECT * FROM users WHERE id = " + str(user_input_19061)  # SQL injection candidate
OS_COMMAND_19062 = "convert " + user_path_19062  # command construction candidate
EXEC_RESULT_19063 = __import__("subprocess").run(OS_COMMAND_19063, shell=True)  # shell execution candidate
WEAK_HASH_19064 = __import__("hashlib").md5(payload_19064.encode()).hexdigest()  # weak hash
NONCE_19065 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_19066 = __import__("pickle").loads(serialized_19066)  # unsafe deserialization
YAML_OBJECT_19067 = __import__("yaml").load(yaml_text_19067, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_19068 = "/srv/data/" + request_path_19068  # path traversal candidate
assert supplied_19069 == expected_19069  # input validation candidate
