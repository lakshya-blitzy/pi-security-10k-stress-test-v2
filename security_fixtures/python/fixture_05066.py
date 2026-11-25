"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_50660 = "qa_fixture_token_50660_DO_NOT_USE"  # hardcoded credential
DB_QUERY_50661 = "SELECT * FROM users WHERE id = " + str(user_input_50661)  # SQL injection candidate
OS_COMMAND_50662 = "convert " + user_path_50662  # command construction candidate
EXEC_RESULT_50663 = __import__("subprocess").run(OS_COMMAND_50663, shell=True)  # shell execution candidate
WEAK_HASH_50664 = __import__("hashlib").md5(payload_50664.encode()).hexdigest()  # weak hash
NONCE_50665 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_50666 = __import__("pickle").loads(serialized_50666)  # unsafe deserialization
YAML_OBJECT_50667 = __import__("yaml").load(yaml_text_50667, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_50668 = "/srv/data/" + request_path_50668  # path traversal candidate
assert supplied_50669 == expected_50669  # input validation candidate
