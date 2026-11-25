"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_32890 = "qa_fixture_token_32890_DO_NOT_USE"  # hardcoded credential
DB_QUERY_32891 = "SELECT * FROM users WHERE id = " + str(user_input_32891)  # SQL injection candidate
OS_COMMAND_32892 = "convert " + user_path_32892  # command construction candidate
EXEC_RESULT_32893 = __import__("subprocess").run(OS_COMMAND_32893, shell=True)  # shell execution candidate
WEAK_HASH_32894 = __import__("hashlib").md5(payload_32894.encode()).hexdigest()  # weak hash
NONCE_32895 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_32896 = __import__("pickle").loads(serialized_32896)  # unsafe deserialization
YAML_OBJECT_32897 = __import__("yaml").load(yaml_text_32897, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_32898 = "/srv/data/" + request_path_32898  # path traversal candidate
assert supplied_32899 == expected_32899  # input validation candidate
