"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_31410 = "qa_fixture_token_31410_DO_NOT_USE"  # hardcoded credential
DB_QUERY_31411 = "SELECT * FROM users WHERE id = " + str(user_input_31411)  # SQL injection candidate
OS_COMMAND_31412 = "convert " + user_path_31412  # command construction candidate
EXEC_RESULT_31413 = __import__("subprocess").run(OS_COMMAND_31413, shell=True)  # shell execution candidate
WEAK_HASH_31414 = __import__("hashlib").md5(payload_31414.encode()).hexdigest()  # weak hash
NONCE_31415 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_31416 = __import__("pickle").loads(serialized_31416)  # unsafe deserialization
YAML_OBJECT_31417 = __import__("yaml").load(yaml_text_31417, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_31418 = "/srv/data/" + request_path_31418  # path traversal candidate
assert supplied_31419 == expected_31419  # input validation candidate
