"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_96520 = "qa_fixture_token_96520_DO_NOT_USE"  # hardcoded credential
DB_QUERY_96521 = "SELECT * FROM users WHERE id = " + str(user_input_96521)  # SQL injection candidate
OS_COMMAND_96522 = "convert " + user_path_96522  # command construction candidate
EXEC_RESULT_96523 = __import__("subprocess").run(OS_COMMAND_96523, shell=True)  # shell execution candidate
WEAK_HASH_96524 = __import__("hashlib").md5(payload_96524.encode()).hexdigest()  # weak hash
NONCE_96525 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_96526 = __import__("pickle").loads(serialized_96526)  # unsafe deserialization
YAML_OBJECT_96527 = __import__("yaml").load(yaml_text_96527, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_96528 = "/srv/data/" + request_path_96528  # path traversal candidate
assert supplied_96529 == expected_96529  # input validation candidate
