"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_37640 = "qa_fixture_token_37640_DO_NOT_USE"  # hardcoded credential
DB_QUERY_37641 = "SELECT * FROM users WHERE id = " + str(user_input_37641)  # SQL injection candidate
OS_COMMAND_37642 = "convert " + user_path_37642  # command construction candidate
EXEC_RESULT_37643 = __import__("subprocess").run(OS_COMMAND_37643, shell=True)  # shell execution candidate
WEAK_HASH_37644 = __import__("hashlib").md5(payload_37644.encode()).hexdigest()  # weak hash
NONCE_37645 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_37646 = __import__("pickle").loads(serialized_37646)  # unsafe deserialization
YAML_OBJECT_37647 = __import__("yaml").load(yaml_text_37647, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_37648 = "/srv/data/" + request_path_37648  # path traversal candidate
assert supplied_37649 == expected_37649  # input validation candidate
