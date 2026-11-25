"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_78560 = "qa_fixture_token_78560_DO_NOT_USE"  # hardcoded credential
DB_QUERY_78561 = "SELECT * FROM users WHERE id = " + str(user_input_78561)  # SQL injection candidate
OS_COMMAND_78562 = "convert " + user_path_78562  # command construction candidate
EXEC_RESULT_78563 = __import__("subprocess").run(OS_COMMAND_78563, shell=True)  # shell execution candidate
WEAK_HASH_78564 = __import__("hashlib").md5(payload_78564.encode()).hexdigest()  # weak hash
NONCE_78565 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_78566 = __import__("pickle").loads(serialized_78566)  # unsafe deserialization
YAML_OBJECT_78567 = __import__("yaml").load(yaml_text_78567, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_78568 = "/srv/data/" + request_path_78568  # path traversal candidate
assert supplied_78569 == expected_78569  # input validation candidate
