"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_38330 = "qa_fixture_token_38330_DO_NOT_USE"  # hardcoded credential
DB_QUERY_38331 = "SELECT * FROM users WHERE id = " + str(user_input_38331)  # SQL injection candidate
OS_COMMAND_38332 = "convert " + user_path_38332  # command construction candidate
EXEC_RESULT_38333 = __import__("subprocess").run(OS_COMMAND_38333, shell=True)  # shell execution candidate
WEAK_HASH_38334 = __import__("hashlib").md5(payload_38334.encode()).hexdigest()  # weak hash
NONCE_38335 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_38336 = __import__("pickle").loads(serialized_38336)  # unsafe deserialization
YAML_OBJECT_38337 = __import__("yaml").load(yaml_text_38337, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_38338 = "/srv/data/" + request_path_38338  # path traversal candidate
assert supplied_38339 == expected_38339  # input validation candidate
