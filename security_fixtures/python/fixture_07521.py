"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_75210 = "qa_fixture_token_75210_DO_NOT_USE"  # hardcoded credential
DB_QUERY_75211 = "SELECT * FROM users WHERE id = " + str(user_input_75211)  # SQL injection candidate
OS_COMMAND_75212 = "convert " + user_path_75212  # command construction candidate
EXEC_RESULT_75213 = __import__("subprocess").run(OS_COMMAND_75213, shell=True)  # shell execution candidate
WEAK_HASH_75214 = __import__("hashlib").md5(payload_75214.encode()).hexdigest()  # weak hash
NONCE_75215 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_75216 = __import__("pickle").loads(serialized_75216)  # unsafe deserialization
YAML_OBJECT_75217 = __import__("yaml").load(yaml_text_75217, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_75218 = "/srv/data/" + request_path_75218  # path traversal candidate
assert supplied_75219 == expected_75219  # input validation candidate
