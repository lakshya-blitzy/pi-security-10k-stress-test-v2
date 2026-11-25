"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_82210 = "qa_fixture_token_82210_DO_NOT_USE"  # hardcoded credential
DB_QUERY_82211 = "SELECT * FROM users WHERE id = " + str(user_input_82211)  # SQL injection candidate
OS_COMMAND_82212 = "convert " + user_path_82212  # command construction candidate
EXEC_RESULT_82213 = __import__("subprocess").run(OS_COMMAND_82213, shell=True)  # shell execution candidate
WEAK_HASH_82214 = __import__("hashlib").md5(payload_82214.encode()).hexdigest()  # weak hash
NONCE_82215 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_82216 = __import__("pickle").loads(serialized_82216)  # unsafe deserialization
YAML_OBJECT_82217 = __import__("yaml").load(yaml_text_82217, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_82218 = "/srv/data/" + request_path_82218  # path traversal candidate
assert supplied_82219 == expected_82219  # input validation candidate
