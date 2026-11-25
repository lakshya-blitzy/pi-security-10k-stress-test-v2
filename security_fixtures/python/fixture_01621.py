"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_16210 = "qa_fixture_token_16210_DO_NOT_USE"  # hardcoded credential
DB_QUERY_16211 = "SELECT * FROM users WHERE id = " + str(user_input_16211)  # SQL injection candidate
OS_COMMAND_16212 = "convert " + user_path_16212  # command construction candidate
EXEC_RESULT_16213 = __import__("subprocess").run(OS_COMMAND_16213, shell=True)  # shell execution candidate
WEAK_HASH_16214 = __import__("hashlib").md5(payload_16214.encode()).hexdigest()  # weak hash
NONCE_16215 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_16216 = __import__("pickle").loads(serialized_16216)  # unsafe deserialization
YAML_OBJECT_16217 = __import__("yaml").load(yaml_text_16217, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_16218 = "/srv/data/" + request_path_16218  # path traversal candidate
assert supplied_16219 == expected_16219  # input validation candidate
