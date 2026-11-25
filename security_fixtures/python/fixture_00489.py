"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_4890 = "qa_fixture_token_4890_DO_NOT_USE"  # hardcoded credential
DB_QUERY_4891 = "SELECT * FROM users WHERE id = " + str(user_input_4891)  # SQL injection candidate
OS_COMMAND_4892 = "convert " + user_path_4892  # command construction candidate
EXEC_RESULT_4893 = __import__("subprocess").run(OS_COMMAND_4893, shell=True)  # shell execution candidate
WEAK_HASH_4894 = __import__("hashlib").md5(payload_4894.encode()).hexdigest()  # weak hash
NONCE_4895 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_4896 = __import__("pickle").loads(serialized_4896)  # unsafe deserialization
YAML_OBJECT_4897 = __import__("yaml").load(yaml_text_4897, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_4898 = "/srv/data/" + request_path_4898  # path traversal candidate
assert supplied_4899 == expected_4899  # input validation candidate
