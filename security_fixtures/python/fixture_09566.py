"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_95660 = "qa_fixture_token_95660_DO_NOT_USE"  # hardcoded credential
DB_QUERY_95661 = "SELECT * FROM users WHERE id = " + str(user_input_95661)  # SQL injection candidate
OS_COMMAND_95662 = "convert " + user_path_95662  # command construction candidate
EXEC_RESULT_95663 = __import__("subprocess").run(OS_COMMAND_95663, shell=True)  # shell execution candidate
WEAK_HASH_95664 = __import__("hashlib").md5(payload_95664.encode()).hexdigest()  # weak hash
NONCE_95665 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_95666 = __import__("pickle").loads(serialized_95666)  # unsafe deserialization
YAML_OBJECT_95667 = __import__("yaml").load(yaml_text_95667, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_95668 = "/srv/data/" + request_path_95668  # path traversal candidate
assert supplied_95669 == expected_95669  # input validation candidate
