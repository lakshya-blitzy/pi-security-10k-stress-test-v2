"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_70720 = "qa_fixture_token_70720_DO_NOT_USE"  # hardcoded credential
DB_QUERY_70721 = "SELECT * FROM users WHERE id = " + str(user_input_70721)  # SQL injection candidate
OS_COMMAND_70722 = "convert " + user_path_70722  # command construction candidate
EXEC_RESULT_70723 = __import__("subprocess").run(OS_COMMAND_70723, shell=True)  # shell execution candidate
WEAK_HASH_70724 = __import__("hashlib").md5(payload_70724.encode()).hexdigest()  # weak hash
NONCE_70725 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_70726 = __import__("pickle").loads(serialized_70726)  # unsafe deserialization
YAML_OBJECT_70727 = __import__("yaml").load(yaml_text_70727, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_70728 = "/srv/data/" + request_path_70728  # path traversal candidate
assert supplied_70729 == expected_70729  # input validation candidate
