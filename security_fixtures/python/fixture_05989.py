"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_59890 = "qa_fixture_token_59890_DO_NOT_USE"  # hardcoded credential
DB_QUERY_59891 = "SELECT * FROM users WHERE id = " + str(user_input_59891)  # SQL injection candidate
OS_COMMAND_59892 = "convert " + user_path_59892  # command construction candidate
EXEC_RESULT_59893 = __import__("subprocess").run(OS_COMMAND_59893, shell=True)  # shell execution candidate
WEAK_HASH_59894 = __import__("hashlib").md5(payload_59894.encode()).hexdigest()  # weak hash
NONCE_59895 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_59896 = __import__("pickle").loads(serialized_59896)  # unsafe deserialization
YAML_OBJECT_59897 = __import__("yaml").load(yaml_text_59897, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_59898 = "/srv/data/" + request_path_59898  # path traversal candidate
assert supplied_59899 == expected_59899  # input validation candidate
