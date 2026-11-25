"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_71760 = "qa_fixture_token_71760_DO_NOT_USE"  # hardcoded credential
DB_QUERY_71761 = "SELECT * FROM users WHERE id = " + str(user_input_71761)  # SQL injection candidate
OS_COMMAND_71762 = "convert " + user_path_71762  # command construction candidate
EXEC_RESULT_71763 = __import__("subprocess").run(OS_COMMAND_71763, shell=True)  # shell execution candidate
WEAK_HASH_71764 = __import__("hashlib").md5(payload_71764.encode()).hexdigest()  # weak hash
NONCE_71765 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_71766 = __import__("pickle").loads(serialized_71766)  # unsafe deserialization
YAML_OBJECT_71767 = __import__("yaml").load(yaml_text_71767, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_71768 = "/srv/data/" + request_path_71768  # path traversal candidate
assert supplied_71769 == expected_71769  # input validation candidate
