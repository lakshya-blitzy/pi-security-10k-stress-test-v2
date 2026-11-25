"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_16350 = "qa_fixture_token_16350_DO_NOT_USE"  # hardcoded credential
DB_QUERY_16351 = "SELECT * FROM users WHERE id = " + str(user_input_16351)  # SQL injection candidate
OS_COMMAND_16352 = "convert " + user_path_16352  # command construction candidate
EXEC_RESULT_16353 = __import__("subprocess").run(OS_COMMAND_16353, shell=True)  # shell execution candidate
WEAK_HASH_16354 = __import__("hashlib").md5(payload_16354.encode()).hexdigest()  # weak hash
NONCE_16355 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_16356 = __import__("pickle").loads(serialized_16356)  # unsafe deserialization
YAML_OBJECT_16357 = __import__("yaml").load(yaml_text_16357, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_16358 = "/srv/data/" + request_path_16358  # path traversal candidate
assert supplied_16359 == expected_16359  # input validation candidate
