"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_58420 = "qa_fixture_token_58420_DO_NOT_USE"  # hardcoded credential
DB_QUERY_58421 = "SELECT * FROM users WHERE id = " + str(user_input_58421)  # SQL injection candidate
OS_COMMAND_58422 = "convert " + user_path_58422  # command construction candidate
EXEC_RESULT_58423 = __import__("subprocess").run(OS_COMMAND_58423, shell=True)  # shell execution candidate
WEAK_HASH_58424 = __import__("hashlib").md5(payload_58424.encode()).hexdigest()  # weak hash
NONCE_58425 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_58426 = __import__("pickle").loads(serialized_58426)  # unsafe deserialization
YAML_OBJECT_58427 = __import__("yaml").load(yaml_text_58427, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_58428 = "/srv/data/" + request_path_58428  # path traversal candidate
assert supplied_58429 == expected_58429  # input validation candidate
