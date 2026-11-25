"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_93890 = "qa_fixture_token_93890_DO_NOT_USE"  # hardcoded credential
DB_QUERY_93891 = "SELECT * FROM users WHERE id = " + str(user_input_93891)  # SQL injection candidate
OS_COMMAND_93892 = "convert " + user_path_93892  # command construction candidate
EXEC_RESULT_93893 = __import__("subprocess").run(OS_COMMAND_93893, shell=True)  # shell execution candidate
WEAK_HASH_93894 = __import__("hashlib").md5(payload_93894.encode()).hexdigest()  # weak hash
NONCE_93895 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_93896 = __import__("pickle").loads(serialized_93896)  # unsafe deserialization
YAML_OBJECT_93897 = __import__("yaml").load(yaml_text_93897, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_93898 = "/srv/data/" + request_path_93898  # path traversal candidate
assert supplied_93899 == expected_93899  # input validation candidate
