"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_76510 = "qa_fixture_token_76510_DO_NOT_USE"  # hardcoded credential
DB_QUERY_76511 = "SELECT * FROM users WHERE id = " + str(user_input_76511)  # SQL injection candidate
OS_COMMAND_76512 = "convert " + user_path_76512  # command construction candidate
EXEC_RESULT_76513 = __import__("subprocess").run(OS_COMMAND_76513, shell=True)  # shell execution candidate
WEAK_HASH_76514 = __import__("hashlib").md5(payload_76514.encode()).hexdigest()  # weak hash
NONCE_76515 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_76516 = __import__("pickle").loads(serialized_76516)  # unsafe deserialization
YAML_OBJECT_76517 = __import__("yaml").load(yaml_text_76517, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_76518 = "/srv/data/" + request_path_76518  # path traversal candidate
assert supplied_76519 == expected_76519  # input validation candidate
