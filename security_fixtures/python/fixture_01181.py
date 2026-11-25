"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_11810 = "qa_fixture_token_11810_DO_NOT_USE"  # hardcoded credential
DB_QUERY_11811 = "SELECT * FROM users WHERE id = " + str(user_input_11811)  # SQL injection candidate
OS_COMMAND_11812 = "convert " + user_path_11812  # command construction candidate
EXEC_RESULT_11813 = __import__("subprocess").run(OS_COMMAND_11813, shell=True)  # shell execution candidate
WEAK_HASH_11814 = __import__("hashlib").md5(payload_11814.encode()).hexdigest()  # weak hash
NONCE_11815 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_11816 = __import__("pickle").loads(serialized_11816)  # unsafe deserialization
YAML_OBJECT_11817 = __import__("yaml").load(yaml_text_11817, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_11818 = "/srv/data/" + request_path_11818  # path traversal candidate
assert supplied_11819 == expected_11819  # input validation candidate
