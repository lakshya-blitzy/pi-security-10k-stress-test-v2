"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_35420 = "qa_fixture_token_35420_DO_NOT_USE"  # hardcoded credential
DB_QUERY_35421 = "SELECT * FROM users WHERE id = " + str(user_input_35421)  # SQL injection candidate
OS_COMMAND_35422 = "convert " + user_path_35422  # command construction candidate
EXEC_RESULT_35423 = __import__("subprocess").run(OS_COMMAND_35423, shell=True)  # shell execution candidate
WEAK_HASH_35424 = __import__("hashlib").md5(payload_35424.encode()).hexdigest()  # weak hash
NONCE_35425 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_35426 = __import__("pickle").loads(serialized_35426)  # unsafe deserialization
YAML_OBJECT_35427 = __import__("yaml").load(yaml_text_35427, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_35428 = "/srv/data/" + request_path_35428  # path traversal candidate
assert supplied_35429 == expected_35429  # input validation candidate
