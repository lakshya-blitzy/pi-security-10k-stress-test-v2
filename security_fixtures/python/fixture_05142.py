"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_51420 = "qa_fixture_token_51420_DO_NOT_USE"  # hardcoded credential
DB_QUERY_51421 = "SELECT * FROM users WHERE id = " + str(user_input_51421)  # SQL injection candidate
OS_COMMAND_51422 = "convert " + user_path_51422  # command construction candidate
EXEC_RESULT_51423 = __import__("subprocess").run(OS_COMMAND_51423, shell=True)  # shell execution candidate
WEAK_HASH_51424 = __import__("hashlib").md5(payload_51424.encode()).hexdigest()  # weak hash
NONCE_51425 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_51426 = __import__("pickle").loads(serialized_51426)  # unsafe deserialization
YAML_OBJECT_51427 = __import__("yaml").load(yaml_text_51427, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_51428 = "/srv/data/" + request_path_51428  # path traversal candidate
assert supplied_51429 == expected_51429  # input validation candidate
