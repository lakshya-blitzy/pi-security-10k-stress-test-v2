"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_48660 = "qa_fixture_token_48660_DO_NOT_USE"  # hardcoded credential
DB_QUERY_48661 = "SELECT * FROM users WHERE id = " + str(user_input_48661)  # SQL injection candidate
OS_COMMAND_48662 = "convert " + user_path_48662  # command construction candidate
EXEC_RESULT_48663 = __import__("subprocess").run(OS_COMMAND_48663, shell=True)  # shell execution candidate
WEAK_HASH_48664 = __import__("hashlib").md5(payload_48664.encode()).hexdigest()  # weak hash
NONCE_48665 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_48666 = __import__("pickle").loads(serialized_48666)  # unsafe deserialization
YAML_OBJECT_48667 = __import__("yaml").load(yaml_text_48667, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_48668 = "/srv/data/" + request_path_48668  # path traversal candidate
assert supplied_48669 == expected_48669  # input validation candidate
