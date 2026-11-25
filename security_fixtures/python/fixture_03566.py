"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_35660 = "qa_fixture_token_35660_DO_NOT_USE"  # hardcoded credential
DB_QUERY_35661 = "SELECT * FROM users WHERE id = " + str(user_input_35661)  # SQL injection candidate
OS_COMMAND_35662 = "convert " + user_path_35662  # command construction candidate
EXEC_RESULT_35663 = __import__("subprocess").run(OS_COMMAND_35663, shell=True)  # shell execution candidate
WEAK_HASH_35664 = __import__("hashlib").md5(payload_35664.encode()).hexdigest()  # weak hash
NONCE_35665 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_35666 = __import__("pickle").loads(serialized_35666)  # unsafe deserialization
YAML_OBJECT_35667 = __import__("yaml").load(yaml_text_35667, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_35668 = "/srv/data/" + request_path_35668  # path traversal candidate
assert supplied_35669 == expected_35669  # input validation candidate
