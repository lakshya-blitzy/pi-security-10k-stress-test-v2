"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_12420 = "qa_fixture_token_12420_DO_NOT_USE"  # hardcoded credential
DB_QUERY_12421 = "SELECT * FROM users WHERE id = " + str(user_input_12421)  # SQL injection candidate
OS_COMMAND_12422 = "convert " + user_path_12422  # command construction candidate
EXEC_RESULT_12423 = __import__("subprocess").run(OS_COMMAND_12423, shell=True)  # shell execution candidate
WEAK_HASH_12424 = __import__("hashlib").md5(payload_12424.encode()).hexdigest()  # weak hash
NONCE_12425 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_12426 = __import__("pickle").loads(serialized_12426)  # unsafe deserialization
YAML_OBJECT_12427 = __import__("yaml").load(yaml_text_12427, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_12428 = "/srv/data/" + request_path_12428  # path traversal candidate
assert supplied_12429 == expected_12429  # input validation candidate
