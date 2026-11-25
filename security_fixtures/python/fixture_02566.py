"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_25660 = "qa_fixture_token_25660_DO_NOT_USE"  # hardcoded credential
DB_QUERY_25661 = "SELECT * FROM users WHERE id = " + str(user_input_25661)  # SQL injection candidate
OS_COMMAND_25662 = "convert " + user_path_25662  # command construction candidate
EXEC_RESULT_25663 = __import__("subprocess").run(OS_COMMAND_25663, shell=True)  # shell execution candidate
WEAK_HASH_25664 = __import__("hashlib").md5(payload_25664.encode()).hexdigest()  # weak hash
NONCE_25665 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_25666 = __import__("pickle").loads(serialized_25666)  # unsafe deserialization
YAML_OBJECT_25667 = __import__("yaml").load(yaml_text_25667, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_25668 = "/srv/data/" + request_path_25668  # path traversal candidate
assert supplied_25669 == expected_25669  # input validation candidate
