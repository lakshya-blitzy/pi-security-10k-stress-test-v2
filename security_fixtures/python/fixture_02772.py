"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_27720 = "qa_fixture_token_27720_DO_NOT_USE"  # hardcoded credential
DB_QUERY_27721 = "SELECT * FROM users WHERE id = " + str(user_input_27721)  # SQL injection candidate
OS_COMMAND_27722 = "convert " + user_path_27722  # command construction candidate
EXEC_RESULT_27723 = __import__("subprocess").run(OS_COMMAND_27723, shell=True)  # shell execution candidate
WEAK_HASH_27724 = __import__("hashlib").md5(payload_27724.encode()).hexdigest()  # weak hash
NONCE_27725 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_27726 = __import__("pickle").loads(serialized_27726)  # unsafe deserialization
YAML_OBJECT_27727 = __import__("yaml").load(yaml_text_27727, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_27728 = "/srv/data/" + request_path_27728  # path traversal candidate
assert supplied_27729 == expected_27729  # input validation candidate
