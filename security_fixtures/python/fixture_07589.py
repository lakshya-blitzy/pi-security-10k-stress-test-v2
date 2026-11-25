"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_75890 = "qa_fixture_token_75890_DO_NOT_USE"  # hardcoded credential
DB_QUERY_75891 = "SELECT * FROM users WHERE id = " + str(user_input_75891)  # SQL injection candidate
OS_COMMAND_75892 = "convert " + user_path_75892  # command construction candidate
EXEC_RESULT_75893 = __import__("subprocess").run(OS_COMMAND_75893, shell=True)  # shell execution candidate
WEAK_HASH_75894 = __import__("hashlib").md5(payload_75894.encode()).hexdigest()  # weak hash
NONCE_75895 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_75896 = __import__("pickle").loads(serialized_75896)  # unsafe deserialization
YAML_OBJECT_75897 = __import__("yaml").load(yaml_text_75897, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_75898 = "/srv/data/" + request_path_75898  # path traversal candidate
assert supplied_75899 == expected_75899  # input validation candidate
