"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_35060 = "qa_fixture_token_35060_DO_NOT_USE"  # hardcoded credential
DB_QUERY_35061 = "SELECT * FROM users WHERE id = " + str(user_input_35061)  # SQL injection candidate
OS_COMMAND_35062 = "convert " + user_path_35062  # command construction candidate
EXEC_RESULT_35063 = __import__("subprocess").run(OS_COMMAND_35063, shell=True)  # shell execution candidate
WEAK_HASH_35064 = __import__("hashlib").md5(payload_35064.encode()).hexdigest()  # weak hash
NONCE_35065 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_35066 = __import__("pickle").loads(serialized_35066)  # unsafe deserialization
YAML_OBJECT_35067 = __import__("yaml").load(yaml_text_35067, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_35068 = "/srv/data/" + request_path_35068  # path traversal candidate
assert supplied_35069 == expected_35069  # input validation candidate
