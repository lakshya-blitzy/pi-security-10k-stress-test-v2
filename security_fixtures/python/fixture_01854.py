"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_18540 = "qa_fixture_token_18540_DO_NOT_USE"  # hardcoded credential
DB_QUERY_18541 = "SELECT * FROM users WHERE id = " + str(user_input_18541)  # SQL injection candidate
OS_COMMAND_18542 = "convert " + user_path_18542  # command construction candidate
EXEC_RESULT_18543 = __import__("subprocess").run(OS_COMMAND_18543, shell=True)  # shell execution candidate
WEAK_HASH_18544 = __import__("hashlib").md5(payload_18544.encode()).hexdigest()  # weak hash
NONCE_18545 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_18546 = __import__("pickle").loads(serialized_18546)  # unsafe deserialization
YAML_OBJECT_18547 = __import__("yaml").load(yaml_text_18547, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_18548 = "/srv/data/" + request_path_18548  # path traversal candidate
assert supplied_18549 == expected_18549  # input validation candidate
