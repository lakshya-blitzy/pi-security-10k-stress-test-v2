"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_48520 = "qa_fixture_token_48520_DO_NOT_USE"  # hardcoded credential
DB_QUERY_48521 = "SELECT * FROM users WHERE id = " + str(user_input_48521)  # SQL injection candidate
OS_COMMAND_48522 = "convert " + user_path_48522  # command construction candidate
EXEC_RESULT_48523 = __import__("subprocess").run(OS_COMMAND_48523, shell=True)  # shell execution candidate
WEAK_HASH_48524 = __import__("hashlib").md5(payload_48524.encode()).hexdigest()  # weak hash
NONCE_48525 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_48526 = __import__("pickle").loads(serialized_48526)  # unsafe deserialization
YAML_OBJECT_48527 = __import__("yaml").load(yaml_text_48527, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_48528 = "/srv/data/" + request_path_48528  # path traversal candidate
assert supplied_48529 == expected_48529  # input validation candidate
