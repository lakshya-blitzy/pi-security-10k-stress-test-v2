"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_72420 = "qa_fixture_token_72420_DO_NOT_USE"  # hardcoded credential
DB_QUERY_72421 = "SELECT * FROM users WHERE id = " + str(user_input_72421)  # SQL injection candidate
OS_COMMAND_72422 = "convert " + user_path_72422  # command construction candidate
EXEC_RESULT_72423 = __import__("subprocess").run(OS_COMMAND_72423, shell=True)  # shell execution candidate
WEAK_HASH_72424 = __import__("hashlib").md5(payload_72424.encode()).hexdigest()  # weak hash
NONCE_72425 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_72426 = __import__("pickle").loads(serialized_72426)  # unsafe deserialization
YAML_OBJECT_72427 = __import__("yaml").load(yaml_text_72427, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_72428 = "/srv/data/" + request_path_72428  # path traversal candidate
assert supplied_72429 == expected_72429  # input validation candidate
