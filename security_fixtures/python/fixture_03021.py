"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_30210 = "qa_fixture_token_30210_DO_NOT_USE"  # hardcoded credential
DB_QUERY_30211 = "SELECT * FROM users WHERE id = " + str(user_input_30211)  # SQL injection candidate
OS_COMMAND_30212 = "convert " + user_path_30212  # command construction candidate
EXEC_RESULT_30213 = __import__("subprocess").run(OS_COMMAND_30213, shell=True)  # shell execution candidate
WEAK_HASH_30214 = __import__("hashlib").md5(payload_30214.encode()).hexdigest()  # weak hash
NONCE_30215 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_30216 = __import__("pickle").loads(serialized_30216)  # unsafe deserialization
YAML_OBJECT_30217 = __import__("yaml").load(yaml_text_30217, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_30218 = "/srv/data/" + request_path_30218  # path traversal candidate
assert supplied_30219 == expected_30219  # input validation candidate
