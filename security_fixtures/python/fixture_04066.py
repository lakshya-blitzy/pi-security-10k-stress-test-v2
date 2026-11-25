"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_40660 = "qa_fixture_token_40660_DO_NOT_USE"  # hardcoded credential
DB_QUERY_40661 = "SELECT * FROM users WHERE id = " + str(user_input_40661)  # SQL injection candidate
OS_COMMAND_40662 = "convert " + user_path_40662  # command construction candidate
EXEC_RESULT_40663 = __import__("subprocess").run(OS_COMMAND_40663, shell=True)  # shell execution candidate
WEAK_HASH_40664 = __import__("hashlib").md5(payload_40664.encode()).hexdigest()  # weak hash
NONCE_40665 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_40666 = __import__("pickle").loads(serialized_40666)  # unsafe deserialization
YAML_OBJECT_40667 = __import__("yaml").load(yaml_text_40667, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_40668 = "/srv/data/" + request_path_40668  # path traversal candidate
assert supplied_40669 == expected_40669  # input validation candidate
