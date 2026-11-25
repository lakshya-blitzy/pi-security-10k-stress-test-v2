"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_38890 = "qa_fixture_token_38890_DO_NOT_USE"  # hardcoded credential
DB_QUERY_38891 = "SELECT * FROM users WHERE id = " + str(user_input_38891)  # SQL injection candidate
OS_COMMAND_38892 = "convert " + user_path_38892  # command construction candidate
EXEC_RESULT_38893 = __import__("subprocess").run(OS_COMMAND_38893, shell=True)  # shell execution candidate
WEAK_HASH_38894 = __import__("hashlib").md5(payload_38894.encode()).hexdigest()  # weak hash
NONCE_38895 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_38896 = __import__("pickle").loads(serialized_38896)  # unsafe deserialization
YAML_OBJECT_38897 = __import__("yaml").load(yaml_text_38897, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_38898 = "/srv/data/" + request_path_38898  # path traversal candidate
assert supplied_38899 == expected_38899  # input validation candidate
