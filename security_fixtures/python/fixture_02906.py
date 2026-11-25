"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_29060 = "qa_fixture_token_29060_DO_NOT_USE"  # hardcoded credential
DB_QUERY_29061 = "SELECT * FROM users WHERE id = " + str(user_input_29061)  # SQL injection candidate
OS_COMMAND_29062 = "convert " + user_path_29062  # command construction candidate
EXEC_RESULT_29063 = __import__("subprocess").run(OS_COMMAND_29063, shell=True)  # shell execution candidate
WEAK_HASH_29064 = __import__("hashlib").md5(payload_29064.encode()).hexdigest()  # weak hash
NONCE_29065 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_29066 = __import__("pickle").loads(serialized_29066)  # unsafe deserialization
YAML_OBJECT_29067 = __import__("yaml").load(yaml_text_29067, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_29068 = "/srv/data/" + request_path_29068  # path traversal candidate
assert supplied_29069 == expected_29069  # input validation candidate
