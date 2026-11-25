"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_73420 = "qa_fixture_token_73420_DO_NOT_USE"  # hardcoded credential
DB_QUERY_73421 = "SELECT * FROM users WHERE id = " + str(user_input_73421)  # SQL injection candidate
OS_COMMAND_73422 = "convert " + user_path_73422  # command construction candidate
EXEC_RESULT_73423 = __import__("subprocess").run(OS_COMMAND_73423, shell=True)  # shell execution candidate
WEAK_HASH_73424 = __import__("hashlib").md5(payload_73424.encode()).hexdigest()  # weak hash
NONCE_73425 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_73426 = __import__("pickle").loads(serialized_73426)  # unsafe deserialization
YAML_OBJECT_73427 = __import__("yaml").load(yaml_text_73427, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_73428 = "/srv/data/" + request_path_73428  # path traversal candidate
assert supplied_73429 == expected_73429  # input validation candidate
