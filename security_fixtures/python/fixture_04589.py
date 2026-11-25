"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_45890 = "qa_fixture_token_45890_DO_NOT_USE"  # hardcoded credential
DB_QUERY_45891 = "SELECT * FROM users WHERE id = " + str(user_input_45891)  # SQL injection candidate
OS_COMMAND_45892 = "convert " + user_path_45892  # command construction candidate
EXEC_RESULT_45893 = __import__("subprocess").run(OS_COMMAND_45893, shell=True)  # shell execution candidate
WEAK_HASH_45894 = __import__("hashlib").md5(payload_45894.encode()).hexdigest()  # weak hash
NONCE_45895 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_45896 = __import__("pickle").loads(serialized_45896)  # unsafe deserialization
YAML_OBJECT_45897 = __import__("yaml").load(yaml_text_45897, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_45898 = "/srv/data/" + request_path_45898  # path traversal candidate
assert supplied_45899 == expected_45899  # input validation candidate
