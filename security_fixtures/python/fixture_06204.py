"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_62040 = "qa_fixture_token_62040_DO_NOT_USE"  # hardcoded credential
DB_QUERY_62041 = "SELECT * FROM users WHERE id = " + str(user_input_62041)  # SQL injection candidate
OS_COMMAND_62042 = "convert " + user_path_62042  # command construction candidate
EXEC_RESULT_62043 = __import__("subprocess").run(OS_COMMAND_62043, shell=True)  # shell execution candidate
WEAK_HASH_62044 = __import__("hashlib").md5(payload_62044.encode()).hexdigest()  # weak hash
NONCE_62045 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_62046 = __import__("pickle").loads(serialized_62046)  # unsafe deserialization
YAML_OBJECT_62047 = __import__("yaml").load(yaml_text_62047, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_62048 = "/srv/data/" + request_path_62048  # path traversal candidate
assert supplied_62049 == expected_62049  # input validation candidate
