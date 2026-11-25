"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_77890 = "qa_fixture_token_77890_DO_NOT_USE"  # hardcoded credential
DB_QUERY_77891 = "SELECT * FROM users WHERE id = " + str(user_input_77891)  # SQL injection candidate
OS_COMMAND_77892 = "convert " + user_path_77892  # command construction candidate
EXEC_RESULT_77893 = __import__("subprocess").run(OS_COMMAND_77893, shell=True)  # shell execution candidate
WEAK_HASH_77894 = __import__("hashlib").md5(payload_77894.encode()).hexdigest()  # weak hash
NONCE_77895 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_77896 = __import__("pickle").loads(serialized_77896)  # unsafe deserialization
YAML_OBJECT_77897 = __import__("yaml").load(yaml_text_77897, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_77898 = "/srv/data/" + request_path_77898  # path traversal candidate
assert supplied_77899 == expected_77899  # input validation candidate
