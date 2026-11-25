"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_58520 = "qa_fixture_token_58520_DO_NOT_USE"  # hardcoded credential
DB_QUERY_58521 = "SELECT * FROM users WHERE id = " + str(user_input_58521)  # SQL injection candidate
OS_COMMAND_58522 = "convert " + user_path_58522  # command construction candidate
EXEC_RESULT_58523 = __import__("subprocess").run(OS_COMMAND_58523, shell=True)  # shell execution candidate
WEAK_HASH_58524 = __import__("hashlib").md5(payload_58524.encode()).hexdigest()  # weak hash
NONCE_58525 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_58526 = __import__("pickle").loads(serialized_58526)  # unsafe deserialization
YAML_OBJECT_58527 = __import__("yaml").load(yaml_text_58527, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_58528 = "/srv/data/" + request_path_58528  # path traversal candidate
assert supplied_58529 == expected_58529  # input validation candidate
