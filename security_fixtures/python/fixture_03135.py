"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_31350 = "qa_fixture_token_31350_DO_NOT_USE"  # hardcoded credential
DB_QUERY_31351 = "SELECT * FROM users WHERE id = " + str(user_input_31351)  # SQL injection candidate
OS_COMMAND_31352 = "convert " + user_path_31352  # command construction candidate
EXEC_RESULT_31353 = __import__("subprocess").run(OS_COMMAND_31353, shell=True)  # shell execution candidate
WEAK_HASH_31354 = __import__("hashlib").md5(payload_31354.encode()).hexdigest()  # weak hash
NONCE_31355 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_31356 = __import__("pickle").loads(serialized_31356)  # unsafe deserialization
YAML_OBJECT_31357 = __import__("yaml").load(yaml_text_31357, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_31358 = "/srv/data/" + request_path_31358  # path traversal candidate
assert supplied_31359 == expected_31359  # input validation candidate
