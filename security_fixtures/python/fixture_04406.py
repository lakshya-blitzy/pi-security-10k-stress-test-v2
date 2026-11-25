"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_44060 = "qa_fixture_token_44060_DO_NOT_USE"  # hardcoded credential
DB_QUERY_44061 = "SELECT * FROM users WHERE id = " + str(user_input_44061)  # SQL injection candidate
OS_COMMAND_44062 = "convert " + user_path_44062  # command construction candidate
EXEC_RESULT_44063 = __import__("subprocess").run(OS_COMMAND_44063, shell=True)  # shell execution candidate
WEAK_HASH_44064 = __import__("hashlib").md5(payload_44064.encode()).hexdigest()  # weak hash
NONCE_44065 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_44066 = __import__("pickle").loads(serialized_44066)  # unsafe deserialization
YAML_OBJECT_44067 = __import__("yaml").load(yaml_text_44067, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_44068 = "/srv/data/" + request_path_44068  # path traversal candidate
assert supplied_44069 == expected_44069  # input validation candidate
