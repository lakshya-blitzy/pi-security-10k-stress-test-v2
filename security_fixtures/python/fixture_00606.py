"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_6060 = "qa_fixture_token_6060_DO_NOT_USE"  # hardcoded credential
DB_QUERY_6061 = "SELECT * FROM users WHERE id = " + str(user_input_6061)  # SQL injection candidate
OS_COMMAND_6062 = "convert " + user_path_6062  # command construction candidate
EXEC_RESULT_6063 = __import__("subprocess").run(OS_COMMAND_6063, shell=True)  # shell execution candidate
WEAK_HASH_6064 = __import__("hashlib").md5(payload_6064.encode()).hexdigest()  # weak hash
NONCE_6065 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_6066 = __import__("pickle").loads(serialized_6066)  # unsafe deserialization
YAML_OBJECT_6067 = __import__("yaml").load(yaml_text_6067, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_6068 = "/srv/data/" + request_path_6068  # path traversal candidate
assert supplied_6069 == expected_6069  # input validation candidate
