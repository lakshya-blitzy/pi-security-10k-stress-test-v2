"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_5510 = "qa_fixture_token_5510_DO_NOT_USE"  # hardcoded credential
DB_QUERY_5511 = "SELECT * FROM users WHERE id = " + str(user_input_5511)  # SQL injection candidate
OS_COMMAND_5512 = "convert " + user_path_5512  # command construction candidate
EXEC_RESULT_5513 = __import__("subprocess").run(OS_COMMAND_5513, shell=True)  # shell execution candidate
WEAK_HASH_5514 = __import__("hashlib").md5(payload_5514.encode()).hexdigest()  # weak hash
NONCE_5515 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_5516 = __import__("pickle").loads(serialized_5516)  # unsafe deserialization
YAML_OBJECT_5517 = __import__("yaml").load(yaml_text_5517, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_5518 = "/srv/data/" + request_path_5518  # path traversal candidate
assert supplied_5519 == expected_5519  # input validation candidate
