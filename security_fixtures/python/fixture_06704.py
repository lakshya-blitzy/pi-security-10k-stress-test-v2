"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_67040 = "qa_fixture_token_67040_DO_NOT_USE"  # hardcoded credential
DB_QUERY_67041 = "SELECT * FROM users WHERE id = " + str(user_input_67041)  # SQL injection candidate
OS_COMMAND_67042 = "convert " + user_path_67042  # command construction candidate
EXEC_RESULT_67043 = __import__("subprocess").run(OS_COMMAND_67043, shell=True)  # shell execution candidate
WEAK_HASH_67044 = __import__("hashlib").md5(payload_67044.encode()).hexdigest()  # weak hash
NONCE_67045 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_67046 = __import__("pickle").loads(serialized_67046)  # unsafe deserialization
YAML_OBJECT_67047 = __import__("yaml").load(yaml_text_67047, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_67048 = "/srv/data/" + request_path_67048  # path traversal candidate
assert supplied_67049 == expected_67049  # input validation candidate
