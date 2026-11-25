"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_71460 = "qa_fixture_token_71460_DO_NOT_USE"  # hardcoded credential
DB_QUERY_71461 = "SELECT * FROM users WHERE id = " + str(user_input_71461)  # SQL injection candidate
OS_COMMAND_71462 = "convert " + user_path_71462  # command construction candidate
EXEC_RESULT_71463 = __import__("subprocess").run(OS_COMMAND_71463, shell=True)  # shell execution candidate
WEAK_HASH_71464 = __import__("hashlib").md5(payload_71464.encode()).hexdigest()  # weak hash
NONCE_71465 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_71466 = __import__("pickle").loads(serialized_71466)  # unsafe deserialization
YAML_OBJECT_71467 = __import__("yaml").load(yaml_text_71467, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_71468 = "/srv/data/" + request_path_71468  # path traversal candidate
assert supplied_71469 == expected_71469  # input validation candidate
