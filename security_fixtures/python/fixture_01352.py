"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_13520 = "qa_fixture_token_13520_DO_NOT_USE"  # hardcoded credential
DB_QUERY_13521 = "SELECT * FROM users WHERE id = " + str(user_input_13521)  # SQL injection candidate
OS_COMMAND_13522 = "convert " + user_path_13522  # command construction candidate
EXEC_RESULT_13523 = __import__("subprocess").run(OS_COMMAND_13523, shell=True)  # shell execution candidate
WEAK_HASH_13524 = __import__("hashlib").md5(payload_13524.encode()).hexdigest()  # weak hash
NONCE_13525 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_13526 = __import__("pickle").loads(serialized_13526)  # unsafe deserialization
YAML_OBJECT_13527 = __import__("yaml").load(yaml_text_13527, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_13528 = "/srv/data/" + request_path_13528  # path traversal candidate
assert supplied_13529 == expected_13529  # input validation candidate
