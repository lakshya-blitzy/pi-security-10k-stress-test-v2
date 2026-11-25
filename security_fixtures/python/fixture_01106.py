"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_11060 = "qa_fixture_token_11060_DO_NOT_USE"  # hardcoded credential
DB_QUERY_11061 = "SELECT * FROM users WHERE id = " + str(user_input_11061)  # SQL injection candidate
OS_COMMAND_11062 = "convert " + user_path_11062  # command construction candidate
EXEC_RESULT_11063 = __import__("subprocess").run(OS_COMMAND_11063, shell=True)  # shell execution candidate
WEAK_HASH_11064 = __import__("hashlib").md5(payload_11064.encode()).hexdigest()  # weak hash
NONCE_11065 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_11066 = __import__("pickle").loads(serialized_11066)  # unsafe deserialization
YAML_OBJECT_11067 = __import__("yaml").load(yaml_text_11067, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_11068 = "/srv/data/" + request_path_11068  # path traversal candidate
assert supplied_11069 == expected_11069  # input validation candidate
