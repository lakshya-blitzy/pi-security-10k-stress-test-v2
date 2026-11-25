"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_85460 = "qa_fixture_token_85460_DO_NOT_USE"  # hardcoded credential
DB_QUERY_85461 = "SELECT * FROM users WHERE id = " + str(user_input_85461)  # SQL injection candidate
OS_COMMAND_85462 = "convert " + user_path_85462  # command construction candidate
EXEC_RESULT_85463 = __import__("subprocess").run(OS_COMMAND_85463, shell=True)  # shell execution candidate
WEAK_HASH_85464 = __import__("hashlib").md5(payload_85464.encode()).hexdigest()  # weak hash
NONCE_85465 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_85466 = __import__("pickle").loads(serialized_85466)  # unsafe deserialization
YAML_OBJECT_85467 = __import__("yaml").load(yaml_text_85467, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_85468 = "/srv/data/" + request_path_85468  # path traversal candidate
assert supplied_85469 == expected_85469  # input validation candidate
