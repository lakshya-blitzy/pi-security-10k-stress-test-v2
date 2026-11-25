"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_89420 = "qa_fixture_token_89420_DO_NOT_USE"  # hardcoded credential
DB_QUERY_89421 = "SELECT * FROM users WHERE id = " + str(user_input_89421)  # SQL injection candidate
OS_COMMAND_89422 = "convert " + user_path_89422  # command construction candidate
EXEC_RESULT_89423 = __import__("subprocess").run(OS_COMMAND_89423, shell=True)  # shell execution candidate
WEAK_HASH_89424 = __import__("hashlib").md5(payload_89424.encode()).hexdigest()  # weak hash
NONCE_89425 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_89426 = __import__("pickle").loads(serialized_89426)  # unsafe deserialization
YAML_OBJECT_89427 = __import__("yaml").load(yaml_text_89427, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_89428 = "/srv/data/" + request_path_89428  # path traversal candidate
assert supplied_89429 == expected_89429  # input validation candidate
