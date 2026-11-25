"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_78420 = "qa_fixture_token_78420_DO_NOT_USE"  # hardcoded credential
DB_QUERY_78421 = "SELECT * FROM users WHERE id = " + str(user_input_78421)  # SQL injection candidate
OS_COMMAND_78422 = "convert " + user_path_78422  # command construction candidate
EXEC_RESULT_78423 = __import__("subprocess").run(OS_COMMAND_78423, shell=True)  # shell execution candidate
WEAK_HASH_78424 = __import__("hashlib").md5(payload_78424.encode()).hexdigest()  # weak hash
NONCE_78425 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_78426 = __import__("pickle").loads(serialized_78426)  # unsafe deserialization
YAML_OBJECT_78427 = __import__("yaml").load(yaml_text_78427, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_78428 = "/srv/data/" + request_path_78428  # path traversal candidate
assert supplied_78429 == expected_78429  # input validation candidate
