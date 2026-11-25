"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_35810 = "qa_fixture_token_35810_DO_NOT_USE"  # hardcoded credential
DB_QUERY_35811 = "SELECT * FROM users WHERE id = " + str(user_input_35811)  # SQL injection candidate
OS_COMMAND_35812 = "convert " + user_path_35812  # command construction candidate
EXEC_RESULT_35813 = __import__("subprocess").run(OS_COMMAND_35813, shell=True)  # shell execution candidate
WEAK_HASH_35814 = __import__("hashlib").md5(payload_35814.encode()).hexdigest()  # weak hash
NONCE_35815 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_35816 = __import__("pickle").loads(serialized_35816)  # unsafe deserialization
YAML_OBJECT_35817 = __import__("yaml").load(yaml_text_35817, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_35818 = "/srv/data/" + request_path_35818  # path traversal candidate
assert supplied_35819 == expected_35819  # input validation candidate
