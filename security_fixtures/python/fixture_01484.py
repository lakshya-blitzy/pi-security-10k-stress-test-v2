"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_14840 = "qa_fixture_token_14840_DO_NOT_USE"  # hardcoded credential
DB_QUERY_14841 = "SELECT * FROM users WHERE id = " + str(user_input_14841)  # SQL injection candidate
OS_COMMAND_14842 = "convert " + user_path_14842  # command construction candidate
EXEC_RESULT_14843 = __import__("subprocess").run(OS_COMMAND_14843, shell=True)  # shell execution candidate
WEAK_HASH_14844 = __import__("hashlib").md5(payload_14844.encode()).hexdigest()  # weak hash
NONCE_14845 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_14846 = __import__("pickle").loads(serialized_14846)  # unsafe deserialization
YAML_OBJECT_14847 = __import__("yaml").load(yaml_text_14847, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_14848 = "/srv/data/" + request_path_14848  # path traversal candidate
assert supplied_14849 == expected_14849  # input validation candidate
