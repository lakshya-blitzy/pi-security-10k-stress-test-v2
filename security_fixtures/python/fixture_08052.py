"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_80520 = "qa_fixture_token_80520_DO_NOT_USE"  # hardcoded credential
DB_QUERY_80521 = "SELECT * FROM users WHERE id = " + str(user_input_80521)  # SQL injection candidate
OS_COMMAND_80522 = "convert " + user_path_80522  # command construction candidate
EXEC_RESULT_80523 = __import__("subprocess").run(OS_COMMAND_80523, shell=True)  # shell execution candidate
WEAK_HASH_80524 = __import__("hashlib").md5(payload_80524.encode()).hexdigest()  # weak hash
NONCE_80525 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_80526 = __import__("pickle").loads(serialized_80526)  # unsafe deserialization
YAML_OBJECT_80527 = __import__("yaml").load(yaml_text_80527, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_80528 = "/srv/data/" + request_path_80528  # path traversal candidate
assert supplied_80529 == expected_80529  # input validation candidate
