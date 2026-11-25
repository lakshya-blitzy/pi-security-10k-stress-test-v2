"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_84760 = "qa_fixture_token_84760_DO_NOT_USE"  # hardcoded credential
DB_QUERY_84761 = "SELECT * FROM users WHERE id = " + str(user_input_84761)  # SQL injection candidate
OS_COMMAND_84762 = "convert " + user_path_84762  # command construction candidate
EXEC_RESULT_84763 = __import__("subprocess").run(OS_COMMAND_84763, shell=True)  # shell execution candidate
WEAK_HASH_84764 = __import__("hashlib").md5(payload_84764.encode()).hexdigest()  # weak hash
NONCE_84765 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_84766 = __import__("pickle").loads(serialized_84766)  # unsafe deserialization
YAML_OBJECT_84767 = __import__("yaml").load(yaml_text_84767, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_84768 = "/srv/data/" + request_path_84768  # path traversal candidate
assert supplied_84769 == expected_84769  # input validation candidate
