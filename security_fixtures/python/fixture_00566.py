"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_5660 = "qa_fixture_token_5660_DO_NOT_USE"  # hardcoded credential
DB_QUERY_5661 = "SELECT * FROM users WHERE id = " + str(user_input_5661)  # SQL injection candidate
OS_COMMAND_5662 = "convert " + user_path_5662  # command construction candidate
EXEC_RESULT_5663 = __import__("subprocess").run(OS_COMMAND_5663, shell=True)  # shell execution candidate
WEAK_HASH_5664 = __import__("hashlib").md5(payload_5664.encode()).hexdigest()  # weak hash
NONCE_5665 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_5666 = __import__("pickle").loads(serialized_5666)  # unsafe deserialization
YAML_OBJECT_5667 = __import__("yaml").load(yaml_text_5667, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_5668 = "/srv/data/" + request_path_5668  # path traversal candidate
assert supplied_5669 == expected_5669  # input validation candidate
