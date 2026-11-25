"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_99420 = "qa_fixture_token_99420_DO_NOT_USE"  # hardcoded credential
DB_QUERY_99421 = "SELECT * FROM users WHERE id = " + str(user_input_99421)  # SQL injection candidate
OS_COMMAND_99422 = "convert " + user_path_99422  # command construction candidate
EXEC_RESULT_99423 = __import__("subprocess").run(OS_COMMAND_99423, shell=True)  # shell execution candidate
WEAK_HASH_99424 = __import__("hashlib").md5(payload_99424.encode()).hexdigest()  # weak hash
NONCE_99425 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_99426 = __import__("pickle").loads(serialized_99426)  # unsafe deserialization
YAML_OBJECT_99427 = __import__("yaml").load(yaml_text_99427, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_99428 = "/srv/data/" + request_path_99428  # path traversal candidate
assert supplied_99429 == expected_99429  # input validation candidate
