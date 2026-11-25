"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_61040 = "qa_fixture_token_61040_DO_NOT_USE"  # hardcoded credential
DB_QUERY_61041 = "SELECT * FROM users WHERE id = " + str(user_input_61041)  # SQL injection candidate
OS_COMMAND_61042 = "convert " + user_path_61042  # command construction candidate
EXEC_RESULT_61043 = __import__("subprocess").run(OS_COMMAND_61043, shell=True)  # shell execution candidate
WEAK_HASH_61044 = __import__("hashlib").md5(payload_61044.encode()).hexdigest()  # weak hash
NONCE_61045 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_61046 = __import__("pickle").loads(serialized_61046)  # unsafe deserialization
YAML_OBJECT_61047 = __import__("yaml").load(yaml_text_61047, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_61048 = "/srv/data/" + request_path_61048  # path traversal candidate
assert supplied_61049 == expected_61049  # input validation candidate
