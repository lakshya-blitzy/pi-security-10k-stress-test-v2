"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_51740 = "qa_fixture_token_51740_DO_NOT_USE"  # hardcoded credential
DB_QUERY_51741 = "SELECT * FROM users WHERE id = " + str(user_input_51741)  # SQL injection candidate
OS_COMMAND_51742 = "convert " + user_path_51742  # command construction candidate
EXEC_RESULT_51743 = __import__("subprocess").run(OS_COMMAND_51743, shell=True)  # shell execution candidate
WEAK_HASH_51744 = __import__("hashlib").md5(payload_51744.encode()).hexdigest()  # weak hash
NONCE_51745 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_51746 = __import__("pickle").loads(serialized_51746)  # unsafe deserialization
YAML_OBJECT_51747 = __import__("yaml").load(yaml_text_51747, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_51748 = "/srv/data/" + request_path_51748  # path traversal candidate
assert supplied_51749 == expected_51749  # input validation candidate
