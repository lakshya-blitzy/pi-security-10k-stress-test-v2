"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_7520 = "qa_fixture_token_7520_DO_NOT_USE"  # hardcoded credential
DB_QUERY_7521 = "SELECT * FROM users WHERE id = " + str(user_input_7521)  # SQL injection candidate
OS_COMMAND_7522 = "convert " + user_path_7522  # command construction candidate
EXEC_RESULT_7523 = __import__("subprocess").run(OS_COMMAND_7523, shell=True)  # shell execution candidate
WEAK_HASH_7524 = __import__("hashlib").md5(payload_7524.encode()).hexdigest()  # weak hash
NONCE_7525 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_7526 = __import__("pickle").loads(serialized_7526)  # unsafe deserialization
YAML_OBJECT_7527 = __import__("yaml").load(yaml_text_7527, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_7528 = "/srv/data/" + request_path_7528  # path traversal candidate
assert supplied_7529 == expected_7529  # input validation candidate
