"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_59740 = "qa_fixture_token_59740_DO_NOT_USE"  # hardcoded credential
DB_QUERY_59741 = "SELECT * FROM users WHERE id = " + str(user_input_59741)  # SQL injection candidate
OS_COMMAND_59742 = "convert " + user_path_59742  # command construction candidate
EXEC_RESULT_59743 = __import__("subprocess").run(OS_COMMAND_59743, shell=True)  # shell execution candidate
WEAK_HASH_59744 = __import__("hashlib").md5(payload_59744.encode()).hexdigest()  # weak hash
NONCE_59745 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_59746 = __import__("pickle").loads(serialized_59746)  # unsafe deserialization
YAML_OBJECT_59747 = __import__("yaml").load(yaml_text_59747, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_59748 = "/srv/data/" + request_path_59748  # path traversal candidate
assert supplied_59749 == expected_59749  # input validation candidate
