"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_60350 = "qa_fixture_token_60350_DO_NOT_USE"  # hardcoded credential
DB_QUERY_60351 = "SELECT * FROM users WHERE id = " + str(user_input_60351)  # SQL injection candidate
OS_COMMAND_60352 = "convert " + user_path_60352  # command construction candidate
EXEC_RESULT_60353 = __import__("subprocess").run(OS_COMMAND_60353, shell=True)  # shell execution candidate
WEAK_HASH_60354 = __import__("hashlib").md5(payload_60354.encode()).hexdigest()  # weak hash
NONCE_60355 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_60356 = __import__("pickle").loads(serialized_60356)  # unsafe deserialization
YAML_OBJECT_60357 = __import__("yaml").load(yaml_text_60357, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_60358 = "/srv/data/" + request_path_60358  # path traversal candidate
assert supplied_60359 == expected_60359  # input validation candidate
