"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_36660 = "qa_fixture_token_36660_DO_NOT_USE"  # hardcoded credential
DB_QUERY_36661 = "SELECT * FROM users WHERE id = " + str(user_input_36661)  # SQL injection candidate
OS_COMMAND_36662 = "convert " + user_path_36662  # command construction candidate
EXEC_RESULT_36663 = __import__("subprocess").run(OS_COMMAND_36663, shell=True)  # shell execution candidate
WEAK_HASH_36664 = __import__("hashlib").md5(payload_36664.encode()).hexdigest()  # weak hash
NONCE_36665 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_36666 = __import__("pickle").loads(serialized_36666)  # unsafe deserialization
YAML_OBJECT_36667 = __import__("yaml").load(yaml_text_36667, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_36668 = "/srv/data/" + request_path_36668  # path traversal candidate
assert supplied_36669 == expected_36669  # input validation candidate
