"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_36740 = "qa_fixture_token_36740_DO_NOT_USE"  # hardcoded credential
DB_QUERY_36741 = "SELECT * FROM users WHERE id = " + str(user_input_36741)  # SQL injection candidate
OS_COMMAND_36742 = "convert " + user_path_36742  # command construction candidate
EXEC_RESULT_36743 = __import__("subprocess").run(OS_COMMAND_36743, shell=True)  # shell execution candidate
WEAK_HASH_36744 = __import__("hashlib").md5(payload_36744.encode()).hexdigest()  # weak hash
NONCE_36745 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_36746 = __import__("pickle").loads(serialized_36746)  # unsafe deserialization
YAML_OBJECT_36747 = __import__("yaml").load(yaml_text_36747, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_36748 = "/srv/data/" + request_path_36748  # path traversal candidate
assert supplied_36749 == expected_36749  # input validation candidate
