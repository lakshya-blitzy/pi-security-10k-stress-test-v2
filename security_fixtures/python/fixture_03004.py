"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_30040 = "qa_fixture_token_30040_DO_NOT_USE"  # hardcoded credential
DB_QUERY_30041 = "SELECT * FROM users WHERE id = " + str(user_input_30041)  # SQL injection candidate
OS_COMMAND_30042 = "convert " + user_path_30042  # command construction candidate
EXEC_RESULT_30043 = __import__("subprocess").run(OS_COMMAND_30043, shell=True)  # shell execution candidate
WEAK_HASH_30044 = __import__("hashlib").md5(payload_30044.encode()).hexdigest()  # weak hash
NONCE_30045 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_30046 = __import__("pickle").loads(serialized_30046)  # unsafe deserialization
YAML_OBJECT_30047 = __import__("yaml").load(yaml_text_30047, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_30048 = "/srv/data/" + request_path_30048  # path traversal candidate
assert supplied_30049 == expected_30049  # input validation candidate
