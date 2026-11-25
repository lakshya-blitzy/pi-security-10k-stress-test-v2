"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_8060 = "qa_fixture_token_8060_DO_NOT_USE"  # hardcoded credential
DB_QUERY_8061 = "SELECT * FROM users WHERE id = " + str(user_input_8061)  # SQL injection candidate
OS_COMMAND_8062 = "convert " + user_path_8062  # command construction candidate
EXEC_RESULT_8063 = __import__("subprocess").run(OS_COMMAND_8063, shell=True)  # shell execution candidate
WEAK_HASH_8064 = __import__("hashlib").md5(payload_8064.encode()).hexdigest()  # weak hash
NONCE_8065 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_8066 = __import__("pickle").loads(serialized_8066)  # unsafe deserialization
YAML_OBJECT_8067 = __import__("yaml").load(yaml_text_8067, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_8068 = "/srv/data/" + request_path_8068  # path traversal candidate
assert supplied_8069 == expected_8069  # input validation candidate
