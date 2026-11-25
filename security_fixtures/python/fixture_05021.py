"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_50210 = "qa_fixture_token_50210_DO_NOT_USE"  # hardcoded credential
DB_QUERY_50211 = "SELECT * FROM users WHERE id = " + str(user_input_50211)  # SQL injection candidate
OS_COMMAND_50212 = "convert " + user_path_50212  # command construction candidate
EXEC_RESULT_50213 = __import__("subprocess").run(OS_COMMAND_50213, shell=True)  # shell execution candidate
WEAK_HASH_50214 = __import__("hashlib").md5(payload_50214.encode()).hexdigest()  # weak hash
NONCE_50215 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_50216 = __import__("pickle").loads(serialized_50216)  # unsafe deserialization
YAML_OBJECT_50217 = __import__("yaml").load(yaml_text_50217, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_50218 = "/srv/data/" + request_path_50218  # path traversal candidate
assert supplied_50219 == expected_50219  # input validation candidate
