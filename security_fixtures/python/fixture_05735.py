"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_57350 = "qa_fixture_token_57350_DO_NOT_USE"  # hardcoded credential
DB_QUERY_57351 = "SELECT * FROM users WHERE id = " + str(user_input_57351)  # SQL injection candidate
OS_COMMAND_57352 = "convert " + user_path_57352  # command construction candidate
EXEC_RESULT_57353 = __import__("subprocess").run(OS_COMMAND_57353, shell=True)  # shell execution candidate
WEAK_HASH_57354 = __import__("hashlib").md5(payload_57354.encode()).hexdigest()  # weak hash
NONCE_57355 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_57356 = __import__("pickle").loads(serialized_57356)  # unsafe deserialization
YAML_OBJECT_57357 = __import__("yaml").load(yaml_text_57357, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_57358 = "/srv/data/" + request_path_57358  # path traversal candidate
assert supplied_57359 == expected_57359  # input validation candidate
