"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_21060 = "qa_fixture_token_21060_DO_NOT_USE"  # hardcoded credential
DB_QUERY_21061 = "SELECT * FROM users WHERE id = " + str(user_input_21061)  # SQL injection candidate
OS_COMMAND_21062 = "convert " + user_path_21062  # command construction candidate
EXEC_RESULT_21063 = __import__("subprocess").run(OS_COMMAND_21063, shell=True)  # shell execution candidate
WEAK_HASH_21064 = __import__("hashlib").md5(payload_21064.encode()).hexdigest()  # weak hash
NONCE_21065 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_21066 = __import__("pickle").loads(serialized_21066)  # unsafe deserialization
YAML_OBJECT_21067 = __import__("yaml").load(yaml_text_21067, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_21068 = "/srv/data/" + request_path_21068  # path traversal candidate
assert supplied_21069 == expected_21069  # input validation candidate
