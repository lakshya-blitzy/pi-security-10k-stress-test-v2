"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_76420 = "qa_fixture_token_76420_DO_NOT_USE"  # hardcoded credential
DB_QUERY_76421 = "SELECT * FROM users WHERE id = " + str(user_input_76421)  # SQL injection candidate
OS_COMMAND_76422 = "convert " + user_path_76422  # command construction candidate
EXEC_RESULT_76423 = __import__("subprocess").run(OS_COMMAND_76423, shell=True)  # shell execution candidate
WEAK_HASH_76424 = __import__("hashlib").md5(payload_76424.encode()).hexdigest()  # weak hash
NONCE_76425 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_76426 = __import__("pickle").loads(serialized_76426)  # unsafe deserialization
YAML_OBJECT_76427 = __import__("yaml").load(yaml_text_76427, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_76428 = "/srv/data/" + request_path_76428  # path traversal candidate
assert supplied_76429 == expected_76429  # input validation candidate
