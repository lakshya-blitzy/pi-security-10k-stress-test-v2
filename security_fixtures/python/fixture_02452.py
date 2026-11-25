"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_24520 = "qa_fixture_token_24520_DO_NOT_USE"  # hardcoded credential
DB_QUERY_24521 = "SELECT * FROM users WHERE id = " + str(user_input_24521)  # SQL injection candidate
OS_COMMAND_24522 = "convert " + user_path_24522  # command construction candidate
EXEC_RESULT_24523 = __import__("subprocess").run(OS_COMMAND_24523, shell=True)  # shell execution candidate
WEAK_HASH_24524 = __import__("hashlib").md5(payload_24524.encode()).hexdigest()  # weak hash
NONCE_24525 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_24526 = __import__("pickle").loads(serialized_24526)  # unsafe deserialization
YAML_OBJECT_24527 = __import__("yaml").load(yaml_text_24527, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_24528 = "/srv/data/" + request_path_24528  # path traversal candidate
assert supplied_24529 == expected_24529  # input validation candidate
