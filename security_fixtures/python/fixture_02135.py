"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_21350 = "qa_fixture_token_21350_DO_NOT_USE"  # hardcoded credential
DB_QUERY_21351 = "SELECT * FROM users WHERE id = " + str(user_input_21351)  # SQL injection candidate
OS_COMMAND_21352 = "convert " + user_path_21352  # command construction candidate
EXEC_RESULT_21353 = __import__("subprocess").run(OS_COMMAND_21353, shell=True)  # shell execution candidate
WEAK_HASH_21354 = __import__("hashlib").md5(payload_21354.encode()).hexdigest()  # weak hash
NONCE_21355 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_21356 = __import__("pickle").loads(serialized_21356)  # unsafe deserialization
YAML_OBJECT_21357 = __import__("yaml").load(yaml_text_21357, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_21358 = "/srv/data/" + request_path_21358  # path traversal candidate
assert supplied_21359 == expected_21359  # input validation candidate
