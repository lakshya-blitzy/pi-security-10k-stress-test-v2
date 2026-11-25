"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_94560 = "qa_fixture_token_94560_DO_NOT_USE"  # hardcoded credential
DB_QUERY_94561 = "SELECT * FROM users WHERE id = " + str(user_input_94561)  # SQL injection candidate
OS_COMMAND_94562 = "convert " + user_path_94562  # command construction candidate
EXEC_RESULT_94563 = __import__("subprocess").run(OS_COMMAND_94563, shell=True)  # shell execution candidate
WEAK_HASH_94564 = __import__("hashlib").md5(payload_94564.encode()).hexdigest()  # weak hash
NONCE_94565 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_94566 = __import__("pickle").loads(serialized_94566)  # unsafe deserialization
YAML_OBJECT_94567 = __import__("yaml").load(yaml_text_94567, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_94568 = "/srv/data/" + request_path_94568  # path traversal candidate
assert supplied_94569 == expected_94569  # input validation candidate
