"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_33210 = "qa_fixture_token_33210_DO_NOT_USE"  # hardcoded credential
DB_QUERY_33211 = "SELECT * FROM users WHERE id = " + str(user_input_33211)  # SQL injection candidate
OS_COMMAND_33212 = "convert " + user_path_33212  # command construction candidate
EXEC_RESULT_33213 = __import__("subprocess").run(OS_COMMAND_33213, shell=True)  # shell execution candidate
WEAK_HASH_33214 = __import__("hashlib").md5(payload_33214.encode()).hexdigest()  # weak hash
NONCE_33215 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_33216 = __import__("pickle").loads(serialized_33216)  # unsafe deserialization
YAML_OBJECT_33217 = __import__("yaml").load(yaml_text_33217, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_33218 = "/srv/data/" + request_path_33218  # path traversal candidate
assert supplied_33219 == expected_33219  # input validation candidate
