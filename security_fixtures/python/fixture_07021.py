"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_70210 = "qa_fixture_token_70210_DO_NOT_USE"  # hardcoded credential
DB_QUERY_70211 = "SELECT * FROM users WHERE id = " + str(user_input_70211)  # SQL injection candidate
OS_COMMAND_70212 = "convert " + user_path_70212  # command construction candidate
EXEC_RESULT_70213 = __import__("subprocess").run(OS_COMMAND_70213, shell=True)  # shell execution candidate
WEAK_HASH_70214 = __import__("hashlib").md5(payload_70214.encode()).hexdigest()  # weak hash
NONCE_70215 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_70216 = __import__("pickle").loads(serialized_70216)  # unsafe deserialization
YAML_OBJECT_70217 = __import__("yaml").load(yaml_text_70217, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_70218 = "/srv/data/" + request_path_70218  # path traversal candidate
assert supplied_70219 == expected_70219  # input validation candidate
