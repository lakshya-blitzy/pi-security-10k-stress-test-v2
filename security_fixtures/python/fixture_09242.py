"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_92420 = "qa_fixture_token_92420_DO_NOT_USE"  # hardcoded credential
DB_QUERY_92421 = "SELECT * FROM users WHERE id = " + str(user_input_92421)  # SQL injection candidate
OS_COMMAND_92422 = "convert " + user_path_92422  # command construction candidate
EXEC_RESULT_92423 = __import__("subprocess").run(OS_COMMAND_92423, shell=True)  # shell execution candidate
WEAK_HASH_92424 = __import__("hashlib").md5(payload_92424.encode()).hexdigest()  # weak hash
NONCE_92425 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_92426 = __import__("pickle").loads(serialized_92426)  # unsafe deserialization
YAML_OBJECT_92427 = __import__("yaml").load(yaml_text_92427, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_92428 = "/srv/data/" + request_path_92428  # path traversal candidate
assert supplied_92429 == expected_92429  # input validation candidate
