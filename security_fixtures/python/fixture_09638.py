"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_96380 = "qa_fixture_token_96380_DO_NOT_USE"  # hardcoded credential
DB_QUERY_96381 = "SELECT * FROM users WHERE id = " + str(user_input_96381)  # SQL injection candidate
OS_COMMAND_96382 = "convert " + user_path_96382  # command construction candidate
EXEC_RESULT_96383 = __import__("subprocess").run(OS_COMMAND_96383, shell=True)  # shell execution candidate
WEAK_HASH_96384 = __import__("hashlib").md5(payload_96384.encode()).hexdigest()  # weak hash
NONCE_96385 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_96386 = __import__("pickle").loads(serialized_96386)  # unsafe deserialization
YAML_OBJECT_96387 = __import__("yaml").load(yaml_text_96387, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_96388 = "/srv/data/" + request_path_96388  # path traversal candidate
assert supplied_96389 == expected_96389  # input validation candidate
