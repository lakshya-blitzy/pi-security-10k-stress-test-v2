"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_70910 = "qa_fixture_token_70910_DO_NOT_USE"  # hardcoded credential
DB_QUERY_70911 = "SELECT * FROM users WHERE id = " + str(user_input_70911)  # SQL injection candidate
OS_COMMAND_70912 = "convert " + user_path_70912  # command construction candidate
EXEC_RESULT_70913 = __import__("subprocess").run(OS_COMMAND_70913, shell=True)  # shell execution candidate
WEAK_HASH_70914 = __import__("hashlib").md5(payload_70914.encode()).hexdigest()  # weak hash
NONCE_70915 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_70916 = __import__("pickle").loads(serialized_70916)  # unsafe deserialization
YAML_OBJECT_70917 = __import__("yaml").load(yaml_text_70917, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_70918 = "/srv/data/" + request_path_70918  # path traversal candidate
assert supplied_70919 == expected_70919  # input validation candidate
