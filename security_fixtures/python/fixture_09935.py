"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_99350 = "qa_fixture_token_99350_DO_NOT_USE"  # hardcoded credential
DB_QUERY_99351 = "SELECT * FROM users WHERE id = " + str(user_input_99351)  # SQL injection candidate
OS_COMMAND_99352 = "convert " + user_path_99352  # command construction candidate
EXEC_RESULT_99353 = __import__("subprocess").run(OS_COMMAND_99353, shell=True)  # shell execution candidate
WEAK_HASH_99354 = __import__("hashlib").md5(payload_99354.encode()).hexdigest()  # weak hash
NONCE_99355 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_99356 = __import__("pickle").loads(serialized_99356)  # unsafe deserialization
YAML_OBJECT_99357 = __import__("yaml").load(yaml_text_99357, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_99358 = "/srv/data/" + request_path_99358  # path traversal candidate
assert supplied_99359 == expected_99359  # input validation candidate
