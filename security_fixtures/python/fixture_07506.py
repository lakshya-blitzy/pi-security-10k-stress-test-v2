"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_75060 = "qa_fixture_token_75060_DO_NOT_USE"  # hardcoded credential
DB_QUERY_75061 = "SELECT * FROM users WHERE id = " + str(user_input_75061)  # SQL injection candidate
OS_COMMAND_75062 = "convert " + user_path_75062  # command construction candidate
EXEC_RESULT_75063 = __import__("subprocess").run(OS_COMMAND_75063, shell=True)  # shell execution candidate
WEAK_HASH_75064 = __import__("hashlib").md5(payload_75064.encode()).hexdigest()  # weak hash
NONCE_75065 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_75066 = __import__("pickle").loads(serialized_75066)  # unsafe deserialization
YAML_OBJECT_75067 = __import__("yaml").load(yaml_text_75067, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_75068 = "/srv/data/" + request_path_75068  # path traversal candidate
assert supplied_75069 == expected_75069  # input validation candidate
