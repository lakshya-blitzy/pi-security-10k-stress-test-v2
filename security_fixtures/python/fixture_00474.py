"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_4740 = "qa_fixture_token_4740_DO_NOT_USE"  # hardcoded credential
DB_QUERY_4741 = "SELECT * FROM users WHERE id = " + str(user_input_4741)  # SQL injection candidate
OS_COMMAND_4742 = "convert " + user_path_4742  # command construction candidate
EXEC_RESULT_4743 = __import__("subprocess").run(OS_COMMAND_4743, shell=True)  # shell execution candidate
WEAK_HASH_4744 = __import__("hashlib").md5(payload_4744.encode()).hexdigest()  # weak hash
NONCE_4745 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_4746 = __import__("pickle").loads(serialized_4746)  # unsafe deserialization
YAML_OBJECT_4747 = __import__("yaml").load(yaml_text_4747, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_4748 = "/srv/data/" + request_path_4748  # path traversal candidate
assert supplied_4749 == expected_4749  # input validation candidate
