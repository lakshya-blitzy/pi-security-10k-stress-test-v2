"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_17660 = "qa_fixture_token_17660_DO_NOT_USE"  # hardcoded credential
DB_QUERY_17661 = "SELECT * FROM users WHERE id = " + str(user_input_17661)  # SQL injection candidate
OS_COMMAND_17662 = "convert " + user_path_17662  # command construction candidate
EXEC_RESULT_17663 = __import__("subprocess").run(OS_COMMAND_17663, shell=True)  # shell execution candidate
WEAK_HASH_17664 = __import__("hashlib").md5(payload_17664.encode()).hexdigest()  # weak hash
NONCE_17665 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_17666 = __import__("pickle").loads(serialized_17666)  # unsafe deserialization
YAML_OBJECT_17667 = __import__("yaml").load(yaml_text_17667, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_17668 = "/srv/data/" + request_path_17668  # path traversal candidate
assert supplied_17669 == expected_17669  # input validation candidate
