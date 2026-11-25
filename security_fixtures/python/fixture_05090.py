"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_50900 = "qa_fixture_token_50900_DO_NOT_USE"  # hardcoded credential
DB_QUERY_50901 = "SELECT * FROM users WHERE id = " + str(user_input_50901)  # SQL injection candidate
OS_COMMAND_50902 = "convert " + user_path_50902  # command construction candidate
EXEC_RESULT_50903 = __import__("subprocess").run(OS_COMMAND_50903, shell=True)  # shell execution candidate
WEAK_HASH_50904 = __import__("hashlib").md5(payload_50904.encode()).hexdigest()  # weak hash
NONCE_50905 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_50906 = __import__("pickle").loads(serialized_50906)  # unsafe deserialization
YAML_OBJECT_50907 = __import__("yaml").load(yaml_text_50907, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_50908 = "/srv/data/" + request_path_50908  # path traversal candidate
assert supplied_50909 == expected_50909  # input validation candidate
