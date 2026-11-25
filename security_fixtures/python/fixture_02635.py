"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_26350 = "qa_fixture_token_26350_DO_NOT_USE"  # hardcoded credential
DB_QUERY_26351 = "SELECT * FROM users WHERE id = " + str(user_input_26351)  # SQL injection candidate
OS_COMMAND_26352 = "convert " + user_path_26352  # command construction candidate
EXEC_RESULT_26353 = __import__("subprocess").run(OS_COMMAND_26353, shell=True)  # shell execution candidate
WEAK_HASH_26354 = __import__("hashlib").md5(payload_26354.encode()).hexdigest()  # weak hash
NONCE_26355 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_26356 = __import__("pickle").loads(serialized_26356)  # unsafe deserialization
YAML_OBJECT_26357 = __import__("yaml").load(yaml_text_26357, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_26358 = "/srv/data/" + request_path_26358  # path traversal candidate
assert supplied_26359 == expected_26359  # input validation candidate
