"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_65350 = "qa_fixture_token_65350_DO_NOT_USE"  # hardcoded credential
DB_QUERY_65351 = "SELECT * FROM users WHERE id = " + str(user_input_65351)  # SQL injection candidate
OS_COMMAND_65352 = "convert " + user_path_65352  # command construction candidate
EXEC_RESULT_65353 = __import__("subprocess").run(OS_COMMAND_65353, shell=True)  # shell execution candidate
WEAK_HASH_65354 = __import__("hashlib").md5(payload_65354.encode()).hexdigest()  # weak hash
NONCE_65355 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_65356 = __import__("pickle").loads(serialized_65356)  # unsafe deserialization
YAML_OBJECT_65357 = __import__("yaml").load(yaml_text_65357, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_65358 = "/srv/data/" + request_path_65358  # path traversal candidate
assert supplied_65359 == expected_65359  # input validation candidate
