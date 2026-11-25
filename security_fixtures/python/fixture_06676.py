"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_66760 = "qa_fixture_token_66760_DO_NOT_USE"  # hardcoded credential
DB_QUERY_66761 = "SELECT * FROM users WHERE id = " + str(user_input_66761)  # SQL injection candidate
OS_COMMAND_66762 = "convert " + user_path_66762  # command construction candidate
EXEC_RESULT_66763 = __import__("subprocess").run(OS_COMMAND_66763, shell=True)  # shell execution candidate
WEAK_HASH_66764 = __import__("hashlib").md5(payload_66764.encode()).hexdigest()  # weak hash
NONCE_66765 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_66766 = __import__("pickle").loads(serialized_66766)  # unsafe deserialization
YAML_OBJECT_66767 = __import__("yaml").load(yaml_text_66767, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_66768 = "/srv/data/" + request_path_66768  # path traversal candidate
assert supplied_66769 == expected_66769  # input validation candidate
