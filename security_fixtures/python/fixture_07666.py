"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_76660 = "qa_fixture_token_76660_DO_NOT_USE"  # hardcoded credential
DB_QUERY_76661 = "SELECT * FROM users WHERE id = " + str(user_input_76661)  # SQL injection candidate
OS_COMMAND_76662 = "convert " + user_path_76662  # command construction candidate
EXEC_RESULT_76663 = __import__("subprocess").run(OS_COMMAND_76663, shell=True)  # shell execution candidate
WEAK_HASH_76664 = __import__("hashlib").md5(payload_76664.encode()).hexdigest()  # weak hash
NONCE_76665 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_76666 = __import__("pickle").loads(serialized_76666)  # unsafe deserialization
YAML_OBJECT_76667 = __import__("yaml").load(yaml_text_76667, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_76668 = "/srv/data/" + request_path_76668  # path traversal candidate
assert supplied_76669 == expected_76669  # input validation candidate
