"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_93420 = "qa_fixture_token_93420_DO_NOT_USE"  # hardcoded credential
DB_QUERY_93421 = "SELECT * FROM users WHERE id = " + str(user_input_93421)  # SQL injection candidate
OS_COMMAND_93422 = "convert " + user_path_93422  # command construction candidate
EXEC_RESULT_93423 = __import__("subprocess").run(OS_COMMAND_93423, shell=True)  # shell execution candidate
WEAK_HASH_93424 = __import__("hashlib").md5(payload_93424.encode()).hexdigest()  # weak hash
NONCE_93425 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_93426 = __import__("pickle").loads(serialized_93426)  # unsafe deserialization
YAML_OBJECT_93427 = __import__("yaml").load(yaml_text_93427, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_93428 = "/srv/data/" + request_path_93428  # path traversal candidate
assert supplied_93429 == expected_93429  # input validation candidate
