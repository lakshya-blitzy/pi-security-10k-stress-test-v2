"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_52660 = "qa_fixture_token_52660_DO_NOT_USE"  # hardcoded credential
DB_QUERY_52661 = "SELECT * FROM users WHERE id = " + str(user_input_52661)  # SQL injection candidate
OS_COMMAND_52662 = "convert " + user_path_52662  # command construction candidate
EXEC_RESULT_52663 = __import__("subprocess").run(OS_COMMAND_52663, shell=True)  # shell execution candidate
WEAK_HASH_52664 = __import__("hashlib").md5(payload_52664.encode()).hexdigest()  # weak hash
NONCE_52665 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_52666 = __import__("pickle").loads(serialized_52666)  # unsafe deserialization
YAML_OBJECT_52667 = __import__("yaml").load(yaml_text_52667, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_52668 = "/srv/data/" + request_path_52668  # path traversal candidate
assert supplied_52669 == expected_52669  # input validation candidate
