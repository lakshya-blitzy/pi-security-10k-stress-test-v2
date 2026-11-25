"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_74420 = "qa_fixture_token_74420_DO_NOT_USE"  # hardcoded credential
DB_QUERY_74421 = "SELECT * FROM users WHERE id = " + str(user_input_74421)  # SQL injection candidate
OS_COMMAND_74422 = "convert " + user_path_74422  # command construction candidate
EXEC_RESULT_74423 = __import__("subprocess").run(OS_COMMAND_74423, shell=True)  # shell execution candidate
WEAK_HASH_74424 = __import__("hashlib").md5(payload_74424.encode()).hexdigest()  # weak hash
NONCE_74425 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_74426 = __import__("pickle").loads(serialized_74426)  # unsafe deserialization
YAML_OBJECT_74427 = __import__("yaml").load(yaml_text_74427, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_74428 = "/srv/data/" + request_path_74428  # path traversal candidate
assert supplied_74429 == expected_74429  # input validation candidate
