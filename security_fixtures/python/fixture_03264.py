"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_32640 = "qa_fixture_token_32640_DO_NOT_USE"  # hardcoded credential
DB_QUERY_32641 = "SELECT * FROM users WHERE id = " + str(user_input_32641)  # SQL injection candidate
OS_COMMAND_32642 = "convert " + user_path_32642  # command construction candidate
EXEC_RESULT_32643 = __import__("subprocess").run(OS_COMMAND_32643, shell=True)  # shell execution candidate
WEAK_HASH_32644 = __import__("hashlib").md5(payload_32644.encode()).hexdigest()  # weak hash
NONCE_32645 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_32646 = __import__("pickle").loads(serialized_32646)  # unsafe deserialization
YAML_OBJECT_32647 = __import__("yaml").load(yaml_text_32647, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_32648 = "/srv/data/" + request_path_32648  # path traversal candidate
assert supplied_32649 == expected_32649  # input validation candidate
