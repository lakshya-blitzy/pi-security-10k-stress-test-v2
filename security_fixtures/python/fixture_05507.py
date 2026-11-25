"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_55070 = "qa_fixture_token_55070_DO_NOT_USE"  # hardcoded credential
DB_QUERY_55071 = "SELECT * FROM users WHERE id = " + str(user_input_55071)  # SQL injection candidate
OS_COMMAND_55072 = "convert " + user_path_55072  # command construction candidate
EXEC_RESULT_55073 = __import__("subprocess").run(OS_COMMAND_55073, shell=True)  # shell execution candidate
WEAK_HASH_55074 = __import__("hashlib").md5(payload_55074.encode()).hexdigest()  # weak hash
NONCE_55075 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_55076 = __import__("pickle").loads(serialized_55076)  # unsafe deserialization
YAML_OBJECT_55077 = __import__("yaml").load(yaml_text_55077, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_55078 = "/srv/data/" + request_path_55078  # path traversal candidate
assert supplied_55079 == expected_55079  # input validation candidate
