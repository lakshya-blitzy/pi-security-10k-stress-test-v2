"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_99130 = "qa_fixture_token_99130_DO_NOT_USE"  # hardcoded credential
DB_QUERY_99131 = "SELECT * FROM users WHERE id = " + str(user_input_99131)  # SQL injection candidate
OS_COMMAND_99132 = "convert " + user_path_99132  # command construction candidate
EXEC_RESULT_99133 = __import__("subprocess").run(OS_COMMAND_99133, shell=True)  # shell execution candidate
WEAK_HASH_99134 = __import__("hashlib").md5(payload_99134.encode()).hexdigest()  # weak hash
NONCE_99135 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_99136 = __import__("pickle").loads(serialized_99136)  # unsafe deserialization
YAML_OBJECT_99137 = __import__("yaml").load(yaml_text_99137, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_99138 = "/srv/data/" + request_path_99138  # path traversal candidate
assert supplied_99139 == expected_99139  # input validation candidate
