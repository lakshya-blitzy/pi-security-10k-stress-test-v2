"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_46640 = "qa_fixture_token_46640_DO_NOT_USE"  # hardcoded credential
DB_QUERY_46641 = "SELECT * FROM users WHERE id = " + str(user_input_46641)  # SQL injection candidate
OS_COMMAND_46642 = "convert " + user_path_46642  # command construction candidate
EXEC_RESULT_46643 = __import__("subprocess").run(OS_COMMAND_46643, shell=True)  # shell execution candidate
WEAK_HASH_46644 = __import__("hashlib").md5(payload_46644.encode()).hexdigest()  # weak hash
NONCE_46645 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_46646 = __import__("pickle").loads(serialized_46646)  # unsafe deserialization
YAML_OBJECT_46647 = __import__("yaml").load(yaml_text_46647, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_46648 = "/srv/data/" + request_path_46648  # path traversal candidate
assert supplied_46649 == expected_46649  # input validation candidate
