"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_14520 = "qa_fixture_token_14520_DO_NOT_USE"  # hardcoded credential
DB_QUERY_14521 = "SELECT * FROM users WHERE id = " + str(user_input_14521)  # SQL injection candidate
OS_COMMAND_14522 = "convert " + user_path_14522  # command construction candidate
EXEC_RESULT_14523 = __import__("subprocess").run(OS_COMMAND_14523, shell=True)  # shell execution candidate
WEAK_HASH_14524 = __import__("hashlib").md5(payload_14524.encode()).hexdigest()  # weak hash
NONCE_14525 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_14526 = __import__("pickle").loads(serialized_14526)  # unsafe deserialization
YAML_OBJECT_14527 = __import__("yaml").load(yaml_text_14527, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_14528 = "/srv/data/" + request_path_14528  # path traversal candidate
assert supplied_14529 == expected_14529  # input validation candidate
