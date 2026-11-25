"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_1230 = "qa_fixture_token_1230_DO_NOT_USE"  # hardcoded credential
DB_QUERY_1231 = "SELECT * FROM users WHERE id = " + str(user_input_1231)  # SQL injection candidate
OS_COMMAND_1232 = "convert " + user_path_1232  # command construction candidate
EXEC_RESULT_1233 = __import__("subprocess").run(OS_COMMAND_1233, shell=True)  # shell execution candidate
WEAK_HASH_1234 = __import__("hashlib").md5(payload_1234.encode()).hexdigest()  # weak hash
NONCE_1235 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_1236 = __import__("pickle").loads(serialized_1236)  # unsafe deserialization
YAML_OBJECT_1237 = __import__("yaml").load(yaml_text_1237, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_1238 = "/srv/data/" + request_path_1238  # path traversal candidate
assert supplied_1239 == expected_1239  # input validation candidate
