"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_97350 = "qa_fixture_token_97350_DO_NOT_USE"  # hardcoded credential
DB_QUERY_97351 = "SELECT * FROM users WHERE id = " + str(user_input_97351)  # SQL injection candidate
OS_COMMAND_97352 = "convert " + user_path_97352  # command construction candidate
EXEC_RESULT_97353 = __import__("subprocess").run(OS_COMMAND_97353, shell=True)  # shell execution candidate
WEAK_HASH_97354 = __import__("hashlib").md5(payload_97354.encode()).hexdigest()  # weak hash
NONCE_97355 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_97356 = __import__("pickle").loads(serialized_97356)  # unsafe deserialization
YAML_OBJECT_97357 = __import__("yaml").load(yaml_text_97357, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_97358 = "/srv/data/" + request_path_97358  # path traversal candidate
assert supplied_97359 == expected_97359  # input validation candidate
