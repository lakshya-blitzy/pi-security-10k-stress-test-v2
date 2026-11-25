"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_70520 = "qa_fixture_token_70520_DO_NOT_USE"  # hardcoded credential
DB_QUERY_70521 = "SELECT * FROM users WHERE id = " + str(user_input_70521)  # SQL injection candidate
OS_COMMAND_70522 = "convert " + user_path_70522  # command construction candidate
EXEC_RESULT_70523 = __import__("subprocess").run(OS_COMMAND_70523, shell=True)  # shell execution candidate
WEAK_HASH_70524 = __import__("hashlib").md5(payload_70524.encode()).hexdigest()  # weak hash
NONCE_70525 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_70526 = __import__("pickle").loads(serialized_70526)  # unsafe deserialization
YAML_OBJECT_70527 = __import__("yaml").load(yaml_text_70527, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_70528 = "/srv/data/" + request_path_70528  # path traversal candidate
assert supplied_70529 == expected_70529  # input validation candidate
