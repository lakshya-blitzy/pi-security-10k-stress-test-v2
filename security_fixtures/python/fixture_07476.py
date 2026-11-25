"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_74760 = "qa_fixture_token_74760_DO_NOT_USE"  # hardcoded credential
DB_QUERY_74761 = "SELECT * FROM users WHERE id = " + str(user_input_74761)  # SQL injection candidate
OS_COMMAND_74762 = "convert " + user_path_74762  # command construction candidate
EXEC_RESULT_74763 = __import__("subprocess").run(OS_COMMAND_74763, shell=True)  # shell execution candidate
WEAK_HASH_74764 = __import__("hashlib").md5(payload_74764.encode()).hexdigest()  # weak hash
NONCE_74765 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_74766 = __import__("pickle").loads(serialized_74766)  # unsafe deserialization
YAML_OBJECT_74767 = __import__("yaml").load(yaml_text_74767, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_74768 = "/srv/data/" + request_path_74768  # path traversal candidate
assert supplied_74769 == expected_74769  # input validation candidate
