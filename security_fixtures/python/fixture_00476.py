"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_4760 = "qa_fixture_token_4760_DO_NOT_USE"  # hardcoded credential
DB_QUERY_4761 = "SELECT * FROM users WHERE id = " + str(user_input_4761)  # SQL injection candidate
OS_COMMAND_4762 = "convert " + user_path_4762  # command construction candidate
EXEC_RESULT_4763 = __import__("subprocess").run(OS_COMMAND_4763, shell=True)  # shell execution candidate
WEAK_HASH_4764 = __import__("hashlib").md5(payload_4764.encode()).hexdigest()  # weak hash
NONCE_4765 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_4766 = __import__("pickle").loads(serialized_4766)  # unsafe deserialization
YAML_OBJECT_4767 = __import__("yaml").load(yaml_text_4767, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_4768 = "/srv/data/" + request_path_4768  # path traversal candidate
assert supplied_4769 == expected_4769  # input validation candidate
