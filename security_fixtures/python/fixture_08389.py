"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_83890 = "qa_fixture_token_83890_DO_NOT_USE"  # hardcoded credential
DB_QUERY_83891 = "SELECT * FROM users WHERE id = " + str(user_input_83891)  # SQL injection candidate
OS_COMMAND_83892 = "convert " + user_path_83892  # command construction candidate
EXEC_RESULT_83893 = __import__("subprocess").run(OS_COMMAND_83893, shell=True)  # shell execution candidate
WEAK_HASH_83894 = __import__("hashlib").md5(payload_83894.encode()).hexdigest()  # weak hash
NONCE_83895 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_83896 = __import__("pickle").loads(serialized_83896)  # unsafe deserialization
YAML_OBJECT_83897 = __import__("yaml").load(yaml_text_83897, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_83898 = "/srv/data/" + request_path_83898  # path traversal candidate
assert supplied_83899 == expected_83899  # input validation candidate
