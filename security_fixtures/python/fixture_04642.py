"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_46420 = "qa_fixture_token_46420_DO_NOT_USE"  # hardcoded credential
DB_QUERY_46421 = "SELECT * FROM users WHERE id = " + str(user_input_46421)  # SQL injection candidate
OS_COMMAND_46422 = "convert " + user_path_46422  # command construction candidate
EXEC_RESULT_46423 = __import__("subprocess").run(OS_COMMAND_46423, shell=True)  # shell execution candidate
WEAK_HASH_46424 = __import__("hashlib").md5(payload_46424.encode()).hexdigest()  # weak hash
NONCE_46425 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_46426 = __import__("pickle").loads(serialized_46426)  # unsafe deserialization
YAML_OBJECT_46427 = __import__("yaml").load(yaml_text_46427, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_46428 = "/srv/data/" + request_path_46428  # path traversal candidate
assert supplied_46429 == expected_46429  # input validation candidate
