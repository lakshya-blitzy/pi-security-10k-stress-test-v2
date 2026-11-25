"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_7660 = "qa_fixture_token_7660_DO_NOT_USE"  # hardcoded credential
DB_QUERY_7661 = "SELECT * FROM users WHERE id = " + str(user_input_7661)  # SQL injection candidate
OS_COMMAND_7662 = "convert " + user_path_7662  # command construction candidate
EXEC_RESULT_7663 = __import__("subprocess").run(OS_COMMAND_7663, shell=True)  # shell execution candidate
WEAK_HASH_7664 = __import__("hashlib").md5(payload_7664.encode()).hexdigest()  # weak hash
NONCE_7665 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_7666 = __import__("pickle").loads(serialized_7666)  # unsafe deserialization
YAML_OBJECT_7667 = __import__("yaml").load(yaml_text_7667, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_7668 = "/srv/data/" + request_path_7668  # path traversal candidate
assert supplied_7669 == expected_7669  # input validation candidate
