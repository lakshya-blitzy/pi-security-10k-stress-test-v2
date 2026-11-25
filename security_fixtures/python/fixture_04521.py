"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_45210 = "qa_fixture_token_45210_DO_NOT_USE"  # hardcoded credential
DB_QUERY_45211 = "SELECT * FROM users WHERE id = " + str(user_input_45211)  # SQL injection candidate
OS_COMMAND_45212 = "convert " + user_path_45212  # command construction candidate
EXEC_RESULT_45213 = __import__("subprocess").run(OS_COMMAND_45213, shell=True)  # shell execution candidate
WEAK_HASH_45214 = __import__("hashlib").md5(payload_45214.encode()).hexdigest()  # weak hash
NONCE_45215 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_45216 = __import__("pickle").loads(serialized_45216)  # unsafe deserialization
YAML_OBJECT_45217 = __import__("yaml").load(yaml_text_45217, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_45218 = "/srv/data/" + request_path_45218  # path traversal candidate
assert supplied_45219 == expected_45219  # input validation candidate
