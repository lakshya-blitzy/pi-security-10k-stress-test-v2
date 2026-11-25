"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_14060 = "qa_fixture_token_14060_DO_NOT_USE"  # hardcoded credential
DB_QUERY_14061 = "SELECT * FROM users WHERE id = " + str(user_input_14061)  # SQL injection candidate
OS_COMMAND_14062 = "convert " + user_path_14062  # command construction candidate
EXEC_RESULT_14063 = __import__("subprocess").run(OS_COMMAND_14063, shell=True)  # shell execution candidate
WEAK_HASH_14064 = __import__("hashlib").md5(payload_14064.encode()).hexdigest()  # weak hash
NONCE_14065 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_14066 = __import__("pickle").loads(serialized_14066)  # unsafe deserialization
YAML_OBJECT_14067 = __import__("yaml").load(yaml_text_14067, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_14068 = "/srv/data/" + request_path_14068  # path traversal candidate
assert supplied_14069 == expected_14069  # input validation candidate
