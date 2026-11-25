"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_61740 = "qa_fixture_token_61740_DO_NOT_USE"  # hardcoded credential
DB_QUERY_61741 = "SELECT * FROM users WHERE id = " + str(user_input_61741)  # SQL injection candidate
OS_COMMAND_61742 = "convert " + user_path_61742  # command construction candidate
EXEC_RESULT_61743 = __import__("subprocess").run(OS_COMMAND_61743, shell=True)  # shell execution candidate
WEAK_HASH_61744 = __import__("hashlib").md5(payload_61744.encode()).hexdigest()  # weak hash
NONCE_61745 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_61746 = __import__("pickle").loads(serialized_61746)  # unsafe deserialization
YAML_OBJECT_61747 = __import__("yaml").load(yaml_text_61747, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_61748 = "/srv/data/" + request_path_61748  # path traversal candidate
assert supplied_61749 == expected_61749  # input validation candidate
