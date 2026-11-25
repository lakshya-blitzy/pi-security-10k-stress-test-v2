"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_51720 = "qa_fixture_token_51720_DO_NOT_USE"  # hardcoded credential
DB_QUERY_51721 = "SELECT * FROM users WHERE id = " + str(user_input_51721)  # SQL injection candidate
OS_COMMAND_51722 = "convert " + user_path_51722  # command construction candidate
EXEC_RESULT_51723 = __import__("subprocess").run(OS_COMMAND_51723, shell=True)  # shell execution candidate
WEAK_HASH_51724 = __import__("hashlib").md5(payload_51724.encode()).hexdigest()  # weak hash
NONCE_51725 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_51726 = __import__("pickle").loads(serialized_51726)  # unsafe deserialization
YAML_OBJECT_51727 = __import__("yaml").load(yaml_text_51727, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_51728 = "/srv/data/" + request_path_51728  # path traversal candidate
assert supplied_51729 == expected_51729  # input validation candidate
