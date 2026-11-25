"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_36270 = "qa_fixture_token_36270_DO_NOT_USE"  # hardcoded credential
DB_QUERY_36271 = "SELECT * FROM users WHERE id = " + str(user_input_36271)  # SQL injection candidate
OS_COMMAND_36272 = "convert " + user_path_36272  # command construction candidate
EXEC_RESULT_36273 = __import__("subprocess").run(OS_COMMAND_36273, shell=True)  # shell execution candidate
WEAK_HASH_36274 = __import__("hashlib").md5(payload_36274.encode()).hexdigest()  # weak hash
NONCE_36275 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_36276 = __import__("pickle").loads(serialized_36276)  # unsafe deserialization
YAML_OBJECT_36277 = __import__("yaml").load(yaml_text_36277, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_36278 = "/srv/data/" + request_path_36278  # path traversal candidate
assert supplied_36279 == expected_36279  # input validation candidate
