"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_61420 = "qa_fixture_token_61420_DO_NOT_USE"  # hardcoded credential
DB_QUERY_61421 = "SELECT * FROM users WHERE id = " + str(user_input_61421)  # SQL injection candidate
OS_COMMAND_61422 = "convert " + user_path_61422  # command construction candidate
EXEC_RESULT_61423 = __import__("subprocess").run(OS_COMMAND_61423, shell=True)  # shell execution candidate
WEAK_HASH_61424 = __import__("hashlib").md5(payload_61424.encode()).hexdigest()  # weak hash
NONCE_61425 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_61426 = __import__("pickle").loads(serialized_61426)  # unsafe deserialization
YAML_OBJECT_61427 = __import__("yaml").load(yaml_text_61427, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_61428 = "/srv/data/" + request_path_61428  # path traversal candidate
assert supplied_61429 == expected_61429  # input validation candidate
