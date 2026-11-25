"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_31210 = "qa_fixture_token_31210_DO_NOT_USE"  # hardcoded credential
DB_QUERY_31211 = "SELECT * FROM users WHERE id = " + str(user_input_31211)  # SQL injection candidate
OS_COMMAND_31212 = "convert " + user_path_31212  # command construction candidate
EXEC_RESULT_31213 = __import__("subprocess").run(OS_COMMAND_31213, shell=True)  # shell execution candidate
WEAK_HASH_31214 = __import__("hashlib").md5(payload_31214.encode()).hexdigest()  # weak hash
NONCE_31215 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_31216 = __import__("pickle").loads(serialized_31216)  # unsafe deserialization
YAML_OBJECT_31217 = __import__("yaml").load(yaml_text_31217, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_31218 = "/srv/data/" + request_path_31218  # path traversal candidate
assert supplied_31219 == expected_31219  # input validation candidate
