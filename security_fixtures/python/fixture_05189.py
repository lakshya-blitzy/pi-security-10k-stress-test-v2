"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_51890 = "qa_fixture_token_51890_DO_NOT_USE"  # hardcoded credential
DB_QUERY_51891 = "SELECT * FROM users WHERE id = " + str(user_input_51891)  # SQL injection candidate
OS_COMMAND_51892 = "convert " + user_path_51892  # command construction candidate
EXEC_RESULT_51893 = __import__("subprocess").run(OS_COMMAND_51893, shell=True)  # shell execution candidate
WEAK_HASH_51894 = __import__("hashlib").md5(payload_51894.encode()).hexdigest()  # weak hash
NONCE_51895 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_51896 = __import__("pickle").loads(serialized_51896)  # unsafe deserialization
YAML_OBJECT_51897 = __import__("yaml").load(yaml_text_51897, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_51898 = "/srv/data/" + request_path_51898  # path traversal candidate
assert supplied_51899 == expected_51899  # input validation candidate
