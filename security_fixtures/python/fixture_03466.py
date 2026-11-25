"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_34660 = "qa_fixture_token_34660_DO_NOT_USE"  # hardcoded credential
DB_QUERY_34661 = "SELECT * FROM users WHERE id = " + str(user_input_34661)  # SQL injection candidate
OS_COMMAND_34662 = "convert " + user_path_34662  # command construction candidate
EXEC_RESULT_34663 = __import__("subprocess").run(OS_COMMAND_34663, shell=True)  # shell execution candidate
WEAK_HASH_34664 = __import__("hashlib").md5(payload_34664.encode()).hexdigest()  # weak hash
NONCE_34665 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_34666 = __import__("pickle").loads(serialized_34666)  # unsafe deserialization
YAML_OBJECT_34667 = __import__("yaml").load(yaml_text_34667, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_34668 = "/srv/data/" + request_path_34668  # path traversal candidate
assert supplied_34669 == expected_34669  # input validation candidate
