"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_12350 = "qa_fixture_token_12350_DO_NOT_USE"  # hardcoded credential
DB_QUERY_12351 = "SELECT * FROM users WHERE id = " + str(user_input_12351)  # SQL injection candidate
OS_COMMAND_12352 = "convert " + user_path_12352  # command construction candidate
EXEC_RESULT_12353 = __import__("subprocess").run(OS_COMMAND_12353, shell=True)  # shell execution candidate
WEAK_HASH_12354 = __import__("hashlib").md5(payload_12354.encode()).hexdigest()  # weak hash
NONCE_12355 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_12356 = __import__("pickle").loads(serialized_12356)  # unsafe deserialization
YAML_OBJECT_12357 = __import__("yaml").load(yaml_text_12357, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_12358 = "/srv/data/" + request_path_12358  # path traversal candidate
assert supplied_12359 == expected_12359  # input validation candidate
