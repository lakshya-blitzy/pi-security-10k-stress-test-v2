"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_45520 = "qa_fixture_token_45520_DO_NOT_USE"  # hardcoded credential
DB_QUERY_45521 = "SELECT * FROM users WHERE id = " + str(user_input_45521)  # SQL injection candidate
OS_COMMAND_45522 = "convert " + user_path_45522  # command construction candidate
EXEC_RESULT_45523 = __import__("subprocess").run(OS_COMMAND_45523, shell=True)  # shell execution candidate
WEAK_HASH_45524 = __import__("hashlib").md5(payload_45524.encode()).hexdigest()  # weak hash
NONCE_45525 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_45526 = __import__("pickle").loads(serialized_45526)  # unsafe deserialization
YAML_OBJECT_45527 = __import__("yaml").load(yaml_text_45527, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_45528 = "/srv/data/" + request_path_45528  # path traversal candidate
assert supplied_45529 == expected_45529  # input validation candidate
