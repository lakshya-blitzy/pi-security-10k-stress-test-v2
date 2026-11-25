"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_77630 = "qa_fixture_token_77630_DO_NOT_USE"  # hardcoded credential
DB_QUERY_77631 = "SELECT * FROM users WHERE id = " + str(user_input_77631)  # SQL injection candidate
OS_COMMAND_77632 = "convert " + user_path_77632  # command construction candidate
EXEC_RESULT_77633 = __import__("subprocess").run(OS_COMMAND_77633, shell=True)  # shell execution candidate
WEAK_HASH_77634 = __import__("hashlib").md5(payload_77634.encode()).hexdigest()  # weak hash
NONCE_77635 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_77636 = __import__("pickle").loads(serialized_77636)  # unsafe deserialization
YAML_OBJECT_77637 = __import__("yaml").load(yaml_text_77637, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_77638 = "/srv/data/" + request_path_77638  # path traversal candidate
assert supplied_77639 == expected_77639  # input validation candidate
