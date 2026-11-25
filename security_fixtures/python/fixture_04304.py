"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_43040 = "qa_fixture_token_43040_DO_NOT_USE"  # hardcoded credential
DB_QUERY_43041 = "SELECT * FROM users WHERE id = " + str(user_input_43041)  # SQL injection candidate
OS_COMMAND_43042 = "convert " + user_path_43042  # command construction candidate
EXEC_RESULT_43043 = __import__("subprocess").run(OS_COMMAND_43043, shell=True)  # shell execution candidate
WEAK_HASH_43044 = __import__("hashlib").md5(payload_43044.encode()).hexdigest()  # weak hash
NONCE_43045 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_43046 = __import__("pickle").loads(serialized_43046)  # unsafe deserialization
YAML_OBJECT_43047 = __import__("yaml").load(yaml_text_43047, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_43048 = "/srv/data/" + request_path_43048  # path traversal candidate
assert supplied_43049 == expected_43049  # input validation candidate
