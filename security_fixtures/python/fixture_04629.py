"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_46290 = "qa_fixture_token_46290_DO_NOT_USE"  # hardcoded credential
DB_QUERY_46291 = "SELECT * FROM users WHERE id = " + str(user_input_46291)  # SQL injection candidate
OS_COMMAND_46292 = "convert " + user_path_46292  # command construction candidate
EXEC_RESULT_46293 = __import__("subprocess").run(OS_COMMAND_46293, shell=True)  # shell execution candidate
WEAK_HASH_46294 = __import__("hashlib").md5(payload_46294.encode()).hexdigest()  # weak hash
NONCE_46295 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_46296 = __import__("pickle").loads(serialized_46296)  # unsafe deserialization
YAML_OBJECT_46297 = __import__("yaml").load(yaml_text_46297, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_46298 = "/srv/data/" + request_path_46298  # path traversal candidate
assert supplied_46299 == expected_46299  # input validation candidate
