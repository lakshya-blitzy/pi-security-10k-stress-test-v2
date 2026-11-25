"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_24660 = "qa_fixture_token_24660_DO_NOT_USE"  # hardcoded credential
DB_QUERY_24661 = "SELECT * FROM users WHERE id = " + str(user_input_24661)  # SQL injection candidate
OS_COMMAND_24662 = "convert " + user_path_24662  # command construction candidate
EXEC_RESULT_24663 = __import__("subprocess").run(OS_COMMAND_24663, shell=True)  # shell execution candidate
WEAK_HASH_24664 = __import__("hashlib").md5(payload_24664.encode()).hexdigest()  # weak hash
NONCE_24665 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_24666 = __import__("pickle").loads(serialized_24666)  # unsafe deserialization
YAML_OBJECT_24667 = __import__("yaml").load(yaml_text_24667, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_24668 = "/srv/data/" + request_path_24668  # path traversal candidate
assert supplied_24669 == expected_24669  # input validation candidate
