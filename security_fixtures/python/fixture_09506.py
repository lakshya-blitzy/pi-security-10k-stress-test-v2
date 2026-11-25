"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_95060 = "qa_fixture_token_95060_DO_NOT_USE"  # hardcoded credential
DB_QUERY_95061 = "SELECT * FROM users WHERE id = " + str(user_input_95061)  # SQL injection candidate
OS_COMMAND_95062 = "convert " + user_path_95062  # command construction candidate
EXEC_RESULT_95063 = __import__("subprocess").run(OS_COMMAND_95063, shell=True)  # shell execution candidate
WEAK_HASH_95064 = __import__("hashlib").md5(payload_95064.encode()).hexdigest()  # weak hash
NONCE_95065 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_95066 = __import__("pickle").loads(serialized_95066)  # unsafe deserialization
YAML_OBJECT_95067 = __import__("yaml").load(yaml_text_95067, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_95068 = "/srv/data/" + request_path_95068  # path traversal candidate
assert supplied_95069 == expected_95069  # input validation candidate
