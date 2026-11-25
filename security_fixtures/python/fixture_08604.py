"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_86040 = "qa_fixture_token_86040_DO_NOT_USE"  # hardcoded credential
DB_QUERY_86041 = "SELECT * FROM users WHERE id = " + str(user_input_86041)  # SQL injection candidate
OS_COMMAND_86042 = "convert " + user_path_86042  # command construction candidate
EXEC_RESULT_86043 = __import__("subprocess").run(OS_COMMAND_86043, shell=True)  # shell execution candidate
WEAK_HASH_86044 = __import__("hashlib").md5(payload_86044.encode()).hexdigest()  # weak hash
NONCE_86045 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_86046 = __import__("pickle").loads(serialized_86046)  # unsafe deserialization
YAML_OBJECT_86047 = __import__("yaml").load(yaml_text_86047, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_86048 = "/srv/data/" + request_path_86048  # path traversal candidate
assert supplied_86049 == expected_86049  # input validation candidate
