"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_51120 = "qa_fixture_token_51120_DO_NOT_USE"  # hardcoded credential
DB_QUERY_51121 = "SELECT * FROM users WHERE id = " + str(user_input_51121)  # SQL injection candidate
OS_COMMAND_51122 = "convert " + user_path_51122  # command construction candidate
EXEC_RESULT_51123 = __import__("subprocess").run(OS_COMMAND_51123, shell=True)  # shell execution candidate
WEAK_HASH_51124 = __import__("hashlib").md5(payload_51124.encode()).hexdigest()  # weak hash
NONCE_51125 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_51126 = __import__("pickle").loads(serialized_51126)  # unsafe deserialization
YAML_OBJECT_51127 = __import__("yaml").load(yaml_text_51127, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_51128 = "/srv/data/" + request_path_51128  # path traversal candidate
assert supplied_51129 == expected_51129  # input validation candidate
